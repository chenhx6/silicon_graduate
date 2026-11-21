---
type: source
title: "郑宽宽 2021 博士论文：119Cs、119Ba 和118Cs 的集体性与形状"
aliases: [郑宽宽论文, Kuankuan Zheng JUROGAM3 MARA thesis]
created: 2026-09-10
updated: 2026-09-10
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment-and-model
reading_depth: deep-read
title_original: "Collectivity and shape phenomena in extremely neutron deficient 119Cs, 119Ba, and 118Cs studied with the JUROGAM 3 + MARA setup"
authors: [郑宽宽]
journal: "Université Paris-Saclay 博士学位论文"
year: 2021
pages: 177
language: en/fr
canonical_source: "Zheng, Kuankuan. Collectivity and shape phenomena in extremely neutron deficient 119Cs, 119Ba, and 118Cs[D]. Université Paris-Saclay, 2021."
citation_key: "zheng_2021_118cs-collectivity-shape"
raw_file: "raw/theses/degree-dissertation/郑宽宽.pdf"
raw_sha256: "72A90D742C6FC7ED0872F072BFFEBA0AB0D342D7C5BFD43E478FEB8953365AFE"
nuclei: [118cs, 119ba, 119cs]
experiments: [jurogam3-mara-119cs-119ba-118cs]
models: [particle-number-conserving-cranked-shell-model, tilted-axis-cranking, covariant-density-functional-theory]
observables: [lifetime, moments-of-inertia, alignment, bm1-be2-ratio, signature-splitting]
methods: [in-beam-gamma-spectroscopy, recoil-mass-separator, gamma-gamma-coincidence]
tags: [a120, shape-coexistence, chirality, triaxiality, phd-thesis]
---

# 郑宽宽 2021：`119Cs`、`119Ba`、`118Cs`

## Bibliographic Record

郑宽宽，*Collectivity and shape phenomena in extremely neutron deficient 119Cs, 119Ba, and 118Cs studied with the JUROGAM 3 + MARA setup*，Université Paris-Saclay 博士学位论文，2021，177 页。原始 PDF SHA-256 为 `72A90D742C6FC7ED0872F072BFFEBA0AB0D342D7C5BFD43E478FEB8953365AFE`。

## Scope and Reading Depth

- `deep-read`：177 页底本的科研与书证范围已对账。PDF 11–68 为 Chs.1–4，69–106 为 \(^{119}\mathrm{Cs}\)，107–122 为 \(^{119}\mathrm{Ba}\)，123–146 为 \(^{118}\mathrm{Cs}\)，147–148 为结论，149–177 为附录、图表目录、书目和双语摘要。整源计入 167 页，另 10 页为献辞、致谢、空白及仅有页眉或页码的页。
- 理论背景沿用既有通读并回核目录、核心公式与源内应用。实验章、三核结果、时谱和附录以本次原文回核和三篇对应出版版补齐。结果表按逐页范围及代表行审计，未逐项转录或重拟合，参考文献未逐篇复核。

## Summary

论文用 JUROGAM 3 + MARA 研究 `119Cs`、`119Ba`、`118Cs` 的高自旋集体性、形状共存和 revolving chiral 候选，报告异能态寿命与 PNC-CSM/TAC-CDFT 比较。

## Key Results

实验使用 JUROGAM 3 + MARA，建立 `119Cs`、`118Cs` 从低自旋到高自旋的能级图，并在 `119Ba` 发现新带（Abstract；Chs.5–8）。

| issue_id | 主张 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DD-20260910-MP-037 | `119Ba`/`119Cs` 的 `5/2−`、`11/2−` 带头 isomer 半衰期分别为 `0.36(2) μs`、`55(5) μs`；`118Cs` `7+` isomer 半衰期为 `0.55(6) μs`。 | experimental-fact | direct | Abstract；Chs.5–7；Ch.8 pp.141–148 | true |
| DD-20260910-MP-038 | `119Cs` 低自旋同时出现 prolate 与 oblate 结构；Band 3 的 `πh11/2[505]11/2−` 与 Band 1 的 `πh11/2[541]3/2−` 被用于形状共存解释。 | experimental-criterion + author-interpretation | indirect | Ch.5.3.1 pp.77–85；Ch.8 | true |
| DD-20260910-MP-039 | `119Cs` Bands 8/9 近简并、alignment 和 `B(M1)/B(E2)` 系统学被作者解释为只含质子的 revolving chiral doublet；PNC-CSM/TAC-CDFT 给出 3D 几何。 | author-interpretation + model-result | indirect | Ch.5.3.2 pp.85–90；Ch.8 pp.147–148 | true |
| DD-20260910-MP-040 | 论文将 `118Cs` `πh11/2⊗νh11/2` 的 `8+` band-head 与 `7+` isomer 作为异能态/高自旋结构案例，并提出厚靶高统计寿命实验。 | experimental-fact + next-route | direct/indirect | Ch.7.4；Ch.8.2 | true |

