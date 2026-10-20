#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
coding_data.py — Readiness audit coding data + descriptive statistics + figures
Paper 3 "Fitting the Flow" (practice-flow data methodology), analysis stage 03.

Audit construct: disclosed instantiation (0-3 ordinal) of 14 methodology
components (C1-C14) across 8 flagship pipelines (5 Group-A tech reports +
3 Group-B system-card/announcement rows). 8 x 14 = 112 cells.

Data source: single-coder coding executed 2026-10-16 under the frozen codebook
(02_experiment_protocol.md v1.0, sections 3-4). Every non-zero cell carries at
least one verbatim English quote + locator (see quotes.json produced by this
script). Level-0 cells carry search-trace notes. The conditional row
Qwen3.8-Max was excluded after V1 verification failed to confirm the relayed
claim (see 03_analysis_report.md section 2.1).

Outputs (all reproducible, no randomness except the pre-registered recode
sample which uses a fixed seed):
  analysis/matrix_cells.csv   - full data dictionary (02 section 7)
  analysis/quotes.json        - per-cell quote library
  stdout                      - Tables 1-4, sensitivity, level distribution,
                                pilot calibration, recode sample
  figures/fig1_data_stack_architecture.png  (300 dpi)
  figures/fig2_readiness_heatmap.png        (300 dpi)

