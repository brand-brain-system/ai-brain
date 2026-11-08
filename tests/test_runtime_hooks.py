"""Runtime regressions for the brain's hooks. Run: python -m unittest discover -s tests -v.

Origin: Parker's test_runtime_hooks.py, adapted for Brand-brain v1.1: hooks are driven
through the brain's .claude/settings.json (no Codex twin), there is no git-guard
(brains are shared through git), and session-start gives the git reminder.
"""

import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest

FACTORY = Path(__file__).resolve().parents[1]
BUNDLE = FACTORY / "templates/brand-routines"
CLOUD_SIGNALS = ("CLAUDE_CODE_REMOTE",)


def local_env(**extra):
    env = {k: v for k, v in os.environ.items() if k not in CLOUD_SIGNALS}
    env.update(extra)
    return env


def bash():
    found = shutil.which("bash")
    if os.name == "nt":
        git_bash = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "bin" / "bash.exe"
        if git_bash.exists():
            return str(git_bash)
    return found


def make_brand(root):
    shutil.copytree(BUNDLE / "claude", root / ".claude")
    mount = root / "brain-system"
    (mount / "creative-strategy-context").mkdir(parents=True)
    shutil.copyfile(FACTORY / "creative-strategy-context/expertise-routing.md",
                    mount / "creative-strategy-context/expertise-routing.md")
    (mount / "source.md").write_text("fixture method\n")
    (root / "sub-context-docs").mkdir()


def context_limit():
    source = (BUNDLE / "claude/hooks/craft-context.py").read_text(encoding="utf-8")
    for line in source.splitlines():
        if line.startswith("MAX_CONTEXT_BYTES"):
            return int(line.split("=")[1].strip())
    raise AssertionError("craft-context.py has no MAX_CONTEXT_BYTES")


