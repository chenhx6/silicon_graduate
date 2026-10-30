---
type: source
title: "Tawseef 等 2026：Pd 与 Cd 同位素磁转动与反磁转动的微观投影壳模型研究"
aliases: [Tawseef 2026 microscopic MR AMR, PRC 113 054307, arXiv 2601.12496]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: journal-article-theoretical
reading_depth: deep-read
title_original: "Microscopic investigation of magnetic and antimagnetic rotational motion in atomic nuclei"
authors: [W. Tawseef, Nazira Nazir, S. Jehangir, J. A. Sheikh, C. Majumder, S. Chakraborty, G. B. Vakil, G. H. Bhat, N. A. Rather]
journal: "Physical Review C"
year: 2026
volume: "113"
pages: "054307"
doi: "10.1103/xbsc-q21d"
arxiv: "2601.12496v1"
language: en
canonical_source: "https://doi.org/10.1103/xbsc-q21d"
citation_key: tawseef_2026_MR_AMR_Pd_Cd
raw_file: "raw/papers/gpt/tawseef-2026-microscopic-mr-amr-arxiv2601.12496v1.pdf"
raw_sha256: "eddb5f0d931ae4132f03aeb53d9b7a8d21f18d404653b5f2a1e3238c9156c199"
nuclei: [101Pd, 103Pd, 107Pd, 109Pd, 111Pd, 103Cd, 105Cd, 107Cd, 109Cd, 111Cd]
models: [projected-shell-model, semiclassical-particle-rotor-model]
observables: [energy-levels, BE2, BM1, J2-over-BE2]
methods: [angular-momentum-projection, configuration-mixing, multi-quasiparticle-diagonalization]
tags: [Day27, antimagnetic-rotation, magnetic-rotation, projected-shell-model, shears, A100]
---

# Tawseef 等（2026）：Pd 与 Cd 同位素磁转动与反磁转动的微观投影壳模型研究

## Bibliographic Record

W. Tawseef 等，*Microscopic investigation of magnetic and antimagnetic rotational motion in atomic nuclei*，*Physical Review C* **113**, 054307 (2026)，DOI `10.1103/xbsc-q21d`。Crossref 与 Web of Science 登记发表于 2026-05-19；官方预印本为 `arXiv:2601.12496v1`（15 页，1109927 bytes，SHA-256 `eddb5f0d931ae4132f03aeb53d9b7a8d21f18d404653b5f2a1e3238c9156c199`）。获取回执见 `outputs/literature-acquisition/20261029-day27-tawseef2026.json`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。完整通读 15 页正文与参考文献列表，详细核验 Table I，视觉核对 Figs. 1–17。
- Covered scope: 扩展至两个主谐振子壳层（two major oscillator shells）与五准粒子（5-qp）基底的投影壳模型（PSM）微观理论框架；半经典粒子-转子模型（SCM）比较；10 个奇中子核素（101,103,107,109,111Pd 与 103,105,107,109,111Cd）的能谱、能带交叉、准粒子占据波函数成分、B(E2)、B(M1) 与 J(2)/B(E2) 演化；109Cd 中 AMR 与 MR 模式在同核不同带中的共存。
- Not covered: 原 PSM 矩阵对角化程序源代码、未公开的多组态 Slater 行列式投影重叠矩阵元。

## Summary

论文将投影壳模型（PSM）推广至两个主谐振子壳层并包含奇质量核的高达五准粒子组态，系统研究了 A≈100 质量区 10 个奇中子 Pd 与 Cd 同位素的磁转动（MR）与反磁转动（AMR）能带。微观投影波函数表明，在能带交叉后波函数不仅具有主要的剪刀组态，还伴随显著的中子与质子多准粒子混合。模型自洽重现了 AMR 典型的 B(E2) 随自旋下降与巨大的 J(2)/B(E2)（150–600 ℏ²MeV⁻¹(eb)⁻²）比值，并在 109Cd 中成功描述了基态负宇称带（AMR）与激发负宇称带（MR）的同核多模式共存。