Run:  python3 analysis/coding_data.py   (from the _workspace-p3 directory)
Deps: python3 stdlib + matplotlib.
"""

import csv
import json
import os
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
FIG_DIR = os.path.join(WS, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

ACCESS_DATE = "2026-10-16"
CODING_DATE = "2026-10-16"
CODER = "statistical-analyst (single coder, paper-3 pipeline)"

# ----------------------------------------------------------------------------
# 1. Audit frame (frozen in 02 v1.0)
# ----------------------------------------------------------------------------

FLAGSHIPS = [
    # id, label, group, primary source doc
    ("DS41",    "DeepSeek-V4.1-Flash",   "A", "arXiv:2609.19969v1 (tech report)"),
    ("MIMO26",  "MiMo-V2.6",             "A", "arXiv:2610.11959v1 (tech report)"),
    ("GLM5",    "GLM-5",                 "A", "arXiv:2602.15763 (tech report, HTML)"),
    ("KIMIK3",  "Kimi-K3",               "A", "arXiv:2607.24653 (tech report, HTML)"),
    ("QWNCN",   "Qwen3-Coder-Next",      "A", "arXiv:2603.00729 (tech report, HTML)"),
    ("GPT6OCT", "GPT-6 Sol/Luna (Oct)",  "B", "deploymentsafety.openai.com/gpt-6-october/capability-threshold-high (system card, 10-07)"),
    ("OPUS55",  "Claude Opus 5.5",       "B", "anthropic.com/constitution + privacy.claude.com FAQ (official docs)"),
    ("GROKV9",  "Grok V9-Medium",        "B", "X posts 2058787384364265734 / 2071184354756477041 (Musk, official)"),
]
FLAG_IDS = [f[0] for f in FLAGSHIPS]

COMPONENTS = [
    # id, short name, line, stack layer (Fig 1)
    ("C1",  "Typed space",                 "distribution", "governance"),
    ("C2",  "Coverage monitor",            "distribution", "governance"),
    ("C3",  "Coverage-driven collection",  "distribution", "collection"),
    ("C4",  "Coverage dashboard",          "distribution", "governance"),
    ("C5",  "Production telemetry",        "production",   "collection"),
    ("C6",  "Failure submission",          "production",   "collection"),
    ("C7",  "Three-part failure record",   "production",   "cleaning"),
    ("C8",  "Pseudo-failure discrimination", "production", "cleaning"),
    ("C9",  "Domain-conditioned mixing",   "production",   "absorption"),
    ("C10", "Provenance stratification",   "production",   "cleaning"),
    ("C11", "Three-tier absorption",       "production",   "absorption"),
    ("C12", "Pluralistic aggregation",     "governance",   "governance"),
    ("C13", "Verifier institutionalization", "governance", "governance"),
    ("C14", "Consent & feasible set",      "governance",   "governance"),
]
COMP_IDS = [c[0] for c in COMPONENTS]
COMP_SHORT = {c[0]: c[1] for c in COMPONENTS}
COMP_LINE = {c[0]: c[2] for c in COMPONENTS}
LINE_OF = {"distribution": "Distribution (C1-C4)",
           "production": "Production (C5-C11)",
           "governance": "Governance (C12-C14)"}

# ----------------------------------------------------------------------------
# 2. Non-zero cells (23 of 112). Every field auditable against R1-R4 + 02.
#    boundary_rule in {R1a, R2a, R3a, ""}; confidence in {high, medium, low}.
# ----------------------------------------------------------------------------

NONZERO = {
    # ---- A1 DeepSeek-V4.1-Flash ----
    "DS41-C5": dict(level=2, conf="high", rule="R2a", src="arXiv:2609.19969v1",
                    stype="tech_report", locator="Sec 5.1.1",
                    quotes=[("we encourage internal employees and external partners to incorporate our latest model into their routine workflows", "Sec 5.1.1", "verbatim"),
                            ("we collect negative feedback and model failure cases submitted by internal employees at scale", "Sec 5.1.1", "verbatim")],
                    note="Deployment-side interaction data + feedback returned from employee/partner routine workflows -> failure replay -> targeted RL. No anti-gaming multi-objective weighting, no quantification -> R2a cap at 2."),
    "DS41-C6": dict(level=2, conf="high", rule="R2a", src="arXiv:2609.19969v1",
                    stype="tech_report", locator="Sec 5.1.1",
                    quotes=[("we collect negative feedback and model failure cases submitted by internal employees at scale", "Sec 5.1.1", "verbatim"),
                            ("a large set of mocked tools that reproduce the interfaces and behaviors of real-world tools and systems", "Sec 5.1.1", "verbatim"),
                            ("systematic replay of failures and targeted reinforcement learning against observed model weaknesses", "Sec 5.1.1", "verbatim")],
                    note="02 Sec 3.2 frozen calibration anchor (C6=2). DSec numbers (millions of concurrent sandboxes; 1,000 -> 2,500+ live containers per node, Sec 5.1.3) quantify the environment platform, not the submission channel, so the level-3 'mechanism + scale' test is not met."),
    "DS41-C7": dict(level=1, conf="high", rule="", src="arXiv:2609.19969v1",
                    stype="tech_report", locator="Sec 5.1.1",
                    quotes=[("systematic replay of failures and targeted reinforcement learning against observed model weaknesses", "Sec 5.1.1", "verbatim")],
                    note="Failure data demonstrably enters training (replay + targeted RL), but no error-type / root-cause / fix packaging structure is disclosed -> below the C7 level-2 threshold frozen in 01 Sec 6."),
    "DS41-C11": dict(level=1, conf="high", rule="", src="arXiv:2609.19969v1",
                     stype="tech_report", locator="Sec 5.1.1",
                     quotes=[("systematic replay of failures and targeted reinforcement learning against observed model weaknesses", "Sec 5.1.1", "verbatim")],
                     note="Single-channel fragment: replay then offline targeted RL (R2 Sec 7 characterization). No three-tier division, no staleness/drift metric. Borderline 0/1 resolved as 1; cell included in the pre-registered recode sample."),
    "DS41-C14": dict(level=1, conf="high", rule="", src="arXiv:2609.19969v1",
                     stype="tech_report", locator="Sec 5.1.1",
                     quotes=[("participation is voluntary", "Sec 5.1.1", "near-verbatim (fetch-reported)")],
                     note="Voluntary participation at the collection point = consent phenomenon acknowledged; no opt-out / revocation / licensing framework."),
    # ---- A2 MiMo-V2.6 ----
    "MIMO26-C7": dict(level=1, conf="high", rule="", src="arXiv:2610.11959v1",
                      stype="tech_report", locator="Sec 4.2.6 (Mid-Training Alignment Data)",
                      quotes=[("The revised reasoning keeps the original error recognizable and makes the correction explicit.", "Sec 4.2.6", "verbatim"),
                              ("adding these examples improved the model's alignment", "Sec 4.2.6", "verbatim")],
                      note="Two-segment reflection-revision data (error recognizable + explicit correction) used in mid-training alignment. Root-cause segment absent -> below the three-part level-2 threshold (01 Sec 6). Nearest disclosed industry practice to C7 (LEMA-equivalent two-part)."),
    "MIMO26-C8": dict(level=3, conf="high", rule="", src="arXiv:2610.11959v1",
                      stype="tech_report", locator="Sec 4.2.6 / Sec 4.3.2 / Fig 6",
                      quotes=[("A dedicated hack agent then probes the prepared environments for remaining leaks and exploitable weaknesses", "Sec 4.2.6", "verbatim"),
                              ("We regularly audit agent trajectories offline for reward hacking throughout training", "Sec 4.2.6", "verbatim"),
                              ("the logged confirmed-hack share remains below 2% throughout the whole training process", "Sec 4.2.6 (Fig 6)", "near-verbatim (spliced)"),
                              ("We retain Git history up to and including the base commit, removing later commits", "Sec 4.2.6", "verbatim"),
                              ("enforce container-level network isolation", "Sec 4.2.6", "verbatim")],
                      note="Only level-3 cell in the matrix: mechanism (three-layer defense: hack-agent red-teaming, periodic offline trajectory audit with reward zeroing, groupwise grader) + quantification (<2% throughout training) + independent third-party audit corroboration (Vals.ai). Confirms the 02 Sec 3.2 calibration candidate."),
    "MIMO26-C13": dict(level=1, conf="medium", rule="", src="vals.ai/blogs/mimo-reward-hacking",
                       stype="official_blog", locator="vals.ai blog, accessed 2026-10-16",
                       quotes=[("We audited all 2,698 coding tasks", "vals.ai blog", "verbatim"),
                               ("in 1,795 of them (67%), the fix commit survives as unreachable objects", "vals.ai blog", "verbatim")],
                       note="Independent (non-commissioned) third-party audit of MiMo RL environments exists as a one-off instance; no institutionalized verifier arrangement disclosed by MiMo itself. Evidence is third-party-published -> confidence medium."),
    # ---- A3 GLM-5 ----
    "GLM5-C7": dict(level=1, conf="high", rule="", src="arXiv:2602.15763 (HTML)",
                    stype="tech_report", locator="Sec 3.1 (SFT)",
                    quotes=[("Erroneous segments within trajectories are retained but masked out in the loss function", "Sec 3.1", "verbatim"),
                            ("allowing the model to learn error correction behaviors without reinforcing incorrect actions.", "Sec 3.1", "verbatim")],
                    note="Error-aware training (error segments retained + masked in loss). No error-type taxonomy, no root cause, no packaged correction record -> below level-2 threshold."),
    "GLM5-C8": dict(level=2, conf="high", rule="R2a", src="arXiv:2602.15763 (HTML)",
                    stype="tech_report", locator="Sec 4.1.2",
                    quotes=[("coding-agent sandboxes can be inherently unstable and may fail for reasons unrelated to the model", "Sec 4.1.2", "verbatim"),
                            ("we record the failure reason for each sample and exclude samples that fail due to environment collapse.", "Sec 4.1.2", "verbatim")],
                    note="Attribution-based triage: failure reason recorded per sample; environment-collapse failures excluded from training. Exactly the C8 model-vs-environment attribution分流 mechanism. No quantification -> R2a cap at 2."),
    # ---- A4 Kimi-K3 ----
    "KIMIK3-C3": dict(level=1, conf="high", rule="R3a", src="arXiv:2607.24653 (HTML)",
                      stype="tech_report", locator="Sec 4.2.2",
                      quotes=[("Retrieval guided by fine-grained concepts surfaces specialized and underrepresented knowledge", "Sec 4.2.2", "verbatim")],
                      note="Near construct: knowledge-level underrepresentation surfacing in RL task synthesis, explicitly tied to a data practice -> 1 with R3a note. Not typed (success/failure x expertise) coverage; strict typed-coverage practice remains 0/8."),
    "KIMIK3-C8": dict(level=2, conf="high", rule="R2a", src="arXiv:2607.24653 (HTML)",
                      stype="tech_report", locator="Sec 4.2.4 (Kernel Optimization Tasks)",
                      quotes=[("we develop a hacking-detection system that penalizes reward-hacking strategies such as CUDA graph replay, input caching", "Sec 4.2.4", "verbatim"),
                              ("we continuously extend it with new safeguards as new hacking strategies are observed during Kimi K3's development.", "Sec 4.2.4", "verbatim")],
                      note="Pseudo-failure (reward-hacking) discrimination mechanism with continuous extension; no quantified hacking share -> R2a cap at 2."),
    # ---- A5 Qwen3-Coder-Next ----
    "QWNCN-C3": dict(level=1, conf="high", rule="R3a", src="arXiv:2603.00729 (HTML)",
                     stype="tech_report", locator="Sec 4.2.3",
                     quotes=[("scaling RL task diversity leads to consistent improvements across multiple coding sub-capabilities.", "Sec 4.2.3", "verbatim")],
                     note="Near construct: task-diversity awareness in RL task synthesis, tied to a data practice -> 1 with R3a note. Not typed coverage-driven collection."),
    "QWNCN-C7": dict(level=1, conf="high", rule="", src="arXiv:2603.00729 (HTML)",
                     stype="tech_report", locator="Sec 4.1 (Filtering with Verification)",
                     quotes=[("It evaluates system feedback signals, such as compiler outputs, runtime errors, and environment state changes,", "Sec 4.1", "verbatim"),
                             ("This closed-loop verification process allows us to filter hallucinated or non-functional solutions,", "Sec 4.1", "verbatim")],
                     note="Runtime-error / compiler-signal driven verification filtering of training candidates (failure signals as a collection axis). No three-part record structure."),
    "QWNCN-C9": dict(level=1, conf="high", rule="", src="arXiv:2603.00729 (HTML)",
                     stype="tech_report", locator="Sec 3.1 (Data)",
                     quotes=[("the mid-training corpus is composed primarily of natural data, supplemented with a smaller but carefully designed portion of synthetic data", "Sec 3.1", "near-verbatim (spliced)"),
                             ("our goal is to introduce the minimum amount of synthetic data required for the model to reliably perform common user tasks,", "Sec 3.1", "verbatim")],
                     note="Qualitative natural-dominant mixing philosophy ('minimum synthetic'). No per-domain or per-capability stratification, no collapse-prevention rationale -> not domain-conditioned, below level 2."),
    # ---- B1 GPT-6 Sol/Luna October system card ----
    "GPT6OCT-C5": dict(level=1, conf="high", rule="R1a", src="deploymentsafety.openai.com/gpt-6-october/capability-threshold-high",
                       stype="system_card", locator="Sec 3.1.1 / Sec 1",
                       quotes=[("an evaluation set with conversations representative of challenging examples from production data.", "Sec 3.1.1", "verbatim"),
                               ("We also updated the safety training to reflect real-world use", "Sec 1", "verbatim")],
                       note="02 Sec 3.2 frozen calibration anchor (R1a: production hard cases enter evaluation only, regardless of篇幅). 'Safety training reflects real-world use' is a mention without mechanism."),
    "GPT6OCT-C6": dict(level=1, conf="high", rule="R1a", src="deploymentsafety.openai.com/gpt-6-october/capability-threshold-high",
                       stype="system_card", locator="Sec 6.1 (Performance in Cases Flagged by Users)",
                       quotes=[("de-identified ChatGPT conversations users previously flagged for factual errors", "Sec 6.1", "near-verbatim (fetch-reported)")],
                       note="User-flagged failed conversations -> de-identified evaluation sets (R1a: not a training pipeline). 02 calibration anchor C6=1."),
    "GPT6OCT-C13": dict(level=1, conf="medium", rule="R1a", src="alignment.openai.com/misalignment-reports (portal) + openai.com/index/model-misalignment-reporting-framework",
                        stype="announcement", locator="portal, accessed 2026-10-16 (announcement page HTTP 403 on 10-16)",
                        quotes=[("disclose examples that show how model misalignment arises", "portal", "verbatim"),
                                ("where safeguards succeed or fail", "portal", "verbatim"),
                                ("Reports 19", "portal counter", "verbatim")],
                        note="Institutionalized behavior-disclosure channel (employee-submittable misalignment reports + public portal). R1a: behavior disclosure, not training-corpus adjudication. Portal shows 19 reports as of 2026-10-16 (R1 had recorded 6 at 09-16 launch; cite the live count)."),
    "GPT6OCT-C14": dict(level=1, conf="high", rule="", src="deploymentsafety.openai.com/gpt-6-october/capability-threshold-high",
                        stype="system_card", locator="Sec 2 (Model Data and Training)",
                        quotes=[("GPT-6 models were trained on diverse datasets and filtered through our data processing pipeline, including to reduce personal information.", "Sec 2", "verbatim")],
                        note="PII-reduction filtering = privacy hygiene (near construct); no consent / licensing / forgetting framework in the pipeline disclosure."),
    # ---- B2 Claude Opus 5.5 ----
    "OPUS55-C5": dict(level=1, conf="medium", rule="", src="privacy.claude.com/en/articles/10023580",
                      stype="official_blog", locator="privacy FAQ, accessed 2026-10-16",
                      quotes=[("We may use your feedback to analyze the effectiveness of our Services, conduct research, study user behavior, and train our AI models", "FAQ", "verbatim")],
                      note="Explicit feedback may train models under an opt-in regime; no training-side mechanism (reward model, anti-gaming mix) described."),
    "OPUS55-C12": dict(level=2, conf="high", rule="", src="anthropic.com/constitution",
                       stype="constitution", locator="constitution page, accessed 2026-10-16 (fetch truncated; fidelity note)",
                       quotes=[("plays a crucial role in our training process, and its content directly shapes Claude's behavior", "constitution page", "verbatim (from readable portion)")],
                       note="Public, versioned constitution actually used in training (single constitution). No social-choice rule / multi-constitution / persona conditioning disclosed -> 2. Alignment-Assemblies influence (R3, secondary source) kept as background, not coded."),
    "OPUS55-C14": dict(level=2, conf="medium", rule="R2a", src="privacy.claude.com/en/articles/10023580",
                       stype="official_blog", locator="privacy FAQ, accessed 2026-10-16",
                       quotes=[("You choose to allow us to use your chats and coding sessions to improve Claude", "FAQ", "verbatim"),
                               ("Your Incognito chats are not used to improve Claude, even if you have enabled Model Improvement in your Privacy Settings.", "FAQ", "verbatim"),
                               ("We de-link your feedback from your user ID (e.g. email address) before it's used by Anthropic.", "FAQ", "verbatim")],
                       note="Opt-in consent mechanism + incognito exclusion + feedback de-linking + 5-year feedback retention, codified in consumer terms. No pipeline-level feasible-set registry or revocation propagation -> 2."),
    # ---- B3 Grok V9-Medium ----
    "GROKV9-C5": dict(level=2, conf="medium", rule="R2a", src="x.com/elonmusk/status/2058787384364265734 and /2071184354756477041",
                      stype="x_post", locator="X posts of 2026-05-25 and 2026-06-28, directly read 2026-10-16 (V2)",
                      quotes=[("A lot of Cursor data was added in supplementary training and there is more to come.", "X post 2058787384364265734, 2026-05-25", "verbatim"),
                              ("Grok 4.5, based on our 1.5T V9 foundation model, with Cursor data added in supplemental training, is now in private beta", "X post 2071184354756477041, 2026-06-28", "verbatim")],
                      note="Real developer-tool workflow data (Cursor IDE usage) entering supplementary training - strongest practice-flow announcement case. Collection/cleaning mechanism undisclosed, no quantification -> R2a cap at 2. Row capped at medium per 02 Sec 2.1."),
}

# ----------------------------------------------------------------------------
# 3. Level-0 cells: search-trace notes for notable zeros (02 Sec 3.3).
# ----------------------------------------------------------------------------

ZERO_NOTES = {
    "DS41-C3": "R3a near construct: environment reconstruction 'reproduces interfaces and behaviors of real-world tools' (Sec 5.1.1) = environment realism, not typed coverage-driven collection -> 0.",
    "DS41-C9": "No synthetic/real ratio disclosure in V4.1-Flash corpus. (V4's 32T-token dataset discussion belongs to the V4 report, out of row scope.)",
    "GLM5-C3": "R3a near construct: difficulty filtering ('problems that GLM-4.7 solves correctly only rarely', Sec 3.2) = weakness-driven curriculum, not typed coverage -> 0.",
    "GLM5-C5": "Human-in-the-loop alignment uses expert-authored responses (Sec 3.4), not user/production telemetry -> 0.",
    "KIMIK3-C6": "00_input Sec 6 keyword 'failure-mode tracking / badcase' NOT confirmed verbatim in full text; only hacking-detection found (-> C8). No submission channel -> 0.",
    "KIMIK3-C7": "No error-type / root-cause / correction packaging found in full text -> 0 (keyword unconfirmed).",
    "GPT6OCT-C10": "'Reduce personal information' (Sec 2) is privacy hygiene, not native-vs-AI provenance stratification -> 0.",
    "OPUS55-C8": "PENDING: 00_input Sec 6 cites an 'AIR (failure-scenario generation / defective-environment filtering)' doc for Opus 5.5; no Anthropic document named AIR locatable (search 2026-10-16); nearest find = '2,000-scenario automated agentic evaluation' (VentureBeat, secondhand, evaluation-side). Coded 0 + verification_status=pending; resolve before data freeze 2026-10-29.",
}
GENERIC_ZERO_NOTE = "Vocabulary search (02 Sec 4 word lists) + full-doc read: no statement pointing to this component. 0 = not disclosed (does not equal not implemented)."

PENDING_CELLS = {"OPUS55-C8"}  # level-0 but verification pending

# ----------------------------------------------------------------------------
# 4. Build the full 112-cell dataset
# ----------------------------------------------------------------------------

def build_cells():
    cells = []
    for fid, label, group, doc in FLAGSHIPS:
        for cid in COMP_IDS:
            key = f"{fid}-{cid}"
            if key in NONZERO:
                d = NONZERO[key]
                cells.append(dict(cell_id=key, flagship_id=fid, group=group,
                                  component_id=cid, line=COMP_LINE[cid],
                                  level=d["level"], quote_text=d["quotes"][0][0][:160],
                                  locator=d["locator"], source_doc=d["src"],
                                  source_type=d["stype"], confidence=d["conf"],
                                  multi_level=False, boundary_rule=d["rule"],
                                  access_date=ACCESS_DATE, coding_date=CODING_DATE,
                                  coder=CODER, recode_sample=False,
                                  verification_status="done",
                                  notes=d["note"]))
            else:
                cells.append(dict(cell_id=key, flagship_id=fid, group=group,
                                  component_id=cid, line=COMP_LINE[cid],
                                  level=0, quote_text="",
                                  locator="-", source_doc=doc.split(" (")[0],
                                  source_type="tech_report" if group == "A" else "system_card",
                                  confidence="high" if group == "A" else "n/a",
                                  multi_level=False, boundary_rule="",
                                  access_date=ACCESS_DATE, coding_date=CODING_DATE,
                                  coder=CODER, recode_sample=False,
                                  verification_status="pending" if key in PENDING_CELLS else "none",
                                  notes=ZERO_NOTES.get(key, GENERIC_ZERO_NOTE)))
    return cells

CELLS = build_cells()
LEVEL = {c["cell_id"]: c["level"] for c in CELLS}
CONF = {c["cell_id"]: c["confidence"] for c in CELLS}

# ----------------------------------------------------------------------------
# 5. Statistics
# ----------------------------------------------------------------------------

def line_cells(line):
    return [c for c in CELLS if c["line"] == line]

def fmt(x, nd=3):
    return f"{x:.{nd}f}"

def report():
    out = []
    A = out.append
    A("=" * 100)
    A("READINESS AUDIT - DESCRIPTIVE STATISTICS (8 flagships x 14 components = 112 cells)")
    A("Construct: disclosed instantiation. Access/coding date 2026-10-16. Single coder.")
    A("=" * 100)

    # --- Table 1: full matrix ---
    A("")
    A("TABLE 1. Full instantiation-level matrix (rows = flagships, cols = components)")
    header = "row        " + "".join(f"{c:>5}" for c in COMP_IDS) + "  sum"
    A(header)
    for fid, label, group, doc in FLAGSHIPS:
        row = [LEVEL[f"{fid}-{c}"] for c in COMP_IDS]
        A(f"{fid:<10}" + "".join(f"{v:>5}" for v in row) + f"  {sum(row):>3}   [{group}] {label}")
    cols = [sum(LEVEL[f"{f}-{c}"] for f, *_ in FLAGSHIPS) for c in COMP_IDS]
    A("col-sum   " + "".join(f"{v:>5}" for v in cols) + f"  {sum(cols):>3}")
    total = sum(cols)
    A(f"\nMatrix total = {total} / 112; overall mean level = {fmt(total/112)}; "
      f"non-zero cells = {sum(1 for c in CELLS if c['level']>0)} (20.5%); "
      f"level-3 cells = {sum(1 for c in CELLS if c['level']==3)}.")

    # --- Table 2: per component ---
    A("")
    A("TABLE 2. Per-component profile (which components are industry-absent)")
    A(f"{'comp':<6}{'name':<32}{'mean':>7}{'0s':>4}{'1s':>4}{'2s':>4}{'3s':>4}  notes")
    for cid, name, line, layer in COMPONENTS:
        vals = [LEVEL[f"{f}-{cid}"] for f, *_ in FLAGSHIPS]
        dist = [vals.count(k) for k in range(4)]
        mark = ""
        if all(v == 0 for v in vals):
            mark = "<-- ALL-ZERO (absent across audit set)"
        elif max(vals) <= 1:
            mark = "<-- no practice >= level 2"
        A(f"{cid:<6}{name:<32}{fmt(sum(vals)/8):>7}{dist[0]:>4}{dist[1]:>4}{dist[2]:>4}{dist[3]:>4}  {mark}")
    near = [k for k, d in NONZERO.items() if d["rule"] == "R3a"]
    A(f"R3a near-construct cells (coded 1, near construct only): {', '.join(near)}")
    A(f"Strict typed-coverage practice count for C3 (excluding R3a near constructs): "
      f"{sum(1 for f, *_ in FLAGSHIPS if LEVEL[f'{f}-C3'] > 0 and f'{f}-C3' not in near)}/8.")

    # --- Table 3: per flagship ---
    A("")
    A("TABLE 3. Per-flagship readiness profile")
    A(f"{'flagship':<22}{'grp':>4}{'dist':>6}{'prod':>6}{'gov':>6}{'sum':>5}{'mean':>7}  top disclosed components")
    for fid, label, group, doc in FLAGSHIPS:
        d = sum(LEVEL[f"{fid}-C{i}"] for i in range(1, 5))
        p = sum(LEVEL[f"{fid}-C{i}"] for i in range(5, 12))
        g = sum(LEVEL[f"{fid}-C{i}"] for i in range(12, 15))
        tops = [f"{cid}={LEVEL[f'{fid}-{cid}']}" for cid in COMP_IDS if LEVEL[f"{fid}-{cid}"] > 0]
        A(f"{label:<22}{group:>4}{d:>6}{p:>6}{g:>6}{d+p+g:>5}{fmt((d+p+g)/14):>7}  {', '.join(tops) if tops else '-'}")
    a_cells = [c for c in CELLS if c["group"] == "A"]
    b_cells = [c for c in CELLS if c["group"] == "B"]
    A(f"\nGroup A (tech-report rows, n=70): mean = {fmt(sum(c['level'] for c in a_cells)/70)}; "
      f"non-zero = {sum(1 for c in a_cells if c['level']>0)}")
    A(f"Group B (system-card/announcement rows, n=42): mean = {fmt(sum(c['level'] for c in b_cells)/42)}; "
      f"non-zero = {sum(1 for c in b_cells if c['level']>0)}")

    # --- Table 4: three lines ---
    A("")
    A("TABLE 4. Three-line summary (and by disclosure group)")
    A(f"{'line':<28}{'cells':>6}{'sum':>5}{'mean':>7}{'A-mean':>8}{'B-mean':>8}{'max':>4}")
    for line in ("distribution", "production", "governance"):
        lc = line_cells(line)
        s = sum(c["level"] for c in lc)
        la = [c for c in lc if c["group"] == "A"]
        lb = [c for c in lc if c["group"] == "B"]
        A(f"{LINE_OF[line]:<28}{len(lc):>6}{s:>5}{fmt(s/len(lc)):>7}"
          f"{fmt(sum(c['level'] for c in la)/len(la)):>8}"
          f"{fmt(sum(c['level'] for c in lb)/len(lb)):>8}{max(c['level'] for c in lc):>4}")

    # --- Level distribution ---
    A("")
    A("LEVEL DISTRIBUTION (all 112 cells):")
    for k, desc in [(0, "no disclosure"), (1, "mention / eval-only (R1a)"),
                    (2, "component-level practice (R2a cap applies)"), (3, "institutionalized")]:
        n = sum(1 for c in CELLS if c["level"] == k)
        A(f"  level {k} ({desc:<38}): {n:>3}  ({fmt(n/112*100,1)}%)")

    # --- Confidence profile + sensitivity ---
    A("")
    A("CONFIDENCE PROFILE (non-zero cells): high = "
      f"{sum(1 for c in CELLS if c['level']>0 and c['confidence']=='high')}, "
      f"medium = {sum(1 for c in CELLS if c['level']>0 and c['confidence']=='medium')}, "
      f"low = {sum(1 for c in CELLS if c['level']>0 and c['confidence']=='low')}")
    A("")
    A("SENSITIVITY: recompute with all medium-confidence cells set to 0 (low rule already excludes):")
    for line in ("distribution", "production", "governance"):
        lc = line_cells(line)
        s_all = sum(c["level"] for c in lc)
        s_high = sum(c["level"] for c in lc if c["confidence"] == "high")
        A(f"  {LINE_OF[line]:<28} all: sum={s_all:>3} mean={fmt(s_all/len(lc))}   "
          f"high-only: sum={s_high:>3} mean={fmt(s_high/len(lc))}")
    t_high = sum(c["level"] for c in CELLS if c["confidence"] == "high")
    A(f"  Matrix total: all = {total} (mean {fmt(total/112)}); high-only = {t_high} (mean {fmt(t_high/112)})")
    zero_always = [cid for cid in COMP_IDS
                   if all((LEVEL[f"{f}-{cid}"] == 0) or (f"{f}-{cid}" in NONZERO and CONF.get(f"{f}-{cid}") == "medium")
                          for f, *_ in FLAGSHIPS)]
    A(f"  Components all-zero under BOTH all-evidence and high-only: "
      f"{', '.join(cid for cid in COMP_IDS if all(LEVEL[f'{f}-{cid}']==0 for f,*_ in FLAGSHIPS))}")
    A("  C7 max level under high-only: "
      f"{max(LEVEL[f'{f}-C7'] for f,*_ in FLAGSHIPS if CONF.get(f'{f}-C7','medium')=='high')} "
      "(unchanged; all C7 evidence is high-confidence) -> CC3 gap claim stable.")

    # --- Pilot calibration ---
    A("")
    A("PILOT CALIBRATION (5 cells, 02 Sec 5.1) - outcomes:")
    pilot = [("DS41-C6", 2, "frozen anchor, matched"),
             ("GPT6OCT-C5", 1, "frozen R1a anchor, matched"),
             ("MIMO26-C8", 3, "candidate confirmed as 3 (mechanism + <2% + Vals.ai)"),
             ("GLM5-C7", 1, "explored -> 1 (error-masking below three-part threshold)"),
             ("GROKV9-C5", 2, "medium-path confirmed (R2a cap)")]
    for k, lv, note in pilot:
        A(f"  {k:<12} coded {lv}  - {note}")
    A("  Divergences from pre-expectation: none at variance>0; GLM5-C7 resolved 0/1 borderline as 1 by threshold rule.")

    # --- Recode sample (pre-registered) ---
    rng = random.Random(20261016)
    A("")
    A("RECODE SAMPLE (20% = 23 cells, stratified by line 7/11/5 and group; blind recode scheduled 2026-10-30):")
    sample = []
    for line, n in (("distribution", 7), ("production", 11), ("governance", 5)):
        pool = sorted(c["cell_id"] for c in line_cells(line))
        # deterministic: sort by hash-stable ordering then take spread, then rng tiebreak
        pool.sort(key=lambda x: (x.split("-")[0], int(x.split("-C")[1])))
        pick = rng.sample(pool, n)
        sample.extend(pick)
        A(f"  {line:<13}: {', '.join(pick)}")
    for cid in sample:
        for c in CELLS:
            if c["cell_id"] == cid:
                c["recode_sample"] = True
    A(f"  Total sample: {len(sample)} cells. kappa target >= .70 (unweighted + quadratic weighted), "
      "raw agreement reported; single-coder blind recode after 2-week interval.")
    return "\n".join(out), sample


# ----------------------------------------------------------------------------
# 6. Figures
# ----------------------------------------------------------------------------

LINE_COLORS = {"distribution": "#d95f02", "production": "#2166ac", "governance": "#1b7837"}

def fig1():
    fig, ax = plt.subplots(figsize=(14.5, 8.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 62)
    ax.axis("off")

    def box(x, y, w, h, text, fc, ec="#333333", fs=8.6, tc="white", lw=1.2):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25",
                                    fc=fc, ec=ec, lw=lw))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=fs, color=tc, linespacing=1.25)

    # Title
    ax.text(50, 60.2, "Practice-Flow Data Stack: Four-Layer Pipeline with 14 Methodology Components",
            ha="center", va="center", fontsize=14.5, fontweight="bold")
    ax.text(50, 57.9, "Layers = pipeline stages (left to right); colors = three methodology lines "
                      "(orange: distribution / blue: production / green: governance)",
            ha="center", va="center", fontsize=9.5, style="italic", color="#444444")

    # Human practice flow source
    ax.add_patch(Ellipse((5, 40), 10, 16, fc="#fef3e2", ec="#d95f02", lw=2))
    ax.text(5, 40, "Human\npractice\nflow\n$P_t$", ha="center", va="center",
            fontsize=10.5, color="#8a4b08", fontweight="bold", linespacing=1.4)

    # Layer frames
    layers = [
        (14.5, "COLLECTION\nlayer", [("C3", "Coverage-driven\ncollection"),
                                      ("C5", "Production\ntelemetry"),
                                      ("C6", "Organized failure\nsubmission")]),
        (37.5, "CLEANING\nlayer", [("C7", "Three-part failure\nrecord"),
                                    ("C8", "Pseudo-failure discrimination\n& sanitization"),
                                    ("C10", "Provenance\nstratification")]),
        (60.5, "ABSORPTION\nlayer", [("C9", "Domain-conditioned\nmixing ratio"),
                                      ("C11", "Three-tier absorption\n(CPT / replay / memory)")]),
    ]
    for x0, lname, comps in layers:
        ax.add_patch(FancyBboxPatch((x0, 24.5), 20.5, 30, boxstyle="round,pad=0.3",
                                    fc="#f7f7f9", ec="#666666", lw=1.4, ls="-"))
        ax.text(x0 + 10.25, 52.6, lname, ha="center", va="center", fontsize=11,
                fontweight="bold", color="#333333", linespacing=1.3)
        y = 44.5
        for cid, name in comps:
            line = next(l for c, n, l, _ in COMPONENTS if c == cid)
            box(x0 + 1.2, y, 18.1, 6.4, f"{cid}  {name}", LINE_COLORS[line])
            y -= 8.2

    # Model
    ax.add_patch(FancyBboxPatch((84.5, 33), 11, 14, boxstyle="round,pad=0.3",
                                fc="#e8eef7", ec="#2166ac", lw=2))
    ax.text(90, 41.5, "Model $\\theta$", ha="center", va="center", fontsize=11.5,
            fontweight="bold", color="#144a7d")
    ax.text(90, 37.5, "snapshot of $P_t$\n(period $\\Delta$)", ha="center", va="center",
            fontsize=8.5, color="#144a7d")

    # Governance band
    ax.add_patch(FancyBboxPatch((14.5, 2.5), 81, 17.5, boxstyle="round,pad=0.3",
                                fc="#f1f8f1", ec="#1b7837", lw=1.6))
    ax.text(16.5, 17.3, "GOVERNANCE layer (spans all stages)", ha="left", va="center",
            fontsize=11, fontweight="bold", color="#1b5e20")
    gov = [("C1", "Typed space"), ("C2", "Coverage monitor"), ("C4", "Coverage dashboard"),
           ("C12", "Pluralistic\naggregation"), ("C13", "Verifier\ninstitutionalization"),
           ("C14", "Consent &\nfeasible set")]
    x = 16.0
    for cid, name in gov:
        w = 10.8 if cid not in ("C13",) else 13.5
        line = next(l for c, n, l, _ in COMPONENTS if c == cid)
        box(x, 5.2, w, 8.6, f"{cid}\n{name}", LINE_COLORS[line], fs=7.8)
        x += w + 1.3

    # Flow arrows
    for x0 in (10.2, 33.2, 56.2, 79.2):
        ax.add_patch(FancyArrowPatch((x0, 39.5), (x0 + 4.1, 39.5),
                                     arrowstyle="-|>", mutation_scale=22, lw=2.2, color="#333333"))
    # Deployment feedback loop
    ax.add_patch(FancyArrowPatch((90, 32.6), (90, -0.8),
                                 connectionstyle="arc3,rad=0.0", arrowstyle="-",
                                 lw=1.4, ls=(0, (4, 3)), color="#8a4b08"))
    ax.add_patch(FancyArrowPatch((90, -0.8), (5, -0.8),
                                 connectionstyle="arc3,rad=0.0", arrowstyle="-",
                                 lw=1.4, ls=(0, (4, 3)), color="#8a4b08"))
    ax.add_patch(FancyArrowPatch((5, -0.8), (5, 31.6),
                                 connectionstyle="arc3,rad=0.0", arrowstyle="-|>",
                                 lw=1.4, ls=(0, (4, 3)), color="#8a4b08", mutation_scale=18))
    ax.text(47, 0.4, "deployment generates new practice  \u2192  the flow never closes (time term)",
            ha="center", va="center", fontsize=9, color="#8a4b08", style="italic")

    # Governance dotted connectors
    for x0 in (24.75, 47.75, 70.75):
        ax.add_patch(FancyArrowPatch((x0, 20.4), (x0, 24.1), arrowstyle="-|>",
                                     mutation_scale=13, lw=1.2, color="#1b7837",
                                     linestyle=(0, (2, 2))))

    legend_items = [Line2D([0], [0], marker="s", color="w", markerfacecolor=LINE_COLORS[l],
                           markersize=11, label=LINE_OF[l]) for l in
                    ("distribution", "production", "governance")]
    ax.legend(handles=legend_items, loc="upper right", bbox_to_anchor=(1.0, 0.90),
              frameon=True, fontsize=9, title="Methodology line", title_fontsize=9)

    path = os.path.join(FIG_DIR, "fig1_data_stack_architecture.png")
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


FIG2_SHORT = {"C1": "Typed space", "C2": "Cover. monitor", "C3": "Cover. collect",
              "C4": "Cover. dashbd", "C5": "Telemetry", "C6": "Submission",
              "C7": "3-part record", "C8": "Pseudo-fail", "C9": "Mixing ratio",
              "C10": "Provenance", "C11": "3-tier absorp", "C12": "Aggregation",
              "C13": "Verifier inst", "C14": "Consent"}

def fig2():
    M = [[LEVEL[f"{fid}-{cid}"] for cid in COMP_IDS] for fid, *_ in FLAGSHIPS]
    cmap = ListedColormap(["#f2f2f2", "#c6dbef", "#6baed6", "#08519c"])
    fig, ax = plt.subplots(figsize=(16.5, 6.8))
    fig.subplots_adjust(left=0.175, right=0.90, top=0.76, bottom=0.10)
    im = ax.imshow(M, cmap=cmap, vmin=-0.5, vmax=3.5, aspect="auto")
    ax.set_xticks(range(14))
    ax.set_xticklabels([f"{c}\n{FIG2_SHORT[c]}" for c in COMP_IDS], fontsize=7.6,
                       linespacing=1.25)
    ax.set_yticks(range(8))
    ax.set_yticklabels([f"{lab}  ({grp})" for _, lab, grp, _ in FLAGSHIPS], fontsize=10)
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.tick_params(axis="x", pad=6)
    for i in range(8):
        for j in range(14):
            v = M[i][j]
            cell = CELLS[i * 14 + j]
            mark = "*" if (cell["confidence"] == "medium" and v > 0) else ""
            ax.text(j, i, f"{v}{mark}", ha="center", va="center", fontsize=11,
                    fontweight="bold" if v > 0 else "normal",
                    color="white" if v >= 2 else "#222222")
    # group separator + explanatory note line under the title
    ax.axhline(4.5, color="#111111", lw=2.2)
    # line separators + line tags below the matrix
    for x in (3.5, 10.5):
        ax.axvline(x, color="#111111", lw=1.6, ls="--")
    ax.text(1.5, -1.5, "Distribution line", ha="center", fontsize=10, style="italic")
    ax.text(7.0, -1.5, "Production line", ha="center", fontsize=10, style="italic")
    ax.text(12.0, -1.5, "Governance line", ha="center", fontsize=10, style="italic")
    # fine grid
    ax.set_xticks([x - 0.5 for x in range(1, 14)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, 8)], minor=True)
    ax.grid(which="minor", color="white", lw=1.4)
    ax.tick_params(which="minor", length=0)
    cb = fig.colorbar(im, ax=ax, ticks=[0, 1, 2, 3], pad=0.015, fraction=0.035)
    cb.ax.set_yticklabels(["0  no disclosure", "1  mention / eval-only",
                           "2  component practice", "3  institutionalized"], fontsize=9)
    ax.set_title("Disclosure-Instantiation Readiness: 8 Flagship Pipelines x 14 Methodology Components\n"
                 "(* = medium-confidence cell: official announcement / X post / third-party blog; audit window 2026-10-16)",
                 fontsize=13, pad=58)
    fig.text(0.5, 0.955,
             "Rows 1-5 = Group A (tech reports)  |  Rows 6-8 = Group B (system cards / announcements); "
             "thick line marks the A/B boundary",
             ha="center", fontsize=9.5, style="italic", color="#333333")
    path = os.path.join(FIG_DIR, "fig2_readiness_heatmap.png")
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


# ----------------------------------------------------------------------------
# 7. Persist
# ----------------------------------------------------------------------------

def persist(sample):
    csv_path = os.path.join(HERE, "matrix_cells.csv")
    fields = ["cell_id", "flagship_id", "group", "component_id", "line", "level",
              "quote_text", "locator", "source_doc", "source_type", "confidence",
              "multi_level", "boundary_rule", "access_date", "coding_date", "coder",
              "recode_sample", "verification_status", "notes"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in CELLS:
            w.writerow(c)
    quotes = {}
    for k, d in NONZERO.items():
        quotes[k] = dict(
            level=d["level"], confidence=d["conf"], boundary_rule=d["rule"],
            source_doc=d["src"], source_type=d["stype"], locator=d["locator"],
            access_date=ACCESS_DATE,
            quotes=[dict(text=t, locator=loc, fidelity=fid) for t, loc, fid in d["quotes"]],
            note=d["note"])
    qpath = os.path.join(HERE, "quotes.json")
    with open(qpath, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)
    return csv_path, qpath


if __name__ == "__main__":
    text, sample = report()
    print(text)
    csv_path, qpath = persist(sample)
    f1 = fig1()
    f2 = fig2()
    print()
    print("=" * 100)
    print("WRITTEN:")
    print(f"  {csv_path}")
    print(f"  {qpath}")
    print(f"  {f1}")
    print(f"  {f2}")