## Competing Interpretations and Limitations

`119Cs` 的 prolate/oblate 与 revolving chirality 依赖 PNC-CSM、TAC-CDFT、alignment 和相对转移强度；近简并、signature 和 `B(M1)/B(E2)` 不能单独证明静态手征。该 thesis 与相关期刊结果存在共同实验 lineage，不能重复计数。

- Related: [[187au]]（只作高自旋 Au/Cs 比较）、[[chiral-doublet-bands]]、[[triaxial-shape-coexistence]]、[[wobbling-vs-signature-partner]]。

### P0

- `DD-20260910-MP-037/038/039`：核对三个半衰期、Band 1/3/8/9 身份、形状和 RχD 的必要伴随证据。

### P1

- `DD-20260910-MP-040`：核对 `118Cs` isomer 未来实验方案和 `119Cs`/`118Cs` source independence。

`knowledge_increment`: 增加 A≈120 质子滴线附近形状共存与 revolving-chiral 候选的完整 thesis chain；`boundary-knowledge`: 解释高度依赖模型和相对强度，保留候选层级。

## Extracted Pages

- 理论/实验技术：Chs.1–4；`119Cs`：Ch.5，PDF pp.69–100；`119Ba`：Ch.6；`118Cs`：Ch.7；总结：Ch.8，PDF pp.141–148。

## 2026-11-21 版本与谱学方法回核

- 现有 177 页底本与馆藏 `105017_ZHENG_2021_archivage.pdf`（178 页）按同一论文登记。存档版多一页机构封面，后续 175 个非空页的规范化提取文本按页完全对应，另有两组空白页经渲染对应。此为文本与页码对账。下列 PDF 页码使用 177 页底本，正文印刷页为 PDF 页减 6。
- PDF 63／印刷 p.57，DCO 实际矩阵以 \(157.6^\circ\) 组为 x，\(75.5^\circ+104.5^\circ\) 组为 y。按 Eq. (4.9)，分子为目标线在 \(157.6^\circ\) 且门线在近 \(90^\circ\) 组，分母交换两线对应的角组。Eq. (4.8) 的两个门角字面都写作 \(\theta_1\)。数据几何采用 Eq. (4.9)、矩阵叙述及结果表注。二极门示例约 \(1.0,2.1\)，四极门约 \(0.46,1\)，对应各自的偶极、四极目标线。
- PDF 64／印刷 p.58，\(R_{\rm ac}\) 两个投影均使用全角门，分子为 \(133.6^\circ+157.6^\circ\) 角组，分母为 \(75.5^\circ+104.5^\circ\) 角组，见 Eqs. (4.10)–(4.11)。PDF 66–67／印刷 pp.60–61 的 \(A=(aN_\perp-N_\parallel)/(aN_\perp+N_\parallel)\)，\(P=A/Q(E_\gamma)\)。论文把 \(a(E_\gamma)\) 的拟合归于 Ref. 118，结果表列 \(A\) 或 \(A_p\)。该节的 “PDCO” 是其偏振测量段落标题。
- PDF 120／印刷 p.114，\(^{119}\mathrm{Ba}\) Table 6.2 的 161.5 keV 行给 \(R_{\rm DCO}=1.2(1)\)（伸展偶极门），\(a_2=-0.72(12)\)、\(a_4=0.40(23)\)、\(A_p=-0.14(5)\)，以及 \(-2.3(2)\) 或 \(-0.3(5)\) 两支。保留两支和表题原记 \(\delta(M1/E2)\)。正文 Eq. (2.60) 在将总 \(\Delta I=1\) 分支强度乘以 \(1/(1+\delta^2)\) 提取 M1 分量时，对应 E2/M1 的振幅比。两处属于不同定位，当前证据未闭合该表的分子约定。表注和 Fig. 4.6 也未说明偏振量对该行的两支是否另有筛选，不能从 \(A_p\) 和 \(\delta\) 同行推定联合拟合。
- 附录 A Table A.1 给出 39 个探测器位置，分别为 \(157.6^\circ\) 5 个、\(133.6^\circ\) 10 个、\(104.5^\circ\) 和 \(75.5^\circ\) 各 12 个。方位角零点竖直向上，从上游观察顺时针递增。附录原表给名义几何。实际探测响应仍依赖能效、阈值和入选事件。

