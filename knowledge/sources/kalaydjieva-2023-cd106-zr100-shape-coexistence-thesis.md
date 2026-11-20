---
type: source
title: "Kalaydjieva 2023 - Shape coexistence in nuclei with A approximately 100"
title_original: "Study of shape coexistence in nuclei with A≈100 using stable and radioactive ion beams"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: skimmed
authors: ["Desislava Kalaydjieva"]
year: 2023
institution: Université Paris-Saclay
doi: 10.70675/c170c2b4z5cecz4187z8bacz070f04c3f6c4
canonical_source: "Desislava Kalaydjieva, Université Paris-Saclay doctoral dissertation, HAL tel-04472302v1"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/129736_KALAYDJIEVA_2023_archivage.pdf
raw_sha256: 8a888adca2429166e6b4878a342173313754ceb77b8f3f0f8f21c71e9acd7005
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261120-kalaydjieva-experiment-crosswalk/manifest.json
nuclei: ["106Cd", "100Zr"]
tags: [shape-coexistence, coulomb-excitation, angular-correlation, mixing-ratio, thesis]
---

# Kalaydjieva 2023：¹⁰⁶Cd 库仑激发与 ¹⁰⁰Zr β 衰变谱学

## Bibliographic Record

巴黎萨克雷大学博士论文，2023 年 10 月 20 日答辩，NNT 2023UPASP134。馆藏为 246 页 HAL v1，封页记载 2024 年 2 月 22 日存档。PDF 1–2 核对身份。正文中的印刷页比 PDF 页小 19。

## Summary

¹⁰⁶Cd 部分检验在经验安全能量以上测得的相对 γ 产额能约束哪些电磁矩阵元。¹⁰⁰Zr 部分用 β 衰变后的 γγ 相对开角测量确定若干低位能级的自旋并估计 δ。两部分都展示了同一类边界：拟合所得量取决于可分辨的布居或衰变路径，以及外部谱学信息对这些路径的约束。

## Scope and Reading Depth

已定向回读两实验的归一、拟合和结构解释，并核对两份会议论文及两个摘要的实验依赖关系。Thesis `reading_depth` 按局部覆盖登记。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| KAL-CD-YIELD | Cd 各角区对 \(2_1^+\to0_1^+\) 的 γ 产额归一。 | method | direct-source | PDF 48–50，§4.3.2 |
| KAL-CD-E3 | 允许 \(3_1^-\) 两步布居时，现有数据不能独立确定测试的两种耦合。 | inference | model-dependent | PDF 112–115，表 6.4 |
| KAL-ZR-AC | 自由 \(a_2,a_4\) 的拟合优度和受约束 δ 拟合的检验须分别记录。 | method | direct-source | PDF 194–202，表 12.4、图 12.12–12.15 |
| KAL-ZR-LINEAGE | 2026 年报告给同一 GRIFFIN 数据的新 δ 区间；Wu 使用另一台谱仪和另一采集。 | evidence-audit | direct-source | 2026 会议论文 §§2–4.1；Wu 2024 出版者摘要 |

### ¹⁰⁶Cd 的产额、光学势与矩阵元

- 2015 GANIL 的 770 MeV ¹⁰⁶Cd 束轰击 ⁹²Mo，在 VAMOS++ 中识别散射粒子、在 AGATA 中测量符合 γ 射线。采集只接受已识别的粒子与 γ 符合，未记录弹性粒子样本供绝对效率标定。每个实验室散射角区间的 γ 产额对本区间的 \(2_1^+\to0_1^+\) 产额归一，多个比值共享该分母。PDF 13、48–50，§4.3.2，图 4.9。
- FRESCO 比较纯库仑与含核作用的耦合道截面。论文对照的是截面与实测相对 γ 产额的变化趋势，后者包含馈入及靶厚与角接受度的平均。GOSIA 在 \(\theta_\mathrm{LAB}=19.7^\circ,20.5^\circ,21.5^\circ\) 的低角数据上拟合矩阵元，再对照高角产额。排除两个激发 \(0^+\) 跃迁的第三角区后，相关 E2 矩阵元增大 14%–17%。仅把若干 yrast 线的更高角区纳入测试时，\(6_1^+\to4_1^+\) E2 矩阵元增大 11%，其变化被计入误差。PDF 83、87、102–104，§§5.6.4、6.2。
- 表 5.6 主列对应独立观测的粒子—γ 产额。表 5.7、5.8 的部分矩阵元依赖外部 γ 分支或混合比。表 5.9 还列出主要由输入谱学数据决定的拟合值。正负号测试先选定态的相位，再检查相对符号；表 6.1 的部分判别借助寿命、角度趋势或过大的 \(B(E2)\)。例如，翻转 \(\langle2_1^+\Vert E2\Vert4_2^+\rangle\) 令绝对 \(\chi^2\) 降低 8，但得到的 \(4_2^+\) 寿命比文献值短约十倍。采用值及误差按矩阵元分别纳入所测试的角区、强馈入和符号解。PDF 105–110，§§6.2.1–6.2.2，表 6.1–6.2。
- 表 6.3 的 \(2_2^+\) 对角 E2 值 \(+1.32(8)\,e\,\mathrm b\) 来自外部资料。置零此项对低角结果影响较小；在 26.5° 和 29.5°，标准解的 \(2_2^+\to2_1^+\) 模拟产额分别高 16% 和 25%。该测试未计入最终误差；采用的对角信息及高角核相互作用均影响解释。PDF 110–112，§6.2.3，表 6.3。
- 表 6.4 单一标准布居路径给 \(B(E3;5_2^-\to2_1^+)=40(3)\) W.u.、\(B(E3;1^-\to2_1^+)=45(3)\) W.u.。若容许经 \(3_1^-\) 的 E3–E2 两步馈入，拟合的直接耦合显著减小。引入 26 W.u. 的 \(5_1^-\to3_1^-\) E2 耦合可解释全部 \(5_1^-\) 布居，使该态直接 E3 幅接近零。现有产额不能同时确定两条路径的矩阵元；在测试的耦合模型下，作者据此提取 E3 上限。PDF 112–115、145–148，§6.2.4 和表 6.4，§§7.3–7.4。PDF 112 正文一次将 8.5 W.u. 标作 \(B(E2)\)，对应表格、耦合及上下文均为 E3。
- 表 7.1 给出由拟合和外部 E2 矩阵元合成的 \(\langle Q^2\rangle(2_1^+)/\langle Q^2\rangle(0_1^+)=1.00(7)\)。论文按本实验输入讨论与 Gray 等较小比值的差异。\(K=2\) 候选 \(3^+\) 的部分 \(B(E2)\) 采用外部 δ 双解中 E2 成分较强者，因而带成员解释有选支条件。作者对 \(6^+\) 强跃迁保留 γ 带及 seniority 态与转动态混合两种解释。PDF 137、139–142，表 7.1，图 7.8–7.10。弱 E2 分支与独立寿命可区分部分方案。

