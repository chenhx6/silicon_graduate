---
type: source
title: "Li 2016 - Algebraic collective model and core-quasiparticle coupling"
aliases: ["Li 2016 CQPC", "Weichuan Li doctoral thesis 2016"]
created: 2026-11-19
updated: 2026-11-19
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis-theory-and-software
reading_depth: read
title_original: Algebraic Collective Model and Its Application to Core Quasiparticle Coupling
authors: ["Weichuan Li"]
year: 2016
institution: University of Notre Dame
doi: 10.7274/6682x348f37
url: https://doi.org/10.7274/6682x348f37
canonical_source: "Li, PhD dissertation, University of Notre Dame, title page October 2016"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/LiWeichuan102016D.pdf
raw_sha256: 93ec952858b08181114498a1202ade3b7530fcbdf338fdd617d48ab26325beb4
raw_storage_status: archived-local
archive_required: true
nuclei: ["135Pr", "134Ce", "109Pd", "110Pd", "103Rh", "111Ru"]
tags: [ACM, CQPC, triaxiality, gamma-softness, wobbling, thesis]
---

# Li 2016：软核、刚核与准粒子耦合的比较

## Bibliographic Record

博士论文，导师 Stefan Frauendorf、Mark A. Caprio，题名页日期 October 2016
（PDF2）。CurateND 自身封面提供上述 DOI、Version 1 和数码日期
`03-10-2016`（PDF1）；不据数码格式推定另一学位授予日。
封面称 Public Domain Mark，版权页却称 All Rights Reserved（PDF3）：
保留权利说明冲突，未公开原件或整段摘录。

## Scope and Reading Depth

- **Covered scope**：五个 Gemini 主读单元已返回 PDF1–111，涵盖正文七章、
  附录 A 参数、B 图谱、C 输入输出及参考文献。管理层按关键原页核验，
  并非双方重读全文。最后单元的书目 locator 错误已定向订正；未采纳
  核素误写、无依据的程序实现保证、附录转移量身份等越界内容。
- **Not covered**：未取得并运行作者 ACM/CQPC 实际代码，未重建外部
  SO(5) 系数程序，未复现收敛测试；未重新核读所有引用实验原件，
  未重新拟合能谱、寿命或混合比，未运行 PDM。
- 记为 `read` 而非 `deep-read`：已完整覆盖主线并核关键原页，
  但上述形式和实现边界仍在；输入页全部发送本身不等于科学验收。

## Summary

本文用QTR/QTD比较奇核对核芯模型的敏感性，提出准粒子增强刚性的解释，
并介绍ACM的Python实现。电磁强度比能谱提供额外约束，但比较受参数设定、
实验输入依赖和原件内部公式/标签冲突限制，未构成独立实验或代码复现。

## Scientific Question and Model Design

问题不是重新测量偏振或提取混合比，而是：相邻偶偶核的软集体核芯输入，
能否直接用于奇质量核？若不能，哪些观测区分核芯模型与耦合机制？

- **QTD**：用 ACM 求解含转动与四极振动自由度的 Bohr 核芯，再耦合准粒子。
- **QTR**：用三轴转子核芯耦合准粒子；部分计算允许惯量随自旋变化，
  不能把名称中的 rigid 理解为所有自由度均严格不变。
- **比较对象**：第3章 Pd/Rh/Ru 链、第4章 135Pr、第5章 109Pd 低自旋态；
  第6章介绍 Python ACM 实现，第7章总结。

来源：PDF11–13、26–28、33–34、51、60、69–70、86–87。

## Hamiltonian and Observable Chain

### 核芯输入与 CQPC

PDF26–27，Eqs.2.18–2.23：奇核态在相邻 A−1 核芯的粒子分量与
A+1 核芯的空穴分量空间求解。总矩阵为准粒子块与核芯块之和：

\[
H=H_{qp}+H_c,\qquad
H_{qp}=\begin{pmatrix}
\varepsilon-\lambda+\tau&\Delta\\
\Delta&-(\varepsilon-\lambda+\tau)
\end{pmatrix},\qquad
H_c=\begin{pmatrix}E_c&0\\0&E_c\end{pmatrix}.
\]

四极耦合含核芯与单粒子约化矩阵元及角动量重耦合系数。
这里的配对能隙大写 Δ 不是电磁多极混合比 δ。
第2章概述给 Δ=1.226 MeV（PDF28），但 Table4.1 为0.7 MeV、
Tables5.2/5.3 为1.2 MeV；不能推广为全篇固定1.226 MeV。

