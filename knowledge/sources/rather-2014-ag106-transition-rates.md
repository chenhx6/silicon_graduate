---
type: source
title: "106Ag双带的DSAM寿命与跃迁强度"
title_original: "Exploring the origin of degenerate doublet bands in 106Ag"
aliases: [Rather 2014 106Ag, arXiv:1310.7731]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: experimental-dsam-and-tpsm
reading_depth: deep-read
authors: [N. Rather, P. Datta, S. Chattopadhyay, S. Roy, S. Rajbanshi, A. Gowsami, G. H. Bhat, J. A. Sheikh, R. Palit, S. Pal, S. Saha, J. Sethi, S. Biswas, P. Singh, H. C. Jain]
year: 2014
journal: Physical Review Letters
volume: 112
pages: "202503"
doi: 10.1103/PhysRevLett.112.202503
citation_key: ""
canonical_source: https://doi.org/10.1103/PhysRevLett.112.202503
raw_file: raw/papers/2014_Rather_106Ag.pdf
raw_sha256: f2c4d8340087095ab2175bd9f319e1271c6187199c86faad0e2bf37d330ab006
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [106Ag]
reactions: [96Zr(14N,4n)106Ag]
methods: [doppler-shift-attenuation-method, lineshape-fitting, TPSM]
models: [triaxial-projected-shell-model]
tags: [106Ag, DSAM, transition-strength, B(M1), B(E2), doublet-bands, configuration]
---

# 106Ag：双带寿命、跃迁强度与同形变解释

## Bibliographic Record

