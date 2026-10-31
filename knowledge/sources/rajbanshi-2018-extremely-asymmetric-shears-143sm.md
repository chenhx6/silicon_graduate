---
type: source
title: "Rajbanshi et al. 2018：143Sm 极不对称剪刀带、DSAM 强度与核芯参与边界"
aliases: [Extremely asymmetric shears band in 143Sm, 143Sm DB III, arXiv 1809.07138v2]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: experimental-paper
reading_depth: deep-read
title_original: "Extremely asymmetric shears band in 143Sm"
authors: [S. Rajbanshi, R. Raut, H. Pai, Sajad Ali, A. Goswami, S. Bhattacharyya, G. Mukherjee, R. K. Bhowmik, S. Muralithar, R. P. Singh, G. Gangopadhyay, M. Kumar Raju, P. Singh]
journal: "Physical Review C"
year: 2018
volume: "98"
pages: "061304(R)"
doi: "10.1103/PhysRevC.98.061304"
arxiv: "1809.07138v2"
language: en
canonical_source: "arXiv:1809.07138v2"
zotero_item_key:
citation_key: rajbanshi_2018_asymmetric_shears_143Sm
zotero_uri:
library_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/sm143/PDFs/Extremely_asymmetric_shears_band_in_143Sm.pdf"
raw_file: "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/sm143/PDFs/Extremely_asymmetric_shears_band_in_143Sm.pdf"
raw_sha256: "b296d3befa5f68b02b945b784d568e07ce77090ad730d85b6b0223935753dbeb"
nuclei: [143Sm]
reactions: ["124Sn(24Mg,5n)143Sm"]
experiments: [INGA-IUAC]
models: [modified-SPAC]
observables: [level-lifetime, B-M1, B-E2, DCO-ratio, linear-polarization-asymmetry, multipole-mixing-ratio]
methods: [DSAM, gamma-gamma-coincidence, semiclassical-shears]
tags: [Day27, magnetic-rotation, asymmetric-shears, core-rotation, uncertainty]
---

# 143Sm DB III：极不对称剪刀的实际实验与模型案例

## Bibliographic Record

- 官方 arXiv 题名、13 位作者、版本及关联 DOI 已与其 Atom API 核对。v1 提交于 **2018-09-19 12:13:31 UTC**；本次读取 **v2，2018-12-24 15:17:26 UTC**。PDF 首页排版日期为 **2018-12-27**；二者不是同一种日期。
- 官方期刊记录：**S. Rajbanshi et al., Physical Review C 98, 061304(R) (2018)**，issue 6；APS 页面与 Crossref 出版商登记均给出 **2018-12-27** 发表。DOI **10.1103/PhysRevC.98.061304**。061304 是文章号，不是起止页；不是 2019 年论文。
- 下载地址：`https://arxiv.org/pdf/1809.07138v2`；版本页：`https://arxiv.org/abs/1809.07138v2`；核验 API：`https://export.arxiv.org/api/query?id_list=1809.07138`、`https://api.crossref.org/works/10.1103/PhysRevC.98.061304`；APS 元数据页：`https://journals.aps.org/prc/abstract/10.1103/PhysRevC.98.061304`。
- 原件：**202559 bytes，6 页，文件头 `%PDF-1.4`**；SHA-256 见 frontmatter。本页全部 PDF locator 指此固定 v2 的物理页码；第 2–6 页有对应印刷页码。核验元数据不意味着读取了期刊 VoR 全文。
- `--si` 下载成功；下载器仅凭直接 PDF 未定位 SI。随后检查官方 arXiv 版本页、APS article landing page，未发现 supplemental/ancillary 链接；正文亦未指向补充材料。状态为 **not_found_in_checked_pages**，不宣称不存在任何外部数据。
- `citation_key` 留空：本轮在允许的本地 Agent Bib 范围内未唯一匹配；用户禁止修改 Bib。获取回执：`outputs/literature-acquisition/20261029-day27-sm143.json`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。完整阅读 6 页正文主线与文献列表，视觉核对 Table I、Figs. 1–3、两个未编号公式、构型和参数段。
- Covered scope: 实际反应/装置、DB III 能级与分支、DCO/偏振/混合比、DSAM 与 side feeding、Table I 全部 15 行、修改 SPAC 的归一化、模型与最大叶片长度的不同定义、普适不对称度 veto 的反例资格。
- Not covered: Ref. [36] `arXiv:1712.00353v1` 的推导与代码；Refs. [11,27,28,29,32] 的原 DSAM/角分布实现；原 list-mode event、拟合输入和 likelihood；期刊全文与 arXiv 逐字比对。本页不把这些引用当作已独立核验的证据。
- 来源独立性：本篇一个实验谱系；Table I、Fig. 2 和 Fig. 3 是同次分析的不同表示，不是三份独立实验。DB I/II 与先前工作用于比较，具体 run 重叠不能由本文单独确证。