### 哪些量真正有区分力

第3章明确说仅靠带能量和转动频率不足以区分两种计算（PDF38）。
所展示的 QTR/QTD 的 E2 强度可相近，而 M1 强度可明显不同。
作者用横向磁矩解释这种敏感性（PDF39–41，Eqs.3.3–3.6）：

\[
\boldsymbol\mu=g_j\boldsymbol j+g_R\boldsymbol R,
\quad R_\perp=-j_\perp,
\quad\mu_\perp=(g_j-g_R)j_\perp=(g_R-g_j)R_\perp.
\]

这是该模型中的机制说明，不是普适的强度大小定理。
PDF44 明确给反向例外：γ≈30° 时 QTR 的 B(M1) 可以小于 QTD；
调整 γ 拟合摆动能后才明显增大。该章电磁比较主要是模型预测，
作者要求进一步测量 B(M1)；不能因此写成整篇没有实验跃迁强度。

## Key Results

| ID | claim_kind | 原文支持的主张 | evidence_level | locator / boundary |
| --- | --- | --- | --- | --- |
| LI16-1 | model-design | QTR 的核芯输入可按奇核能谱调整，QTD 的集体势按偶偶邻核谱拟合；比较并非自动同自由度、同标定问题 | direct | PDF34、60–62；未进行共同参数重拟合 |
| LI16-2 | model-result | 第3章所计算的 QTD 摆动能随自旋上升；QTR 可有先降后升，两者差异依赖耦合及形变参数 | direct | PDF41、44；不是全体软核的无条件定理 |
| LI16-3 | author-interpretation | 准粒子使核芯更刚是作者解释计算优劣的图像 | direct | PDF59、68、86；不是直接测量奇核的势能刚度 |
| LI16-4 | source-dependence | 135Pr 章节承担合作实验的理论解释，不能算另一次独立偏振/δ测量 | direct | PDF51；实验身份见参考文献[9]，PDF107–108 |
| LI16-5 | model-limit | 135Pr QTR 的旋称伙伴带约高500 keV；作者说高自旋五准粒子结构变化超出其模型 | direct | PDF55；不能把整体能谱符合当作全部状态已解释 |
| LI16-6 | experimental-input | 109Pd 寿命、跃迁强度引用 Bucher 等，非本论文另做一次独立测量 | direct | PDF60、68、110，参考文献[39] |
| LI16-7 | model-result | Table5.6 的 QTD 给11/2−基态、5/2第一态15 keV，实验则5/2第一态0 keV | direct | PDF65–68；说明这一参数实现不符，不排除所有软核模型 |
| LI16-8 | evidence-limit | 能谱较好不保证全部电磁强度符合；两模型均有不符实测或上限的行 | direct | Tables5.4/5.5，PDF62–65；不把上限当中心值或显著性 |

### 109Pd：同时保留成功与失败

原表下标按同自旋态的顺序保留；以下不是重新评估数据。

| 量 / 跃迁 | 实验，按原表 | QTR | QTD | Locator |
| --- | --- | --- | --- | --- |
| B(E2)，(7/2)₁→(5/2)₁，e²b² | 0.65(56) | 0.840363 | 0.028 | PDF62，Table5.4 |
| B(E2)，(7/2)₂→(5/2)₁，e²b² | <0.014 | 0.007479 | 0.72 | PDF62，Table5.4 |
| B(E2)，(5/2)₃→(1/2)₁，e²b² | <0.0050 | 0.017745 | 0.3 | PDF62，Table5.4 |
| B(M1)，(5/2)₂→(5/2)₁，μN² | <0.00022 | 0.004 | 0.052 | PDF64，Table5.5 |

QTR 的 γ、单粒子能级、核芯2+能量及耦合参数在能谱拟合中相关
（PDF60）。Tables5.2/5.3 的核芯2+能量分别0.203869、0.374 MeV。
表中不同参数来源应保留；不能只凭“没有看到拟合某个量”宣称它是
经过预注册或独立盲测的验证集。

## ACM Implementation and Reproduction Boundary

第6章将径向 SU(1,1) 基与角向 SO(5) 基组合，分解四极坐标
\(q_m=\beta Q_m(\gamma,\Omega)\)（PDF70–71）。
径向算符矩阵、角矩阵及重耦合用于组装 Hamiltonian 与电磁算符。
角基的 Casimir 本征值为 ν(ν+3)（PDF75，Eq.6.22）。