class RuntimeHooks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="brain runtime test ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        make_brand(self.root)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.settings = json.loads((self.root / ".claude/settings.json").read_text(encoding="utf-8"))
        self.limit = context_limit()

    def commands(self):
        for event, groups in self.settings["hooks"].items():
            for group in groups:
                for hook in group["hooks"]:
                    yield event, hook

    def run_command(self, command, cwd, payload="{}", env=None):
        shell = bash()
        if not shell:
            self.skipTest("bash is not available")
        return subprocess.run([shell, "-c", command], cwd=cwd, input=payload, env=env or local_env(),
                              text=True, encoding="utf-8", capture_output=True, timeout=30)

    def invoke(self, name, payload=None, cwd=None, env=None):
        command = [sys.executable, str(self.root / ".claude/hooks/run-hook.py"), name]
        return subprocess.run(command, cwd=cwd or self.root, env=local_env(**(env or {})),
                              input=json.dumps(payload or {}), text=True, encoding="utf-8",
                              capture_output=True, timeout=10)

    def decision(self, inputs, tool="Bash", cwd=None):
        result = self.invoke("mount-guard", {"tool_name": tool,
                             "tool_input": inputs, "cwd": str(cwd or self.root)})
        self.assertEqual(result.returncode, 0, result.stderr)
        return bool(result.stdout and json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"] == "deny")

    # --- settings ------------------------------------------------------------

    def test_settings_shape(self):
        self.assertNotIn("outputStyle", self.settings)
        deny = self.settings["permissions"]["deny"]
        for rule in ("Edit(brain-system/**)", "Write(brain-system/**)"):
            self.assertIn(rule, deny)
        events = set(self.settings["hooks"])
        self.assertEqual(events, {"SessionStart", "UserPromptSubmit", "PreToolUse", "PostToolUse"})
        for event, hook in self.commands():
            with self.subTest(event=event):
                self.assertEqual(hook["shell"], "bash")
                self.assertIn("PY=python", hook["command"])
                self.assertNotIn("git-guard", hook["command"])
                self.assertNotIn("usage-log", hook["command"])

    # --- the launcher ----------------------------------------------------------

    def test_launcher_from_nested_directory(self):
        nested = self.root / "sub-context-docs"
        for event, hook in self.commands():
            result = self.run_command(hook["command"], nested)
            self.assertEqual(result.returncode, 0, (event, result.stderr))
            if event in {"UserPromptSubmit", "SessionStart"}:
                self.assertTrue(json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"])

    def test_launcher_does_not_cross_repository_boundaries(self):
        nested_repo = self.root / "nested-repo"
        nested_repo.mkdir()
        subprocess.run(["git", "init", "-q", str(nested_repo)], check=True)
        self.assert_hooks_skipped(nested_repo)

    def test_missing_dispatcher_is_a_successful_noop(self):
        (self.root / ".claude/hooks/run-hook.py").unlink()
        self.assert_hooks_skipped(self.root / "sub-context-docs")

    def test_launcher_outside_a_repository_is_a_successful_noop(self):
        with tempfile.TemporaryDirectory(prefix="brain no repository ") as directory:
            self.assert_hooks_skipped(Path(directory))

    def assert_hooks_skipped(self, cwd):
        for event, hook in self.commands():
            result = self.run_command(hook["command"], cwd)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")

    # --- mount-guard -----------------------------------------------------------

    def test_direct_shell_writes(self):
        if os.name == "nt":
            self.skipTest("POSIX shell syntax; Windows command shapes are tested separately")
        for command in (
            "printf fixture > brain-system/file.md",
            "printf fixture >> brain-system/file.md",
            "rm brain-system/source.md", "mv brain-system/source.md brand.md",
            "cp brand.md brain-system/source.md", "cp -t brain-system brand.md",
            "tee brain-system/file.md", "sed -i s/a/b/ brain-system/source.md",
            "cd brain-system && touch file.md", 'touch "brain-system/file with spaces.md"',
        ):
            with self.subTest(command=command):
                self.assertTrue(self.decision({"command": command}))
        for command in (
            "cat brain-system/source.md", "rg fixture brain-system",
            "cp brain-system/source.md brand.md", "git -C brain-system fetch origin",
            "git -C brain-system checkout v2", "printf fixture > brand.md",
        ):
            with self.subTest(command=command):
                self.assertFalse(self.decision({"command": command}))

    def test_file_tools_into_the_mount(self):
        for tool, key in (("Write", "file_path"), ("NotebookEdit", "notebook_path")):
            self.assertTrue(self.decision({key: "brain-system/source.md"}, tool))
        self.assertFalse(self.decision({"file_path": "brand-lens.md"}, "Write"))

    def test_symlink_target_and_unrelated_same_name(self):
        alias = self.root / "method-alias"
        try:
            alias.symlink_to(self.root / "brain-system", target_is_directory=True)
        except OSError as error:
            self.skipTest(f"Symlinks unavailable: {error}")
        self.assertTrue(self.decision({"file_path": "method-alias/file.md"}, "Write"))
        self.assertFalse(self.decision({"file_path": "examples/brain-system/file.md"}, "Write"))

    def test_windows_shell_targets(self):
        inspect = runpy.run_path(str(BUNDLE / "claude/hooks/mount-guard.py"))["shell_targets"]
        cases = {
            r"copy brand.md brain-system\file.md /A": r"brain-system\file.md",
            r"copy /B brand.md brain-system\file.md /b /Y": r"brain-system\file.md",
            r"move /Y brand.md brain-system\file.md": r"brain-system\file.md",
            r"del /F /Q brain-system\file.md": r"brain-system\file.md",
            r"erase /Q brain-system\file.md": r"brain-system\file.md",
            r"rd /S /Q brain-system\folder": r"brain-system\folder",
        }
        for command, target in cases.items():
            with self.subTest(command=command):
                targets = [path for path, cwd in inspect(command, self.root, windows=True)]
                self.assertIn(target, targets)
        command = r"copy brain-system\source.md brand.md /A"
        self.assertEqual(list(inspect(command, self.root, windows=True)), [("brand.md", self.root)])

    # --- craft-context ---------------------------------------------------------

    def test_full_catalog_and_profile_budget(self):
        result = self.invoke("craft-context")
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        source = (self.root / "brain-system/creative-strategy-context/expertise-routing.md").read_text(encoding="utf-8")
        for row in source.splitlines():
            if row.startswith("|") and ".md" in row:
                self.assertIn(row, context)
        self.assertIn("paths are relative to brain-system/creative-strategy-context/)", context)
        self.assertLessEqual(len(context.encode("utf-8")), self.limit)
        profile = self.root / "users/fixture/user-profile.md"
        profile.parent.mkdir(parents=True)
        profile.write_text("文" * 2500, encoding="utf-8")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Read users/fixture/user-profile.md in full", context)
        self.assertLessEqual(len(context.encode("utf-8")), self.limit)
        catalog = self.root / "brain-system/creative-strategy-context/expertise-routing.md"
        catalog.write_text("<!-- DOC-MAP:START -->\n" + "fixture " * 10000 + "\n<!-- DOC-MAP:END -->")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("catalog has not been injected", context)
        self.assertLessEqual(len(context.encode("utf-8")), self.limit)

    def test_multibyte_context_uses_a_conservative_token_bound(self):
        catalog = self.root / "brain-system/creative-strategy-context/expertise-routing.md"
        catalog.write_text("<!-- DOC-MAP:START -->\n" + "文" * 6000 + "\n<!-- DOC-MAP:END -->", encoding="utf-8")
        context = json.loads(self.invoke("craft-context").stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertLessEqual(len(context.encode("utf-8")), self.limit)
        self.assertIn("catalog has not been injected", context)

    # --- pull-log and session-start -------------------------------------------

    def test_pull_log_uses_brand_root_from_nested_directory(self):
        key = hashlib.sha256(str(self.root).encode()).hexdigest()[:16]
        log = Path(tempfile.gettempdir()) / f"parker-pull-log-{key}.jsonl"
        self.addCleanup(lambda: log.unlink(missing_ok=True))
        result = self.invoke("pull-log", {"tool_name": "mcp__fixture__read", "session_id": "fixture"}, self.root / "sub-context-docs")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(log.read_text(encoding="utf-8"))["tool"], "mcp__fixture__read")

    def test_session_start_gives_the_git_reminder(self):
        def context(**env):
            result = self.invoke("session-start", {}, env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]

        laptop = context()
        self.assertIn("shared: through git", laptop)
        self.assertIn("Never force-push", laptop)
        self.assertNotIn("Parker Desktop", laptop)
        cloud = context(CLAUDE_CODE_REMOTE="true")
        self.assertIn("this is a cloud run", cloud)
        self.assertIn("could not be saved", cloud)


if __name__ == "__main__":
    unittest.main()