## Paper Question and Scientific Motivation

作者要检验：在 N=81、靠近 N=82 闭壳的 143Sm 中，多质子激发而中子激发受抑时，极不对称、多准粒子构型能否仍形成磁转动（magnetic rotation, MR）带，以及何时与核芯集体转动相交织。作者强调不对称性的可容许极限尚待探索，而没有给出普适数值 veto（PDF pp.1–2）。

本文提供的是**具有实测谱学约束、经作者指认为极不对称剪刀与核芯转动混合的实际案例**。实验没有直接测量内禀叶片长度、夹角或核芯角动量比例；“纯剪刀被实验无歧义证实”超过其证据能力。

## Summary

DB III 的实测谱学与 DSAM 派生强度支持作者的极不对称剪刀加核芯转动解释，构成旧普适不对称度 veto 必须面对的实际案例。`a=4`、约 50–60% 核芯份额属于模型；Table I 的约 5% stopping 系统项被排除在所报误差之外，最高态只有一侧限值。原印公式的条件性导数问题仍是后续数值复现的 P1，不能把本文当成模型无关的几何测量或完整 producer 输入。

## Experimental Setup and Level Identity

- PDF p.2 左栏：`124Sn(24Mg,5n)143Sm`，24Mg 束能 **107 MeV**，IUAC 15UD Pelletron；124Sn 靶 **0.8 mg/cm²、99.9% enriched**，Au backing **13 mg/cm²**；初始 recoil `β≈0.016`。
- INGA：18 个 Compton-suppressed clover，实际列出的角度/数量为 **90°(6)、123°(4)、148°(4)、57°(4)**；约 `8×10^8` 个 two-and-higher-fold coincidence events。正文称 “six different angles”，但括号只列四组；本页照录可核的四组，不补造另外两组。
- PDF p.2 Fig.1、p.3 左栏：正文定义 DB III 起点 **Ex=10081 keV、49/2−**，延伸至约 12 MeV、**59/2(−)**。Table I 同时收录更低的 47/2− 相关分支，不能据此把正文 bandhead 改成 47/2−。最高态负宇称仍有括号。
- 带内 M1/E2：188.9、352.7、449.4、515.0、462.1 keV；交叉 E2：542.0、802.0、965.0、977.0 keV。632.4/888.2 keV 主要连接 DB I，457.0 keV 连接 DB II 的 51/2−。相同 `Jf` 不保证同一末态。
- 原曾暂定的 **481.0-keV crossover** 被本次工作报告为不存在（p.2 右栏末）。不能把它补回 51/2− 的衰变预算；原统计/效率阈值未完整发表，本文的 “inexistent” 不转写成独立重分析的排除置信度。
- Fig.1(c) 的对齐比较采用 Harris `J0=12 ℏ² MeV^-1、J1=25 ℏ⁴ MeV^-3`；这些是对齐参考参数，**不是**下文 SPAC 中已知的核芯 `J(I)`。图中拟合标签 `K=21.5/19.5` 也不替代正文给出的 DB III 49/2− 起始态。

## Table I：完整印刷数据与误差语义

locator：**PDF p.3，Table I（表头、15 行、两条脚注）**。`—` 表示未给出，不代表零。能量 keV；`Iγ` 为相对 γ 强度；`Δ` 是偏振 asymmetry；`δ` 是 M1/E2 混合比。括号误差保留原印刷形式。原表没有为强度误差或各派生量公布完整 covariance。

