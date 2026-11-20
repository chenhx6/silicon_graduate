---
type: source
title: "Hayes 2005 博士论文：178Hf 中 K 守恒的破缺"
aliases: [Hayes 2005 178Hf thesis, Violations of K-Conservation in 178Hf]
created: 2026-09-05
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment-and-model
reading_depth: deep-read
title_original: "Violations of K-Conservation in 178Hf"
authors: [Adam B. Hayes]
advisor: [Douglas Cline]
journal: "University of Rochester doctoral dissertation"
year: 2005
volume:
pages: 293
doi:
arxiv:
language: en
canonical_source: "Hayes, Adam B. Violations of K-Conservation in 178Hf[D]. University of Rochester, 2005."
zotero_item_key:
citation_key: "hayes_2005_178hf-violations-conservation"
zotero_uri:
library_file: "raw/theses/degree-dissertation/violations of K-Conservation in 178Hf.pdf"
raw_file: "raw/theses/degree-dissertation/violations of K-Conservation in 178Hf.pdf"
raw_sha256: "4982B80A3E830CFE034E51428D2467C7D94852607D8DBB773E1B66A820EBDDC0"
archive_required: true
nuclei: [178hf]
reactions: ["178Hf(136Xe,136Xe')178Hf Coulomb excitation", "178Hf beam activation on Ta"]
experiments: []
models: [spin-dependent-mixing-model, alaga-rule, projected-shell-model]
observables: [coulomb-excitation-yield, electromagnetic-matrix-element, k-mixing, hindrance-factor]
methods: [gamma-gamma-coincidence, coulomb-excitation, doppler-correction, particle-identification]
tags: [a180, high-k, k-mixing, coulomb-excitation, rotational-alignment, isomer, phd-thesis]
---

# Hayes 2005：`178Hf` 中 K 守恒的破缺

## 2026-11-07 定向原读：K混合来自跃迁两端

本次核对293页原件和哈希。该PDF的字体映射使常规文本提取产生乱码，
本次以原页渲染并OCR复核题名、Abstract（PDF pp.6–7）和完整Ch.12结论
（PDF pp.279–281＝印刷pp.246–248）；不以乱码文本或OCR成功冒称新完成293页精读。

| ID | 来源陈述 | claim_kind | locator | 解释边界 |
|---|---|---|---|---|
| HB05-R7-1 | 两次安全能量库仑激发实验及矩阵元分析显示，名义低K带随自旋增加混入较高K分量；作者将其与转动顺排联系。 | experimental-fact + author-interpretation | Abstract PDF pp.6–7；Ch.12 PDF pp.279–280 | 不等于直接测得非零静态γ，更不要求高K异能态自身已强烈混合。 |
| HB05-R7-2 | 结论将I≳12ℏ附近低K至高K带间强度接近约1 W.u.、部分折合阻碍接近1，与高K带仍较纯的情形并列报告。 | author-interpretation | PDF p.280，印刷p.247 | 属于该实验/模型分析中的带间矩阵元，不是所有178Hf衰变支路或所有形变核的普适阈值。 |
| HB05-R7-3 | 作者明确建议比较176Hf与178Hf的8−异能态库仑激发，以及其它质量区，以区分单粒子和集体转动效应。 | author-interpretation | PDF p.281，印刷p.248 | 这是跨区可检验研究路线，不能记成已取得的比较结果。 |

**Knowledge Impact：revises。** 对
[[high-spin-isomers-and-decay-modes-systematics]] 和
[[reduced-hindrance-factor]] 的影响：禁戒跃迁由初、末态波函数及算符共同决定；
小fν不能唯一反演三轴形变。P0：本次未发现未隔离的原件/哈希问题。
P1：需保留安全激发、拟合约束、矩阵元相关及不同支路多极性的适用条件。

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Adam B. Hayes，*Violations of K-Conservation in 178Hf*，University of Rochester，博士学位论文，2005，293 页。原始 PDF SHA-256 为 `4982B80A3E830CFE034E51428D2467C7D94852607D8DBB773E1B66A820EBDDC0`。

### 2026-11-21 原页对账：产额、活度与拟合条件

