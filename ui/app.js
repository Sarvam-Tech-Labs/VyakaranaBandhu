/*
 * Vyākaraṇa Toolkit — UI behaviour.
 *
 * Talks to the local server.py JSON API. Everything rendered here is built
 * from the engine's own output; nothing is invented client-side, and where a
 * field is missing the row is dropped rather than filled with a placeholder.
 */

/* ==================================================================== */
/* Small helpers                                                        */
/* ==================================================================== */

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

/** Escapes text for interpolation into an HTML template string. */
function esc(value) {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** True for values worth rendering a row for. */
function has(value) {
  if (value === null || value === undefined) return false;
  if (typeof value === "string") return value.trim() !== "";
  if (Array.isArray(value)) return value.length > 0;
  if (typeof value === "object") return Object.keys(value).length > 0;
  return true;
}

function announce(message) {
  $("#live-region").textContent = message;
}

async function api(path, body) {
  const response = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}

/** Renders a Banner for an engine/network failure. */
function errorBanner(message) {
  return `<div class="banner banner--error" role="alert">
    <strong>The engine could not complete that request.</strong> ${esc(message)}
  </div>`;
}

/** Wraps an async submit: disables the button, shows a pending label. */
async function withPending(button, pendingLabel, work) {
  const original = button.textContent;
  button.disabled = true;
  button.textContent = pendingLabel;
  try {
    await work();
  } finally {
    button.disabled = false;
    button.textContent = original;
  }
}

/* ==================================================================== */
/* Theme + reading size (same storage keys and behaviour as Prasadam)   */
/* ==================================================================== */

const THEME_KEY = "theme";
const READING_SIZE_KEY = "reading-size";
const THEME_LIGHT_COLOR = "#FEFCF8";
const THEME_DARK_COLOR = "#1A1412";

function applyTheme(theme) {
  const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const dark = theme === "dark" || (theme === "system" && systemPrefersDark);
  const el = document.documentElement;
  el.classList.toggle("dark", dark);
  el.style.colorScheme = dark ? "dark" : "light";
  const content = dark ? THEME_DARK_COLOR : THEME_LIGHT_COLOR;
  $$('meta[name="theme-color"]').forEach((m) => m.setAttribute("content", content));
}

function initThemeToggle() {
  const group = $(".theme-toggle");
  let current = "system";
  try {
    const stored = localStorage.getItem(THEME_KEY);
    if (stored === "light" || stored === "dark" || stored === "system") current = stored;
  } catch (_) {}

  const paint = () =>
    $$("button", group).forEach((b) =>
      b.setAttribute("aria-pressed", String(b.dataset.theme === current))
    );
  paint();

  group.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    current = button.dataset.theme;
    try {
      localStorage.setItem(THEME_KEY, current);
    } catch (_) {
      /* private mode — apply anyway */
    }
    applyTheme(current);
    paint();
  });

  // When following the system, re-apply on OS scheme changes.
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (current === "system") applyTheme("system");
  });
}

function initReadingSizeToggle() {
  const group = $(".reading-size");
  let current = "default";
  try {
    const stored = localStorage.getItem(READING_SIZE_KEY);
    if (stored === "lg" || stored === "xl") current = stored;
  } catch (_) {}

  const paint = () =>
    $$("button", group).forEach((b) =>
      b.setAttribute("aria-pressed", String(b.dataset.size === current))
    );
  paint();

  group.addEventListener("click", (event) => {
    const button = event.target.closest("button");
    if (!button) return;
    current = button.dataset.size;
    try {
      localStorage.setItem(READING_SIZE_KEY, current);
    } catch (_) {}
    if (current === "default") delete document.documentElement.dataset.readingSize;
    else document.documentElement.dataset.readingSize = current;
    paint();
  });
}

/* ==================================================================== */
/* Routing — the header nav switches sections                           */
/* ==================================================================== */

const ROUTES = ["classifier", "subanta", "reverse", "tinanta", "krdanta", "chandas", "astadhyayi"];

function showRoute(route) {
  const target = ROUTES.includes(route) ? route : ROUTES[0];
  // A prakriyā opened from the paradigm belongs to that section only.
  closeModal();
  $$("[data-page]").forEach((page) => {
    page.hidden = page.dataset.page !== target;
  });
  $$(".site-nav__link").forEach((link) => {
    if (link.dataset.route === target) link.setAttribute("aria-current", "page");
    else link.removeAttribute("aria-current");
  });
}

function initRouting() {
  const fromHash = () => showRoute(location.hash.replace("#", ""));
  window.addEventListener("hashchange", fromHash);
  fromHash();
}

/* ==================================================================== */
/* Shared render fragments                                              */
/* ==================================================================== */

function pill(text, tone = "neutral") {
  return `<span class="pill${tone === "neutral" ? "" : ` pill--${tone}`}">${esc(text)}</span>`;
}

function stat(label, value, sub, accent) {
  return `<div class="stat${accent ? ` stat--${accent}` : ""}">
    <p class="stat__label">${esc(label)}</p>
    <p class="stat__value">${esc(value)}</p>
    ${sub ? `<p class="stat__sub">${esc(sub)}</p>` : ""}
  </div>`;
}

/** Humanises an engine key like "ajanta_a_masculine" for display. */
function humanise(key) {
  if (!has(key)) return "";
  const spaced = String(key).replace(/_/g, " ");
  return spaced.charAt(0).toUpperCase() + spaced.slice(1);
}

/** A label-above-value definition row. Returns "" when the value is empty. */
function def(label, value) {
  if (!has(value)) return "";
  return `<div>
    <p class="def__label">${esc(label)}</p>
    <p class="def__value">${esc(value)}</p>
  </div>`;
}

/** An apparatus layer inside a verse card. */
function layer(label, value, deva) {
  if (!has(value)) return "";
  return `<div class="layer-row">
    <p class="layer-row__label">${esc(label)}</p>
    <p class="layer-row__value${deva ? " font-devanagari" : ""}">${esc(value)}</p>
  </div>`;
}

/** The shared derivation timeline used by prakriyā, kṛdanta, and taddhita. */
function timeline(steps, { formKey = "string", descKey = "explanation" } = {}) {
  if (!has(steps)) return "";
  return `<ol class="timeline">
    ${steps
      .map((step) => {
        const stage = [step.stage, step.regime, step.rule_type].filter(has).join(" · ");
        return `<li class="timeline__step">
          <div class="timeline__meta">
            <span class="timeline__form font-devanagari-serif">${esc(step[formKey] || step.form)}</span>
            ${has(step.sutra) ? `<span class="timeline__sutra">${esc(step.sutra)}</span>` : ""}
          </div>
          ${stage ? `<p class="timeline__sutra">${esc(stage)}</p>` : ""}
          ${has(step[descKey] || step.desc) ? `<p class="timeline__desc">${esc(step[descKey] || step.desc)}</p>` : ""}
          ${has(step.hnv) ? `<p class="timeline__desc italic">Harināmāmṛta: ${esc(step.hnv)}</p>` : ""}
        </li>`;
      })
      .join("")}
  </ol>`;
}

/* ==================================================================== */
/* 1. Classifier & verse analysis                                       */
/* ==================================================================== */

/** Maps a predicted class onto a Pill tone. Tones carry meaning, not decoration. */
function classTone(predicted) {
  if (predicted === "Both") return "primary";
  if (predicted === "None") return "neutral";
  return "info";
}