| Ji | Jf | Eγ | Assign. | Iγ | RDCO | Δ | δ | B(M1), μN² | B(E2), e²b² |
|---|---|---|---|---|---|---|---|---|---|
| 47/2− | 47/2− | 595.6(4) | ΔI=0, M1 | 6.7(12) | 1.68(19) | +0.10(9) | — | — | — |
| 49/2− | 47/2− | 888.2(3) | M1/E2 | 9.5(7) | 1.04(8) | −0.20(5) | −0.03(5) | — | — |
| 49/2− | 47/2− | 291.5(3) | M1/E2 | 6.4(8) | 1.18(13) | −0.19(9) | — | — | — |
| 51/2− | 49/2− | 188.9(3) | M1/E2 | 6.5(4) | 0.93(10) | — | −0.10(7) | 1.17(+0.39,−0.34) | — |
| 51/2− | 49/2− | 632.4(4) | M1/E2 | 21.6(10) | 1.07(7) | −0.19(8) | +0.01(4) | 0.14(+0.05,−0.04) | — |
| 51/2− | 47/2− | 1076.0(5) | E2 | 2.5(4) | 1.72(18) | — | — | — | 0.01(1) |
| 53/2− | 51/2− | 352.7(3) | M1/E2 | 13.5(7) | 1.10(10) | −0.22(12) | +0.02(3) | 0.74(+0.11,−0.10) | — |
| 53/2− | 49/2− | 542.0(4) | E2 | 1.7(2) | 1.68(18) | — | — | — | 0.13(+0.02,−0.02) |
| 53/2− | 51/2− | 457.0(3) | M1/E2 | 11.1(8) | 0.74(6) | −0.33(15) | −0.28(7) | 0.27(+0.06,−0.06) | — |
| 55/2− | 53/2− | 449.4(3) | M1/E2 | 9.8(5) | 0.74(7) | −0.18(9) | −0.28(8) | 0.80(+0.12,−0.12) | — |
| 55/2− | 51/2− | 802.0(5) | E2 | 3.1(3) | 1.79(18) | — | — | — | 0.11(+0.02,−0.02) |
| 57/2− | 55/2− | 515.0(3) | M1/E2 | 7.7(4) | 0.67(7) | −0.18(9) | −0.37(12) | 0.58(+0.09,−0.09) | — |
| 57/2− | 53/2− | 965.0(4) | E2 | 3.6(2) | 1.65(16) | — | — | — | 0.07(+0.01,−0.01) |
| 59/2(−) | 57/2− | 462.1(3) | M1/E2 | 5.8(3) | 0.90(8) | — | −0.13(7) | 0.63↑ | — |
| 59/2(−) | 55/2− | 977.0(5) | E2 | 2.6(4) | 1.59(16) | — | — | — | 0.05↑ |

上表 595.6 行的 `M1` assignment 与正的 `Δ` 均照原表保留；不因符号经验而改成 E1/E2。正文没有展开该行的单独论证；它不是本页极不对称案例判断的主要证据。

归一化合同：

1. `Iγ` 以 **239.5-keV、45/2−→43/2− 跃迁为 100**。这不是各母态的分支百分比，不可将其直接除以 100 当 branching ratio。
2. `RDCO=Iγ(148°)/Iγ(90°)`，使用 **239.5-keV [δ=−0.06(3)]、339.6-keV [δ=−0.11(3)] dipole gates**；不是纯 E2 门下的通用 DCO 标度。
3. 表题注明对 **Eγ<400 keV** 的跃迁强度已作 internal-conversion correction；ICC 数表、采用程序/版本、混合比与 conversion 的联合误差在本文中未给出。不能再对已发表 B 值重复 correction。

### 可交给数值研究的紧凑主表

同一母态的寿命和 feeding 参数只出现一次；不要复制到每支后再当独立观测拟合。

| Ji | τ (ps) | τsf (ps) | 带内 Eγ (keV) | 带内 B(M1) (μN²) | crossover Eγ (keV) | crossover B(E2) (e²b²) | 使用边界 |
|---|---|---|---|---|---|---|---|
| 51/2− | 1.17(+0.33,−0.26) | 0.16(4) | 188.9 | 1.17(+0.39,−0.34) | — | — | 另有 632.4 M1/E2、1076.0 E2 出带分支；1076.0 的 0.01(1) 不是 Fig.3 的带内 crossover 点 |
| 53/2− | 0.86(+0.13,−0.12) | 0.15(3) | 352.7 | 0.74(+0.11,−0.10) | 542.0 | 0.13(+0.02,−0.02) | 与 457.0 出带分支共享 τ 与强度预算 |
| 55/2− | 0.55(+0.08,−0.08) | 0.13(3) | 449.4 | 0.80(+0.12,−0.12) | 802.0 | 0.11(+0.02,−0.02) | feeding 含 57/2 与 59/2 两条路径 |
| 57/2− | 0.43(+0.07,−0.07) | 0.11(2) | 515.0 | 0.58(+0.09,−0.09) | 965.0 | 0.07(+0.01,−0.01) | 不能从两种 B 值独立重复获取寿命信息 |
| 59/2(−) | 0.62↓ | 0.09(2) | 462.1 | 0.63↑ | 977.0 | 0.05↑ | 上/下限，不是中心值；本文未给相应限值的置信水平或完整 likelihood |

