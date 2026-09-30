// Loads ui/app.js into a DOM-less Node context and renders real engine JSON
// with renderSandhi(). Run by tests/test_sandhi_ui.py; exits non-zero on a fault.
const fs = require("fs");
const vm = require("vm");
const root = require("path").join(__dirname, "..", "..", "ui", "app.js");
const src = fs.readFileSync(root, "utf8");
const noop = () => {};
const el = () => ({ addEventListener: noop, classList: { toggle: noop, add: noop, remove: noop }, style: {}, dataset: {}, setAttribute: noop, removeAttribute: noop, querySelector: () => null, querySelectorAll: () => [] });
const ctx = {
  console, setTimeout, clearTimeout, fetch: () => Promise.reject(new Error("no network in check")),
  document: { addEventListener: noop, querySelector: () => null, querySelectorAll: () => [], documentElement: el(), getElementById: () => null },
  window: { matchMedia: () => ({ matches: false, addEventListener: noop }), addEventListener: noop },
  location: { hash: "" },
  localStorage: { getItem: () => null, setItem: noop },
};
vm.createContext(ctx);
vm.runInContext(src + "\n;this.__api = { renderSandhi, renderSandhiStep, renderSandhiSplit };", ctx);
const payloads = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
let failures = 0;
for (const [text, data] of Object.entries(payloads)) {
  const html = ctx.__api.renderSandhi(data);
  const problems = [];
  if (/undefined|NaN|\[object/.test(html)) problems.push("leaks undefined/NaN/[object]");
  for (const o of data.outcomes) for (const s of o.steps) {
    if (!html.includes(`data-open-sutra="${s.sutra}"`)) problems.push(`no link for ${s.sutra}`);
    if (!html.includes(s.sutra_deva)) problems.push(`no devanagari text for ${s.sutra}`);
    if (!html.includes(s.sutra_iast)) problems.push(`no iast text for ${s.sutra}`);
  }
  for (const surface of data.surfaces_deva) if (!html.includes(surface)) problems.push(`result ${surface} missing`);
  if (data.outcomes.length > 1 && !/Derivation 2 of/.test(html)) problems.push("second derivation not labelled");
  console.log((problems.length ? "FAIL " : "ok   ") + text + "  (" + html.length + " chars)" + (problems.length ? "  " + problems.join("; ") : ""));
  failures += problems.length;
}
// an XSS-shaped input must be escaped, not interpreted
const evil = JSON.parse(JSON.stringify(payloads["iti ādi"]));
evil.surfaces = ["<img src=x onerror=alert(1)>"]; evil.surfaces_deva = ["<b>x</b>"];
const escaped = ctx.__api.renderSandhi(evil);
if (/<img|<b>x/.test(escaped)) { console.log("FAIL unescaped markup"); failures++; } else console.log("ok   markup in data is escaped");
// The split card, when a payload for it is given.
if (process.argv[3]) {
  const splits = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
  for (const data of splits) {
    const html = ctx.__api.renderSandhiSplit(data);
    const problems = [];
    if (/undefined|NaN|\[object/.test(html)) problems.push("leaks undefined/NaN/[object]");
    for (const item of data.splits || []) {
      for (const w of item.words) if (!html.includes(w)) problems.push(`word ${w} missing`);
      for (const s of item.derivation.steps) if (!html.includes(`data-open-sutra="${s.sutra}"`)) problems.push(`no link for ${s.sutra}`);
      if (!html.includes(item.validated ? "words known" : "unvalidated")) problems.push("validation pill missing");
    }
    console.log((problems.length ? "FAIL " : "ok   ") + "split of " + data.input + "  (" + html.length + " chars)" + (problems.length ? "  " + problems.join("; ") : ""));
    failures += problems.length;
  }
  const bad = JSON.parse(JSON.stringify(splits[0]));
  bad.splits[0].words = ["<script>alert(1)</script>"];
  if (/<script>alert/.test(ctx.__api.renderSandhiSplit(bad))) { console.log("FAIL unescaped split markup"); failures++; } else console.log("ok   markup in split data is escaped");
  const empty = ctx.__api.renderSandhiSplit({ input: "x", splits: [], note: "" });
  if (!/No split of/.test(empty)) { console.log("FAIL empty split message"); failures++; } else console.log("ok   an empty split result is explained");
}
process.exit(failures ? 1 : 0);
