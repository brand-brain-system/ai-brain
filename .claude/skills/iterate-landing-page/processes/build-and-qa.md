# Build and QA the iteration

## Build

1. Copy the editable source from `baseline/` into `working/`. The baseline stays untouched.
2. Preserve the source stack and component system when available. If the baseline is self-contained HTML, keep the iteration self-contained.
3. Apply the approved `change-plan.md`. Use one source of truth for changed copy and assets; do not patch generated output in multiple places.
4. Keep every unplanned section and shared system materially unchanged. A supporting change must already be named in the plan.
5. Name the output as a new version, never the original filename when both sit in the same folder.

## QA

1. Capture full desktop and phone screenshots of the iteration.
2. Compare baseline and iteration side by side with the shared `lp-compare.py` utility. Check every planned change and every preserve decision.
3. Run shared `lp-qa.mjs` against the new output. Treat regressions as failures. Keep pre-existing baseline failures in a separate list unless the direction asked to fix them.
4. Confirm:
   - every approved changed line appears exactly once and unchanged copy did not drift;
   - the CTA destinations, offer, proof, forms, analytics hooks, and interactions were preserved unless planned otherwise;
   - desktop and phone layouts work, with no new overflow or clipping;
   - local assets are present and self-contained output has no unintended remote dependency;
   - new claims, numbers, and quotes are sourced and allowed;
   - no new console errors or dead safe interactions were introduced.
5. Fix the editable source and rebuild. Never repair only the generated file.

Do not submit forms, complete purchases, follow destructive controls, or send data to live endpoints during QA.

