---
type: source
title: "Roy et al. 2011 - Systematics of antimagnetic rotation in even-even Cd isotopes"
aliases: [Roy 2011 110Cd antimagnetic rotation, Roy 2011 PLB Cd systematics]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: experiment-and-theory
reading_depth: deep-read
title_original: "Systematics of antimagnetic rotation in even–even Cd isotopes"
authors: [Santosh Roy, S. Chattopadhyay, Pradip Datta, S. Pal, S. Bhattacharya, R. K. Bhowmik, A. Goswami, H. C. Jain, R. Kumar, S. Muralithar, D. Negi, R. Palit, R. P. Singh]
journal: "Physics Letters B"
year: 2011
volume: 694
pages: "322-326"
doi: "10.1016/j.physletb.2010.10.018"
citation_key: Roy_2011_PLB
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-10-28
canonical_source: "Roy et al., Phys. Lett. B 694, 322 (2011)"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/roy-2011-cd110-systematics-plb.pdf"
raw_sha256: "2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a"
nuclei: [110Cd, 106Cd, 108Cd]
reactions: [96Zr-18O-4n]
experiments: [INGA, DSAM-lineshape]
models: [classical-particle-plus-rotor, AMR-plus-core-rotation, two-shears]
observables: [level-lifetime, BE2, dynamic-moment-of-inertia, alignment]
methods: [DSAM, lineshape-analysis, gamma-gamma-coincidence]
tags: [110Cd, antimagnetic-rotation, DSAM, shears-mechanism, even-even-Cd]
---

# Systematics of antimagnetic rotation in even–even Cd isotopes

## Bibliographic Record

- S. Roy *et al.*, *Phys. Lett. B* **694**, 322–326 (2011), DOI `10.1016/j.physletb.2010.10.018`.
- 规范文件：`raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/roy-2011-cd110-systematics-plb.pdf`（5 页，SHA-256 `2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a`）。

## Scope and Reading Depth

- 全文 5 页精读（pp. 322–326）：实验测量（`96Zr(18O, 4n)110Cd` 反应，70 MeV，INGA 阵列 18 叶 clover 探测器，LINESHAPE 寿命分析）、Table 1 寿命与 B(E2) 提取、经典两粒子加转子模型公式（Eqs. 1–6）、`106,108,110Cd` 系统学对比与总结。
- 局限与未覆盖：阻止本领（stopping power）系统误差未计入拟合误差（原文注明可能达 20%）；高自旋 26+ 及以上仅得到顶层有效寿命。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RO11-1 | 测得 110Cd 准基态能带 16+ 至 24+ 态平均寿命分别为 tau = 0.36(3)、0.23(3)、0.17(3)、0.21(7) 和 0.27(7) ps；对应带内 E2 跃迁强度呈现自旋上升下的稳步平缓下降：B(E2) = 0.14(1)、0.12(2)、0.11(2)、0.09(3) 和 0.06(2) (eb)^2。 | experimental-fact | direct | p.324, Table 1 | true |
| RO11-2 | 与邻近偶偶核 106,108Cd 的“纯反磁转动”（核心惯量 Im=0）不同，110Cd 的高自旋反磁转动由对称双剪刀机制与核心集体转动共同驱动，核心转动惯量采用并由I(ω)比较支持 Im = 19.5 MeV^-1 hbar^2（约半刚体转子值）。 | model-interpretation | contextual | pp.325-326, Fig. 4 | true |
| RO11-3 | 核心转动与双剪刀闭合的耦合自然解释了 110Cd 在 hbar omega = 0.65–0.72 MeV 处出现的 8 hbar 顺对齐增益，以及 B(E2) 未发生骤降而是在 0.06–0.14 (eb)^2 维持平缓过渡平台的实验事实。 | model-result | contextual | pp.325-326, text and Fig. 4(b) | true |
| RO11-4 | 原Table1的110Cd跃迁初态16、18、20、22、24对应1075、1224、1323、1314、1358keV。旧116–341是选择部分ENSDF区间并以端点B配比所得，非原表报告的完整范围，撤回其直接测量认证。 | source-correction | direct | p.324 Table1；见下述有限差分边界 | true |

| RO11-VPN-01 | 108Cd、106Cd的I(ω)比较采用Vπν=1.2 MeV；110Cd将该值固定，作者总结三核均取1.2 MeV。随N变化的主要显式输入是jν、n和核芯响应，而不是本论文测出Vπν随N单调变化。 | model-input-and-author-summary | direct-original | printed324–326 Eqs3–6、Fig3及结论 | true |

## Summary

Roy et al. (2011) 报告了 110Cd 高自旋能级的多探测器 DSAM 线形寿命分析与反磁转动系统学研究。实验确立了 16+ 至 24+ 能级的寿命与递减的 B(E2) 跃迁几率，并用经典粒子加转子模型支持以下解释：110Cd 属于双剪刀反磁转动与核心集体转动耦合的典型案例，成功解释了其转动惯量大、顺对齐增益显著以及 B(E2) 平缓过渡的独特性质。

## Competing Interpretations and Limitations