function renderSingleWord(result) {
  const probabilities = result.ml_probabilities || {};
  const rows = Object.entries(probabilities).sort((a, b) => b[1] - a[1]);

  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(result.devanagari)}</p>
        <p class="result-headline-latin">${esc(result.iast)}</p>
      </div>
      <div class="row">
        ${pill(result.predicted_class, classTone(result.predicted_class))}
        ${has(result.confidence) ? pill(`${(result.confidence * 100).toFixed(1)}% confidence`, "neutral") : ""}
      </div>
    </div>

    <div class="def-list def-list--2 mt-4">
      ${def("Subtype", result.subtype)}
      ${def("Rule", result.rule_name)}
      ${def("Sūtra", result.sutra)}
      ${def("Padaccheda", result.padacheda)}
      ${def("Vigraha", result.samasa)}
      ${def("Meaning", result.meaning)}
    </div>

    ${
      has(result.explanation)
        ? `<p class="help-text leading-relaxed mt-4">${esc(result.explanation)}</p>`
        : ""
    }

    ${
      has(result.prakriti_pratyaya)
        ? `<div class="mt-4">
            <h3 class="section-subheading">Prakṛti + pratyaya</h3>
            <p class="layer-row__value font-devanagari">${esc(result.prakriti_pratyaya.formula_dev)}</p>
            <p class="help-text">${esc(result.prakriti_pratyaya.formula_iast)} — ${esc(result.prakriti_pratyaya.analysis)}</p>
          </div>`
        : ""
    }

    ${
      has(result.splits)
        ? `<div class="mt-4">
            <h3 class="section-subheading">Constituent split</h3>
            <div class="token-grid">
              ${result.splits
                .map(
                  (split) => `<div class="token-card">
                    <p class="token-card__deva">${esc(split.left_dev)} + ${esc(split.right_dev)}</p>
                    <p class="text-xs muted">${esc(split.left_iast)} + ${esc(split.right_iast)}</p>
                    ${has(split.description) ? `<p class="timeline__desc mt-2">${esc(split.description)}</p>` : ""}
                  </div>`
                )
                .join("")}
            </div>
          </div>`
        : ""
    }

    ${
      has(result.sandhi_steps)
        ? `<div class="mt-4">
            <h3 class="section-subheading">Sandhi steps</h3>
            <ul class="timeline">
              ${result.sandhi_steps
                .map((s) => `<li class="timeline__step"><p class="timeline__desc">${esc(s)}</p></li>`)
                .join("")}
            </ul>
          </div>`
        : ""
    }

    ${
      has(result.deep_commentary)
        ? `<div class="mt-4">
            <h3 class="section-subheading">Commentary</h3>
            <p class="help-text leading-relaxed">${esc(result.deep_commentary)}</p>
          </div>`
        : ""
    }

    ${
      rows.length
        ? `<div class="mt-4">
            <h3 class="section-subheading">Model probabilities</h3>
            <div class="table-scroll mt-2">
              <table class="data-table" style="min-width: 20rem">
                <thead><tr><th>Class</th><th>Probability</th></tr></thead>
                <tbody>
                  ${rows
                    .map(
                      ([name, p]) =>
                        `<tr><td>${esc(name)}</td><td style="font-variant-numeric: tabular-nums">${(p * 100).toFixed(2)}%</td></tr>`
                    )
                    .join("")}
                </tbody>
              </table>
            </div>
          </div>`
        : ""
    }
  </div>`;
}

function renderViseshyaMap(map) {
  if (!has(map) || !has(map.relationships)) return "";
  return `<div class="card card--pad">
    <h2 class="section-heading">Viśeṣya–viśeṣaṇa concord</h2>
    <p class="help-text">
      ${esc(map.total_pairs_identified)} agreement group${map.total_pairs_identified === 1 ? "" : "s"}
      identified by shared vibhakti, vacana, and liṅga.
    </p>
    <div class="token-grid">
      ${map.relationships
        .map(
          (rel) => `<div class="token-card">
            <p class="token-card__deva">${esc(rel.viseshya.pada_devanagari)}</p>
            <p class="text-xs muted">${esc(rel.viseshya.pada_iast)} — ${esc(rel.viseshya.role)}</p>
            <p class="text-xs muted mt-2">${esc(rel.concord)} · ${esc(rel.karaka_role)}</p>
            <div class="row mt-2">
              ${rel.viseshanas.map((v) => pill(v.pada_devanagari, "info")).join("")}
            </div>
            ${has(rel.karaka_sutra) ? `<p class="timeline__sutra mt-2">${esc(rel.karaka_sutra)}</p>` : ""}
          </div>`
        )
        .join("")}
    </div>
  </div>`;
}

/**
 * Dependency diagram, drawn from the engine's nodes/edges rather than its
 * bundled SVG — that one ships a hardcoded dark-violet canvas that would
 * clash with the palette in both themes.
 */
function renderDependencyGraph(tree) {
  if (!has(tree) || !has(tree.nodes)) return "";

  const rootId = tree.root_verb;
  const root = tree.nodes.find((n) => n.id === rootId || n.is_verb) || tree.nodes[0];
  const others = tree.nodes.filter((n) => n !== root);

  const NODE_W = 150;
  const NODE_H = 52;
  const GAP_X = 22;
  const perRow = Math.min(4, Math.max(1, others.length));
  const rows = Math.ceil(others.length / perRow) || 1;
  const width = Math.max(perRow * (NODE_W + GAP_X) + GAP_X, 520);
  const rowGap = 96;
  const height = 90 + rows * rowGap + 20;
  const rootX = width / 2 - NODE_W / 2;
  const rootY = 16;

  const relationOf = (id) => {
    const edge = (tree.edges || []).find((e) => e.to === id || e.from === id);
    return edge ? edge.relation : "";
  };

  const box = (node, x, y, isRoot) => `
    <g>
      <rect x="${x}" y="${y}" rx="12" ry="12" width="${NODE_W}" height="${NODE_H}"
            fill="${isRoot ? "var(--color-primary-container)" : "var(--color-surface)"}"
            stroke="${isRoot ? "var(--color-primary)" : "var(--color-outline-variant)"}" stroke-width="1.5" />
      <text x="${x + NODE_W / 2}" y="${y + 22}" text-anchor="middle"
            font-family="var(--font-devanagari-serif)" font-size="16"
            fill="${isRoot ? "var(--color-on-primary-container)" : "var(--color-on-surface)"}">${esc(node.text_devanagari)}</text>
      <text x="${x + NODE_W / 2}" y="${y + 40}" text-anchor="middle"
            font-family="var(--font-sans)" font-size="10.5"
            fill="var(--color-on-surface-variant)">${esc(node.karaka_label || node.role || "")}</text>
    </g>`;

  const children = others
    .map((node, i) => {
      const row = Math.floor(i / perRow);
      const col = i % perRow;
      const inRow = Math.min(perRow, others.length - row * perRow);
      const rowWidth = inRow * NODE_W + (inRow - 1) * GAP_X;
      const x = (width - rowWidth) / 2 + col * (NODE_W + GAP_X);
      const y = 90 + row * rowGap;
      const startX = rootX + NODE_W / 2;
      const startY = rootY + NODE_H;
      const endX = x + NODE_W / 2;
      const midY = (startY + y) / 2;
      const relation = relationOf(node.id);
      return `
        <path d="M ${startX} ${startY} C ${startX} ${midY}, ${endX} ${midY}, ${endX} ${y}"
              fill="none" stroke="var(--color-outline-variant)" stroke-width="1.5" />
        ${
          relation
            ? `<text x="${endX}" y="${y - 8}" text-anchor="middle" font-family="var(--font-sans)"
                 font-size="10" fill="var(--color-on-surface-variant)">${esc(relation)}</text>`
            : ""
        }
        ${box(node, x, y, false)}`;
    })
    .join("");

  return `<div class="card card--pad">
    <h2 class="section-heading">Kāraka dependency</h2>
    ${has(tree.anvaya_prose) ? `<p class="layer-row__value font-devanagari">${esc(tree.anvaya_prose)}</p>` : ""}
    ${has(tree.anvaya_english) ? `<p class="help-text">${esc(tree.anvaya_english)}</p>` : ""}
    <div class="graph-host">
      <svg viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" role="img"
           aria-label="Kāraka dependency diagram">
        ${box(root, rootX, rootY, true)}
        ${children}
      </svg>
    </div>
  </div>`;
}

function renderVerse(result) {
  const summary = result.class_summary || {};
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(result.devanagari)}</p>
        <p class="result-headline-latin">${esc(result.iast)}</p>
      </div>
      <div class="row">
        ${pill("Verse", "primary")}
        ${has(result.meter) ? pill(result.meter, "info") : ""}
      </div>
    </div>

    <div class="grid-auto mt-4">
      ${stat("Words", result.token_count, null, "primary")}
      ${stat("Both", summary["Both"] ?? 0, "sandhi + samāsa")}
      ${stat("Sandhi only", summary["Sandhi Only"] ?? 0)}
      ${stat("Samāsa only", summary["Samāsa Only"] ?? 0)}
      ${stat("Neither", summary["None"] ?? 0)}
    </div>

    <div class="mt-6">
      ${layer("Anvaya (prose order)", result.anvaya, true)}
      ${layer("Anvaya — IAST", result.anvaya_iast, false)}
      ${layer("Padaccheda", result.full_padacheda, true)}
      ${layer("Prakṛti + pratyaya pipeline", result.prakriti_pratyaya_pipeline, true)}
    </div>
  </div>

  ${renderViseshyaMap(result.viseshya_viseshana_map)}

  <div class="card card--pad">
    <h2 class="section-heading">Word by word</h2>
    <p class="help-text">Each pada classified independently, with its own sūtra citation.</p>
    <div class="token-grid">
      ${(result.token_results || [])
        .map(
          (token) => `<div class="token-card">
            <p class="token-card__deva">${esc(token.devanagari)}</p>
            <p class="text-xs muted">${esc(token.iast)}</p>
            <div class="row mt-2">${pill(token.predicted_class, classTone(token.predicted_class))}</div>
            ${has(token.subtype) ? `<p class="text-xs muted mt-2">${esc(token.subtype)}</p>` : ""}
            ${has(token.padacheda) ? `<p class="text-sm mt-2 font-devanagari">${esc(token.padacheda)}</p>` : ""}
            ${has(token.sutra) ? `<p class="timeline__sutra mt-2">${esc(token.sutra)}</p>` : ""}
          </div>`
        )
        .join("")}
    </div>
  </div>`;
}

function initClassifier() {
  const form = $("#classify-form");
  const input = $("#classify-input");
  const count = $("#classify-count");
  const output = $("#classify-output");
  const submit = $("#classify-submit");

  input.addEventListener("input", () => {
    count.textContent = `${input.value.length.toLocaleString("en-IN")} / 4,000`;
  });

  $("#classify-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-example]");
    if (!button) return;
    input.value = button.dataset.example;
    count.textContent = `${input.value.length.toLocaleString("en-IN")} / 4,000`;
    output.innerHTML = "";
    input.focus();
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text) {
      output.innerHTML = `<div class="banner banner--warn">Enter some Sanskrit first.</div>`;
      return;
    }

    await withPending(submit, "Analysing grammar…", async () => {
      try {
        const result = await api("/api/classify", { text });
        if (result.is_verse) {
          output.innerHTML = renderVerse(result);
          announce(`Verse analysed: ${result.token_count} words, metre ${result.meter}.`);
          // The dependency tree is a second engine pass; append it once ready
          // so the verse apparatus is readable immediately.
          try {
            const tree = await api("/api/verse/dependency_tree", { verse: text });
            output.insertAdjacentHTML("beforeend", renderDependencyGraph(tree));
          } catch (_) {
            /* the apparatus above stands on its own without the diagram */
          }
        } else {
          output.innerHTML = renderSingleWord(result);
          announce(`Classified as ${result.predicted_class}.`);
        }
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  });
}

/* ==================================================================== */
/* 2. Śabdarūpa generator                                               */
/* ==================================================================== */

let currentParadigm = null;

function renderParadigm(data) {
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(data.stem_devanagari)}</p>
        <p class="result-headline-latin">${esc(data.stem_iast)}</p>
      </div>
      <div class="row">
        ${pill(humanise(data.gender), "primary")}
        ${pill(humanise(data.paradigm), "info")}
        ${pill(`${data.total_cells} forms`)}
      </div>
    </div>

    <p class="help-text mt-4">
      Select any form to replay its derivation, sup affix, and commentary concordance.
    </p>

    <div class="table-scroll mt-4">
      <table class="data-table">
        <thead>
          <tr>
            <th>Vibhakti</th>
            <th>Ekavacana</th>
            <th>Dvivacana</th>
            <th>Bahuvacana</th>
          </tr>
        </thead>
        <tbody>
          ${data.table
            .map(
              (row) => `<tr>
                <td>
                  <p class="medium">${esc(row.vibhakti)}</p>
                  <p class="text-xs muted">${esc(row.karaka_role)}</p>
                  <p class="timeline__sutra">${esc(row.karaka_sutra)}</p>
                </td>
                ${row.forms
                  .map(
                    (cell) => `<td>
                      <button type="button" class="cell-btn"
                              data-vibhakti="${esc(row.vibhakti_idx)}" data-vacana="${esc(cell.vacana_idx)}"
                              title="Open the prakriyā for ${esc(cell.iast)}">
                        <span class="cell-btn__deva font-devanagari">${esc(cell.devanagari)}</span>
                        <span class="cell-btn__iast" style="display:block">${esc(cell.iast)}</span>
                        <span class="timeline__sutra" style="display:block">${esc(cell.raw_sup_dev)} · ${esc(cell.sutra)}</span>
                      </button>
                    </td>`
                  )
                  .join("")}
              </tr>`
            )
            .join("")}
        </tbody>
      </table>
    </div>
  </div>`;
}

function initSubanta() {
  const form = $("#subanta-form");
  const stemInput = $("#subanta-stem");
  const genderSelect = $("#subanta-gender");
  const output = $("#subanta-output");

  async function generate() {
    const stem = stemInput.value.trim();
    if (!stem) {
      output.innerHTML = `<div class="banner banner--warn">Enter a prātipadika first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", form);
    await withPending(submit, "Generating…", async () => {
      try {
        const data = await api("/api/subanta/generate", {
          stem,
          gender: genderSelect.value || null,
        });
        if (data.error) {
          output.innerHTML = errorBanner(data.error);
          return;
        }
        currentParadigm = { stem, gender: genderSelect.value || null };
        output.innerHTML = renderParadigm(data);
        announce(`Paradigm generated for ${data.stem_iast}: ${data.total_cells} forms.`);
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    generate();
  });

  $("#subanta-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-stem]");
    if (!button) return;
    stemInput.value = button.dataset.stem;
    genderSelect.value = button.dataset.gender || "";
    generate();
  });

  // Cell -> prakriyā modal.
  output.addEventListener("click", (event) => {
    const cell = event.target.closest(".cell-btn");
    if (!cell || !currentParadigm) return;
    openPrakriya(
      currentParadigm.stem,
      currentParadigm.gender,
      Number(cell.dataset.vibhakti),
      Number(cell.dataset.vacana)
    );
  });
}

/* ==================================================================== */
/* Prakriyā modal                                                       */
/* ==================================================================== */

let modalPada = null;

