// motion.js: motion helpers for pages rendered frame by frame (window.seek(t)).
// Loaded as a classic script (file:// pages can't import ES modules), so everything hangs on window.M.
// Every function is a pure function of time: frame 812 renders without simulating frames 0-811.
// Springs, track() and swapAlpha() adapted from the motion-design course (movez Substack, Oct 2026).
(function () {
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const lerp = (a, b, p) => a + (b - a) * p;

  // Closed-form damped spring, 0 -> 1, starting at t = 0. k = stiffness, d = damping.
  function spring(t, k = 170, d = 26) {
    if (t <= 0) return 0;
    const w0 = Math.sqrt(k), z = d / (2 * w0);
    if (z < 1) {
      const wd = w0 * Math.sqrt(1 - z * z);
      return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t));
    }
    return 1 - Math.exp(-w0 * t) * (1 + w0 * t); // z >= 1 treated as critical
  }

  // Named feels. Use these instead of raw numbers so a whole film can be retuned in one place.
  const FEEL = {
    snappy:  [320, 30], // buttons, toggles, price hits, leading edges
    default: [170, 26], // cards, containers, the camera
    heavy:   [90, 19],  // big type, product hero, logo lockups: no visible overshoot
    playful: [220, 14], // stickers, badges: visible overshoot, use sparingly
  };
  const feel = (name) => FEEL[name] || FEEL.default;

  // A value that changes target several times: one spring per change, summed, so motion stays
  // continuous. keys: [[time, value], ...] sorted by time.
  function track(t, keys, name = 'default') {
    const [k, d] = feel(name);
    let v = keys[0][1];
    for (let i = 1; i < keys.length; i++) v += (keys[i][1] - keys[i - 1][1]) * spring(t - keys[i][0], k, d);
    return v;
  }

  // 0 -> 1 from time `at` with a named feel. The workhorse: M.in(t, 0.4, 'heavy').
  const enter = (t, at, name = 'default') => spring(t - at, ...feel(name));

  // Text inside a morphing box: in shortly after the morph starts, out just before the next one.
  const swapAlpha = (t, tIn, tOut) => Math.min(clamp((t - tIn - 0.08) / 0.12), clamp((tOut - 0.1 - t) / 0.1));

  // Seamless loop: map any t into [0, dur).
  const loopT = (t, dur) => ((t % dur) + dur) % dur;

  // Seeded random (mulberry32). Math.random is banned in render mode.
  function rng(seed) {
    return () => {
      seed |= 0; seed = seed + 0x6D2B79F5 | 0;
      let x = Math.imul(seed ^ seed >>> 15, 1 | seed);
      x = x + Math.imul(x ^ x >>> 7, 61 | x) ^ x;
      return ((x ^ x >>> 14) >>> 0) / 4294967296;
    };
  }

  // Words of a headline landing one by one: returns 0..1 per word index.
  const stagger = (t, at, i, gap = 0.07, name = 'snappy') => enter(t, at + i * gap, name);

  // Write transform + opacity to an element in one call. p: {x, y, s, r, o} (px, px, scale, deg, 0-1).
  function set(el, p) {
    const x = p.x || 0, y = p.y || 0, s = p.s === undefined ? 1 : p.s, r = p.r || 0;
    el.style.transform = `translate(${x}px, ${y}px) scale(${s}) rotate(${r}deg)`;
    el.style.opacity = p.o === undefined ? 1 : clamp(p.o);
  }

  window.M = { clamp, lerp, spring, FEEL, track, in: enter, enter, swapAlpha, loopT, rng, stagger, set };
})();