软件分 angular_basis、radial_basis、operator、hamiltonian、
solve_hamiltonian 五个模块；正文指定用 SciPy 对角化
（PDF79–85，Tables6.1–6.5）。这说明作者的软件设计，不等于本轮实际安装或运行。

附录C输入例给 M=15、Vmax=50、lambda=6、a=1、Lmax=6、nmax=4，
势参数 beta0=2.1、chi=0.9、xi=10（PDF101–102）。
这些是一个示例，不是已经核实的全核区收敛标准。未来重建需检查基组测度、
算符归一、角系数、截断收敛和绝对单位；不承诺改正几个印刷式就可复现。

## Internal Discrepancies and Evidence Limits

- **几何与摆动能**：PDF28–29 对纵向几何的文字与 Fig.2.7（PDF31）不一致；
  图中 j 沿 m 轴，文字却写 perpendicular。Eq.2.25（PDF29）印作
  \(E(J,1)-[E(J,0)+E(J+1,0)]/2\)，不是自动可用的对称邻态实现。
  保留字面与图示差异，未认证作者实际代码。
- **惯量轴标签**：Table4.2（PDF53）原列为 J_l/J_m/J_s=7.4/5.6/1.8，
  c=0.116，惯量单位 ħ²/MeV；与背景 Fig.2.7/2.8 的 J_m>J_s>J_l
  不相容。不能暗换列名来符合通常排序。Eq.4.1 还需区分 Θ_i 与自旋相关 J_i。
- **跃迁身份**：Table4.3（PDF55）末两行初末自旋按字面差2，却同时列有 M1 比值。
  原行能量754.6、710.2 keV。未在本次核对中替换末态自旋或将这些行当无歧义输入。
- **模型名称与引用**：PDF56 在 QTD 小节写 QTR；PDF68 写 QTR 优于 QTR。
  第4章把 Matta 实验引用为[30]，而实际书目[30]为 Frauendorf–Dönau 理论、
  Matta 2015 在[9]（PDF107–109）。保留编号不一致，不虚构另一实验。
- **图例不是观测**：PDF94 的 Fig.B.6(a)画有113Pd实验第二序列，
  与PDF36仅列101/109/111Pd的文字范围有张力；同页111Pd面板也不能仅凭
  共用图例就认定每个标示系列都实际画出了数据。图上 band 标签不独立证明运动模式。
- **公式与软件不能混同**：PDF71的基组内积、PDF78的动能/Laplacian符号、
  PDF79的四极算符归一及PDF83的总 Hamiltonian 存在需对照的式间问题。
  未将它们直接编码，也不据此宣布作者实际计算错误。
- **附录输出身份**：C.2题为能量却列转移形式，C.3题为B(E2)却列能谱形式
  （PDF102–106）。未认证前一列表究竟为约化矩阵元还是归一B(E2)。
  PDF83指示例在Appendix B，但B实际为图谱、C为输入输出；不能将错引当脚本已取得。

## Competing Interpretations and Limitations

作者的“奇粒子刚化核芯”与“参数自由度、核芯迁移或模型截断影响比较”的解释
应区分：后者是待检验竞争假说，不是已经证实的拟合假象。
一个有区分力的后续比较是保持相同实验约束、明确拟合量与检验量、
对两套模型分别做参数敏感性检查，再联合看能谱、M1/E2及转移强度。
仅用同一能谱拟合优劣不能独立测出核芯的动态刚度。

## Extracted Pages

实际输入覆盖PDF1–111；关键原页核查含PDF26–32、38–41、44、51–56、
59–68、71、78–79、83、86–87、94–95、101–111。
页图与完整模型响应仅保留本地tmp；这份页码清单不表示逐一认证全部公式和表格单元。

## Knowledge Impact and Learning Decision

- **Supports**：[[wobbling-model-common-input-and-evidence-boundary]] 中
  “轴、惯量、对齐近似与观测量须共同对账”的方法要求。
- **Limits**：软偶偶邻核不能直接推出奇核一定软，也不能从某一QTD实现失败
  倒推奇核被直接证明严格刚性；B(M1)的相对大小同样依赖参数。
- **Persistence**：本来源页和共同输入方法页最小增量；不改既有135Pr争议的实验裁决。
  该论文复用既有合作实验，不新增独立实验票数。不组织尚未成熟的全馆藏综合。
- **Audit**：Codex self-audit，不是人工审核；运行进度与返工清单留在任务回执，
  科学使用仍回到上述原页和未解决的形式/实现边界。