| ID | 证据与结果 | 原件定位 |
|---|---|---|
| HB05-YIELD | 薄靶 \(^{136}\mathrm{Xe}+{}^{178}\mathrm{Hf}\) 的 Gammasphere–CHICO 数据，按散射角区及粒子身份选取并逐事例校正 Doppler。以基带 \(8^+\to6^+\) 归一，门控产额校正包含逐光子的效率、门跃迁内转换与旁支。低至约 \(10^{-4}\) 的谱线有可测值及上限两种。 | PDF 69–102，§§3.1–4.2，式 4.1 |
| HB05-ACT | 五片 Ta 靶的活化实验有四片用于离线结果。表 6.9 按 88%、80%、76%、72% 库仑垒列 \(\sigma_{16^+}=11(3),6(2),1.4(4),0.6(2)\) mb，均从 325–426 keV 双符合活度换算。首靶的两种单峰活度和双符合活度共享效率量，不独立。靶厚随时间变化影响剂量和束能，正文另估约 20% 的截面影响。 | PDF 146–190，§§5–6，表 6.7–6.9、图 6-11 |
| HB05-COMBINED | \(K=16^+\) 的 prompt \(19^+\to18^+\) 产额和离线 \(16^+\) 活度一起限制矩阵元。单参数 SDM 在高自旋强度已经过大时仍低估活度约 3–6 倍，线性自旋参数化也无法兼顾两组测量。逐项约束拟合另使用未见馈入的上限。表 9.14 的耦合误差、对角误差和上下限各有意义，部分矩阵元只获上限。 | PDF 191–204、259，§§7.1–7.4、图 7-1 至 7-4、表 9.14 |
| HB05-BRANCH40 | \(6^+\) 异能态至 \(K=4^+\) 带头的约 40 keV 支路，通过带头次级 γ 强度间接测量。计入转换约占总宽度 \(19(1)\%\)，表 4.4 给 \(B(E2)=1.03(7)\) W.u.，\(\alpha_{\rm IC}=216\)。这个值和按完整宽度重新归一的其他支路共同进入布居分析。 | PDF 99、134–138，§4.4、表 4.4 |
| HB05-PATHS | 对 \(8^-\) 带，GSB 和 γ 带的 E3 耦合以及高位 \(8^-_2\) 带的馈入共同影响产额。不同 \(K\) 分量假设可给相似结果，拟合偏好保留明确模型依赖。表 9.3 上半是按在线拟合矩阵元积分的截面，下半是 Ta 活化测得的截面。 | PDF 119–132、233–246，表 4.1–4.3、图 9-2、表 9.3 |

- 表 7.1 对 \(14^-\) 馈入的 M2 算例给 \(17(4)\%\)。其前提包括弱峰归属及给定转换系数，末段说明最终矩阵元表采用未作该馈入调整的拟合。两份实验的响应、共享量和未计入的条件校正须随值保留。见 PDF 202–204。
- PDF 214 的 §8.5 把两条 \(8^-\) 带写为 1174 与 1479 keV，PDF 233 的 §9.5 标题把低带印为 1147 keV。两处同指异能态带，已在原页核对两种印刷值。PDF 214 的 §8.4 将 \(K=6^+\) 的 \(14^+\) 升级及 \(15^+\) 暂定分开，表 8.1 的新能级标记应结合该文字说明。
- 高 \(K\) 的不同组态可以在同一 \(K\) 内强混合。§9.5.2 的两个 \(8^-\) 带正是此例，不能用这个混合证明 \(K\) 本身丧失。§10 的低 \(K\) 端混合解释使用自旋趋势、异能态寿命和高 \(K\) 带比较；尚不能从单个带间强度确定唯一的 \(K\) 分布。
- [[campaign-g07-hayes-2002-178hf-coulex-paths]] 是同作者的期刊比较入口。学位论文印刷 253 页的书目引用该条，期刊正文此次仍未取得。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF 1、6–293 的题页、摘要目录、12 章、图表及参考文献，合计 289 页科研与书证范围。逐页 OCR 用来定位，数字、弱线与符号以重点原页核对为准。Chapter 11 保留为作者讨论。
- Not covered: PDF 2–5 的献词、履历和致谢不计科研覆盖。全部矩阵元未逐项复算，外引文献的全文和原始事件另查。
- Coverage caveats: PDF 的文本编码不可直接可靠提取；关键结论以视觉/OCR 页面、章节和表号为 locator，正式使用仍应回看原页。

## Paper Question and Scientific Motivation

论文用安全能量下的 Coulomb excitation 研究 `178Hf` 高-K 带与低-K 带之间的电磁矩阵元，检验随自旋增加的 K-selection rule 破缺、旋转 alignment 与 isomer depopulation 路径（Abstract；Chapters 1–2、12）。

## Method and Design Logic

Experiment I 以 650 MeV `136Xe` 激发 89% 富集 `178Hf` 靶，Gammasphere+CHICO 提供逐事件 Doppler-corrected γ 数据；Experiment II 用 `178Hf` beam 在 Ta target 上 72–88% Coulomb barrier 激发 `16+` isomer。将 level-scheme、yield、activity、Alaga rule 和 spin-dependent mixing（SDM）/矩阵元拟合联合起来，得到 K-mixing 与 hindrance 约束（Abstract；Chapters 3–7、12）。

## Key Evidence and Reasoning Chain