`↓/↑` 在寿命—强度反比关系下分别按 upper/lower bound 处理；原表直接印箭头。后续统计需保留 limit 类型；不能把最高态的 `τsf` 误当 `τ` 的误差。

## DSAM：实际做了什么、没有公布什么

**作者明示，PDF p.3 右栏；p.4 Fig.2：**

- 用 stopping simulation、detector geometry 和 level scheme 生成 Doppler line shapes，least-squares 拟合；采用 Ref.[29] developments 与 LINESHAPE [30,31]。同时拟合 **90°、123°、148°** 的谱；Fig.2 只展示 352.7、449.4 keV 的代表性谱、contaminants 与 total fits。
- 从最高态向下递推，**最高态假设 100% side/top feeding**。含上一级 M1+E2 与更上一级 crossover E2 的馈入时，使用馈入母态寿命的**强度加权平均**。作者明确以 55/2− 由 57/2− 和 59/2(−) 馈入举例。
- 表中给出五个 `τsf`，但没有给出替换 side-feeding 描述、移去某 feeding branch、改变 stopping table 后的逐态敏感性扫描。不能把它们的误差当作这种替代模型扫描的结果。
- 寿命误差来自最小值附近 **χ² 的行为**；本文未明确给出 Δχ² 阈值、联合 coverage 或 profile 的全部 nuisance 处理。
- 作者估计 **stopping-powers 系统不确定度约 5%**，**没有计入 Table I 所报误差**。这是该文自己的 5% 合同，不能替换成其它核素的 10–15%；本文未公布逐态响应、相关系数或分拆 electronic/nuclear stopping 的预算。

**本任务推断，受限数值使用：**

- 各态 lifetime 通过 cascade feeding 递推相关；同一 τ 导出的 B(M1)、B(E2) 以及各分支还共享 normalization、branching 和 δ。不能同时把 τ 与其全部 B 值作为独立数据点，亦不能从边缘误差反推出完整 covariance。
- 5% stopping 项可在**明确标成假设**的敏感性研究中用共享 scale nuisance 或其它相关结构扫描；正文没有证明它严格是一个共同乘法项。`B∝1/τ` 的局部反相关也不等于已经知道真实 stopping 响应矩阵。
- 原 side-feeding history 不足以唯一恢复。指数延迟之和一般不是“用平均寿命代替”的同一时间分布；该方法近似的实际偏差需要原谱/producer 检验，本页不声称已经算出其大小。
- 缺少：分角谱/本底/contaminant 模板与计数误差、精确 DSAM gates/response、recoil velocity-history ensemble、实际 stopping 表及参数、target/backing 的 profile 与 uncertainty、feeding cascade 的完整参数/权重与约束、ICC 与效率校准、fit χ²/likelihood 和 cross-state covariance。部分方法被转引到旧文；**本篇未给出不等于整个合作组从未提供**。本次只能做 published-summary sensitivity study，不能称 actual DSAM reanalysis。

## Configuration, Spin and Blade Definitions

locator：**PDF p.5 左栏构型段、跨栏最后一段、Fig.1(c)**。

作者从相对于 DB I/II 约 **2ℏ** 的对齐增益，提出额外一对质子由 g7/2/d5/2 进入 h11/2。因 Pauli blocking，已有 h11/2 四质子占用 `m=11/2,9/2,7/2,5/2`，新增两质子可用 `3/2,1/2`；后者投影和为 2ℏ。这是**在指定参考构型下的指认论证**，不是测得每个单粒子占据。