- 实验提取的能级寿命直接依赖阻止本领数据库，存在约 20% 的系统不确定度包络。
- 经典的粒子加转子模型中，粒子-空穴排斥互作用参数 V_pinu ~ 1.2 MeV 与空穴-空穴互作用参数 V_pipi ~ 0–0.2 MeV 属于唯象参数，未包含三维微观自洽平均场形变自适应涨落。
- 跃迁能量接近的 1323 与 1314 keV 线形存在重叠，需借助门控矩阵解耦，高自旋端有效侧馈寿命存在模型假设。

## Model Dependence

模型采用两对称剪刀闭合几何 I = j_p + 2 j_h cos(theta)，其中质子空穴 pi(g9/2)^-2 构成剪刀双叶，两对准中子 nu(h11/2)^2 对齐于转动轴。电四极跃迁几率正比于 sin^4(theta)。核心集体转动对频率的贡献由 omega = omega_rot - omega_sh 给出。

## Knowledge Impact and Learning Decision

- Effect: `supports` [[antimagnetic-rotation]]、[[shears-mechanism]] 与 [[octupole-mr-amr-evidence-gradient]]；为 110Cd 提供第一手实验寿命与 B(E2) 原始依据。
- Review state: Codex self-audited; not `human-reviewed`.

## Extracted Pages

- [[amr-vpinu-neutron-number-core-polarization-audit]]

- Concepts/notes: [[antimagnetic-rotation]], [[shears-mechanism]], [[octupole-mr-amr-evidence-gradient]].

## Sources

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

Codex source self-audit; all new claims retain `needs_review: true`.

## Day26 原件重读与派生量复核

本段重新核验本地5页PDF的签名、页数与SHA，全文阅读pp322–326，Table1和Eqs1–6定向复核；未取得LINESHAPE输入、逐门计数、阻止本领与feeding联合协方差，不声称重放实验拟合。

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
| --- | --- | --- | --- | --- | --- | --- |
| RO11-D26C-001 | 106Cd在18–24的B(E2)为0.15(1)、0.14(2)、0.07(1)、0.05(1)；108Cd在16–22为0.15(1)、0.14(1)、0.09(1)、0.03（末点effective lifetime）；不能替换成013中的0.42或0.28起始值而仍归本表。 | experimental-fact | direct | single | p324 Table1及脚注a | true |
| RO11-D26C-002 | 110Cd最高26/28的1443keV线重合，顶端只取effective feeding lifetime。作者认为最高28+不由AMR产生；原文没有“同一纯AMR配置已延伸到28+”的认证。 | author-interpretation | direct | single | p323测量段；p326首两段 | true |
| RO11-D26C-003 | 邻接Eγ差为149、99、−9、44keV，按4/ΔEγ得26.85、40.40、−444.44、90.91 ħ²/MeV。负值源于1323→1314的回弯，应保留并标示平滑转子近似失效，不能无提示删掉。 | our-inference | contextual | single | p324 Table1打印中心；022条件代数 | true |
| RO11-D26C-004 | 频率取Eγ/2、位于跃迁平均自旋I−1，则上述导数中心为16、18、20、22。若配以相邻B(E2)算术平均0.130、0.115、0.100、0.075，得到有单位的比值206.5、351.3、−4444.4、1212.1。这是明列插值的练习，并非原表测量或新的AMR阈值。 | our-inference | contextual | single | 同Table1；022频率/自旋约定 | true |
| RO11-D26C-005 | 用纯E2、单位分支、忽略内转换的0.0816/(Eγ^5τ)得到0.1579、0.1291、0.1184、0.0992、0.0654，与表列0.14、0.12、0.11、0.09、0.06不严格相等。未取得转换/分支输入前保留这个差别，不凭假设改作者表值。 | our-inference | contextual | single | p324 Table1；022条件寿命换算 | true |
| RO11-D26C-006 | 19.5 ħ²/MeV是本模型采用约半刚体值；原文描述shears和core约各8ℏ的增量贡献，与013称总自旋分担18%–26%不是同一量。013未再现平台，不能认证其参数为原作者生产复算。 | model-result | direct | single | p325–326 Eqs3–6、Fig4与文字 | true |

`revises`旧RO11-4直接范围认证；`supports`实测B(E2)缓降和作者AMR+core解释，`limits`无单位比值、跨自旋错配与最高态过度外推。可复用反例见 [[day26-quantitative-claim-corrections]]。

### ENSDF 分支与平均寿命的后续核对

[[nndc-2012-cd110-adopted-lifetimes-branches]] NC110-1–4保留同一2011Ro01实验谱系的评价字段。评价半衰期0.250、0.159、0.118、0.15、0.19ps除以ln2，分别约为0.3607、0.2294、0.1702、0.2164、0.2741ps，与本Table1平均寿命对应；因此当前7%–11%的B中心差异不是半衰期/平均寿命混用。五条E2的评价内转换约6.3–9.7×10^(−4)，也不足以独自解释该差别。

22+在评价中另有1100keV RI=37(11)支线，而评价明确记载本实验未在符合门确认它。不能把评价保留的该支线插入本Table1后宣称复现或更正。023对打印B误差与τ传播误差的独立合成只作条件尺度；两者同源且协方差未知，不构成正式显著性检验。归一成因仍待原作者逐门和换算输入。