1. γγγ gates 延伸 GSB、γ、K=4+、K=6+、K=8− 和 K=16+ bands。
2. Coulomb-excitation yields/activation data 约束各带布居和 low-K→high-K transition matrix elements。
3. Alaga rule 描述 K-allowed transitions，SDM 描述 K-forbidden population；拟合比较不同 excitation paths。
4. 低-K bands 的 interband matrix elements 随自旋迅速增加，而高-K bands 保持较少混合，形成 K-distribution 证据。

## Summary

论文报告 `178Hf` 高-K bands 在两个安全能量 Coulomb-excitation 实验中被布居，并测量低-K/高-K 之间的矩阵元。结论是 K-selection rule 的破缺随自旋增加，旋转 alignment 可解释低-K bands 中 higher-K admixture 的快速增长；在约 `I≥12ℏ` 后 K-forbidden transition 的 hindrance 可降至接近允许跃迁的量级，而高-K bands 在更高自旋仍较少混合。作者强调这是 K-distribution 随自旋的首个探测，具体矩阵元和模型仍受实验 yield、SDM/Alaga 假设约束。

## Experimental or Theoretical Setup

- Experiment I：`178Hf(136Xe,136Xe')178Hf`，650 MeV，89% enriched target，Gammasphere+CHICO。
- Experiment II：`178Hf` beam + natural Ta target，72–88% barrier，测 `16+` isomer activation/cross sections。
- γγγ gates、Doppler correction、particle identification、Coulomb-excitation yield fits。
- Alaga rule、spin-dependent mixing model、SDM 和 projected-shell-model/collective interpretation。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| HB05-1 | 两个安全能量 Coulomb-excitation 实验布居 `178Hf` 的 Kπ=0+,2+,4+,6+,8−,16+ bands，并测量 low-K/high-K coupling matrix elements。 | experimental-fact | direct | multiple-independent | Abstract；Ch.12 pp.246–248 | true |
| HB05-2 | Experiment I 用 650 MeV `136Xe` + 89% enriched `178Hf`、Gammasphere/CHICO；Experiment II 用 `178Hf` beam + Ta target 在 72–88% barrier 测 `16+` activation cross section。 | experimental-fact | direct | multiple-independent | Abstract；Chs.3,5 | true |
| HB05-3 | Combined Coulomb-excitation yields show K-selection rule breakdown increasing with spin；低-K→高-K 矩阵元在 `I≈10` 后 rapid increase。 | experimental-criterion + author-interpretation | indirect | multiple-independent | Ch.12 pp.246–247；Ch.10 | true |
| HB05-4 | 对低-K bands，higher-K components 随自旋混入，约 `I≥12ℏ` 后 K-forbidden reduced hindrance 可接近 `fν≈1`；高-K bands 在更高自旋仍较少混合。 | experimental-criterion + author-interpretation | indirect | multiple-independent | Abstract；Ch.10；Ch.12 p.247 | true |
| HB05-5 | Alaga rule 可描述 K-allowed transitions，spin-dependent mixing/SDM 可在多种路径中重现 K-forbidden yields；矩阵元为模型辅助拟合结果。 | model-result | direct | multiple-independent | Ch.4.3；Ch.7；Ch.9 | true |
| HB05-6 | 作者把低-K K-distribution 的快速变化与 rotational alignment 联系起来，并讨论 Coulomb depopulation/isomer release 的可能性。 | author-interpretation | indirect | multiple-independent | Ch.10–12 | true |
| HB05-7 | PDF 文本层存在编码问题；标题、作者、摘要和关键结论已视觉核对，但表格/弱矩阵元正式引用需回看原始页面。 | analytical-boundary | direct | single | Visual pp.1,6–7,246–248；TOC pp.8–12 | true |

## Nuclear Structure Information

- `178Hf`：GSB、γ、K=4+、K=6+、K=8− 和 K=16+ isomer bands。
- K-mixing、K-forbidden electromagnetic transitions、Coulomb excitation 和 rotational alignment。

## Authors' Interpretation

作者认为 K 是低自旋高-K bands 的近似好量子数，但在低-K bands 随自旋增加迅速失效；旋转 alignment 是主要解释，K-forbidden transitions 可成为 isomer depopulation 的路径。

## Model Results

- Alaga rule / SDM：矩阵元和 Coulomb-excitation yields。
- Projected-shell/collective models：K-mixing 和转动解释。

## Competing Interpretations and Limitations