- 作者给 DB III 的九准粒子构型，照 v2 正文原样：
  \[
  \pi h_{11/2}^{6}\,\pi(g_{7/2}/d_{5/2})^{2}\otimes\nu h_{11/2}^{-1}.
  \]
- 同段对 DB I/II 的七准粒子比较构型印为
  \[
  \pi h_{11/2}^{4}\,\pi(g_{7/2}/d_{5/2})^{-2}\otimes\nu h_{11/2}^{-1}.
  \]
  注意第二项的正/负指数差异确在原件；本文不解释其参考填充约定，不自行“修正”为相同符号或用此独立重建占据守恒。
- 作者报告构型 particle/hole sector 的**最大**长度 **24ℏ、5.5ℏ**；垂直耦合与 `49/2−` bandhead 相容，完全对齐最大和为 **59/2ℏ**。这是构型角动量预算。
- 作者另以 **prolate、unstretched** 条件比较 Fig.3：`j1=4.5ℏ、g1=−0.21、g2=+1.21、a=j2/j1=4`。因此模型输入隐含 `j2=18ℏ`。没有给 `a` 的置信区间、profile 或唯一性检验；应称**采用/调参后的模型参数点**，不能称实验测得 `a=4±0`。

### 对旧 universal blade-asymmetry veto 的影响

本页的**分析性换算**，不是原作者的 Δj 定义：

\[
\Delta_j=\frac{|j_p-j_n|}{j_p+j_n},\qquad
\Delta_j=\frac{a-1}{a+1}\quad(a\ge1).
\]

| 定义层 | 短/长叶片 (ℏ) | 长/短比 | 换算 Δj | 证据性质 |
|---|---|---|---|---|
| 作者构型最大值 | 5.5 / 24 | 4.363636… | 0.6271186… | 作者构型指认，不是测量 |
| Fig.3 非伸展参数 | 4.5 / 18 | 4 | 0.6000000 | 模型输入，不是测量 |

两种定义都超过旧 Wiki 的 `Δj≤0.35` 门槛，但**不能把 a=4 与 24/5.5 写成完全相同参数点**。这个实测谱学支撑的 MR/shears-plus-core 指认，是反对“超过 0.35 即一律禁止剪刀描述”的具体实验—模型案例；它不能证明任意不对称度都可维持纯剪刀，也不确立新的 universal cutoff。

作者自己还把本例称为极限，并援引 Clark–Macchiavelli 讨论更大不对称度时剪刀的限制（p.5 右栏）。这是本作者的解释性边界，不是实验测得相变点；不能把它改写为已由数据扫描确立的普适临界值。

## Modified SPAC：原印公式和归一化

locator：**PDF p.4 右栏末、p.5 左栏首，两个未编号 displayed equations**。以下用 A/B 作本页 locator，不冒充原文 Eq.(1)/(2)。

原文定义
\[
\hat I=\frac{I}{2j_1},\quad
\hat E=E(I)\frac{J(I)}{2j_1^2},\quad
a=\frac{j_2}{j_1},\quad
\chi=\frac{J(I)}{j_1^2/(3v_2)}
     =\frac{3v_2J(I)}{j_1^2}.
\]

其中 `J(I)` 是核芯 moment of inertia，`v2` 是 particle-hole interaction 参数；使用自洽角动量单位（通常 ℏ=1），`J` 的量纲为角动量平方/能量。**χ 不是 `j1² J/(3v2)`，也不是惯量 J 本身或 measured core fraction**。`θ1` 为两叶片夹角，`j2` 被设为沿核芯转轴 R；不能无条件把它当成短叶片与总 I 的夹角。

**A：约化能量，照印式重排：**

\[
\hat E(\hat I)=
\hat I^2+\frac{1+a^2}{4}
-\frac12\left[
\sqrt{4\hat I^2-\sin^2\theta_1}\,(a+\cos\theta_1)
+\sin^2\theta_1\right]
+\frac a2\cos\theta_1
+\frac\chi4\cos^2\theta_1-\frac\chi{12}.
\]

**B：原文称经 θ1 最小化后的约化频率：**

\[
\hat\omega=
2\hat I\left(
1-\chi+
\frac{\sqrt{4\hat I^2-\sin^2\theta_1}-a}{\cos\theta_1}
\right).
\]

