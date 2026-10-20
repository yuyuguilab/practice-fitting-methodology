[English](README.md) | **简体中文**

# 拟合实践：前沿模型训练的数据方法论——附 2026 旗舰管线就绪度审计

*余玉桂 · 余玉桂战略研究室 · they4897@gmail.com*

**[阅读论文（PDF）](paper_zh.pdf) · [英文版（PDF）](paper.pdf) · [LaTeX 源码](paper_zh.tex) · [审计矩阵](analysis/matrix_cells.csv)**

## 一句话方法论

存量有墙，流量无墙——**而流量需要一个栈**：横跨四层数据栈（采集 → 清洗 → 吸收，治理带横贯全程）的十四个协议组件，按三条线组织，把人类实践变成可训练的数据供给。

本文是 **AGI 人本拟合论**（human-referential fitting theory，[概念 DOI 10.5281/zenodo.23391808](https://doi.org/10.5281/zenodo.23391808)）的工程姊妹篇：理论命名拟合对象——实践而非作品；本文规定管线。

## 就绪度审计数字一览

八条 2026 旗舰管线（DeepSeek-V4.1-Flash、MiMo-V2.6、GLM-5、Kimi K3、Qwen3-Coder-Next、GPT-6 Sol/Luna、Claude Opus 5.5、Grok V9-Medium），按十四个组件的披露实例化评分（0–3 级），每个非零格附逐字引文与定位符：

- 总分 **32 / 112**（均级 0.286）；89 格（79.5%）为零
- 三线尖锐分离：**生产 0.393 ≫ 治理 0.333 ≫ 分布 0.062**
- 四个组件在全部八份披露中缺席：类型空间（C1）、覆盖监测器（C2）、覆盖仪表盘（C4）、出处分层（C10）
- 矩阵中唯一的 3 级格：MiMo-V2.6 的伪失败甄别（C8）
- 离方法论最近的管线：DeepSeek-V4.1-Flash（7 分，均值 0.500）

## 仓库内容

| 路径 | 内容 |
|---|---|
| `paper_zh.pdf` / `paper.pdf` | 中英文稿件（含 LaTeX 源码） |
| `analysis/matrix_cells.csv` | 完整 8×14 审计矩阵：112 格，含级别、置信度、边界规则、逐字引文、定位符、来源文档与访问日期（2026-10-16）；89 个零分格保留检索痕迹 |
| `analysis/quotes.json` | 全部非零格的英文逐字引文、定位符与保真度分级 |
| `analysis/coding_data.py` | 冻结的 0–3 量表、边界规则（R1a/R2a/R3a）、逐组件检索词表、试标校准格 |
| `analysis/number_citations.py` | 参考文献重编号工具 |
| `figures/` | 图 1（四层数据栈架构）与图 2（就绪度热图），300 dpi |
| `04_manuscript_zh.md` / `04_manuscript.md` | 中英文 Markdown 版稿件 |

## 十四个组件

**分布 = 类型化的全谱覆盖（C1–C4）**：类型空间 · 覆盖监测器 · 覆盖驱动采集 · 覆盖仪表盘。
**生产 = 永续采集（C5–C11）**：生产遥测 · 组织化失败提交 · 三段式失败记录 · 伪失败甄别 · 域条件化混合 · 出处分层 · 三层吸收。
**治理 = 多元聚合（C12–C14）**：聚合机制 · 验证器制度化 · 同意与可行集。

每个组件给出操作性定义、协议规范、失败模式，以及与规范明确分开的既有实例化小结。

## 审计的可复现性

编码由单一编码者依冻结编码手册完成，限度在论文第 6 节如实陈述；20% 分层样本（23 格）的盲评重编码定于 2026-10-30 执行，此后将在下一版本报告原始一致率与 Cohen's κ。全部编码断言可经 `matrix_cells.csv` 中的逐字引文回溯。

## 相关工作（同一研究纲领）

- **理论**：《拟合实践，而非作品：AGI 人本拟合论》（[10.5281/zenodo.23391808](https://doi.org/10.5281/zenodo.23391808)，[GitHub](https://github.com/yuyuguilab/practice-fitting-theory)）
- **失败数据审计**：《成功给方向，失败给精度》（[10.5281/zenodo.23355929](https://doi.org/10.5281/zenodo.23355929)，[GitHub](https://github.com/yuyuguilab/failure-data-audit)）

## 许可

`analysis/` 中的代码采用 MIT 许可（见 [LICENSE](LICENSE)）；稿件、图表与编码数据采用 CC BY 4.0。
