**English** | [简体中文](README.zh-CN.md)

# Fitting the Practice: A Data Methodology for Frontier Model Training, with a Readiness Audit of 2026 Flagship Pipelines

*Yugui Yu · YYG Strategy Lab · they4897@gmail.com*

**[Read the paper (PDF)](paper.pdf) · [中文版（PDF）](paper_zh.pdf) · [LaTeX source](paper.tex) · [Audit matrix](analysis/matrix_cells.csv)**

## The methodology in one sentence

The stock has a wall; the flow does not — **and the flow requires a stack**: fourteen protocol components across a four-layer data stack (collection → cleaning → absorption, with a governance band), organized into three lines, that turn human practice into a trainable data supply.

This is the engineering companion to the **human-referential fitting theory of AGI** (AGI 人本拟合论, [concept DOI 10.5281/zenodo.23391808](https://doi.org/10.5281/zenodo.23391808)): the theory names the fitting object — practice, not works; this paper specifies the pipeline.

## The readiness audit in numbers

Eight 2026 flagship pipelines (DeepSeek-V4.1-Flash, MiMo-V2.6, GLM-5, Kimi K3, Qwen3-Coder-Next, GPT-6 Sol/Luna, Claude Opus 5.5, Grok V9-Medium), scored 0–3 on disclosed instantiation of each component, every non-zero cell carrying a verbatim quote and locator:

- **32 / 112** total (mean level 0.286); 89 cells (79.5%) are zero
- Three lines separate sharply: **production 0.393 ≫ governance 0.333 ≫ distribution 0.062**
- Four components absent from all eight disclosures: typed space (C1), coverage monitor (C2), coverage dashboard (C4), provenance stratification (C10)
- The matrix's only level-3 cell: MiMo-V2.6's pseudo-failure discrimination (C8)
- Closest pipeline to the methodology: DeepSeek-V4.1-Flash (7 points, mean 0.500)

## What is here

| Path | Contents |
|---|---|
| `paper.pdf` / `paper_zh.pdf` | English and Chinese manuscripts (LaTeX sources included) |
| `analysis/matrix_cells.csv` | The full 8×14 audit matrix: 112 cells with level, confidence grade, boundary rule, verbatim quote, locator, source document, and access date (2026-10-16); the 89 zero cells retain their search traces |
| `analysis/quotes.json` | Verbatim English quotes with locators and fidelity grades for all non-zero cells |
| `analysis/coding_data.py` | Frozen 0–3 scale, boundary rules (R1a/R2a/R3a), per-component search vocabularies, pilot calibration cells |
| `analysis/number_citations.py` | Reference renumbering utilities |
| `figures/` | Fig. 1 (four-layer data stack) and Fig. 2 (readiness heatmap), 300 dpi |
| `04_manuscript.md` / `04_manuscript_zh.md` | Markdown editions of both manuscripts |

## The fourteen components

**Distribution = typed full-spectrum coverage (C1–C4):** typed type space · coverage monitor · coverage-driven collection · coverage dashboard.
**Production = perpetual collection (C5–C11):** production telemetry · organized failure submission · three-part failure records · pseudo-failure discrimination · domain-conditioned mixing · provenance stratification · three-tier absorption.
**Governance = pluralistic aggregation (C12–C14):** aggregation mechanisms · verifier institutionalization · consent and the feasible set.

Each component carries an operational definition, a protocol, failure modes, and an instantiation survey kept explicitly separate from the normative spec.

## Reproducing the audit

The coding is single-coder under a frozen codebook, with limitations stated in §6 of the paper; a 20% stratified blind re-coding (23 cells) is scheduled for 2026-10-30, after which raw agreement and Cohen's κ will be reported in the next version. All coded claims trace to verbatim quotes in `matrix_cells.csv`.

## Related work in this program

- **The theory:** *Fitting the Practice, Not the Works: A Human-Referential Theory of AGI* ([10.5281/zenodo.23391808](https://doi.org/10.5281/zenodo.23391808), [GitHub](https://github.com/yuyuguilab/practice-fitting-theory))
- **The failure-data audit:** *Success Provides Direction, Failure Provides Precision* ([10.5281/zenodo.23355929](https://doi.org/10.5281/zenodo.23355929), [GitHub](https://github.com/yuyuguilab/failure-data-audit))

## License

Code in `analysis/` is licensed MIT (see [LICENSE](LICENSE)); the manuscript, figures, and coding data are licensed CC BY 4.0.