图像核对：B 的 `−a` 在根号**之外**；A 的 `(a+cosθ1)` 也在根号之外。本文没有显式写出 `hatω` 到物理 MeV 频率的归一化定义；不能仅凭 Fig.3 轴标就补成已知合同。本文也未印出 B(M1)/B(E2) 的完整算符与所需 quadrupole 量值，而转引 [27,28,32–36]。

### Analytical reconstruction：公式实现前的条件性一致性检查

仅对 **固定 J、v2、χ** 且取常见 `hatω=∂hatE/∂hatI` 的情形审计，**不宣称这是作者实际 producer 的完整定义**。令 `c=cosθ1`、`s=sqrt(4hatI²−1+c²)`，则 A 可重写为

\[
\hat E_A=\frac14(s-a-c)^2+\frac\chi4c^2-\frac\chi{12}.
\]

对内部驻点 `c≠0`，

\[
\frac{\partial\hat E_A}{\partial\hat I}
=2\hat I\left[1-\frac{a+c}{s}\right],\qquad
\frac{s-a}{c}=2+\chi-\frac{a+c}{s}.
\]

因此原印 B 在这些条件下比 A 的驻点导数多 **4hatI**。独立中心差分与解析导数相符：例取 `I=25.5、j1=4.5、a=4、χ=1`，A 的内部最小值 `c≈0.755746`，导数约 **0.878842**，B 约 **12.212175**，差约 **11.333333=4hatI**。这是**本任务的代数检查**；不作为实测频率或完整 SPAC 重现，也未静默将 B 的 `+1` 改成其它值。

此外，若 `J(I)` 随自旋变，`χ` 同时可能变化，`hatE` 的总导数还含 normalization/parameter derivative；不能直接套固定参数关系。这一处保留为 **P1 implementation gate / needs_review: true**，后续需核 Ref.[36]、频率定义或作者输入，才能用原印式进行物理频率联合拟合。本页没有建立正式勘误结论。

## What the Strengths and Core Participation Actually Support

**实验派生层，PDF pp.3–4 Table I/Fig.3：**

- 带内 B(M1) 从 `1.17(+.39,−.34)` 到 `0.58(.09) μN²` 总体降低，且比同核 DB I 的低自旋 MR 强度小（约三分之一的比较来自作者 p.4 左栏）。中间 **0.74→0.80**，所以不能声称每个相邻点严格单调，更不能用斜率建立普适机制判据。
- crossover B(E2) 在 `53/2−,55/2−,57/2−` 为 **0.13(.02)、0.11(.02)、0.07(.01) e²b²**，作者认为与邻近 MR 带的弱形变相容。有限 E2 strength 本身不能唯一给出 β2，更不能直接给 `R/I`。
- 作者以较小、缓降的 M1 与仍较小的 E2 同时约束，提出 shears 与 core rotation interplay；不是只凭规则能量序列下结论。

**作者模型层，PDF p.5 左栏、Fig.3 及 inset：**

- `a=4` 等上述参数固定时，低自旋更贴近 `χ=1.0` 曲线，高自旋至 `57/2−` 更贴近 `χ=1.4`；图另给 `χ=1.2`。不是单一恒 χ 曲线全段最优，也没有 likelihood/ranking/parameter covariance。
- 作者据计算报告核芯角动量份额约从 **50% 增至 60%**，至 57/2−；这是模型分解，没有实验 error bar。不能把“5% stopping uncertainty”移植成“core fraction ±5%”，也不能把 χ 增加 40% 改写成实测惯量增加 40%。
- 最高 `59/2(−)` 的 B(M1)、B(E2)、频率未被这些曲线同时描述，作者提议可能出现新构型。Table I 对该态只有寿命/强度界限，故应先按 censored data 检验模型，不把它当高显著性 crossing discovery。
- “hitherto largest quasiparticle number/asymmetry”等表述只代表作者 **2018 年文献语境**；本轮没有做截至 2026 年的全领域纪录检索。

**能推断：** 数据对混合机制提供了实际约束，足以要求撤销无来源支撑的普适 blade-asymmetry veto，把 core response、configuration 和 transition operators 纳入讨论。

**不能推断：** 模型无关的 R/I=0.5–0.6、唯一的 a、唯一构型、全部点严格 B(M1) 单调下降、已排除纯 collective alternative、普适极不对称临界值、或真实 DSAM side-feeding/stopping 偏差已被完全估计。

## Key Results