function renderConcordance(concordance) {
  if (!has(concordance) || !has(concordance.concordance_steps)) return "";
  return `<div>
    <h3 class="section-heading">Four-commentary concordance</h3>
    <p class="help-text">
      The same derivation step read by the Aṣṭādhyāyī, the Mahābhāṣya, the Harināmāmṛta, and the
      Bāla-toṣaṇī, with the reconciliation each pass yields.
    </p>
    <div class="stack-sm mt-3">
      ${concordance.concordance_steps
        .map(
          (step) => `<div class="concordance-step">
            <div class="timeline__meta">
              <span class="timeline__form font-devanagari-serif">${esc(step.intermediate_string)}</span>
              <span class="timeline__sutra">Step ${esc(step.step)} · ${esc(step.stage)}</span>
            </div>
            <div class="concordance-grid">
              <div class="concordance-lens concordance-lens--p1">
                <p class="def__label">Aṣṭādhyāyī</p>
                <p class="text-xs">${esc(step.p1_astadhyayi.sutra)}</p>
                <p class="text-xs muted">${esc(step.p1_astadhyayi.type)} · ${esc(step.p1_astadhyayi.regime)}</p>
              </div>
              <div class="concordance-lens concordance-lens--p2">
                <p class="def__label">Mahābhāṣya</p>
                <p class="text-xs">${esc(step.p2_mahabhashya.jurisprudence)}</p>
                <p class="text-xs muted">${esc(step.p2_mahabhashya.stem_grade)}</p>
              </div>
              <div class="concordance-lens concordance-lens--p3">
                <p class="def__label">Harināmāmṛta</p>
                <p class="text-xs">${esc(step.p3_harinamamrita.sutra_principle)}</p>
                <p class="text-xs muted">${esc(step.p3_harinamamrita.affix_bhakti)}</p>
              </div>
              <div class="concordance-lens concordance-lens--p4">
                <p class="def__label">Bāla-toṣaṇī</p>
                <p class="text-xs">${esc(step.p4_bala_toshani.exegesis)}</p>
                <p class="text-xs muted">${esc(step.p4_bala_toshani.cosmology)}</p>
              </div>
            </div>
            ${
              has(step.reconciliation_verdict)
                ? `<p class="timeline__desc mt-2">${esc(step.reconciliation_verdict)}</p>`
                : ""
            }
          </div>`
        )
        .join("")}
    </div>
    ${
      has(concordance.grand_verdict)
        ? `<div class="banner banner--success mt-3">${esc(concordance.grand_verdict)}</div>`
        : ""
    }
  </div>`;
}

async function openPrakriya(stem, gender, vibhaktiIdx, vacanaIdx) {
  const scrim = $("#modal-scrim");
  const body = $("#modal-body");
  scrim.hidden = false;
  document.body.style.overflow = "hidden";
  body.innerHTML = `<p class="help-text">Replaying the derivation…</p>`;

  try {
    const data = await api("/api/subanta/prakriya", {
      stem,
      gender,
      vibhakti_idx: vibhaktiIdx,
      vacana_idx: vacanaIdx,
    });

    modalPada = data.final_pada_iast;
    $("#modal-slot").textContent = `${data.vibhakti} · ${data.vacana}`;
    $("#modal-title").textContent = data.final_pada_devanagari;
    $("#modal-title-latin").textContent = data.final_pada_iast;

    const hnv = data.hnv_prakriya || {};
    body.innerHTML = `
      <div class="def-list def-list--2">
        ${def("Stem", `${data.stem_devanagari} (${data.stem_iast})`)}
        ${def("Gender / paradigm", `${humanise(data.gender)} · ${humanise(data.paradigm)}`)}
        ${def("Raw sup affix", `${data.raw_sup_dev} (${data.raw_sup})`)}
        ${def("Steps", data.total_steps)}
      </div>

      ${
        has(data.stem_grade)
          ? `<div class="note-box" style="display:block">
              <p class="def__label">Aṅga grade</p>
              <p class="def__value">${esc(data.stem_grade.grade)} — ${esc(data.stem_grade.sutra)}</p>
              <p class="timeline__desc">${esc(data.stem_grade.desc)}</p>
            </div>`
          : ""
      }

      ${
        has(data.karaka_info)
          ? `<div class="note-box" style="display:block">
              <p class="def__label">Kāraka</p>
              <p class="def__value">${esc(data.karaka_info.role)} — ${esc(data.karaka_info.sutra)}</p>
              <p class="timeline__desc">${esc(data.karaka_info.meaning)}</p>
            </div>`
          : ""
      }

      <div>
        <h3 class="section-heading">Derivation</h3>
        ${timeline(data.derivation_steps)}
      </div>

      ${
        has(hnv)
          ? `<details class="note-box">
              <summary>Harināmāmṛta reading</summary>
              <div class="def-list def-list--2 mt-2">
                ${def("Treatise", hnv.treatise)}
                ${def("Nārāyaṇa base", hnv.narayana_base)}
                ${def("Viṣṇubhakti affix", hnv.visnubhakti_affix)}
                ${def("Category", hnv.visnubhakti_category)}
                ${def("Relationship", hnv.bhakti_relationship)}
                ${def("Saṅketa operation", hnv.sanketa_operation)}
                ${def("Completed viṣṇupada", hnv.completed_visnupada)}
              </div>
              ${has(hnv.bala_toshani_exegesis) ? `<p class="timeline__desc mt-2">${esc(hnv.bala_toshani_exegesis)}</p>` : ""}
              ${has(hnv.theological_meditation) ? `<p class="timeline__desc italic mt-2">${esc(hnv.theological_meditation)}</p>` : ""}
            </details>`
          : ""
      }

      <div id="modal-concordance"><p class="help-text">Loading the concordance…</p></div>
    `;

    try {
      const concordance = await api("/api/subanta/concordance", {
        stem,
        gender,
        vibhakti_idx: vibhaktiIdx,
        vacana_idx: vacanaIdx,
      });
      $("#modal-concordance").innerHTML = renderConcordance(concordance);
    } catch (_) {
      $("#modal-concordance").innerHTML = "";
    }
  } catch (error) {
    body.innerHTML = errorBanner(error.message);
  }
}

function closeModal() {
  $("#modal-scrim").hidden = true;
  document.body.style.overflow = "";
}

function initModal() {
  $("#modal-close").addEventListener("click", closeModal);
  $("#modal-scrim").addEventListener("click", (event) => {
    if (event.target === $("#modal-scrim")) closeModal();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !$("#modal-scrim").hidden) closeModal();
  });
  $("#modal-export").addEventListener("click", () => {
    if (modalPada) downloadDossier(modalPada, "markdown");
  });
}

/* ==================================================================== */
/* 3. Reverse pada analysis                                             */
/* ==================================================================== */

async function downloadDossier(pada, format) {
  try {
    const result = await api("/api/dossier/export", { pada, format });
    const content = result.content || "";
    const extension = format === "html" ? "html" : "md";
    const type = format === "html" ? "text/html" : "text/markdown";
    const url = URL.createObjectURL(new Blob([content], { type: `${type};charset=utf-8` }));
    const link = document.createElement("a");
    link.href = url;
    link.download = `${pada}-brief.${extension}`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    announce(`Brief for ${pada} downloaded.`);
  } catch (error) {
    announce(`Could not export the brief: ${error.message}`);
  }
}

function renderReading(reading, index) {
  const defense = reading.legal_defense || {};
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="text-lg medium">
          <span class="font-devanagari-serif">${esc(reading.stem_devanagari)}</span>
          <span class="muted text-sm"> ${esc(reading.stem_iast)}</span>
        </p>
        <p class="text-sm muted">${esc(reading.vibhakti)} · ${esc(reading.vacana)}</p>
      </div>
      <div class="row">
        ${pill(`Reading ${index + 1}`, "primary")}
        ${pill(humanise(reading.gender))}
      </div>
    </div>

    <div class="def-list def-list--2 mt-4">
      ${def("Governing sūtra", reading.sutra)}
      ${def("Base authority", defense.base_authority)}
      ${def("Kāraka jurisdiction", defense.karaka_jurisdiction)}
      ${def("Gender proof", defense.gender_proof)}
      ${has(defense.stem_grade) ? def("Aṅga grade", `${defense.stem_grade.grade} — ${defense.stem_grade.sutra}`) : ""}
    </div>

    ${has(defense.pratijna) ? `<p class="timeline__desc italic mt-4">${esc(defense.pratijna)}</p>` : ""}

    ${
      has(defense.statutes)
        ? `<details class="note-box mt-4">
            <summary>Statutes relied on (${defense.statutes.length})</summary>
            <div class="stack-sm mt-2">
              ${defense.statutes
                .map(
                  (s) => `<div>
                    <p class="def__value"><span class="font-devanagari">${esc(s.sutra_dev)}</span> — ${esc(s.sutra)}</p>
                    <p class="timeline__sutra">${esc(s.type)}</p>
                    <p class="timeline__desc">${esc(s.function)}</p>
                  </div>`
                )
                .join("")}
            </div>
          </details>`
        : ""
    }

    ${
      has(defense.mahabhashya_dialectic)
        ? `<details class="note-box mt-2">
            <summary>Mahābhāṣya dialectic</summary>
            <div class="stack-sm mt-2">
              ${Object.entries(defense.mahabhashya_dialectic)
                .map(([k, v]) => def(k.replace(/_/g, " "), v))
                .join("")}
            </div>
          </details>`
        : ""
    }

    ${
      has(defense.hnv_lens)
        ? `<details class="note-box mt-2">
            <summary>Harināmāmṛta lens</summary>
            <div class="stack-sm mt-2">
              ${Object.entries(defense.hnv_lens)
                .map(([k, v]) => def(k.replace(/_/g, " "), v))
                .join("")}
            </div>
          </details>`
        : ""
    }

    ${has(defense.verdict) ? `<div class="banner banner--success mt-4">${esc(defense.verdict)}</div>` : ""}
  </div>`;
}

function initReverse() {
  const form = $("#reverse-form");
  const input = $("#reverse-input");
  const output = $("#reverse-output");

  async function analyse() {
    const pada = input.value.trim();
    if (!pada) {
      output.innerHTML = `<div class="banner banner--warn">Enter an inflected pada first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", form);
    await withPending(submit, "Analysing…", async () => {
      try {
        const data = await api("/api/subanta/analyze", { pada });
        const readings = data.analyses || [];
        if (!readings.length) {
          output.innerHTML = `<div class="empty-state">
            No supported reading for <strong>${esc(pada)}</strong>.
            <p class="empty-state__hint">
              The pada is left unanalysed rather than matched to the nearest paradigm. Try a form
              built on one of the stems the generator supports.
            </p>
          </div>`;
          announce(`No supported reading for ${pada}.`);
          return;
        }
        output.innerHTML = `
          <div class="card card--pad">
            <div class="result-head">
              <div>
                <p class="result-headline font-devanagari-serif">${esc(pada)}</p>
                <p class="result-headline-latin">${readings.length} supported reading${readings.length === 1 ? "" : "s"}</p>
              </div>
              <div class="row">
                <button type="button" class="btn btn--secondary btn--sm" data-export="markdown">
                  Markdown brief
                </button>
                <button type="button" class="btn btn--secondary btn--sm" data-export="html">
                  Printable HTML
                </button>
              </div>
            </div>
          </div>
          ${readings.map(renderReading).join("")}`;
        announce(`${readings.length} reading(s) for ${pada}.`);

        $$("[data-export]", output).forEach((button) =>
          button.addEventListener("click", () => downloadDossier(pada, button.dataset.export))
        );
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    analyse();
  });

  $("#reverse-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-pada]");
    if (!button) return;
    input.value = button.dataset.pada;
    analyse();
  });
}

/* ==================================================================== */
/* 4. Tiṅanta conjugator                                                */
/* ==================================================================== */

/** A derivation payload from prakriya_payload() → the shared timeline()'s shape. */
function derivationSteps(derivation) {
  const start = {
    form: `${derivation.start_devanagari} (${derivation.start_iast})`,
    sutra: "",
    desc: "The root as the dhātupāṭha enunciates it — upadeśa, it-letters and all.",
  };
  const steps = derivation.steps.map((step) => ({
    form: `${step.after_devanagari} (${step.after_iast})`,
    sutra: step.sutra,
    desc: step.what,
  }));
  return [start, ...steps];
}