### ¹⁰⁰Zr 的 γγ 相关与 δ

- 用 GRIFFIN 测量 ¹⁰⁰Y β 衰变级联。对每个开角分别建立 prompt 与 mixed-event 矩阵；同门和同峰拟合后，用 prompt 峰面积除以非同时事件面积，并乘全局归一常数。混合事件校正角对数、相对效率等几何/采集效应；有限探测器张角另由 Geant4 的 \(Z_{0,2,4}\) 基函数处理。52 个晶体开角在 add-back 和角对选择后，报告的 666 keV 级联使用 49 点。PDF 191–199，§§12.3–12.4，图 12.10–12.12，附录 E。
- Method 1 以自由 \(a_2,a_4\) 拟合响应。Method 2 将 \(a_2,a_4\) 约束为给定级联、自旋和 δ 的理论值，对 δ 扫描并重新拟合整体尺度。报告的 δ 误差来自 \(\chi^2_{\min}+1\)；模型能否通过 99% 拟合优度阈值是另一个判据。表 12.4 的 \(\chi^2/\mathrm{NDF}\) 列来自 Method 1。PDF 194–200，表 12.4，图 12.12–12.13。

| 上能级及跃迁 | 学位论文正宇称 E2/M1 解 | 原件位置及条件 |
| --- | --- | --- |
| \(2_2^+\) 878.2 keV，约 666 keV → \(2_1^+\) | \(+4.2(1)\) | PDF 196、199，表 12.4、图 12.12。采用 1295 keV 级联模拟模板，最佳自旋明显领先，受约束拟合仍超过论文的 99% 拒绝阈值。666.0 同时为表中所列门能量。 |
| \(2_3^+\) 1196.1 keV，约 983.5 keV → \(2_1^+\) | \(-1.01(3)\) | PDF 183、196–200，表 12.1、12.4、图 12.13。212.6 keV 是门，拟合另一条峰；受约束拟合仍超过拒绝阈值。 |
| \(I=2\) 1441.4 keV，1228.9 keV → \(2_1^+\) | \(+9.4(9)\)，若采用同宇称 | PDF 196、200、202，图 12.15。1295 keV 模拟模板；自旋 2 可通过拟合优度检验，表 12.4 未给上态宇称。 |

1807.5 keV 的 \(I=1\) 解同时用衰变模式排除竞争自旋。1938.0 keV 态用 \(2_2^+\) 中间态，\(\delta=-0.007(7)\) 与零相容，\(1^{(-)}\) 仅为作者建议。1774 keV 的自旋 0 可通过检验；2068 keV 的自旋 0 为暂定，2143 keV 级联受污染。2208.5 keV 的 \(2^+\) 双重态成员靠符合与衰变模式提出；913.78(7) keV 到 1294.8 keV 态的衰变和相对 E2 强度为候选谱带提供线索。要定量比较形变仍需绝对强度与寿命。PDF 196–204、215–218，表 12.4、13.4、图 12.16–12.19、13.9–13.10。

此处 δ 的输入是开角分辨的 γγ 符合计数及响应，论文未使用实测线偏振 \(P\)。按方法记为 γγ 角关联，可作拟合和版本对照；P–δ 样本的线偏振准入条件未满足。

## Related experiments and versions