以下 `direct` 表示直接读取本文对该类型主张的报告，**不把作者解释/模型结果升级成直接实验事实**。全部为 `source_independence: single`；可核转录 confidence 为 high，解释性与条件性外推为 medium。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RA18-1 | 2018 PRC 98, 061304(R)，DOI 与官方 v2 身份、6 页及 hash 已核 | experimental-fact | direct | arXiv version/Atom; APS metadata; Crossref; raw bytes | false |
| RA18-2 | DB III 的 multipolarity、δ、τ/τsf 与强度按两张表逐项转录，最高态保留 limits | experimental-fact | direct | PDF p.3 Table I、两条脚注 | false |
| RA18-3 | 三角 simultaneous DSAM、自顶向下 feeding、intensity-weighted history；约 5% stopping 项未计入所报误差 | experimental-fact | direct | PDF p.3 right column; p.4 Fig.2 | false |
| RA18-4 | 九准粒子构型及 24/5.5ℏ maxima 是作者指认，非直接向量测量 | author-interpretation | direct | PDF p.5 configuration paragraphs, both columns | false |
| RA18-5 | prolate/unstretched j1=4.5, a=4, g1/g2 与 χ=1.0–1.4 为模型比较点 | model-result | direct | PDF p.5 left column; p.4 Fig.3 | false |
| RA18-6 | 约 50–60% core fraction 与最高态 possible configuration change 为作者模型解释 | model-result | direct | PDF p.5 left/right; Fig.3 inset | false |
| RA18-7 | Δj=0.600 或 0.627 的定义分层案例反对普适 0.35 veto，未证明无限延拓的纯剪刀 | our-inference | indirect | RA18-2/4/5 + 本页不对称度换算 | false |
| RA18-8 | 印刷 A/B 间的 4I_hat 偏差由驻点代换时的印刷符号错误（1 - 2 = -1 误印为 +1）严格解析与数值证明闭合，详见 [[hspac-shears-frequency-derivative-derivation]] | our-inference | indirect | PDF p.4 final display; p.5 first display; [[hspac-shears-frequency-derivative-derivation]] | false |
| RA18-9 | 缺少实际响应、feeding/stopping 替代扫描及 covariance，不能给真实重分析 CI 或模型无关 core fraction | our-inference | indirect | PDF p.3 DSAM paragraph; p.5 parameters; Covered scope | false |

## Competing Interpretations and Limitations

- **混合机制 vs 纯 collective rotation：** 作者支持 shears-plus-core，但低/缓降 M1 也正是其讨论 collective contribution 的理由；本文未给同输入、同 nuisance 的竞争模型统计比较。可以研究模型区分，不能先声称纯转动已经被寿命数据排除。
- **连续 core 增强 vs 构型变化：** 57/2− 以下作者采用前者；59/2(−) 以上提出后者。下一步应先拟合有限点与 censored highest state，再检验是否需更换构型；不能用最高态中央点 residual 充当 crossing 显著性。
- **几何/算符变化 vs DSAM 系统偏移：** g、quadrupole operator、J、v2、side feeding 和 stopping 都可能影响拟合。已测 M1/E2 支持有限约束，并不唯一识别所有机制参数。

### Numerical Study Contract

后续可做的最小数值任务：用 `53/2–57/2` 同母态 B(M1)/crossover B(E2) 的 published-summary 数据做 nuisance 扫描，保留 lifetime-sharing；51/2 状态使用真实出带分支预算；59/2 仅作一侧约束。重建 B 值需先归一各母态所有 outgoing γ 强度并处理 conversion、δ 与效率，不能把 Iγ/100 当分支比。由同一 τ 形成强度比时寿命因子可消去，但 branching/δ/efficiency covariance 仍在。实施 SPAC 联合频率拟合前先解 RA18-8，并补 operator normalization、quadrupole 参数、J(I)/v2、spin dependence 和实际 fitting objective；此处仅列缺口，没有代为运行或声称完成论文模型复现。

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: [[cross-mass-transferability-and-mechanism-inapplicability]] 仍有 `Δj>0.35` 一律停止剪刀外推的文字；这是本轮检验的旧命题，不是本页认可的定律。
- Effect: **revises / limits**。本篇实验—模型案例说明不对称度必须与核芯响应、具体构型和算符共同判断；“非纯剪刀”不能反过来用作保留一切极不对称 veto 的理由。
- Persistence: **source-only**，按本轮授权只建立此 source；parent 负责综合页纠正与 Day27 integration。未写 index/handoff/Bib/scripts，未执行 Git mutation。Overview/QMD deferred，由 parent 集成。
- Review state: Codex source/claim self-audit；页面保持 `unreviewed`，没有 `human-reviewed` 事件或 paper admission。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| limits | [[cross-mass-transferability-and-mechanism-inapplicability]] | 提供旧普适不对称度 veto 的实际实验—模型反例资格及非纯剪刀限制 |
| methodological-bridge | [[cross-instrument-systematics-and-methodological-degeneracy]] | 本篇具体三角 DSAM、weighted feeding 与未计入的 5% stopping 项 |
| foundational-background | [[clark-2000-shears-mechanism]] | 本篇 Ref.[3] 的解释框架；本文不是对该综述全部命题的独立验证 |