/** One dhātupāṭha entry, conjugated — its own card with a 3×3 table. */
function renderTinantaEntry(entry) {
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(entry.root_devanagari)}</p>
        <p class="result-headline-latin">${esc(entry.root_iast)} — ${esc(entry.artha)}</p>
      </div>
      <div class="row">
        ${pill(entry.code, "primary")}
        ${pill(entry.gana_name, "info")}
        ${pill(entry.pada_type)}
      </div>
    </div>

    <div class="def-list def-list--2 mt-4">
      ${def("Enunciated (upadeśa)", `${entry.upadesa_devanagari} (${entry.upadesa_iast})`)}
      ${def("Lakāra", "Laṭ — present")}
    </div>

    <div class="table-scroll mt-4">
      <table class="data-table">
        <thead>
          <tr>
            <th>Puruṣa</th>
            <th>Ekavacana</th>
            <th>Dvivacana</th>
            <th>Bahuvacana</th>
          </tr>
        </thead>
        <tbody>
          ${entry.table
            .map(
              (row) => `<tr>
                <td><p class="medium">${esc(row.purusha)}</p></td>
                ${row.forms
                  .map((cell) =>
                    cell.withheld
                      ? `<td><p class="timeline__sutra">withheld — a further sūtra is not yet wired</p></td>`
                      : `<td>
                          <p class="cell-btn__deva font-devanagari">${esc(cell.devanagari)}</p>
                          <p class="cell-btn__iast">${esc(cell.iast)}</p>
                          <details class="note-box mt-2">
                            <summary>Derivation (${cell.derivation.steps.length} sūtras)</summary>
                            <div class="mt-2">${timeline(derivationSteps(cell.derivation))}</div>
                          </details>
                        </td>`
                  )
                  .join("")}
              </tr>`
            )
            .join("")}
        </tbody>
      </table>
    </div>
  </div>`;
}

/** One root the reverse search traced a word back to. */
function renderTinantaMatch(match) {
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(match.root_devanagari)}</p>
        <p class="result-headline-latin">${esc(match.root_iast)} — ${esc(match.artha)}</p>
      </div>
      <div class="row">
        ${pill(match.code, "primary")}
        ${pill(match.gana_name, "info")}
        ${pill(match.pada_type)}
      </div>
    </div>

    <div class="def-list def-list--2 mt-4">
      ${def("Enunciated (upadeśa)", `${match.upadesa_devanagari} (${match.upadesa_iast})`)}
      ${def("Slot", `${match.purusha}, ${match.vacana}`)}
    </div>

    <details class="note-box mt-4" open>
      <summary>Derivation (${match.derivation.steps.length} sūtras)</summary>
      <div class="mt-2">${timeline(derivationSteps(match.derivation))}</div>
    </details>
  </div>`;
}

function initTinanta() {
  const form = $("#tinanta-form");
  const rootInput = $("#tinanta-root");
  const output = $("#tinanta-output");

  async function conjugate() {
    const root = rootInput.value.trim();
    if (!root) {
      output.innerHTML = `<div class="banner banner--warn">Enter a dhātu first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", form);
    await withPending(submit, "Conjugating…", async () => {
      try {
        const data = await api("/api/tinanta/generate", { root });
        if (data.error || !has(data.entries)) {
          output.innerHTML = `<div class="empty-state">
            <strong>${esc(root)}</strong> is not in reach.
            <p class="empty-state__hint">
              ${esc(data.error || "It is not a root the dhātupāṭha has, or its gaṇa is not yet wired into the engine.")}
            </p>
          </div>`;
          return;
        }
        output.innerHTML = data.entries.map(renderTinantaEntry).join("");
        announce(`${root} — ${data.entries.length} dhātupāṭha ${data.entries.length === 1 ? "entry" : "entries"} conjugated in laṭ.`);
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    conjugate();
  });

  $("#tinanta-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-root]");
    if (!button) return;
    rootInput.value = button.dataset.root;
    conjugate();
  });

  const reverseForm = $("#tinanta-reverse-form");
  const reverseInput = $("#tinanta-reverse-input");
  const reverseOutput = $("#tinanta-reverse-output");

  async function traceToRoot() {
    const word = reverseInput.value.trim();
    if (!word) {
      reverseOutput.innerHTML = `<div class="banner banner--warn">Enter a verb form first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", reverseForm);
    await withPending(submit, "Tracing…", async () => {
      try {
        const data = await api("/api/tinanta/reverse", { word });
        if (data.error || !has(data.matches)) {
          reverseOutput.innerHTML = `<div class="empty-state">
            No root in reach makes <strong>${esc(word)}</strong>.
            <p class="empty-state__hint">
              ${esc(data.error || "Either it is not a laṭ parasmaipada/ātmanepada form, or a rule it needs is not yet wired.")}
            </p>
          </div>`;
          return;
        }
        reverseOutput.innerHTML = data.matches.map(renderTinantaMatch).join("");
        announce(`${word} traced to ${data.matches.length} root ${data.matches.length === 1 ? "reading" : "readings"}.`);
      } catch (error) {
        reverseOutput.innerHTML = errorBanner(error.message);
      }
    });
  }

  reverseForm.addEventListener("submit", (event) => {
    event.preventDefault();
    traceToRoot();
  });

  $("#tinanta-reverse-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-word]");
    if (!button) return;
    reverseInput.value = button.dataset.word;
    traceToRoot();
  });
}

/* ==================================================================== */
/* 5. Kṛdanta & taddhita                                                */
/* ==================================================================== */