- K-mixing 的量化依赖 SDM/Alaga systematics、yield fitting 和 matrix-element correlations。
- “K-selection rule breakdown” 是观测到的矩阵元模式及模型解释，不等于 K 量子数在所有 bands 中完全失效。
- PDF OCR/编码问题使弱表格和符号存在误读风险；本页保留 P0/P1。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-HB05-1 | Core reconstruction | 该论文将高-K isomer depopulation 转化为可拟合的 low-K/high-K matrix-element 与 spin-dependent K-distribution 问题。 | HB05-1–6 | unreviewed |
| AR-HB05-2 | Assumptions and dependencies | 结论依赖 Coulomb-excitation model、Alaga/SDM、yield/activity calibration 和 Doppler-corrected level scheme。 | Chs.4–10 | unreviewed |
| AR-HB05-3 | Transfer conditions | 可作为高-K、K-mixing 和 safe Coulomb-excitation 方法桥接，不直接迁移到 A≈130 wobbling。 | HB05-3–7 | unreviewed |
| AR-HB05-4 | Failure conditions | 改变 matrix-element correlations、target yields 或 K assignments 会改变 K-distribution/depoulation 解释。 | Chs.7,9,10 | unreviewed |
| AR-HB05-5 | Reverse/falsification test | 复核各 band yield、matrix-element covariance、hindrance factors，并与 `180Hf`/邻核比较。 | Ch.9–12 | unreviewed |
| AR-HB05-6 | Research-question decision | 作为 K-mixing、isomer depopulation 和 electromagnetic selection-rule 参考源保存。 | HB05-1–7 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 high-spin/rotational background，但没有 `178Hf` K-mixing 的完整 Coulomb-excitation matrix-element source。
- Effect of this source: supports and extends high-K/K-mixing method map；limits 对模型和 OCR 表格的直接引用。
- Reason: 提供随自旋 K-selection breakdown、Alaga/SDM 和 isomer depopulation 的证据链。
- Persistence decision: 新建 source；`178Hf` 先 source-only。
- Review state: 页面 `unreviewed`；HB05-1–7 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[rotational-bands]] | 高-K bands、Coulomb excitation 和矩阵元拟合。 |
| limits | [[signature-splitting]] | K-mixing 是不同于 signature splitting 的选择定则问题。 |
| foundational-background | [[high-spin-phenomena]] | 高自旋 alignment 与 isomer depopulation 背景。 |

## Human Review Triage

### P0

- HB05-1/HB05-2：核对两个实验、reaction、beam energy、target/enrichment 和 band list。
- HB05-3/HB05-4：核对 K-mixing 随自旋的趋势、`I≈12ℏ`、hindrance 和高-K bands 仍较少混合的措辞。
- HB05-7：核对 OCR/视觉核验范围，避免从乱码文本层误引矩阵元或符号。

### P1

- HB05-5/HB05-6：核对 Alaga/SDM 模型条件、alignment interpretation 和 isomer depopulation implications。

### P2/P3

- 后续需要时再建立 `178Hf` nucleus/experiment 页面。

## Extracted Pages

- Nuclei: `178Hf` 暂 source-only。
- Concepts: [[high-spin-phenomena]]、[[rotational-bands]]。

## Non-source Notes and Follow-up

关键页面已视觉/OCR核对；原始 PDF 中从 `pdftohtml` 提取的图片文件属于 raw 用户证据，不能加入本次知识 commit。

## Day21周考推断阶梯审计：178Hf 高 K 异构态与科里奥利 K 混杂证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint016_k_isomer_hindrance_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/k-isomer-hindrance-audit-016.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HB05-D21-1 | Hayes 2005 博士论文实验测定 $^{178}	ext{Hf}$ 库仑激发耦合矩阵元，确立高 $K$ 异构态推断阶梯边界：(1) 自旋依赖的 $K$-选择定则破缺：基态带（$K=0$）向高 $K$ 带的耦合在低自旋（$I \le 6\hbar$）保持高度禁戒（$f_
u \sim 85 - 95$），但在中高自旋迅速受到科里奥利力（$H_C \propto I \cdot j$）对高 $j$ 准粒子轨道（$i_{13/2}$ 中子与 $h_{11/2}$ 质子）的强烈混杂，在 $I \ge 12\hbar$ 处归一化阻退因子暴跌至 $f_
u \approx 1.2 - 1.8$（禁戒性彻底丧失）；(2) 内禀轴对称形状刚性：实测带内过渡四极矩在 $I=2 	o 16\hbar$ 区间保持 $Q_t = 6.95(15)\ e	ext{b}$（$\beta_2 = 0.280$ 恒定，变动仅 $0.43\%$），彻底排除了三轴形变诱导 $K$-混杂假说（若归因于三轴性将伪造出 $\gamma \sim 22^\circ$ 假象）。推断阶梯确立：严禁将 $f_
u \ll 100$ 直接等同于三轴形变或内禀形状突变，判定 $K$-破缺机制必须结合带内四极矩稳定性与科里奥利微观混杂解折叠。 | claim-boundary-audit | direct-and-derived | Ch.10 pp.200-220; Ch.12 pp.246-248; k-isomer-hindrance-audit-016.json | true |