- ¹⁰⁶Cd 与 Siciliano 等 Phys. Rev. C 104, 034320 (2021)，DOI `10.1103/PhysRevC.104.034320`，源于同一次 GANIL RDDS 采集。同一套观测用于不同分析，寿命与激发产额可以提供不同约束。2026 GANIL 会议摘要也报告 AGATA–VAMOS++、⁹²Mo、超安全能量 8%–40% 与 FRESCO/GOSIA 的同一分析路线。会议摘要可作实验溯源，完整后续论文身份仍待核实。
- Kalaydjieva 等 2023 年会议论文，DOI `10.5506/APhysPolBSupp.16.4-A15`，§§2–3、图 1、表 1，报告同一 GRIFFIN 运行中的 2209 keV 双重态。两版低自旋成员分别给 2208.6(1) 和 2208.51(5) keV；共同的 637 keV 馈入门、衰变分支及装置/采集时序支持同一实验归并。
- Kalaydjieva 等 2026 年会议论文，DOI `10.5506/APhysPolBSupp.19.1-A15`，§4.1、图 2–3，使用同一 TRIUMF–GRIFFIN 数据，另给出时间随机矩阵扣除与大于 2 μs 的 mixed-event 窗。该版报告 \(2_2^+\to2_1^+\) 的 \(\delta=4.7^{+1.5}_{-1.1}\)、最小 \(\chi^2/\mathrm{NDF}=1.02\)，以及 \(2_3^+\to2_1^+\) 的 \(\delta=-1.00^{+0.18}_{-0.14}\)、最小 \(\chi^2/\mathrm{NDF}=1.38\)。作者称这些结果为初步结果。版本间的数值、误差和拟合优度须关联各自分析。事件级的差异来源尚未复现。
- Wu 等 Phys. Rev. C 109, 024314 (2024)，DOI `10.1103/PhysRevC.109.024314`，使用 Gammasphere 及质量分离的 ¹⁰⁰,¹⁰⁰ᵐY 衰变，独立于 TRIUMF–GRIFFIN 采集。出版者摘要报告 1294.5 与 1774.0 keV 的 \(0^+\)，并将 1774 keV 态视为更符合球形结构预测的候选。这个结论层级为分支数据与 MCSM 的对照。其全文数据表待单独核查。GRIFFIN 2026 论文 §4.1 给出两条 δ 与 Wu 数据的对照。

两份会议论文的出版版 PDF、APS 摘要页和 GANIL 会议摘要页及哈希保存在 `raw/papers/gpt/query/20261120-kalaydjieva-experiment-crosswalk/manifest.json`。

## Competing Interpretations and Limitations

Cd 的 E3 强度与未分辨 E2 布居路径相关，带指认依赖分支、选支及动力学模型。Zr 的自旋筛选、相对分支、绝对强度和形状模型比较分别依赖不同输入。相同实验的版本分析共享数据。

## Input and response checks

- 附录 A 给出 756.7 MeV 中靶能量的七态 FRESCO 算例，含库仑阶跃矩阵元和核光学势。附录 B–D 则给出 GOSIA 的能级表、矩阵元初值与约束、探测几何、内转换和外部谱学数据入口。角区积分采用 743.4、756.7、770 MeV 网格，以及三个低角区各自的 \(\theta_\mathrm{LAB}\) 和方位接受度。有限接受度积分 \(Y_i^\mathrm{inti}\) 与点值 \(Y_i^\mathrm{poin}\) 的比值用于将实测值转成点值拟合所需的量，\(Y_i^\mathrm{corr}=Y_i^\mathrm{exp}Y_i^\mathrm{poin}/Y_i^\mathrm{inti}\)。校正依赖矩阵元集，须随拟合迭代。PDF 89–91、220–237，式 5.24、5.27，附录 A–D。
- 附录 C 的 `OP,FILE` 把原产额与校正产额分为单元 3 和 4，附录 D 的 `OP,CORR` 说明同样指向单元 3，但所列文件后缀是 `106Cd.f3`，和附录 C 的 `106Cd.yld` 不一致。附录 C 含省略号，附录 D 的积分示例只列三个角区。复核可据选项和编号理解步骤，完整运行仍需原始输入、响应及实测产额文件。PDF 222、228、233–237。
- 附录 E 的晶体坐标和开角统计是并排的两组记录。Clover 13 的四个晶体缺席，开角列仍继续列剩余晶体组合。52 个开角的对数总和为 \(60^2=3600\)，含 60 个同晶体项。按 clover 做 add-back 后删去 0°、15.442°、21.905° 三类，得到 49 个开角。该角表给出几何组合，实测 prompt/mixed-event 峰面积及模拟响应来自各自的数据处理。PDF 193、238–239，表 E.1。

## Extracted Pages

Codex 定向回读两实验的布居、归一、参数拟合和结构解释，并逐页核对附录 A–E（PDF 220–239）。原图检查 PDF 108、114、137、195、197、199、200、202、204、239。覆盖为局部验收。尚需逐页核对两部分的理论、探测器、谱峰校准和完整正文表格。Gemini 的附录 A–B 请求返回 HTTP 502，附录核验归于 Codex。