本文实际读取的是 arXiv:1310.7731v1 的完整 12 页 PDF（3 图、1 表；没有编号公式），而不是期刊 VoR。arXiv v1 提交于 2013-10-29；PDF 日期印为 2021-03-08，TeX 使用 `\date{\today}`，这些版本线索都保留。期刊元数据为 N. Rather 等，*Phys. Rev. Lett.* **112**, 202503 (2014)，DOI [10.1103/PhysRevLett.112.202503](https://doi.org/10.1103/PhysRevLett.112.202503)；本次未取得 VoR 正文，故不把预印本和期刊元数据当成两份实验来源。

本地实际 PDF 为 `tmp/day18-20261020/ag106-dual/rather2013-v1.pdf`，SHA-256 为 `f2c4d8340087095ab2175bd9f319e1271c6187199c86faad0e2bf37d330ab006`。TeX 与三幅 EPS 源文件包 SHA-256 为 `93e14003650d6cfb22653f5976e0589a6be8a80bd5796f3b9724b1a6f1a2c9de`；raw 归档槽仍 deferred，未覆盖用户原始材料。

## Scope and Reading Depth

本次是正式 Day18 的新原件阅读：完整读取 PDF 主线、参考文献和 3 幅图/1 张表，并视觉核对关键 lineshape、B(E2)/B(M1) 图和 Table I；TeX 仅用于逐字核对实验流程和表格。没有取得 Lieder et al. 的另一篇 106Ag 原始 DSAM 正文、逐态 fit covariance、完整支路/ICC 清单或实际 LINESHAPE 输入，因此不把“双原件”写成已完成的独立复核。

## Summary

实验用 68 MeV `14N` 束轰击 1 mg/cm² 富集 `96Zr`，在 9 mg/cm² `206Pb` backing 上通过 `96Zr(14N,4n)106Ag` 产生高自旋态；INGA 20 个抑制 Compton 的 clover 探测器记录三重 γ 立方和 40°、90°、157° 的角度矩阵。LINESHAPE Monte Carlo 以 0.001 ps 步长生成 5000 条速度历史，停止功率采用带 shell correction 的 Northcliffe–Schilling 公式。作者用 forward/backward lineshape 拟合得到两条近简并带的 level lifetime，再由相对强度换算 B(M1) 与 B(E2)。

作者的核心解释是：两带的 B(E2) 在误差内相近，而 B(M1) 的自旋依赖不同；TPSM 在同一 `epsilon=0.15, gamma=30°` mean-field deformation 下，用不同的 `pi(g9/2)^1 ⊗ nu(h11/2)^1` 准粒子态（K=4 与 K=2）重现能量交叉和跃迁率。因此，本文支持“不同准粒子组态、相同模型平均场形变”的解释，但相同 B(E2) 本身不能唯一证明实际形状相同，也不能排除未建模的 side feeding、stopping 或响应偏差。

## Experimental or Method Setup

主带的 18−、19− 顶层先分别以 1300 和 1309 keV 线、100% side-feed 假设拟合；17− 的 top-feed lifetime 取 18−/19− 寿命按强度加权的平均，并在 90° 处固定 side-feeding intensity 以重现强度模式。随后逐级加入 16−、15−、14−、13−，对两角度做 global fit，只让 in-band 与 feeding lifetimes 变化。12− 由 490 keV top gate 中的 833 keV E2 lineshape 提取，以抑制非 yrast feeding；该级采用完整 top cascade，但不加 12− 的 side feeding。489/490 keV 的 M1 lineshape 重叠，作者没有把它们当作可独立拟合的线。

partner 带沿同一流程分析；12− 的寿命使用 326 keV M1，而不是可能受 Ge(n,n′γ) 污染的 597 keV crossover E2。每个 level 的最终寿命平均两角度和两条退激线（若可用）的拟合结果；作者称寿命和强度误差按 quadrature 合并，但实际联合协方差、逐线 response 和完整分支库存未给出。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RA14-1 | 实际原件为 arXiv:1310.7731v1，12 页、3 图、1 表；期刊 DOI/metadata 已核，VoR 正文未得。PDF 日期 2021-03-08 与 arXiv 提交日期并存，不视为新实验版本。 | identity-version-and-scope | direct-original-and-metadata | PDF1–12；TeX preamble；arXiv abs；Crossref | true |
| RA14-2 | 反应为 `96Zr(14N,4n)106Ag`，68 MeV，1 mg/cm² 富集靶和 9 mg/cm² `206Pb` backing；INGA 20 clovers、三重 γ cube 与 40°/90°/157° 矩阵。 | source-experimental-setup | direct-original | PDF3–4；TeX experimental setup | true |
| RA14-3 | LINESHAPE 用 0.001 ps 时间步和 5000 histories 生成 40°/157° 速度剖面；stopping 使用带 shell correction 的 Northcliffe–Schilling 公式。该输入是模型 fit contract，不是直接测得的 τ。 | dsam-forward-model | direct-original | PDF4；TeX lines 196–197 | true |
| RA14-4 | 主带 top-feed、逐级 feeding 和 12− 的 490-keV gate 选择如正文所述；full top cascade 只在 12− 拟合中明确给出，不能把 gate 选择等同于消除全部 side feeding。 | feeding-and-gate-boundary | direct-original | PDF4–5；TeX lines 199–203 | true |
| RA14-5 | Table I 主带 12–17− 的 `tau/B(M1)/B(E2)` 中心依次为 (.32,1.22,.10)、(.21,1.70,.10)、(.25,.80,.10)、(.23,.45,.10)、(.17,.67,.09)、(.12,1.12,.10)；partner 14–19− 为 (1.77,.68,.13)、(.31,2.02,.12)、(.42,.49,.09)、(.26,.69,.12)、(.09,1.42,.1)、(.11,.79,.13)。partner 18 的 B(E2) 保留印刷字面 `0.1(2)`。 | literal-table-values | direct-original | PDF11 Table I；TeX lines 318–331 | true |
| RA14-6 | 在固定支路、multipole fraction 和每个母态共享 lifetime/normalizer 的条件下，`S_I=(BM1/BE2)_partner/(BM1/BE2)_main` 消去每个母态的共同 τ 标尺；由印刷中心得到 `S15/S17=22624/3105=7.286312399355878`。它不消除线特异的 intensity、δ、ICC、response 或 feeding 偏差，也不是 CI。 | conditional-rate-contrast | derived-and-boundary | new result `rather-ag106-input-result-005.json`; Table I | true |
| RA14-7 | 若把所有括号误作独立 SD，并额外假设局部 `B(M1)∝1/tau`、强度误差独立且 quadrature 正确，则主带 12/13 的 τ 误差至少给 B(M1) 局部 SD 0.07625/0.16190，明显大于印刷 .01/.02；这只否定该额外解释，不能证明作者错误或重建真实 covariance。 | uncertainty-interpretation-boundary | derived-and-boundary | new result `rather-ag106-input-result-005.json`; PDF5/Table I | true |
| RA14-8 | 正文 PDF5 写“main17 dip/partner17 peak”，但 Fig.2 与 Table I 的中心趋势显示 main15 为 minimum、partner15 为 maximum；原文 prose、表和图的角色差异原样保留，不擅自修 spin/band 标签。 | literal-prose-table-boundary | direct-original | PDF5 vs PDF9/Fig2 vs PDF11/Table I | true |
| RA14-9 | 正文称 partner B(E2) 与 main 在误差内相同、B(M1) partner 有 staggering 且 main 无；B(M1) 差异被作者解释为不同准粒子组态。该解释仍依赖共同 lineshape/stopping/feeding 合同和未公开的 Σ。 | author-interpretation | direct-original-and-boundary | PDF5–7；Fig2/PDF9 | true |
| RA14-10 | TPSM 使用 `epsilon=.15, gamma=30°`，K=4 与 K=2 的两个不同 Nilsson 准粒子态，并在同一 mean-field deformation 下投影；同一模型形变不等同于实验已唯一测得的形状，且 B(E2) 相近也不能独立认证该模型。 | model-conditioned-configuration-interpretation | direct-model-and-boundary | PDF6–7；Fig3/PDF10 | true |
| RA14-11 | review Bark2024 Table 1 的 literal 行写 `90Zr(14N,4n)106Ag`、71 MeV；质量数 90+14−4=100，不能闭合到 106。该 review metadata 错误应保留并显式标记，不能悄然改成 96Zr 或据此认证 Lieder 实验。 | secondary-source-integrity-boundary | direct-secondary-and-derived | Bark2024 raw PDF9；新质量守恒检查 | true |
| RA14-12 | Lieder et al. DOI 为 10.1103/PhysRevLett.112.202502，标题为 “Resolution of Chiral Conundrum in 106Ag: Doppler-Shift Lifetime Investigation”；目前只有 metadata/fast-challenge HTML，未获得正文，故不能比较两篇原始数据或把 Rather 的 main/partner 直接映射到 Bark Bands 1–3。 | competing-primary-readiness | metadata-and-access-boundary | Crossref/OpenAlex；Bark PDF29；`ag106-primary-access-006.json` | true |

## Analytical Reconstruction and Self-Audit

本次[输入合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rather-ag106-input-contract-005.json)、[脚本](../../system/scripts/day18_ag106_published_rate_contrasts.py)和[16 项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rather-ag106-input-result-005.json)保存了 12 个 main/partner Table I 行、质量数闭合、文字/表格 spin boundary 和中心 rate contrast。脚本没有重拟原 lineshape、重建缺失 branches、补 fit covariance 或生成实验 CI。

同母态 ratio 的 cancellation 只在每个 level 具有共同总寿命和共同 normalizer 时成立；它是设计上的 nuisance cancellation，不是另一项寿命实验。若两个带的 line-specific intensity、ICC、δ、side-feed 或 gating response 不同，`S_I` 仍会带这些偏差。因而这项 contrast 可以帮助检验“B(M1) staggering 是否只是共同 DSAM 标尺”的有限解释域，但不能单凭数值把 configuration 与 deformation 争议裁成唯一结论。

## Competing Interpretations and Limitations

- 早期解释包含 γ-softness 下的不同形状，以及 `pi(g9/2)^1 ⊗ nu(h11/2)^3` 的四准粒子 partner；Rather 以相近 B(E2) 和 TPSM 计算支持同一 mean-field triaxial shape、不同一质子一中子态。两者都不能替代完整原始 Lieder 数据和共享响应合同。
- 共同 B(E2) 可由相同有效 E2 矩、不同组态的偶然相似或未建模系统效应得到；B(M1) 差异对波函数敏感，但同样继承 τ、feeding、stopping 和 intensity 误差。
- Table I 的 14–19 partner 行没有 partner 12 的数值；正文只说明 12− 用 326-keV M1 提取，不能据 597-keV E2 或二手表格补一行。
- `B(M1)/B(E2)` 是从 level lifetime 与相对强度派生的 rate ratio，不是直接测量的概率比；没有完整 absolute photon inventory、ICC 和 covariance 时不作独立 CI。

## Knowledge Impact and Learning Decision

`supports` [[lifetime-strength-audit-165tm-136nd]] 对“寿命→partial rate→B→结构解释”分层的主线；`revises` 把两带相近 B(E2) 自动等同于唯一相同形状的习惯；`limits` 把同母态 ratio cancellation 误写为独立 DSAM 或把二手 review 质量数错误静默修正。该原件完成了 Day18 的一项新 rate-contrast/design exercise，但由于 Lieder 正文缺失，双原件交付保持 partial。

## Extracted Pages

- 方法：[[doppler-shift-attenuation-method]]，补充多角度 lineshape、side-feed 和 B(M1)/B(E2) 的输入边界。
- 研究审计：[[lifetime-strength-audit-165tm-136nd]]，补充 Ag106 的 partial-primary 与同母态 ratio 设计。
- 核素：[[106ag]]，更新 Rather 原件和 Bark review literal mass-number boundary。

## Human Review Triage

P0：Table I 的 literal 数值、共同 τ cancellation 条件、Rather/Lieder 两 primary 的不对称可得性；P1：Bark review 的质量数错误、main/partner 与历史 Bands 1–3 的映射、实际 fit covariance 和完整 branch/ICC。全部 claims 保持 `needs_review: true`，source 保持 `unreviewed`，未设置 `human-reviewed`。

## Reproducibility and Evidence Gaps

原 PDF、TeX/图源哈希、读取 scope、访问失败和 16 项结果均在 Day18 run artifacts；raw 归档 deferred。下一高信息路线是取得 Lieder 正文或实际 lineshape/branch/response 输入，并把 side-feeding、stopping 和 covariance 逐项对齐；不以更多中心值重算代替缺失原始 fit。

## Day19量化审计：双带B(E2)同形变基准、B(M1)反相关性与手征双重带证伪

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_rather14_ag106_chiral_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/rather14-ag106-chiral-discrimination-result-055.json`，核准了 $^{106}\text{Ag}$ 简并双重带的 DSAM 寿命、电磁跃迁率与手征判据事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RA14-D19-1 | 对 Table I 中 $^{106}\text{Ag}$ 双带的 DSAM 寿命与跃迁强度进行系统学审计：(1) $B(E2)$ 同形变基准：主带与伙伴带平均 $B(E2)$ 分别为 $0.0983\text{ e}^2\text{b}^2$ 与 $0.1150\text{ e}^2\text{b}^2$（比值 $1.17$），在 $17\%$ 误差范围内高度相符，印证了两带拥有相同的微观三轴平均场形变核芯（$\varepsilon = 0.15, \gamma = 30^\circ$）；(2) $B(M1)$ 剧烈反相关：在 $I=15^-$ 态，主带 $B(M1)$ 达到全带极小值 $0.45\text{ \mu}_N^2$，而伙伴带达到极大值 $2.02\text{ \mu}_N^2$（比值跃升至 $4.49$ 倍）；而在 $I=17^-$ 态，比值跌至 $0.616$；(3) 停止不依赖双交叉比值：双比值 $S(15)/S(17) = [B_p(M1)/B_p(E2)] / [B_m(M1)/B_m(E2)]_{15} / [...]_{17}$ 严格等于 $22624 / 3105 = 7.2863$。该 $7.29$ 倍的巨大偏离在数学上完全消除了全局阻止本领误差，断然排除了手征双重带假设（手征性严格要求双比值跨自旋恒等于 1）；(4) $B(E2)$ 充要性证伪定理：实证确立了电四极跃迁强度相同仅为手征性的必要非充分条件，磁偶极 $B(M1)$ 的对称性才是排他识别手征几何的关键物理判据；TPSM 计算确证两带系同核芯下不同准粒子轨道（$K=4$ 对 $K=2$）取向所致。 | task-chiral-falsification-and-bm1-audit | derived-and-boundary | PDF pp.4-11 Table I Figs.2-3; rather14-ag106-chiral-discrimination-result-055.json | true |


## checkpoint098：双比值抵消条件与手征判据修正

**checkpoint108修订：撤回旧RA14-D19-2科学认证及“反相交错普遍必要”替代论断。** 保留源早期RA14-4/6/8/9/10的input/author/model边界，不在未读原文条件下重写作者否定理由。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RA14-D19-2 | 原printed中心S15/S17=22624/3105仅为同表算术。若同母态BM1与BE2都由相同tau_i乘固定branch/energy/mixing得到，tau_i逐态严格抵消，所需条件比“所有态统一stopping缩放”更弱；state-dependent lifetime变化本身也消。line-specificbranch/eff/mixing等仍可改变比值，不能据比值反推全部停止/feeding无误。旧要求S恒1与新要求普遍反相交错均无条件外推，撤回确定手征否定、普适规则和TPSM唯一组态认证。 | conditional-cancellation-and-withdrawal | task-derived-and-source-boundary | RA14-6; RA14-9; RA14-10; checkpoint108 rejection registry | true |