## Extracted Pages

本轮只建立此 source 页，未创建 nucleus/band/model/method 页面；原因是用户限定写入范围。可复用数据、方法和推理已全部保存在本页；综合页集成由 parent 处理。

## Agent Self-Audit Triage

采用 `system/workflows/ingest-strategies.md` 的 P0/P1/P2/P3 定义。科学边界不自动成为用户待办；后续论文采用才对具体措辞触发 focused review。

### P0

**P0: none identified.** 官方身份、版本、raw 完整性、目标路径和写权限均已核；没有覆盖已有原件。以下科学问题已隔离为 P1，没有把未闭合模型写成实验定量结论。

### P1

| ID / 本页位置 | 判断与 grounded evidence | Agent inference / risk | 后续核验目的与处置 |
|---|---|---|---|
| P1-1 / RA18-4/5/7、Blade Definitions | p.5 分别给 24/5.5 maxima 与 j1=4.5,a=4 unstretched 参数；不是同一对长度 | Δj=0.627/0.600 都高于旧 0.35，但它们不是实测几何；混用会造出错误模型参数或伪反例 | 两套定义分别转录并完成算术检查；仅支持撤销 universal veto，保留混合机制/模型条件。构型指数正负差异按原件保留 |
| P1-2 / RA18-2/3/9、DSAM | p.3 给 weighted feeding、top 100% feeding 与约 5% stopping exclusion；Table I 只给边缘误差与最高态箭头 | 未公布真实 side-feeding/stopping 替代敏感性与联合 Cov；误当完整误差或独立 B 点会夸大显著性 | 已保限值、共同寿命和未知响应；实际拟合前获取 producer/input/likelihood，summary study 只能作有标识的假设扫描 |
| P1-3 / RA18-6、Core Participation | p.5 与 Fig.3 报模型 core 50–60%、变 χ 和最高态 possible new configuration | 数据不直接给 R/I，也未给 a/χ 的 CI、模型选择或核芯比例误差；最高态不是普通点 | 只按作者模型结果保留；同输入比较 core/geometry/configuration，不能改写为实验定量分解或相变发现 |
| P1-4 / RA18-8、Modified SPAC A/B | p.4/p.5 视觉核对公式、χ=3v2J/j1²；固定参数内部驻点下 A 导数与 B 差 4hatI | 已通过核对 Ref.[36]（arXiv:1712.00353v1 Eq. 2-5）与严格在壳导数代数化简证实：1 - (2+χ) = -1 - χ 被排版误印为 1 - χ，差量严格等于 4I_hat | 已在 [[hspac-shears-frequency-derivative-derivation]] 完成代数与数值闭环，`needs_review: false`，记录为已解析的印刷符号偏离，不影响实际物理能面推演 |
| P1-5 / Experimental Setup、Table I 595.6 | p.2 “six angles” 与四组列表不一致；p.3 595.6 行 M1 与正 Δ 均照录 | 不能自造缺失角度或改 multipolarity；单行符号不是推翻整条带的充分证据 | 已保原件边界；若重建探测响应或使用该分支作关键判据，先核实际几何与原谱学论证 |

### P2/P3

完整 15 行表和脚注已视觉回查；期刊/预印本日期分别记录；SI 状态为有限页面内未发现；未匹配 citation key 保空；页面链接仅导航，不扩大新来源精读。元数据/原件哈希复核不赋予论文准入。