## Model Formulation and Numerical Setup

1. **PSM 微观哈密顿量：**
   \[
   \hat{H} = \hat{H}_0 - \frac{1}{2} \chi \sum_\mu \hat{Q}_\mu^\dagger \hat{Q}_\mu - G_M \hat{P}^\dagger \hat{P} - G_Q \sum_\mu \hat{P}_\mu^\dagger \hat{P}_\mu.
   \]
   单极配对强度 $G_M$ 依据奇偶质量差拟合参数 $G_1 = 22.68$ 与 $G_2 = 16.22$（Eq. 6）；四极配对取 $G_Q = 0.18 G_M$；四极力强度 $\chi$ 由自洽条件决定（Eq. 5）。
2. **电磁跃迁算符：**
   质子有效电荷 $e_p = 1.5 e$，中子有效电荷 $e_n = 0.5 e$；自旋 $g$ 因子淬灭取自由值的 $0.70$（$g_s(\pi) = 5.586 \times 0.70$，$g_s(\nu) = -3.826 \times 0.70$，$g_l(\pi) = 1$，$g_l(\nu) = 0$）。
3. **Table I 关键形变与配对参数：**
   - 101Pd: $\varepsilon = 0.128$（基态 TRS: $0.165$），$\Delta_n = 0.657$，$\Delta_p = 0.772$ MeV；
   - 103Pd: $\varepsilon = 0.180$，$\Delta_n = 0.957$，$\Delta_p = 0.995$ MeV；
   - 105Cd: $\varepsilon = 0.140$，$\Delta_n = 0.586$，$\Delta_p = 0.897$ MeV；
   - 107Cd: $\varepsilon = -0.110$（扁椭），$\Delta_n = 1.142$，$\Delta_p = 0.878$ MeV；
   - 109Cd: $\varepsilon = 0.140$，$\Delta_n = 1.125$，$\Delta_p = 0.947$ MeV。
4. **半经典对比模型（SCM）：**
   双剪刀对称闭合能量式（Eq. 12）采用 $V_{\pi\nu} \approx 1.2\text{ MeV}$，$V_{\pi\pi} \approx 0.2\text{ MeV}$；价空穴取 $\pi(g_{9/2})^{-2}$（Cd）与 $\pi(g_{9/2})^{-4}$（Pd）。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TW26-1 | PSM 扩展至包含两主壳与 5-qp 组态空间，系统求解了 101,103,107,109,111Pd 与 103,105,107,109,111Cd 共 10 个核素的高自旋态。 | model-result | direct | PDF pp.1–3, Sec.II | true |
| TW26-2 | Table I 给出所用轴对称四极形变 $\varepsilon$ 与自洽 BCS 配对能隙 $\Delta_n, \Delta_p$；形变均在 $\varepsilon \approx 0.11 - 0.23$（$\beta_2 \approx 0.12 - 0.25$）的弱形变区间。 | model-input | direct | PDF p.3 Table I | true |
| TW26-3 | 在 101Pd 与 105Cd 中，带交叉不仅包含预期的 $2\nu$ 对齐，且波函数分析（Fig. 11）显示交叉后存在显著的 $1\nu 2\pi$ 与 5-qp 混合，澄清了单纯剪刀几何背后的微观组态复杂性。 | model-result | direct | PDF pp.4–5, 8–11, Figs.2, 7, 11 | true |
| TW26-4 | 9 个 AMR 候选核（除 107Cd 外）的带内 $B(E2)$ 跃迁几率均自发展现出随自旋增加单调下降的特征，与 SCM $\sin^4\theta$ 趋势相符（Figs. 12–13），同时带内 $B(M1) \approx 0$（Fig. 16）。 | model-result | direct | PDF pp.11–13, Figs.12–13, 16 | true |
| TW26-5 | 动态转动惯量与 $B(E2)$ 比值 $\mathcal{J}^{(2)}/B(E2)$ 维持在 $150 - 600\ \hbar^2\text{MeV}^{-1}(e\text{b})^{-2}$ 的高位平台，微观证实了 AMR 区别于全对齐非集体能带终止（带终止时 $\mathcal{J}^{(2)}$ 剧烈塌缩）的核心判据。 | model-result | direct | PDF pp.11–12, Figs.14–15 | true |
| TW26-6 | 107Cd 在微观 PSM 中表现为显著的磁转动（MR）特征：$B(M1) \approx 0.5 - 2.5\ \mu_N^2$ 随自旋下降，而 $B(E2) \approx 0$；微观机制归因于扁椭形变（$\varepsilon = -0.11$）下粒子-空穴垂直非对称耦合。 | model-result | direct | PDF p.12, Figs.13, 16 | true |
| TW26-7 | 109Cd 在同一核中展现出 AMR 与 MR 的共存：yrast 负宇称带为典型的双剪刀 AMR 带，而基于 $1\nu 2\pi$ 构型的激发带展现出标准的 MR 强 $M1$ 阶梯（Fig. 17）。 | model-result | direct | PDF pp.12–13, Fig.17 | true |