## 与期刊出版版的证据关系

- Ch.4 PDF 57–58／印刷 pp.51–52 所述 \(^{64}\mathrm{Zn}\) 束 255 MeV、\(^{58}\mathrm{Ni}\) 靶 \(0.75\,\mathrm{mg/cm^2}\)、JUROGAM 3＋MARA 及 3p、2p1n、3p1n 三条反应道共同定位该次采集。[[zheng-2021-cs118-bands-and-isomers]] 044325-2 明示三核相关结果同次采集。该文 Ref. 20 指向 [[zheng-2021-ba119-neutron-excitations]]。出版 Table I 与学位 Table 6.2 的 e/f 字母互换，按各自表注解释可核实 161.5、146.3 keV 的物理门一致。出版和论文均在 161.5 keV 行保留两支。
- \(^{119}\mathrm{Cs}\) 的 Table 5.2／印刷 p.97 与 [[zheng-2021-cs119-proton-excitations]] Table II 的 208.7 keV 同宇称跃迁行及 1095.6 keV 反宇称行可一一对应。\(^{118}\mathrm{Cs}\) 的 Table 7.1／印刷 p.137 与出版 Table I 的 265.5 keV 行一致。\(^{118}\mathrm{Cs}\) 的 \(0.55(6)\,\mu\mathrm{s}\) 也对应同一组 79、126 keV 延迟计时谱。统计发表作品时分别登记，统计实测证据时各自按同次采集和同一跃迁记录。

## 三核时谱与结构解释的范围

| 对象 | 原文实测或分析输入 | 作者解释与边界 | 定位 |
| --- | --- | --- | --- |
| \(^{119}\mathrm{Cs}\) Band 1，\(11/2^-\) | 靶位约 287 keV 门下，MARA 焦面约 87 keV 线给 \(T_{1/2}=55(5)\,\mu\mathrm{s}\) | 该数值属于退激 Band 1 的时谱。Fig. 5.14 的 287+474 keV 双门用于展示符合关系。Fig. 5.15 左图另为 511 keV 时谱，纵向分析中标的是 \(\tau\)。 | PDF 82／印刷 p.76，Figs. 5.14–5.15 |
| \(^{119}\mathrm{Ba}\) Band 1，\(5/2^-\) | 将靶位 93、113、207、363 keV 各门下 66 keV 延迟时谱相加，给 \(T_{1/2}=0.36(2)\,\mu\mathrm{s}\) | 53、59 keV 支也有相容的时标，误差更大。极弱支路次序还依赖符合、强度与有条件的 Weisskopf 估计。 | PDF 112–113／印刷 pp.106–107，Fig. 6.5；PDF 118–119，Table 6.1 |
| \(^{118}\mathrm{Cs}\) Band 1 下方的 \(7^+\) | 79 和 126 keV 延迟时谱合并，给 \(T_{1/2}=0.55(6)\,\mu\mathrm{s}\) | \(8^+\) 态的纳秒量级属于时序解释。焦面延迟射线缺少角关联，保留 126 keV 多极性和下游归属歧义。 | PDF 128–130／印刷 pp.122–124，Fig. 7.5；PDF 148，Sec. 8.2 |
| \(^{119}\mathrm{Cs}\) Bands 1、3 的形状 | 能级及衰变路径、惯量与对齐曲线；Band 3 缺少至其他负宇称带的观测连接 | PNC-CSM 使用 \(\varepsilon_2=+0.32,-0.17\) 分别描述 Band 1、3。TAC-CDFT 的 \(\pi h_{11/2}\) 势能路径随 \(\beta\) 从扁形偏好转向长形，路径无分隔势垒且沿 \(\gamma\) 很软。缺失跃迁还可与 \(\Delta K\) 阻碍有关。形状指认依赖这些模型与解释。 | PDF 87–89／印刷 pp.81–83，Figs. 5.21–5.23 |
| \(^{119}\mathrm{Cs}\) Bands 8、9 的转动手征候选 | 近简并、相近惯量、相对 \(B(M1)/B(E2)\)，以及 \(\hbar\omega\approx0.32,0.37\) MeV 的两处交叉与约 \(8\hbar\) 对齐增量 | TAC-CDFT 给 \(\gamma\approx12^\circ\)，解只在部分频段收敛。PNC-CSM 测试了较小形变加中子对齐和 \([422]3/2^+\) 等替代，分别出现未见惯量跃变或与衰变、签名分裂不符。Fig. 5.31 的角动量方向是模型示意。 | PDF 91–95／印刷 pp.85–89，Figs. 5.25–5.31 |