function renderDerivative(data, kind) {
  const isKrdanta = kind === "krdanta";
  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(data.derived_stem_devanagari)}</p>
        <p class="result-headline-latin">${esc(data.derived_stem_iast)}</p>
      </div>
      <div class="row">
        ${pill(isKrdanta ? "Kṛdanta" : "Taddhitānta", "primary")}
        ${pill(data.affix_name, "info")}
        ${has(data.affix_category) ? pill(data.affix_category) : ""}
        ${data.is_avyaya ? pill("Avyaya — indeclinable", "warn") : ""}
      </div>
    </div>

    <div class="def-list def-list--2 mt-4">
      ${
        isKrdanta
          ? def("Dhātu", `${data.root_devanagari} (${data.root_iast}) — ${data.root_meaning}`)
          : def("Base stem", `${data.base_stem_devanagari} (${data.base_stem_iast})`)
      }
      ${isKrdanta ? def("Gaṇa", data.root_gana) : ""}
      ${isKrdanta && has(data.upasarga) ? def("Upasarga", data.upasarga) : ""}
      ${def("Semantic role", data.semantic_meaning)}
      ${def("Pāṇinian sūtra", data.sutra_panini)}
      ${def("Harināmāmṛta parallel", data.sutra_hnv)}
    </div>

    ${
      has(data.tika_exegesis)
        ? `<div class="note-box mt-4" style="display:block">
            <p class="def__label">Ṭīkā exegesis</p>
            <p class="timeline__desc">${esc(data.tika_exegesis)}</p>
          </div>`
        : ""
    }

    <div class="mt-4">
      <h3 class="section-heading">Morphophonemic derivation</h3>
      ${timeline(data.derivation_steps, { formKey: "form", descKey: "desc" })}
    </div>
  </div>`;
}

function initDerivatives() {
  const output = $("#derivative-output");

  const krdantaForm = $("#krdanta-form");
  const krdantaRoot = $("#krdanta-root");
  const krdantaAffix = $("#krdanta-affix");
  const krdantaUpasarga = $("#krdanta-upasarga");

  async function deriveKrdanta() {
    const root = krdantaRoot.value.trim();
    if (!root) {
      output.innerHTML = `<div class="banner banner--warn">Enter a dhātu first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", krdantaForm);
    await withPending(submit, "Deriving…", async () => {
      try {
        const data = await api("/api/krdanta/generate", {
          root,
          affix: krdantaAffix.value,
          upasarga: krdantaUpasarga.value.trim() || null,
        });
        if (data.error || !data.derived_stem_iast) {
          output.innerHTML = `<div class="empty-state">
            No supported kṛdanta derivation for <strong>${esc(root)}</strong> + ${esc(krdantaAffix.value)}.
            <p class="empty-state__hint">${esc(data.error || "The root or affix pairing is outside the covered slice.")}</p>
          </div>`;
          return;
        }
        output.innerHTML = renderDerivative(data, "krdanta");
        announce(`Derived ${data.derived_stem_iast}.`);
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  krdantaForm.addEventListener("submit", (event) => {
    event.preventDefault();
    deriveKrdanta();
  });

  $("#krdanta-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-root]");
    if (!button) return;
    krdantaRoot.value = button.dataset.root;
    krdantaAffix.value = button.dataset.affix;
    krdantaUpasarga.value = button.dataset.upasarga || "";
    deriveKrdanta();
  });

  const taddhitaForm = $("#taddhita-form");
  const taddhitaStem = $("#taddhita-stem");
  const taddhitaAffix = $("#taddhita-affix");

  async function deriveTaddhita() {
    const stem = taddhitaStem.value.trim();
    if (!stem) {
      output.innerHTML = `<div class="banner banner--warn">Enter a base stem first.</div>`;
      return;
    }
    const submit = $("button[type=submit]", taddhitaForm);
    await withPending(submit, "Deriving…", async () => {
      try {
        const data = await api("/api/taddhita/generate", { stem, affix: taddhitaAffix.value });
        if (data.error || !data.derived_stem_iast) {
          output.innerHTML = `<div class="empty-state">
            No supported taddhita derivation for <strong>${esc(stem)}</strong> + ${esc(taddhitaAffix.value)}.
            <p class="empty-state__hint">${esc(data.error || "The stem or affix pairing is outside the covered slice.")}</p>
          </div>`;
          return;
        }
        output.innerHTML = renderDerivative(data, "taddhita");
        announce(`Derived ${data.derived_stem_iast}.`);
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  taddhitaForm.addEventListener("submit", (event) => {
    event.preventDefault();
    deriveTaddhita();
  });

  $("#taddhita-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-stem]");
    if (!button) return;
    taddhitaStem.value = button.dataset.stem;
    taddhitaAffix.value = button.dataset.affix;
    deriveTaddhita();
  });
}

/* ==================================================================== */
/* 6. Chandas — syllable weights and metre                              */
/* ==================================================================== */

/** Verdict tone: only a fully grounded identification gets the strong tone. */
function meterTone(status) {
  if (status === "identified") return "success";
  if (status === "provisional") return "primary";
  if (status === "ambiguous") return "warn";
  if (status === "insufficient-evidence") return "warn";
  return "neutral";
}

/* --- aligned grid: rows, yati, word groups, column tracks ------------- */

const GRID_SCRIPT_KEY = "chandas-grid-script";

/** Which script(s) the grid shows: "deva", "iast", or "both". */
function gridScript() {
  try {
    const stored = localStorage.getItem(GRID_SCRIPT_KEY);
    if (stored === "deva" || stored === "iast" || stored === "both") return stored;
  } catch (_) {
    /* private mode — fall through to the default */
  }
  return "both";
}


/**
 * Rows to align. Prefers the metrical pādas the matched candidate claims —
 * that is what makes beat N line up across rows even when the source was
 * supplied as half-verse lines. Falls back to the supplied units when the
 * candidate's evidence does not tile the verse exactly.
 */
function gridRows(report) {
  const all = report.padas.flatMap((pada) => pada.syllables);
  const primary = report.meter && report.meter.primary;
  const verified =
    report.verification.analysis.status === "verified" &&
    report.verification.meter.status === "verified";

  if (primary && verified && primary.padas.length) {
    const evidence = [...primary.padas].sort((a, b) => a.pada_index - b.pada_index);
    const rows = [];
    let previousEnd = 0;
    for (const pada of evidence) {
      const valid =
        pada.syllable_start === previousEnd &&
        pada.syllable_end > pada.syllable_start &&
        pada.syllable_end <= all.length;
      if (!valid) return sourceRows(report);
      rows.push({
        index: pada.pada_index,
        syllables: all.slice(pada.syllable_start, pada.syllable_end),
        evidence: pada,
        meterAligned: true,
      });
      previousEnd = pada.syllable_end;
    }
    if (previousEnd === all.length) return rows;
  }
  return sourceRows(report);
}

function sourceRows(report) {
  return report.padas.map((pada) => ({
    index: pada.index,
    syllables: pada.syllables,
    evidence: null,
    meterAligned: false,
  }));
}

/**
 * Yati positions worth drawing. Only from a stable, exactly-matching,
 * independently verified candidate that actually records one — the catalog
 * stores a caesura only where the cited source fixes it, so absence means
 * "the tradition prescribes no break here", not "unknown".
 */
function auditedYatis(report, maxLength) {
  const meter = report.meter;
  const primary = meter && meter.primary;
  const stable = meter && (meter.status === "identified" || meter.status === "provisional");
  if (
    !primary ||
    !stable ||
    primary.match_type !== "exact" ||
    !primary.yati ||
    report.verification.meter.status !== "verified"
  ) {
    return [];
  }
  return [...new Set(primary.yati)]
    .filter((y) => Number.isInteger(y) && y > 0 && y < maxLength)
    .sort((a, b) => a - b);
}

/**
 * Splits a row into display segments: runs of syllables belonging to one
 * written word ("word"), and single syllables that straddle a space ("weld").
 *
 * A metrical syllable may cross a word boundary — "yat sūrayaḥ" scans
 * ya·tsū — so a welded syllable has no single owning word. Rather than drop
 * the boxes for the whole row, it is left unboxed between the two boxes it
 * joins and marked as the bridge it is. Returns null only when the spans
 * genuinely cannot be ordered.
 */
function wordSegments(report, syllables) {
  if (!syllables.length) return [];
  const segments = [];
  let start = null;
  for (let i = 0; i < syllables.length; i++) {
    const current = syllables[i];
    if (/\s/.test(current.source)) {
      if (start !== null) {
        segments.push({ kind: "word", start, end: i });
        start = null;
      }
      segments.push({ kind: "weld", start: i, end: i + 1 });
      continue;
    }
    if (start === null) {
      start = i;
      continue;
    }
    const previous = syllables[i - 1];
    if (current.span.start < previous.span.end) return null;
    const gap = report.source_text.slice(previous.span.end, current.span.start);
    if (/\s/.test(gap)) {
      segments.push({ kind: "word", start, end: i });
      start = i;
    }
  }
  if (start !== null) segments.push({ kind: "word", start, end: syllables.length });
  return segments;
}

/** The two written fragments a welded syllable bridges, for its tooltip. */
function weldDescription(syllable) {
  const parts = syllable.source.split(/\s+/).filter(Boolean);
  return parts.length === 2
    ? `spans the word boundary — "${parts[0]}" + "${parts[1]}" scan as one syllable`
    : `spans a word boundary — written "${syllable.source}"`;
}

/** CSS grid column for a beat, counting the extra narrow yati tracks. */
function columnTrack(position, yatis) {
  return 2 + position + yatis.filter((y) => y <= position).length;
}

/** CSS grid column of the divider that sits before beat `yati`. */
function yatiTrack(yati, yatis) {
  return 2 + yati + yatis.filter((y) => y < yati).length;
}

function gridTemplate(maxLength, yatis) {
  const tracks = ["auto"];
  for (let position = 0; position < maxLength; position++) {
    if (yatis.includes(position)) tracks.push("0.9rem");
    tracks.push("minmax(2.4rem, auto)");
  }
  return tracks.join(" ");
}

function gridCell(syllable, position, evidence, yatis, gridRow, weld = null) {
  const expected =
    evidence && evidence.expected_pattern ? evidence.expected_pattern[position] : null;
  const mismatch =
    evidence && (evidence.mismatches || []).some((m) => m.position === position);
  const guru = syllable.weight === "guru";
  const licence =
    evidence &&
    evidence.final_anceps_used &&
    evidence.expected_pattern &&
    position === evidence.expected_pattern.length - 1;
  const glyph = (guru ? "—" : "◡") + (licence ? "*" : "");
  const title =
    `${syllable.iast} — ${syllable.reason}` +
    (mismatch
      ? ` | the ${expected === "G" ? "guru" : "laghu"} the rule expects here is absent`
      : "") +
    (licence ? " | filled by the recorded terminal licence" : "") +
    (weld ? ` | ${weld}` : "");

  // Every cell is placed explicitly on the shared tracks — the word box is a
  // backdrop behind them, not a container, so nothing may be auto-placed.
  const place = ` style="grid-row:${gridRow};grid-column:${columnTrack(position, yatis)}"`;
  // Both scripts are always emitted; the grid's data-script decides which are
  // shown, so switching is instant and needs no re-scan. (Rendering
  // syllable.text would print the same string twice for IAST input.)
  return `<div class="gcell${guru ? " gcell--guru" : ""}${mismatch ? " gcell--mismatch" : ""}${weld ? " gcell--weld" : ""}"${place}
              title="${esc(title)}">
    <span class="gcell__deva" lang="sa">${esc(syllable.devanagari)}</span>
    <span class="gcell__iast" lang="sa-Latn">${esc(syllable.iast)}</span>
    <span class="gcell__w">${glyph}</span>
    ${mismatch ? `<span class="gcell__exp">${esc(expected)}</span>` : ""}
  </div>`;
}

function renderAlignedGrid(report) {
  const rows = gridRows(report);
  if (!rows.length) return "";
  const maxLength = Math.max(...rows.map((r) => r.syllables.length));
  if (!maxLength) return "";
  const yatis = auditedYatis(report, maxLength);
  const template = gridTemplate(maxLength, yatis);
  const aligned = rows[0].meterAligned;

  const header = [
    `<span></span>`,
    ...Array.from(
      { length: maxLength },
      (_, position) =>
        `<span class="agrid__num" style="grid-row:1;grid-column:${columnTrack(position, yatis)}">${position + 1}</span>`
    ),
    ...yatis.map(
      (y) =>
        `<span class="agrid__yati-mark" style="grid-row:1;grid-column:${yatiTrack(y, yatis)}" title="yati — prescribed caesura after syllable ${y}">‖</span>`
    ),
  ].join("");

  const body = rows
    .map((row, rowIndex) => {
      const gridRow = rowIndex + 2;
      const segments = wordSegments(report, row.syllables);
      const matras = row.syllables.reduce((total, s) => total + s.matras, 0);
      const label = `<div class="agrid__label" style="grid-row:${gridRow};grid-column:1">
          ${aligned ? "Pāda" : "Unit"} ${row.index + 1}
          <small>${row.syllables.length} akṣara · ${matras} mātrā</small>
        </div>`;

      // The word box is a backdrop spanning its tracks, drawn behind the
      // cells rather than containing them. That keeps every cell placed on
      // the shared column tracks — so alignment survives — while letting the
      // box carry its own margin (the gap that separates one word from the
      // next) and a heavier border.
      const backdrops = (segments || [])
        .filter((segment) => segment.kind === "word")
        .map((segment) => {
          const from = columnTrack(segment.start, yatis);
          const to = columnTrack(segment.end - 1, yatis) + 1;
          return `<div class="agrid__word" aria-hidden="true" style="grid-row:${gridRow};grid-column:${from} / ${to}"></div>`;
        })
        .join("");

      const welded = new Set(
        (segments || [])
          .filter((segment) => segment.kind === "weld")
          .map((segment) => segment.start)
      );

      const cells = row.syllables
        .map((syllable, position) =>
          gridCell(
            syllable,
            position,
            row.evidence,
            yatis,
            gridRow,
            welded.has(position) ? weldDescription(syllable) : null
          )
        )
        .join("");

      const dividers = yatis
        .map(
          (y) =>
            `<span class="agrid__yati-rule" style="grid-row:${gridRow};grid-column:${yatiTrack(y, yatis)}"></span>`
        )
        .join("");

      return label + backdrops + cells + dividers;
    })
    .join("");

  const anyMismatch = rows.some((r) => r.evidence && r.evidence.mismatches.length);
  const anyLicence = rows.some((r) => r.evidence && r.evidence.final_anceps_used);
  const anyWeld = rows.some((r) => r.syllables.some((s) => /\s/.test(s.source)));

  const script = gridScript();
  const option = (value, label) =>
    `<button type="button" data-grid-script="${value}" aria-pressed="${script === value}">${label}</button>`;

  return `<div class="card card--pad">
    <div class="result-head">
      <h2 class="section-heading">Aligned syllable grid</h2>
      <div class="toggle-group grid-script" role="group" aria-label="Grid script">
        ${option("deva", "देवनागरी")}${option("iast", "IAST")}${option("both", "Both")}
      </div>
    </div>
    <p class="help-text">
      ${
        aligned
          ? "Rows are the metrical pādas the matched rule claims, so beat N lines up down the column."
          : "Rows are the units you supplied; no verified candidate was available to align them by."
      }
    </p>
    <div class="agrid-scroll">
      <div class="agrid" data-script="${script}" style="grid-template-columns:${template}">${header}${body}</div>
    </div>
    <p class="grid-legend">
      — guru (heavy) · ◡ laghu (light)${anyLicence ? " · <strong>*</strong> the pāda-final position was filled by the rule's recorded terminal licence" : ""}${anyMismatch ? " · a red outline marks a weight the rule did not expect, with the expected value beneath" : ""}
      ${yatis.length ? `<br><strong>‖</strong> yati — the caesura the cited source prescribes, after syllable ${yatis.join(" and ")}. Word-boundary fit is not checked.` : ""}
      <br>Boxes group the syllables of one written word.${anyWeld ? " A syllable drawn between two boxes with dashed sides is welded across the space by sandhi — it belongs to both words and scans as one beat." : ""}
      <br>Hover a syllable for the rule that decided its weight.
    </p>
  </div>`;
}

function renderMeterVerdict(report) {
  const meter = report.meter;
  if (!meter) return "";
  const primary = meter.primary;
  const classification = primary && primary.classification;

  return `<div class="card card--pad">
    <div class="result-head">
      <div>
        <p class="result-headline font-devanagari-serif">${esc(meter.label)}</p>
        ${
          primary
            ? `<p class="result-headline-latin">${esc(primary.match_type)} match against ${esc(meter.catalog_size)} rules</p>`
            : ""
        }
      </div>
      <div class="row">
        ${pill(meter.status, meterTone(meter.status))}
        ${primary ? pill(primary.tradition) : ""}
      </div>
    </div>

    ${
      primary && primary.template
        ? `<div class="mt-4">
            <h3 class="section-subheading">Template</h3>
            <div class="template-line">${esc(primary.template)}</div>
          </div>`
        : ""
    }

    ${
      classification
        ? `<div class="def-list def-list--2 mt-4">
            ${def("System", classification.system_label)}
            ${classification.count_class ? def("Count class", `${classification.count_class.name} — ${classification.count_class.syllables_per_pada} akṣara per pāda`) : ""}
            ${def("Symmetry", classification.symmetry)}
            ${def("Gaṇa formula", classification.gana_formula)}
            ${def("Yati", classification.yati_statement)}
            ${primary.source ? def("Source", `${primary.source.work} — ${primary.source.locator}`) : ""}
          </div>`
        : ""
    }

    ${
      primary && primary.subtypes
        ? `<div class="row mt-4">${primary.subtypes.map((s) => pill(s, "info")).join("")}</div>`
        : ""
    }

    ${
      primary && primary.notes && primary.notes.length
        ? `<div class="mt-4">${primary.notes.map((n) => `<p class="timeline__desc">${esc(n)}</p>`).join("")}</div>`
        : ""
    }

    ${
      classification && classification.cautions && classification.cautions.length
        ? classification.cautions
            .map((c) => `<div class="banner banner--warn mt-3">${esc(c)}</div>`)
            .join("")
        : ""
    }

    ${
      meter.diagnostics && meter.diagnostics.length
        ? meter.diagnostics
            .map((d) => `<div class="banner banner--info mt-3">${esc(d)}</div>`)
            .join("")
        : ""
    }
  </div>`;
}

function renderAuthority(report) {
  const primary = report.meter && report.meter.primary;
  if (!primary || !primary.authority) return "";
  const authority = primary.authority;
  if (!authority.pairs || !authority.pairs.length) {
    return `<div class="card card--pad">
      <h2 class="section-heading">Authority</h2>
      <p class="help-text">${esc(authority.note)}</p>
      <div class="row mt-3">${pill(authority.coverage, "warn")}</div>
    </div>`;
  }
  return `<div class="card card--pad">
    <h2 class="section-heading">Authority — root and commentary</h2>
    <p class="help-text">${esc(authority.note)}</p>
    <div class="stack-sm mt-3">
      ${authority.pairs
        .map(
          (pair) => `<div class="concordance-step">
            <div class="row">
              ${pill(pair.label, "primary")}
              ${pill(pair.tradition)}
            </div>
            <div class="concordance-grid">
              <div class="concordance-lens concordance-lens--p1">
                <p class="def__label">Mūla — ${esc(pair.root.author)}</p>
                <p class="text-xs">${esc(pair.root.work)}, ${esc(pair.root.locator)}</p>
                <p class="text-xs italic">${esc(pair.root.statement)}</p>
              </div>
              <div class="concordance-lens concordance-lens--p2">
                <p class="def__label">Bhāṣya — ${esc(pair.bhasya.author)}</p>
                <p class="text-xs">${esc(pair.bhasya.work)}, ${esc(pair.bhasya.locator)}</p>
                <p class="text-xs italic">${esc(pair.bhasya.statement)}</p>
              </div>
            </div>
            ${pair.note ? `<p class="timeline__desc mt-2">${esc(pair.note)}</p>` : ""}
          </div>`
        )
        .join("")}
    </div>
  </div>`;
}

function renderChandasCandidates(report) {
  const candidates = (report.meter && report.meter.candidates) || [];
  if (candidates.length < 2) return "";
  return `<div class="card card--pad">
    <h2 class="section-heading">Other candidates</h2>
    <p class="help-text">
      Ranked by evidence. A near match is a diagnostic, never a verdict.
    </p>
    <div class="table-scroll mt-3">
      <table class="data-table" style="min-width: 34rem">
        <thead>
          <tr><th>Metre</th><th>Match</th><th>Distance</th><th>Evidence</th><th>Authority</th></tr>
        </thead>
        <tbody>
          ${candidates
            .slice(1)
            .map(
              (c) => `<tr>
                <td><p class="medium">${esc(c.name)}</p><p class="text-xs muted">${esc(c.kind)}</p></td>
                <td>${esc(c.match_type)}</td>
                <td style="font-variant-numeric: tabular-nums">${esc(c.distance)}</td>
                <td>${esc(c.evidence)}</td>
                <td class="text-xs muted">${esc(c.authority ? c.authority.coverage : "")}</td>
              </tr>`
            )
            .join("")}
        </tbody>
      </table>
    </div>
  </div>`;
}

function renderRuleLegend(report) {
  const used = new Set();
  report.padas.forEach((pada) => pada.syllables.forEach((s) => used.add(s.rule)));
  const rules = Object.entries(report.rules || {}).filter(([key]) => used.has(key));
  if (!rules.length) return "";
  return `<details class="note-box">
    <summary>Deciding rules used in this verse (${rules.length})</summary>
    <div class="rule-legend">
      ${rules
        .map(
          ([key, rule]) => `<div class="rule-legend__item">
            <p class="rule-legend__name">${esc(key)}</p>
            <p class="text-xs">${esc(rule.plain)}</p>
            <p class="timeline__sutra">${esc(rule.sutra)}</p>
          </div>`
        )
        .join("")}
    </div>
  </details>`;
}

function renderVerification(report) {
  const analysis = report.verification.analysis;
  const meter = report.verification.meter;
  const bothOk = analysis.status === "verified" && meter.status === "verified";
  const issues = [...analysis.issues, ...meter.issues];
  return `<div class="banner banner--${bothOk ? "success" : "error"}">
    <strong>${bothOk ? "Independently verified." : "Verification failed."}</strong>
    The syllable scan was rechecked by a separate implementation
    (${esc(analysis.checks)} checks over ${esc(analysis.checked_syllables)} syllables) and the metre
    verdict by another (${esc(meter.checks)} checks).
    ${issues.length ? ` ${issues.length} disagreement(s): ${esc(issues.map((i) => i.code).join(", "))}.` : ""}
  </div>`;
}

function renderChandas(report) {
  if (!report.ok) {
    const errors = (report.diagnostics || []).filter((d) => d.severity === "error");
    return `<div class="empty-state">
      This text could not be scanned.
      <p class="empty-state__hint">
        ${errors.length ? esc(errors.map((d) => d.message).join(" ")) : "No Sanskrit syllables were found."}
      </p>
    </div>`;
  }

  const totals = report.totals;
  const notes = (report.diagnostics || []).filter((d) => d.severity !== "error");

  return `
    <div class="card card--pad">
      <div class="grid-auto">
        ${stat("Pādas", totals.padas, null, "primary")}
        ${stat("Akṣaras", totals.syllables)}
        ${stat("Guru", totals.guru, "heavy")}
        ${stat("Laghu", totals.laghu, "light")}
        ${stat("Mātrās", totals.matras, "total duration")}
      </div>
    </div>
    ${renderMeterVerdict(report)}
    ${renderAlignedGrid(report)}
    ${renderRuleLegend(report)}
    ${renderAuthority(report)}
    ${renderChandasCandidates(report)}
    ${renderVerification(report)}
    ${
      notes.length
        ? `<details class="note-box">
            <summary>Normalization notes (${notes.length})</summary>
            ${notes.map((d) => `<p class="mt-2">${esc(d.message)}</p>`).join("")}
          </details>`
        : ""
    }`;
}

function initChandas() {
  const form = $("#chandas-form");
  const input = $("#chandas-input");
  const output = $("#chandas-output");
  const submit = $("#chandas-submit");

  async function scan() {
    const text = input.value.trim();
    if (!text) {
      output.innerHTML = `<div class="banner banner--warn">Enter a verse first.</div>`;
      return;
    }
    await withPending(submit, "Scanning…", async () => {
      try {
        const report = await api("/api/chandas/analyze", {
          text,
          script: $("#chandas-script").value,
          boundary_mode: $("#chandas-boundary").value,
          tradition: $("#chandas-tradition").value,
        });
        output.innerHTML = renderChandas(report);
        announce(
          report.ok
            ? `${report.totals.syllables} syllables scanned. Metre: ${report.meter.label}.`
            : "The verse could not be scanned."
        );
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    scan();
  });

  $("#chandas-examples").addEventListener("click", (event) => {
    const button = event.target.closest("[data-example]");
    if (!button) return;
    input.value = button.dataset.example;
    scan();
  });

  // Script switching is presentation only — both scripts are already in the
  // DOM, so flip the attribute rather than re-scanning the verse.
  output.addEventListener("click", (event) => {
    const button = event.target.closest("[data-grid-script]");
    if (!button) return;
    const choice = button.dataset.gridScript;
    try {
      localStorage.setItem(GRID_SCRIPT_KEY, choice);
    } catch (_) {
      /* private mode — apply anyway */
    }
    $$(".agrid", output).forEach((grid) => grid.setAttribute("data-script", choice));
    $$("[data-grid-script]", output).forEach((b) =>
      b.setAttribute("aria-pressed", String(b.dataset.gridScript === choice))
    );
    announce(
      choice === "both" ? "Showing Devanāgarī and IAST." : `Showing ${choice === "deva" ? "Devanāgarī" : "IAST"} only.`
    );
  });
}

/* ==================================================================== */
/* Aṣṭādhyāyī — browser, playground and dependency graph                */
/* ==================================================================== */

const ASH = { catalogue: [], current: null, crossLinks: false };

async function ashGet(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}

const EYE_SVG =
  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
     <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
     <circle cx="12" cy="12" r="3" />
   </svg>`;

/**
 * Shows what is still unresolved for a sūtra, anchored to its eye.
 *
 * Fixed rather than absolute, because the list scrolls and an absolutely
 * positioned panel would be clipped by its own container. Hover and focus both
 * open it; a click pins it so the text can be read at leisure or selected.
 */
const PEEK = { pinned: null };

function peekHide(force) {
  if (PEEK.pinned && !force) return;
  PEEK.pinned = null;
  const panel = $("#ash-peek");
  if (!panel) return;
  panel.hidden = true;
  $$("[data-peek]").forEach((b) => b.setAttribute("aria-expanded", "false"));
}

function peekShow(button) {
  const panel = $("#ash-peek");
  const row = ASH.catalogue.find((r) => r.id === button.dataset.peek);
  if (!panel || !row) return;

  const items = (row.outstanding || [])
    .map(
      (finding) => `<div class="ash-peek__item">
        <span class="ash-finding__marker ash-finding__marker--${esc(finding.marker)}">${esc(
        finding.marker
      )}</span>
        <p style="margin:0.35rem 0 0" lang="sa">${esc(finding.text)}</p>
      </div>`
    )
    .join("");

  panel.innerHTML = `<div class="ash-peek__head">
      <span class="ash-peek__id">${esc(row.id)}</span>
      <span class="ash-peek__sutra" lang="sa">${esc(row.devanagari)}</span>
    </div>${items}
    <p class="ash-peek__hint">
      ${
        row.open
          ? "An OPEN finding is a question the sources did not settle."
          : "A SCOPE note is something this codification deliberately does not do."
      }
      Click the eye to keep this open.
    </p>`;

  panel.hidden = false;
  button.setAttribute("aria-expanded", "true");

  // Place it beside the eye, flipped or nudged so it stays on screen.
  const anchor = button.getBoundingClientRect();
  const box = panel.getBoundingClientRect();
  let left = anchor.right + 10;
  if (left + box.width > window.innerWidth - 8) {
    left = Math.max(8, anchor.left - box.width - 10);
  }
  let top = anchor.top - 8;
  if (top + box.height > window.innerHeight - 8) {
    top = Math.max(8, window.innerHeight - box.height - 8);
  }
  panel.style.left = `${left}px`;
  panel.style.top = `${top}px`;
}

/** The pāda a sūtra belongs to — "1.1" from "1.1.9". */
function ashPada(id) {
  const parts = String(id).split(".");
  return `${parts[0]}.${parts[1]}`;
}

function ashListRows(rows) {
  if (!rows.length) {
    return `<p class="ash-list__group">Nothing matches that.</p>`;
  }
  let out = "";
  let pada = null;
  rows.forEach((row) => {
    const here = ashPada(row.id);
    if (here !== pada) {
      pada = here;
      out += `<div class="ash-list__group">Adhyāya ${pada}</div>`;
    }
    const outstanding = row.outstanding || [];
    const dotClass = row.open
      ? "ash-list__flag"
      : "ash-list__flag ash-list__flag--scope";
    // The eye is a sibling of the row button, not a child: a button inside a
    // button is invalid, and this one has to be focusable in its own right.
    const eye = outstanding.length
      ? `<button type="button" class="ash-list__eye" data-peek="${esc(row.id)}"
           aria-expanded="false" aria-describedby="ash-peek"
           aria-label="What is outstanding for ${esc(row.id)}">
           <span class="${dotClass}"></span>${EYE_SVG}
         </button>`
      : "";
    out += `<div class="ash-list__row">
      <button type="button" class="ash-list__item" data-sutra="${esc(row.id)}"
        aria-current="${String(row.id === ASH.current)}">
        <span class="ash-list__id">${esc(row.id)}</span>
        <span class="ash-list__text" lang="sa">${esc(row.devanagari)}</span>
        <span></span>
      </button>
      ${eye}
    </div>`;
  });
  return out;
}

function ashFilter(query) {
  const needle = query.trim().toLowerCase();
  if (!needle) return ASH.catalogue;
  return ASH.catalogue.filter((row) =>
    row.id.includes(needle) ||
    row.devanagari.includes(query.trim()) ||
    row.iast.toLowerCase().includes(needle) ||
    (row.type || "").toLowerCase().includes(needle)
  );
}

/* --- the padaccheda, coloured by the case a paribhāṣā reads ------------- */

const ASH_CASE_CLASS = { 1: "", 5: "pancami", 6: "sasthi", 7: "saptami" };
const ASH_CASE_RULE = {
  5: "fifth — 1.1.67 puts the operation on what follows",
  6: "sixth — 1.1.49 makes this what is replaced",
  7: "seventh — 1.1.66 puts the operation on what precedes",
};

function ashPadaccheda(padas) {
  if (!padas.length) return "";
  const cells = padas
    .map((pada) => {
      const kind = ASH_CASE_CLASS[pada.vibhakti] || "";
      const why = ASH_CASE_RULE[pada.vibhakti] || "";
      return `<span class="ash-pada${kind ? ` ash-pada--${kind}` : ""}"${
        why ? ` title="${esc(why)}"` : ""
      }>
        <span class="ash-pada__word" lang="sa">${esc(pada.word)}</span>
        <span class="ash-pada__case">${esc(pada.case)}</span>
      </span>`;
    })
    .join("");
  return `<div class="card card--pad">
    <h3 class="card__title">Padaccheda</h3>
    <p class="text-sm text-muted">
      The case a word stands in is not decoration — three of the paribhāṣās read it to decide
      where an operation lands. Those three are outlined.
    </p>
    <div class="flex-wrap gap-2 mt-3">${cells}</div>
  </div>`;
}

/* --- the playground ----------------------------------------------------- */

function ashField(field) {
  const id = `ash-f-${field.name.replace(/[^a-z0-9]/gi, "-")}`;
  // The label is a person's question; the hint names the term behind it, so
  // the beginner reads the first and whoever knows the śāstra reads the
  // second. Without them the label is the Python parameter name.
  const hint = field.hint
    ? `<span class="field__hint" lang="sa">${esc(field.hint)}</span>`
    : "";
  if (field.kind === "bool") {
    return `<label class="ash-play__check" for="${id}">
      <input type="checkbox" id="${id}" data-field="${esc(field.name)}"
        ${field.default ? "checked" : ""} />
      <span>${esc(field.label)}${hint}</span>
    </label>`;
  }
  if (field.kind === "select") {
    const options = field.options
      .map(
        (option) =>
          `<option value="${esc(option)}"${
            option === field.default ? " selected" : ""
          }>${esc(option)}</option>`
      )
      .join("");
    return `<label class="field" for="${id}">
      <span class="field__label">${esc(field.label)}</span>${hint}
      <select class="input" id="${id}" data-field="${esc(field.name)}">${options}</select>
    </label>`;
  }
  const value = field.default === null || field.default === undefined ? "" : field.default;
  return `<label class="field" for="${id}">
    <span class="field__label">${esc(field.label)}</span>${hint}
    <input class="input" id="${id}" type="${field.kind === "number" ? "number" : "text"}"
      data-field="${esc(field.name)}" value="${esc(String(value))}"
      spellcheck="false" autocomplete="off" />
  </label>`;
}

/**
 * The ready-made inputs for a rule, as clickable chips.
 *
 * A worked case fills the form with something the Kāśikā actually works; a
 * counter-example fills it with the form the sūtra's own condition keeps out,
 * which is half of what there is to learn. The two are marked apart, since a
 * reader who clicks one and gets "no name at all" should be able to see that
 * was the point.
 */
function ashCases(cases) {
  if (!cases || !cases.length) return "";
  const chip = (c, i) =>
    `<button type="button"
             class="btn btn--secondary btn--sm ash-case${
               c.kind === "counter" ? " ash-case--counter" : ""
             }"
             data-case="${i}"
             title="${esc(c.note || "")}">${
      c.kind === "counter" ? "✕ " : ""
    }${esc(c.label)}</button>`;
  return `<div class="ash-cases">
    <span class="ash-cases__label">Try one</span>
    <div class="example-chips">${cases.map(chip).join("")}</div>
  </div>`;
}

/** Puts one case's values into the form, clearing anything left over. */
function ashFillCase(values) {
  const form = $("#ash-play-form");
  if (!form) return;
  form.querySelectorAll("[data-field]").forEach((el) => {
    const name = el.dataset.field;
    const has = Object.prototype.hasOwnProperty.call(values, name);
    const value = has ? values[name] : null;
    if (el.type === "checkbox") {
      el.checked = has ? Boolean(value) : false;
    } else if (Array.isArray(value)) {
      el.value = value.join(", ");
    } else {
      el.value = has && value !== null && value !== undefined ? String(value) : "";
    }
  });
}

function ashPlayground(detail) {
  const play = detail.playground;
  if (!play.runnable) {
    return `<div class="card card--pad">
      <h3 class="card__title">Run the rule</h3>
      <p class="text-sm">${esc(play.note)}</p>
    </div>`;
  }

  // Fields that came out of a dataclass are boxed together, because they are
  // one argument and the form should not pretend otherwise.
  const loose = play.fields.filter((f) => !f.group);
  const groups = {};
  play.fields.filter((f) => f.group).forEach((f) => {
    (groups[f.group] = groups[f.group] || []).push(f);
  });

  const groupBlocks = Object.entries(groups)
    .map(
      ([name, fields]) => `<div class="ash-play__group">
        <span class="ash-play__group-label">${esc(name)}</span>
        ${fields.map(ashField).join("")}
      </div>`
    )
    .join("");

  const firstLine = (play.doc || "").split("\n\n")[0].replace(/\s+/g, " ").trim();

  return `<div class="card card--pad">
    <h3 class="card__title">Run the rule</h3>
    ${firstLine ? `<p class="text-sm text-muted">${esc(firstLine)}</p>` : ""}
    <form id="ash-play-form" class="mt-3" novalidate>
      <div class="ash-play">
        ${loose.map(ashField).join("")}
        ${groupBlocks}
      </div>
      <div class="flex-wrap gap-2 mt-4">
        <button type="submit" class="btn btn--primary" id="ash-run">Run</button>
        <span class="text-sm text-muted">${esc(play.function)}()</span>
      </div>
      <p class="ash-play__scripts">Type in either script — विश् or
        <span class="mono">viś</span>. What the rule was actually asked is
        echoed below the answer.</p>
    </form>
    ${ashCases(play.cases)}
    <div id="ash-play-output"></div>
  </div>`;
}

/** Renders whatever a rule returned, without knowing its type. */
function ashValue(value, depth = 0) {
  if (value === null || value === undefined) return `<em>nothing</em>`;
  if (typeof value === "boolean") {
    return value ? `<strong>true</strong>` : `false`;
  }
  if (typeof value !== "object") return esc(String(value));
  if (Array.isArray(value)) {
    if (!value.length) return `<em>empty</em>`;
    return `<ul class="list-disc">${value
      .map((item) => `<li>${ashValue(item, depth + 1)}</li>`)
      .join("")}</ul>`;
  }
  const rows = Object.entries(value)
    .filter(([, v]) => v !== null && v !== "" && !(Array.isArray(v) && !v.length))
    .map(
      ([key, v]) =>
        `<dt>${esc(humanise(key))}</dt><dd>${ashValue(v, depth + 1)}</dd>`
    )
    .join("");
  return rows ? `<dl class="ash-kv">${rows}</dl>` : `<em>nothing</em>`;
}

function ashResult(payload) {
  if (!payload.ok) {
    return `<div class="ash-result ash-result--error">${esc(payload.error)}</div>`;
  }
  const tone =
    payload.result === true
      ? " ash-result--true"
      : payload.empty || payload.result === false
        ? " ash-result--empty"
        : "";
  return `<div class="ash-call mt-3">${esc(payload.called)}</div>
    <div class="ash-result${tone}">${ashValue(payload.result)}</div>`;
}

/* --- the dependency graph ----------------------------------------------- */

const ASH_EDGE_CLASS = {
  "anuvṛtti": "anuvrtti",
  "adhikāra": "adhikara",
  related: "related",
};

/**
 * Lays the graph out in rows and draws it as SVG.
 *
 * Anuvṛtti and adhikāra point backward through the text, so their sources go
 * ABOVE the sūtra in hand; `related` is a cross-reference and goes below. Rows
 * are by distance, so a two-step walk stacks upward.
 */
function ashGraph(graph) {
  const byId = {};
  graph.nodes.forEach((node) => (byId[node.id] = node));

  const relatedIds = new Set(
    graph.edges.filter((e) => e.kind === "related").map((e) => e.to)
  );

  const rows = new Map();
  graph.nodes.forEach((node) => {
    let row;
    if (node.root) row = 0;
    else if (relatedIds.has(node.id) && node.distance <= 1) row = 1;
    else row = -node.distance;
    if (!rows.has(row)) rows.set(row, []);
    rows.get(row).push(node);
  });

  const order = Array.from(rows.keys()).sort((a, b) => b - a);
  const W = 96;
  const H = 30;
  const GAP_X = 26;
  const GAP_Y = 66;
  const pos = {};
  let widest = 1;
  order.forEach((row) => {
    widest = Math.max(widest, rows.get(row).length);
  });
  const width = Math.max(widest * (W + GAP_X) + GAP_X, 420);

  order.forEach((row, rowIndex) => {
    const members = rows.get(row).sort((a, b) => a.id.localeCompare(b.id));
    const rowWidth = members.length * (W + GAP_X) - GAP_X;
    const startX = (width - rowWidth) / 2;
    members.forEach((node, i) => {
      pos[node.id] = {
        x: startX + i * (W + GAP_X),
        y: GAP_Y * rowIndex + 16,
      };
    });
  });

  const height = GAP_Y * order.length + 24;

  // Edges between two ancestors, neither of them the sūtra asked about.
  // For a rule under four headings there are far more of these than direct
  // ones — 2.1.21 has 21 against 6 — so they are hidden until asked for.
  const edges = graph.edges
    .filter((edge) => ASH.crossLinks || !edge.cross)
    .filter((edge) => pos[edge.from] && pos[edge.to])
    .map((edge) => {
      const a = pos[edge.from];
      const b = pos[edge.to];
      const x1 = a.x + W / 2;
      const y1 = a.y + H;
      const x2 = b.x + W / 2;
      const y2 = b.y;
      const midY = (y1 + y2) / 2;
      const kind = ASH_EDGE_CLASS[edge.kind] || "related";
      const path = `M ${x1} ${y1} C ${x1} ${midY}, ${x2} ${midY}, ${x2} ${y2}`;
      const label = edge.label
        ? `<text class="ash-graph__label" x="${(x1 + x2) / 2}" y="${midY}"
             text-anchor="middle">${esc(edge.label)}</text>`
        : "";
      return `<path class="ash-graph__edge ash-graph__edge--${kind}" d="${path}">
        <title>${esc(edge.kind)}${edge.label ? ` — ${esc(edge.label)}` : ""}</title>
      </path>${label}`;
    })
    .join("");

  const nodes = graph.nodes
    .map((node) => {
      const p = pos[node.id];
      if (!p) return "";
      const classes = [
        "ash-graph__node",
        node.root ? "ash-graph__node--root" : "",
        node.codified && !node.root ? "ash-graph__node--codified" : "",
      ]
        .filter(Boolean)
        .join(" ");
      const clickable = node.codified && !node.root;
      return `<g class="${classes}"${
        clickable ? ` data-sutra="${esc(node.id)}" role="button" tabindex="0"` : ""
      }>
        <rect x="${p.x}" y="${p.y}" width="${W}" height="${H}" rx="6" />
        <text x="${p.x + W / 2}" y="${p.y + 19}">${esc(node.id)}</text>
        <title>${esc(node.devanagari || node.id)}${
          node.codified ? "" : " — not codified yet"
        }</title>
      </g>`;
    })
    .join("");

  return `<div class="card card--pad">
    <h3 class="card__title">What this sūtra hangs on</h3>
    <p class="text-sm text-muted">
      Sources of carried words are drawn above, cross-references below. A filled box is a sūtra
      already codified — click it to go there. The whole chain is shown: every heading over this
      rule and every sūtra a word is read down from.
    </p>
    ${
      graph.cross_links
        ? `<label class="ash-graph__toggle">
             <input type="checkbox" id="ash-cross"${ASH.crossLinks ? " checked" : ""}>
             <span>also link the ancestors to each other
               <em>(${graph.cross_links} more ${
                 graph.cross_links === 1 ? "line" : "lines"
               })</em></span>
           </label>`
        : ""
    }
    <div class="ash-graph mt-3">
      <svg viewBox="0 0 ${width} ${height}" width="${width}" height="${height}"
           role="img" aria-label="Dependency graph for ${esc(graph.root)}">
        ${edges}${nodes}
      </svg>
    </div>
    <div class="ash-legend">
      <span><span class="ash-legend__swatch" style="border-color:var(--color-primary)"></span>anuvṛtti — a word carried down</span>
      <span><span class="ash-legend__swatch" style="border-color:var(--color-secondary);border-top-style:dashed"></span>adhikāra — a governing heading</span>
      <span><span class="ash-legend__swatch" style="border-color:var(--color-outline);border-top-style:dotted"></span>related — recorded by the codification</span>
    </div>
  </div>`;
}

/* --- findings, sources, and the whole panel ----------------------------- */

function ashFindings(findings) {
  if (!findings.length) return "";
  const rows = findings
    .map(
      (finding) => `<div class="ash-finding">
        <span class="ash-finding__marker ash-finding__marker--${esc(finding.marker)}">${esc(
        finding.marker
      )}</span>
        <span lang="sa">${esc(finding.text)}</span>
      </div>`
    )
    .join("");
  return `<div class="card card--pad">
    <h3 class="card__title">Findings</h3>
    <p class="text-sm text-muted">
      What reading the sources settled, and what it did not. SETTLED is a conclusion; OPEN is a
      question still standing; SCOPE is something the codification deliberately does not do.
    </p>
    <div class="mt-3">${rows}</div>
  </div>`;
}

function ashSources(sources) {
  const rows = sources
    .map(
      (source) => `<div class="ash-source">
        <span class="ash-source__name">${esc(source.source)}</span>
        <span class="ash-status ash-status--${esc(source.status)}">${esc(source.status)}</span>
        <span class="ash-source__quote" lang="sa"
              title="${esc(source.text || source.note || source.locator)}">${esc(
        source.text || source.note || source.locator || "—"
      )}</span>
      </div>`
    )
    .join("");
  // The summary has to be honest with the panel shut. Saying "10 read" and
  // leaving the rest to be discovered would let a collapsed panel imply the
  // apparatus is complete when four slots are empty and one is unreadable.
  const count = (status) => sources.filter((s) => s.status === status).length;
  const parts = [`${count("verified")} read`];
  if (count("pending")) parts.push(`${count("pending")} not yet consulted`);
  if (count("unreadable")) parts.push(`${count("unreadable")} unreadable`);
  if (count("absent")) parts.push(`${count("absent")} silent here`);

  return `<details class="card card--pad">
    <summary><strong>Sources</strong> — ${esc(parts.join(" · "))}</summary>
    <div class="ash-sources mt-3">${rows}</div>
  </details>`;
}

/**
 * The plain-English gist, for a reader meeting the rule for the first time.
 *
 * Sits directly under the sūtra, before any of the apparatus. Technical terms
 * carry both scripts so the same word can be recognised wherever it turns up,
 * and the worked form is set apart because a rule about substitution is far
 * easier to see than to read. The sūtrārtha below it is a source and is named
 * as one; the two lines above are this project's own.
 */
/**
 * What kind of rule this is, for a reader who does not yet know what a
 * saṃjñā rule *is*.
 *
 * Collapsed, with only the two-word label showing. Someone who already knows
 * what a definition rule does sees a small grey word and reads past it;
 * someone who does not can open it. The alternative — printing the paragraph
 * on every sūtra — teaches the beginner once and then gets in their way for
 * the next three hundred rules.
 */
function ashKind(kind) {
  if (!kind || !kind.label) return "";
  const body = kind.plain
    ? `<p class="ash-kind__plain">${esc(kind.plain)}</p>`
    : "";
  return `<details class="ash-kind">
      <summary class="ash-kind__label">
        <span>${esc(kind.label)}</span>
        <span class="ash-kind__more">what does that mean?</span>
      </summary>
      ${body}
    </details>`;
}

function ashGist(gloss) {
  if (!gloss || (!gloss.plain && !gloss.sutrartha)) return "";
  const plain = gloss.plain
    ? `<p class="ash-gist__plain">${esc(gloss.plain)}</p>`
    : "";
  const example = gloss.example
    ? `<div class="ash-gist__example" lang="sa">${esc(gloss.example)}</div>`
    : "";
  const source = gloss.sutrartha
    ? `<div class="ash-gist__source">
         <span class="ash-gist__source-name">Sūtrārtha, as the corpus gives it</span>
         <span lang="sa">${esc(gloss.sutrartha)}</span>
       </div>`
    : "";
  return `<div class="ash-gist">${plain}${example}${source}</div>`;
}

function ashDetail(detail, graph) {
  const anuvrtti = detail.anuvrtti.length
    ? `<p class="text-sm mt-2"><strong>Anuvṛtti:</strong> ${detail.anuvrtti
        .map((a) => `<span lang="sa">${esc(a.word)}</span> <em>(${esc(a.from)})</em>`)
        .join(", ")}</p>`
    : "";
  const adhikara = detail.adhikara.length
    ? `<p class="text-sm"><strong>Adhikāra:</strong> ${detail.adhikara
        .map((a) => esc(a.sutra))
        .join(", ")}</p>`
    : "";

  return `<div class="card card--pad">
      <div class="flex-wrap gap-2" style="justify-content:space-between;align-items:baseline">
        <div>
          <div class="ash-sutra" lang="sa">${esc(detail.devanagari)}</div>
          <div class="ash-sutra__iast">${esc(detail.iast)}</div>
        </div>
        <div class="flex-wrap gap-2">
          <span class="pill pill--neutral">${esc(detail.id)}</span>
          ${detail.type ? `<span class="pill pill--info" lang="sa">${esc(detail.type)}</span>` : ""}
        </div>
      </div>
      ${ashKind(detail.kind)}
      ${ashGist(detail.gloss)}
      ${anuvrtti}${adhikara}
      ${
        detail.codification
          ? `<p class="text-sm mt-3"><strong>Codified as:</strong> ${esc(detail.codification)}</p>`
          : ""
      }
    </div>
    ${ashPadaccheda(detail.padaccheda)}
    ${ashPlayground(detail)}
    ${ashGraph(graph)}
    ${ashFindings(detail.findings)}
    ${ashSources(detail.sources)}`;
}

async function ashSelect(sutraId) {
  ASH.current = sutraId;
  // The chip handler is delegated on the panel, so it cannot close over the
  // detail; the cases are kept here for it to look up by index.
  ASH.cases = [];
  const panel = $("#ash-detail");
  panel.innerHTML = `<div class="card card--pad"><p class="text-sm text-muted">Loading ${esc(
    sutraId
  )}…</p></div>`;
  $$("#ash-list-body .ash-list__item").forEach((button) =>
    button.setAttribute("aria-current", String(button.dataset.sutra === sutraId))
  );
  try {
    const [detail, graph] = await Promise.all([
      ashGet(`/api/astadhyayi/sutra?id=${encodeURIComponent(sutraId)}`),
      ashGet(
        `/api/astadhyayi/graph?id=${encodeURIComponent(sutraId)}`
      ),
    ]);
    ASH.cases = (detail.playground && detail.playground.cases) || [];
    panel.innerHTML = ashDetail(detail, graph);
    announce(`${sutraId} ${detail.iast}`);
  } catch (error) {
    panel.innerHTML = errorBanner(error.message);
  }
}

function initAstadhyayi() {
  const listBody = $("#ash-list-body");
  const search = $("#ash-search");
  const panel = $("#ash-detail");
  if (!listBody || !panel) return;

  let loaded = false;
  const load = async () => {
    if (loaded) return;
    loaded = true;
    try {
      const data = await ashGet("/api/astadhyayi/catalogue");
      ASH.catalogue = data.sutras;
      const percent = ((data.codified / data.total) * 100).toFixed(2);
      $("#ash-bar").style.width = `${Math.max(Number(percent), 0.4)}%`;
      $("#ash-count").textContent = `${data.codified} of ${data.total}`;
      $("#ash-progress-text").textContent =
        `${data.codified} sūtras codified · ${percent}%` +
        (data.pada_complete.length
          ? ` · pāda ${data.pada_complete.join(", ")} complete`
          : "");
      listBody.innerHTML = ashListRows(ASH.catalogue);
      if (ASH.catalogue.length) ashSelect(ASH.catalogue[0].id);
    } catch (error) {
      panel.innerHTML = errorBanner(error.message);
    }
  };

  // Only fetch when the section is actually opened.
  if (location.hash.replace("#", "") === "astadhyayi") load();
  window.addEventListener("hashchange", () => {
    if (location.hash.replace("#", "") === "astadhyayi") load();
  });
  $$('[data-route="astadhyayi"]').forEach((link) =>
    link.addEventListener("click", load)
  );

  search.addEventListener("input", () => {
    listBody.innerHTML = ashListRows(ashFilter(search.value));
  });

  listBody.addEventListener("click", (event) => {
    const eye = event.target.closest("[data-peek]");
    if (eye) {
      const already = PEEK.pinned === eye.dataset.peek;
      peekHide(true);
      if (!already) {
        peekShow(eye);
        PEEK.pinned = eye.dataset.peek;
      }
      return;
    }
    const button = event.target.closest("[data-sutra]");
    if (button) ashSelect(button.dataset.sutra);
  });

  listBody.addEventListener("mouseover", (event) => {
    const eye = event.target.closest("[data-peek]");
    if (eye && !PEEK.pinned) peekShow(eye);
  });

  listBody.addEventListener("mouseout", (event) => {
    if (event.target.closest("[data-peek]")) peekHide(false);
  });

  listBody.addEventListener("focusin", (event) => {
    const eye = event.target.closest("[data-peek]");
    if (eye && !PEEK.pinned) peekShow(eye);
  });

  listBody.addEventListener("focusout", (event) => {
    if (event.target.closest("[data-peek]")) peekHide(false);
  });

  // Scrolling the list would leave the panel stranded beside nothing.
  listBody.parentElement.addEventListener("scroll", () => peekHide(true));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") peekHide(true);
  });

  panel.addEventListener("click", (event) => {
    const node = event.target.closest(".ash-graph__node[data-sutra]");
    if (node) {
      ashSelect(node.dataset.sutra);
      return;
    }
    const toggle = event.target.closest(".ash-graph__toggle");
    if (toggle) event.stopPropagation();
  });

  panel.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") return;
    const node = event.target.closest(".ash-graph__node[data-sutra]");
    if (node) {
      event.preventDefault();
      ashSelect(node.dataset.sutra);
    }
  });

  panel.addEventListener("change", (event) => {
    if (event.target.id !== "ash-cross") return;
    ASH.crossLinks = event.target.checked;
    if (ASH.current) ashSelect(ASH.current);
  });

  panel.addEventListener("click", (event) => {
    const button = event.target.closest("[data-case]");
    if (!button) return;
    const chosen = (ASH.cases || [])[Number(button.dataset.case)];
    if (!chosen) return;
    ashFillCase(chosen.values);
    const form = $("#ash-play-form");
    if (form) form.requestSubmit();
  });

  panel.addEventListener("submit", async (event) => {
    if (event.target.id !== "ash-play-form") return;
    event.preventDefault();
    const values = {};
    $$("[data-field]", event.target).forEach((input) => {
      values[input.dataset.field] =
        input.type === "checkbox" ? input.checked : input.value;
    });
    const output = $("#ash-play-output");
    await withPending($("#ash-run"), "Running…", async () => {
      try {
        const payload = await api("/api/astadhyayi/run", {
          id: ASH.current,
          values,
        });
        output.innerHTML = ashResult(payload);
      } catch (error) {
        output.innerHTML = errorBanner(error.message);
      }
    });
  });
}

/* ==================================================================== */
/* Boot                                                                 */
/* ==================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initThemeToggle();
  initReadingSizeToggle();
  initRouting();
  initClassifier();
  initSubanta();
  initModal();
  initReverse();
  initTinanta();
  initDerivatives();
  initChandas();
  initAstadhyayi();
});