## Competing Interpretations and Limitations

1. **PSM 与 SCM 的微观差异：** SCM 假设了刚性、固定长度的准粒子叶片与纯几何剪刀角 $\theta$，而 PSM 是在变形多体基底上做角动量投影和哈密顿量对角化。PSM 显示能带交叉区存在剧烈的组态混合，表明“纯剪刀角”仅为低能近似。
2. **转动带终止的竞争：** 论文明确指出纯 $B(E2)$ 衰减不足以单独证明 AMR，必须与 $\mathcal{J}^{(2)}$ 保持恒定联合判定，以排除顺排终止带（terminating bands）。
3. **形变参数对能带交叉序的敏感性：** 作者指出在 105Cd 中，较小形变预言质子先对齐，而较大形变预言中子先对齐；这证明微观转动模式识别依然高度敏感于平均场平衡形变输入。

## Extracted Pages

- PDF pp.1–3：引言、两主壳 PSM 公式（Eqs. 1–10）、Table I 形变与配对参数；
- PDF pp.4–5：SCM 模型公式（Eqs. 11–21）、101Pd 能谱与组态图（Figs. 2–3）；
- PDF pp.6–8：103,107–111Pd 与 103–111Cd 能谱及未投影能带交叉图（Figs. 4–8）；
- PDF pp.9–10：对齐角动量 $i_x$ 与波函数组态占据演化（Figs. 9–11）；
- PDF pp.11–13：$B(E2)$、$B(M1)$、$\mathcal{J}^{(2)}/B(E2)$ 系统学演化（Figs. 12–16）及 109Cd 同核 AMR/MR 共存（Fig. 17）；
- PDF pp.13–15：讨论、总结与 62 篇参考文献。

## Knowledge Impact and Learning Decision

- **Existing understanding:** Day 27 讨论了反磁转动（AMR）的四叶片剪刀机制及同核多模式共存。
- **Impact:** `supports` 提供了 A≈100 质量区 10 个核素最新、系统的微观投影壳模型（PSM）与半经典粒子-转子模型（SCM）联合基准；`limits` 证明即使在被认为纯粹的剪刀能带中，微观波函数也充满多准粒子组态混合，不应机械套用单剪刀无混合公式。
- **Persistence:** `source` 页面持久化；关联 `cross-mass-transferability-and-mechanism-inapplicability.md` 与 `multimodal-coexistence-and-phase-boundary-topology.md`。

## Agent Self-Audit Triage

- **P0: none identified.** 官方 DOI、arXiv 全文、哈希与元数据已全量交叉对账；未发现任何阻断项。
- **P1:** 微观波函数混合与半经典几何剪刀角的对应关系在论文中为定性讨论；未提供数字化多组态投影振幅表。
- **P2/P3:** citation_key 暂空；保持标准 schema 规范。
