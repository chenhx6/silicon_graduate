---
type: project
title: 131Ce/133Ce 集体模式判别
aliases: [131Ce collective-mode discrimination]
created: 2026-07-27
updated: 2026-09-29
status: active
review_status: unreviewed
project_stage: l4-milestone-awaiting-review
confidentiality: private
nuclei: [127xe, 129ba, 131ce, 133ce, 131xe, 131ba]
tags: [l3, a130, collective-modes, evidence-map, candidate-l4, n73-isotones]
---

# `131Ce/133Ce` 集体模式判别

## Agent active summary

- 当前排序不变：`131Ce` Bands 1–7 仍以 signature/configuration coupling 为首选，γ-soft core response 是模型辅助背景，wobbling/chirality 未获目标核电磁闭合链支持。
- 2026-08-17 同中子素核验补入两个配置特异控制：Ding 2021 的 N=73 `129Ba/131Ce/133Nd` `[404]7/2+` 系统学支持正宇称组态连续性；`127Xe/129Ba` 的 `h11/2` wobbling 候选只证明邻核机制可行。
- 关键独立性边界：Ding 的 N=73 行是旧实验汇编；`129Ba` 是 legacy-data reanalysis 且沿用 `127Xe` 判据，均不能计为新的 `131Ce` 实验。
- 2026-08-19 locator audit 将 Ding 的 N=73 证据定位到 Figs.4-6，并确认 `129Ba/131Ce/133Nd` 数据分别来自 refs.46/47/48；三篇原始全文仍未进入本轮核验。
- 2026-09-26 continuation audit 已取得并全文核对 refs.47/48：Palacz 1991 `131Ce` 原始高自旋谱学与 Bazzacco 1998 `133Nd` GASP/DCO 谱学；Byrne 1992 `129Ba` 仍为 closed/full-text blocked。两篇新 source 页只加强 contextual configuration continuity，不增加 `131Ce` target-nucleus electromagnetic evidence。
- 下一决定性步骤仍是 `131Ce` 连接跃迁的 measured `δ`/偏振、多带寿命和 absolute strengths。
- 2026-09-27 electromagnetic-manifest audit：Alwaleedi 2013 只有 `δ=0` 派生 `B(M1)/B(E2)`，Singh 2016 与 Li 2004 提供独立但带/宇称范围不同的寿命与 `Q_t`，Petrache 1998 的 `Q0=7.3(4) eb` 属于独立 HD 带；这些来源没有形成 Bands 1–7 的 measured `δ`、偏振和 partner-resolved strength matrix。Crossref/Semantic Scholar 只核验 Gizon 1977 `131Ce/129Ce` 论文身份（DOI `10.1016/0375-9474(77)90679-0`）；OpenAlex 标为 `is_oa=false` 且无 PDF/repository copy，Unpaywall 为 `oa_status=closed` 且无 locations，Semantic Scholar 为 `CLOSED` 且无 abstract；ScienceDirect/CORE 公开请求返回 403。全文与 locator 仍 blocked，暂不纳入科学证据。

## Research Question

以 [[alwaleedi-2013-band-structures-131ce]] 的 Bands 1–7 为 `131Ce` 结构基线，结合 [[ionescu-bujor-1998-static-moments-129-131ce]] 的 `129,131Ce` TDPAD moments/PTR shape anchor，`131Ce/133Ce` 及必要邻核的公开证据最支持哪种形变背景与集体模式？wobbling、chirality、signature-partner/configuration coupling、γ-soft 粒子—芯耦合和 shape coexistence 中哪些仍可行，缺少哪些 observable 阻止裁决？

范围限定：

- 本 milestone 比较已摄入的直接实验来源与模型解释，不把相邻核标签倒灌到 `131Ce`；
- 本轮 L4 只使用用户提供的公开论文数据；用户独立 `131Ce` 实验数据未读取、未推断、未合并。

## Current Hypotheses

| 排序 | 假设 | 当前状态 | 核心理由 | 会改变排序的证据 |
|---|---|---|---|---|
| 1 | signature-partner/configuration coupling 叠加 spin-dependent core response | provisionally preferred | `131Ce` 有完整 crossing/alignment/configuration 链；未出现要求新集体 phonon 的必要证据 | 精确连接跃迁 δ/偏振和寿命显示强集体带间 E2 |
| 2 | γ-soft particle-core coupling / 随自旋变化的非轴响应 | viable model-assisted background | Band-1-like 寿命/`Q_t` 直接约束 E2 集体性与芯响应；γ-soft 标签主要来自 TRS/作者解释，且四个有限点的加权斜率不足 1σ | 更完整的多带 `Q_t`、measured δ/偏振及统一 soft-vs-rigid 模型计算 |
| 3 | chirality | viable for selected `133Ce` pairs; unsupported for `131Ce` baseline | `133Ce` 两组候选有同宇称 links、能量与 ratio fingerprints，但缺 lifetime；`131Ce` 没有等价闭合链 | 同组态双带的 absolute B(E2)/B(M1)、interband transitions 与几何一致性 |
| 4 | shape coexistence | plausible nuclear-level candidate; unestablished for thesis Bands 1–7 | `131Ce` 独立 HD 带有 `Q0=7.3(4) eb`，证明同核存在更高形变尺度；没有证据把它与 thesis Bands 1–7 连接成共存伙伴 | HD–ND links、decay-out、E0/invariants 或共同 PES/配置验证 |
| 5 | wobbling | not supported for current `131Ce` bands | 没有相邻 phonon band identity、enhanced out-of-band E2、可靠 δ/偏振或 wobbling geometry | 明确的 ΔI=1 collective E2 links、B(E2)out/B(E2)in 和一致的 E_wob/角动量几何 |

关键合并判断：`signature/configuration coupling` 描述带身份机制，寿命/`Q_t` 约束 E2 集体性与芯响应，TRS 则提供 γ-soft/非轴形变解释；三层不能互相替代。当前最节约假设的组合是“组态耦合主导、芯响应随自旋或组态变化”，而 γ-soft 是可行但模型辅助的背景，不是寿命独立证明的性质，也不是已经证明的 chirality/wobbling。

## Evidence Available

### 证据地图

| 证据 | 支持 | 限制/反证 | 独立性与权重 |
|---|---|---|---|
| `131Ce` Bands 1–7 的 coincidence、angular ratios、crossings、alignments 与 Table 5.3 组态图 | signature/configuration coupling；spin-dependent core response | `B(M1)/B(E2)` 采用 `δ=0`；无 lifetime/absolute B(E2)/polarization；Table 5.1 Band 2 parity 有 probable typo/source conflict；Table 5.3 对 Band 5 两个低自旋 signature 分量都给出高自旋 `e⊗AEFG` | 目标核直接来源，当前最高权重；[[alwaleedi-2013-band-structures-131ce]] AW13-1–13；2026-08-11 用户审核要求按原表使用，不作 `f⊗AEFG` 重映射 |
| **`131Ce` electromagnetic-manifest audit (2026-09-27)** | AW13-9 `δ=0` branching-derived ratio；SI16-1 与 LI04-1/LI04-3 的 yrast/parity-specific lifetimes；PE98-7 独立 HD `Q0` | 直接数据、派生比值、模型解释和缺失 companion 已分栏；有限 `Q_t` 只能约束 E2 集体性/芯响应 | 未发现同一 Bands 1–7 manifest 的 measured `δ`、偏振、partner-resolved absolute `B(E2)/B(M1)` 或完整 interband matrix；Gizon 1977 因全文/locator 缺失不纳入 | 2013、2016、2004、1998 是不同实验谱系但覆盖不同带/方法；不能按论文数合并为 partner evidence；[[alwaleedi-2013-band-structures-131ce]]、[[singh-2016-lifetime-131ce-133pr]]、[[li-2004-lifetimes-131ce]]、[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] |
| `131Ce` 负宇称 yrast/Band-1-like 序列的 RDDS/DSAM 寿命与 `Q_t` | normal-deformed E2 集体性与芯响应的正交约束；不独立证明 γ-softness | 四个有限点的加权斜率 `−0.030±0.047 eb/ℏ`，不足以建立显著下降；Li 2004 的 limits/effective points 不进入同权 finite-point trend；γ-soft/具体 γ 仍来自 TRS 和作者解释 | [[singh-2016-lifetime-131ce-133pr]] 与 [[li-2004-lifetimes-131ce]] 是独立实验；Singh 表内转载的 Li 行不重复计权；不以简单加权平均裁决两者 |
| `131Ce` 独立 HD band 的 `Q0=7.3(4) eb` | 同核存在强形变序列，提升多极小/shape-coexistence 可行性 | 与 normal-deformed `Q_t` 的几何和 band identity 不同，不能直接合并或认作共存伙伴 | 独立来源；[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] |
| `133Ce` 两组候选伙伴带的同宇称 links、S(I)、relative `B(M1)/B(E2)` 与 RMF+TPRM | chirality 和不同三轴极小/shape coexistence 的作者解释 | 无 lifetime；TPRM 有 moment-of-inertia 调整和 Coriolis attenuation；模型未完全再现 staggering | 同一数据集的实验+模型链，不是独立多源确认；[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] A13-3–13 |
| `133Ce` 2016 完整中高自旋谱学地图 | 多组态竞争、显著三轴模型背景、不同轴/倾斜轴转动 | 旧 Q5/Q7 近简并 signature-partner 解释被新 links 推翻；弱带头和模型匹配非唯一 | 结构更新价值高，但部分复用 2013 数据；[[ayangeakaa-2016-133ce-in-beam]] A16-1–6 |
| `131Ba/133Ce` N=75 signature splitting 的 PES/CSM/QTR | 非轴形变与低-j Coriolis mixing 可共同产生 splitting | S(I) 不是 γ 的单值测量；模型 γ 约定与 attenuation 依赖 | 对机制有直接比较价值，但对 `131Ce` 仅同位素/邻核迁移；[[ding-2021-131ba-133ce-signature-splitting]] D21-1–7 |
| N=73 `129Ba/131Ce/133Nd` 的 `νg7/2[404]7/2+` 系统学 | 正宇称序列的 similar initial alignment/`J^(2)` 与高自旋延伸支持 configuration continuity | 该比较不测得 `131Ce` orbital content，也不把 splitting 反演为唯一 γ；三核原始 band crosswalk 仍需逐来源核验 | Ding 2021 汇编旧实验，属于 target-relevant contextual evidence，不增加独立 `131Ce` 数据集；[[ding-2021-131ba-133ce-signature-splitting]] D21-8, PDF pp.5-6/Figs.4-5, p.9/Fig.6；三核分别归于 refs.46/47/48 |
| **N=73 original-source audit (Palacz 1991/Bazzacco 1998)** | Palacz `131Ce` NORD-BALL 五带纲图、约 `51/2` 高自旋延伸、`g7/2` 正宇称作者指认；Bazzacco `133Nd` GASP DCO/decay-pattern assignments、band-9 `[404]7/2` alignment context | 两篇原始来源仍有不完整 linking、模型/assignment 依赖与 DCO convention 边界；Byrne 1992 `129Ba` 全文不可得，不能用 Ding caption 代替 | [[palacz-1991-high-spin-131ce]] PAL91-1–6；[[bazzacco-1998-rotational-bands-133nd]] BAZ98-1–8；两页只核验 refs.47/48，不能闭合 refs.46 或提升 `131Ce` target electromagnetic evidence |
| N=73 `127Xe/129Ba` 的 `νh11/2` wobbling 候选 | 证明同中子素链中 wobbling 机制可行，并给出 E2-dominant link 应满足的必要判据 | `127Xe` 二声子链有异常 decay topology，651/652-keV 区域受污染；`129Ba` 只有 365-keV link 的 A22/A44/偏振闭合较强，其余 links 缺 A44/完整偏振且作者要求新测量 | 两核实验数据不同，但 `129Ba` 是 legacy-data reanalysis、沿用 `127Xe` 指纹和相近作者解释谱系；只能作机制控制，不能替代 `131Ce` target links；[[chakraborty-2020-multiphonon-longitudinal-wobbling-127xe]] CH20-2–7；[[chakraborty-2024-possibility-wobbling-129ba]] CH24-2–6 |
| `131Xe` wobbling vs unfavoured signature partner 反例 | 小 δ/M1-dominant links 可排除具体 wobbling assignment；建立电磁优先判据 | 不能证明整个核区无 wobbling；弱 transition δ 有系统误差 | 邻核方法学反证；[[chakraborty-2023-131xe-wobbling-origin]]、[[wobbling-vs-signature-partner]] |
| γ-soft IBFM 对若干 odd-A 非 yrast bands 的替代解释 | γ-soft particle-core coupling 不需预设 wobbling phonon即可生成低能带 | 模型参数、band matching 与部分异常 δ 敏感；没有新实验 | 理论替代机制，不能单独裁决目标核；[[nomura-2022-questioning-wobbling-ibfm]] |

### 证据依赖审计

1. `133Ce` 的 MχD、shape-coexistence 与后续谱学地图并非完全独立，因为共享或继承同一批 Gammasphere 数据和 band assignments。
2. Singh 2016 Table 1 转载/再算 Li 2004 行；证据计数以原始实验谱系为单位，不按表格行数增加独立性。
3. `131Ce` thesis 的 configuration map 与 `B(M1)/B(E2)` comparison 共享模型输入，不能当作两条完全独立证据。
4. `131Xe/131Ba/133Ce` 同量异位素/同位素比较只检验机制可行性；它不能替代目标核的电磁 observable。
5. 模型给出的 γ 值使用不同参数化、轴约定和可调量，不能直接平均为“真实 γ”。
6. Ding 2021 的 N=73 `129Ba/131Ce/133Nd` 行直接涉及目标核，但来自 refs.46/47/48 的旧实验汇编；证据内容有用，独立实验计数不增加。当前只核对 Ding 的引用归属，不等于三篇原始论文已完成 claim-level verification。
7. `127Xe` 与 `129Ba` 是不同 N=73 数据集，但 2024 `129Ba` 工作复用旧数据并显式借用 `127Xe` 的 fingerprint/QTR comparison；实验谱系与解释谱系必须分开计数。

### 可区分预测矩阵

| 解释 | 若成立应优先看到 | 当前 `131Ce` 状态 |
|---|---|---|
| signature/configuration coupling | 同组态 signature 序列、可解释 splitting/crossing、links 以 M1 或普通 mixed M1/E2 为主 | 前两项较强；连接跃迁 δ/偏振不足 |
| γ-soft particle-core coupling | γ-sensitive staggering 与多带谱可由同一软芯参数描述，E2 分支随 core collectivity 有一致趋势 | 已有 Band-1-like `Q_t` 尺度，但未建立显著自旋趋势；这些寿命不独立判定 γ-soft，具体 γ 仍依赖 TRS；缺目标核多带统一计算 |
| wobbling | 明确 n_w→n_w−1 的 enhanced out-of-band E2、可靠 δ 与 B(E2)out/B(E2)in、合理 E_wob | 目标核未建立；N=73 `127Xe/129Ba` 只证明机制可行，不能填补 `131Ce` link/strength 缺口 |
| chirality | 同组态近简并 ΔI=1 双带、相似 intraband B(M1)/B(E2)、可解释 interband transitions 与手征几何 | `133Ce` 部分满足；`131Ce` 未建立候选对 |
| shape coexistence | 不同带有可重复的不同 Q_t/绝对 E2 或 invariants，并有受控配置/混合证据 | `131Ce` 有独立 HD 大矩尺度，但缺 HD–ND linking/mixing；未建立 thesis 带间 coexistence |

### `131Xe` mechanism-control transfer boundary (design-only)

`131Xe` C23 提供邻核方法学控制：C23-2 的 671/882-keV links 的 `δ≈0.03(3)/0.09(8)` 与 1055-keV `δ≈0`、C23-3 的小 E2 admixture/M1-dominant interpretation、C23-7 的“未发现 wobbling 实验信号”共同说明三轴模型参数不等于 wobbling 观测。该控制可迁移为 falsifier 逻辑（低 E2/M1-dominant links 会降低 wobbling ranking），但不迁移为 `131Ce` 实验证据；目标核仍需自己的 `δ`、偏振、linking 和 absolute-strength rows。

### `131Xe`–`131Ce` manifest contrast (design-only)

| 字段 | `131Xe` C23 control | `131Ce` AW13 target | transfer rule |
|---|---|---|---|
| direct mixing/polarization | C23-2 reports `δ≈0.03(3), 0.09(8), ≈0` and C23-3 interprets small E2 admixture | AW13-9 remains `δ=0` assumption; AW13-11 records no direct δ/polarization | transfer the test condition, not the value |
| partner identity/linking | C23-1/C23-6 define a proposed unfavoured partner but retain unresolved yrast `13/2−` origin | AW13-1/AW13-2 provide provisional Bands 1–7 identity/linking | each nucleus needs its own linking matrix |
| wobbling falsifier | C23-7: no wobbling signal; M1-dominant links weaken wobbling assignment | target evidence missing; wobbling remains unsupported | use as competing prediction only |
| model shape | C23-4 TPRM `γ=33°` is a model fit | AW13/SI16 γ values are model/interpretation | never copy fitted γ between nuclei |

The contrast is a protocol transfer, not cross-nucleus evidence pooling.

### `135Pr` branch-degeneracy method control (design-only)

`135Pr` supplies a second method control for the `131Ce` manifest. Matta M15-4/M15-5 report large-`|δ|`, E2-rich links and positive polarization; Lv L22-3/L22-4/L22-5 show that angular-distribution fits can retain large/small branches and that joint `P-R_ac` selects small-`|δ|`, M1-dominant solutions; Guo GU21-2/GU21-3 warns that the reported polarization sign alone cannot choose the large branch. The transferable rule is to require common response, polarization magnitude and angular-correlation treatment before treating a `δ` branch as a mode discriminator. The `135Pr` values and band labels remain nucleus-specific.

Sources: [[matta-2015-transverse-wobbling-135pr]], [[lv-2022-evidence-against-wobbling-135pr]], [[guo-2021-comment-transverse-wobbling-135pr]]. Guo is a methodological comment on Matta, not an independent experiment; Lv is an independent JUROGAM II data set.

#### Branch-to-E2 fraction cross-check (design-only)

For the convention `δ=E2/M1`, the E2 fraction is `f_E2=δ²/(1+δ²)`. Matta reports the E2 fractions directly; applying the formula to Lv's small-branch `δ` values gives the central fractions and endpoint ranges below.

| Data set / transition | `δ` branch | `f_E2` | Evidence note |
|---|---:|---:|---|
| Matta 747.0 keV | `−1.24(13)` | `60.6(5.1)%` | M15-4, source-reported fraction |
| Lv 747.3 keV | `−0.47(+0.09/−0.22)` | central `18.1%`; endpoint range `12.6–32.3%` | L22-4/L22-5, independent `P-R_ac` branch |
| Matta 812.8 keV | `−1.54(9)` | `70.3(2.4)%` | M15-4, source-reported fraction |
| Lv 813.2 keV | `−0.37(+0.10/−0.14)` | central `12.0%`; endpoint range `6.8–20.6%` | L22-4/L22-5, independent `P-R_ac` branch |
| Matta 754.6 keV | `−2.38(37)` | `85.0(4.0)%` | M15-4; no matched Lv row asserted here |
| Lv 450.2 keV | `−0.31(+0.10/−0.13)` | central `8.8%`; endpoint range `4.2–16.2%` | L22-4/L22-5; separate link, not the 754.6-keV transition |

The 747/813 point estimates indicate a large-branch versus small-branch interpretation contrast, but these values are not pooled: the campaigns, detector responses, gates and analysis pipelines differ, and Guo's comment reuses Matta's report. This is a branch-sensitivity example, not a common-response significance test or a `131Ce` result.


### `131Ce` next-measurement information-gain ranking (design-only)

该排序是实验设计启发式，不是对现有数据的统计结果。每项按 `discrimination`（能排除多少竞争解释）、`gap`（当前缺口程度）和 `feasibility`（相对可实施性）各给 1–3 级；总分只是排序工具，不能替代响应、协方差或 beam-time 评估。

| 优先级 | 测量包 | discrimination | gap | feasibility | 设计理由 | 支撑 locator |
|---|---|---:|---:|---:|---|---|
| 1 | 连接 `ΔI=1` 跃迁的 measured `δ` + 线偏振 | 3 | 3 | 2 | 直接释放 AW13 的 `δ=0` 假设，区分普通 signature/configuration links 与 wobbling/chirality 所需的 E2/M1 pattern | AW13-9, AW13-11, AR-4 |
| 2 | 同一 Bands 1–7 manifest 的 partner-resolved lifetimes + absolute `B(E2)/B(M1)`/`Q_t` | 3 | 3 | 2 | 将 SI16/LI04 的非 partner E2 controls 变成同带、同口径的 collective-strength test；检验 out-of-band E2 与 core-response排序 | SI16-1, LI04-1, LI04-3, SI16-7 |
| 3 | 完整 interband linking、band identity 和 common transition matrix | 3 | 3 | 2 | 先解决 pairing/identity ambiguity，避免把 crossing、signature partner、wobbling phonon 或 HD–ND 序列误配 | AW13-1, AW13-2, LI04-11, PE98-13 |
| 4 | quadrupole invariants/Coulomb excitation 或统一 soft-vs-rigid model comparison | 2 | 3 | 1 | 对 γ-soft、shape coexistence 和 HD–ND 关系提供形变敏感量，但所需装置/数据和模型协方差更重 | PE98-7, PE98-13, AW13-11 |
| 5 | g-factor、转移/反应选择性及 configuration-sensitive probes | 2 | 2 | 1 | 可降低 orbital/configuration ambiguity，但单独不能建立 partner electromagnetic symmetry | AW13-8, AW13-11, SI16-14 |

最小可执行组合是优先级 1 + 2 + 3；优先级 4 用于 shape question，优先级 5 用于组态确认。该组合保持“identity → transition character → absolute strength → model comparison”的顺序。

### `131Ce` band/transition manifest contract (design-only)

在取得新数据或合法全文前，任何 L3/L4 复核都先填以下字段；空字段保持 `missing`，不得用模型值或相邻核代理填充。

| 字段 | 必填内容 | 当前公开状态 | 失败/阻断检查 |
|---|---|---|---|
| `source_lineage` | DOI/raw hash、反应、阵列、共享数据关系 | AW13、SI16、LI04、PE98 分开记录 | 同一实验转载不得重复计数；无 hash/locator 则停在 discovery |
| `band_level_identity` | band ID、`E_x`、`J^π`、初末态、linking path | AW13-1/AW13-2 可作 provisional identity | parity conflict、duplicate configuration 或缺 linking 时标为 `identity-uncertain` |
| `transition_observable` | `Eγ`、强度及误差、multipolarity、`δ` 及误差/分支、偏振 | AW13-9 只有 `δ=0` 派生比值；direct `δ`/polarization missing | `δ=0` 假设未释放、polarization sign 未标定或 gate 不同则不得比较 |
| `strength_lifetime` | `τ`、side-feeding、absolute `B(E2)/B(M1)`、`Q_t`、限值语义 | SI16/LI04 是非 partner controls；PE98-7 是独立 HD | limit/effective 与 finite point 分开；不同 band/几何不得合并 |
| `linking_identity` | interband links、共用初态/末态、partner candidate | AW13 有部分 linking，partner matrix 未闭合 | 缺 identity 或 shared transition matrix 时禁止 mode label |
| `response_covariance` | efficiency/response、calibration、sorting/fit covariance、negative controls | 当前 source pages 未提供完整 package | 缺 response/covariance/code 不进入 L4 proxy fit |
| `model_comparison` | CSM/QTR/PSM/γ-soft 输入、参数扫描、可区分预测 | 仅有模型/作者解释，未有 common-input manifest | 模型 `γ`/configuration weight 不得写成实验事实 |

Manifest 的最低完成条件是 `source_lineage + band_level_identity + transition_observable + strength_lifetime + linking_identity` 均非 `missing`；`response_covariance` 缺失时最多为 L3 readiness，不能升级为可复现 L4。该 contract 是研究设计资产，不是测量结果。

### Public-source manifest seed rows (design-only)

这些行只把已有 source locator 映射到 contract 字段；它们不是 transition-level 数据表。未知字段保持 `missing`。

| seed row | 可填字段 | 明确缺失字段 | source lineage |
|---|---|---|---|
| `AW13-Bands1-7` | provisional band identity/linking（AW13-1/AW13-2）、`δ=0` 派生比值（AW13-9）、组态/模型标签 | measured `δ`、偏振、寿命、absolute strengths、response/covariance | `100Mo(36S,5n)` Gammasphere thesis；单一目标核谱系 |
| `SI16-131Ce-yrast` | 4 个有限寿命和 3 个限值（SI16-1）、部分 `Q_t`（SI16-2） | partner-resolved identity、direct `δ`/偏振、完整 interband matrix；TRS γ 是模型/解释（SI16-7） | `119Sn(16O,4n)` 独立 yrast lifetime experiment；与 Li 行依赖关系显式保留 |
| `LI04-131Ce-parity-controls` | 正负宇称序列有限/限值寿命和 `Q_t`（LI04-1/LI04-3） | same-parity partner、direct δ/偏振；LI04-11 明确不是 chiral-doublet evidence | `116Sn(19F,p3n)` 独立 DSAM；限值和 finite points 分开 |
| `PE98-131Ce-HD` | HD `Q0=7.3(4) eb`（PE98-7）和 separate-band scope（PE98-13） | HD–ND linking、共存混合、thesis Bands 1–7 partner mapping | `110Pd(28Si,α3n)` GASP+ISIS；独立 HD 扇区 |

Seed-row consistency checks：AW13 的派生 `B(M1)/B(E2)` 不与 SI16/LI04 的 `Q_t` 拼成同一 transition matrix；Singh 转载 Li 的行不重复计权；PE98 HD 不硬映射到 normal-deformed Bands 1–7；缺 response/covariance 时不进入 L4 proxy fit。

### Public-table transition seed rows (AW13; design-only)

以下四行来自 AW13 原始 PDF 的 Tables 4.1–4.4；它们把 `Eγ`、相对强度和角强度比 `R` 接入 manifest，但仍保留 source assignment、δ、偏振和寿命边界。

| row | `Eγ` / `Iγ` / `R` | source assignment | fields still missing | locator |
|---|---|---|---|---|
| `AW13-B1-E2-507.9` | `507.9 keV / 100 / 0.94±0.02` | `15/2−→11/2−`, E2 | measured `δ`, polarization, lifetime/absolute strength | AW13-14; PDF p.63 Table 4.1 |
| `AW13-B1-M1E2-137.4` | `137.4 keV / 68.3±3.2 / 0.50±0.04` | `11/2−→9/2−`, M1/E2 | δ branch/sign, polarization, lifetime/absolute strength | AW13-15; PDF p.64 Table 4.2 |
| `AW13-B4-link-611.1` | `611.1 keV / 25.2±1.1 / 0.56±0.02` | `17/2−→15/2−`, M1/E2; Band 4→Band 1 link | direct δ/polarization, partner matrix, response/covariance | AW13-16; PDF pp.61,66 Table 4.4/Fig.4.5 |
| `AW13-B7-E2-950.3` | `950.3 keV / 24.3±1.4 / 1.01±0.03` | `29/2−→25/2−`, E2 | measured δ/polarization, lifetime/absolute strength | AW13-17; PDF p.65 Table 4.3 |

These rows are source-backed manifest seeds, not a claim that the angular ratio `R` fixes multipolarity or that the source assignment is final.

### AW13 angular-ratio subset cross-check (design-only)

Using the first four Band 1 quadrupole rows in AW13-14 and the first four Band 1 dipole rows in AW13-15, inverse-variance weighting gives `R_E2=0.976±0.017` and `R_M1/E2=0.516±0.023`; the nominal difference is `0.461±0.028` (statistical-only). The E2 subset has `χ²≈20.6` for 3 degrees of freedom, so feeding, detector geometry and unmodelled covariance are material. This check validates that the table carries separated assignment handles; it is not a universal `R` threshold or an independent multipolarity proof.

## Analysis Status

- L3 milestone: completed；用户已完成 parity、δ 假设和数据边界的 claim-level review。
- L4 thesis-only milestone: completed；35 对 proxy 与 11 点 δ 扫描见 [thesis-only report](../../outputs/l4/131ce-thesis-baseline/report.md)。
- L4 lifetime update: completed-provisional；三条独立实验谱系、band crosswalk、限值和公式检查见 [lifetime-informed report](../../outputs/l4/131ce-lifetime-update/report.md)。
- Quantitative null result: Singh 四个有限 `Q_t` 点的加权斜率为 `−0.030±0.047 eb/ℏ`；“随自旋下降”在本子集不足 1σ。
- N=73 isotone milestone: completed-provisional；配置特异比较增强 `[404]7/2+` signature/configuration baseline，但不改变 wobbling 排序。
- Confidence: configuration/signature 机制为 medium；E2 集体性/芯响应约束为 medium；γ-soft background 因依赖 TRS/作者解释维持 low；HD 结构存在为高权重直接证据，但它与 thesis Bands 1–7 的 coexistence 关系为 low。

## Decisions

1. **Provisional milestone conclusion**：`131Ce` 当前最符合 signature/configuration coupling 主导、叠加随自旋或组态变化的 core response；γ-soft/nonaxial 是 TRS 支持的可行背景，而非寿命独立建立的实验属性。
2. 不把 Alwaleedi 的轴对称 TRS 点解释为 γ-rigid 实验证据，也不把其 core-polarization 讨论升级为 shape coexistence。
3. `131Ce` lifetime 消除了“目标带完全没有绝对 E2 约束”的旧缺口，但没有提供伙伴带电磁对称性；chirality/wobbling 状态不升级。
4. wobbling 在当前 `131Ce` Bands 1–7 中没有满足电磁优先判据，状态为 `unsupported`, 不是 `falsified for the nucleus`。
5. N=73 比较修订的是支撑结构而非结论排序：`[404]7/2+` 系统学加强正宇称 configuration baseline；邻近 `h11/2` wobbling 候选不能跨核迁移为 `131Ce` 证据。
6. 决定性 observable 的优先级为：
   1. 连接 ΔI=1 跃迁的 mixing ratio（含 branch/sign）与线偏振；
   2. 多带寿命、absolute B(E2)/B(M1)、Q_t 与带间/带内 E2 比；
   3. 统一 band identity 后的 interband transition matrix；
   4. quadrupole invariants/Coulomb excitation 或同口径 soft-vs-rigid 模型比较。

## Risks and Blockers

- **P0 / downgraded**：视觉复核显示 Alwaleedi Table 5.1 的 Band 2 负宇称与 Figure 4.1、Tables 4.5–4.6 和 Section 5.2.2 冲突，当前为 probable typo；原始单元已隔离，不用于 working parity。用户基于 Figure 4.1 的 provisional map 为 Bands 2/3/5 正宇称、1/4/6/7 负宇称。
- **P0 / resolved by claim-level human review**：Li 2004 文本层损坏，但用户已对照 p.3 接受 LI04-1–4 的 Table 1 视觉转录；LI04-5 作者解释仍待审，source 页面整体不升级。
- **P0 / isolated**：Singh 2016 转载 Li 2004 行不重复计权；Petrache 1998 HD band 保持独立，不并入 thesis Band 1。
- **P1 / resolved by claim-level human review**：Alwaleedi Table 5.3 对 Band 5 给出 `e⊗AE → e⊗AEFG` 与 `f⊗AE → e⊗AEFG`，180 dpi 视觉核验排除了 OCR 误差。2026-08-11 用户要求按原表使用并撤回 `f⊗AEFG` reconstruction；重复高自旋标签的物理连续性仍需独立来源，不影响当前集体模式排序。
- `133Ce` MχD 与 shape-coexistence 证据存在共享数据/模型依赖，独立性低于论文数量表面值。
- **P1 / awaiting focused review**：D21-8 与 N=73 project rows 新增了配置特异的同中子素比较；需确认未把旧实验汇编计为 Ding 2021 新测量，也未把 `127Xe/129Ba` wobbling 标签迁移给 `131Ce`。
- 公开来源尚未给出 `131Ce` Bands 1–7 的统一 measured δ、polarization 和 lifetime matrix。

## L4 milestones

- status: thesis baseline 与 lifetime update 均为 `completed-provisional`；Li 2004 数值转录 P0 已解决，其余 band mapping 与物理解读继续保持 provisional、按使用场景复核。
- 可用数据 A：用户已手动启动 L4，并确认 thesis Tables 4.1–4.7、5.1–5.4 与 Figure 5.5 的公开能量、强度、angular ratios、crossing 和相对 B(M1)/B(E2) 为本轮主要高质量基线。
- lifetime update：三篇公开论文形成独立谱系、band crosswalk、限值与不确定度处理；详见 [reproducible package](../../outputs/l4/131ce-lifetime-update/report.md)。
- 建议分析：建立 band/transition manifest；传播 intensity 与 δ 假设；比较 signature/configuration、γ-soft core coupling、wobbling/chirality 的可区分预测；执行 band-mapping 和 δ 分支敏感性负例。
- 最小数据字段：band/level identity、Eγ、Ei/Ef、Iiπ/Ifπ、intensity 与误差、multipolarity/δ 及误差/分支、polarization、lifetime 或 B(E2)/B(M1)、source locator。
- 可能创新点：把“模式标签争论”转换为可审计的 observable-discrimination score，并量化哪一项新测量提供最大信息增益。
- 定量新发现：Figure 5.5 gated-input P0 未被寿命恢复；Singh 有限点加权平均 `Q_t=2.579±0.099 eb`、斜率 `−0.030±0.047 eb/ℏ`；HD `Q0` 与该均值的尺度比约 2.83，但因 `Q0/Q_t` 几何不同只作尺度提示。
- 解释排序：signature/configuration coupling 仍主导 band identity；寿命/`Q_t` 对 E2 集体性与 core response 提供正交约束，γ-softness 仍是 TRS/作者解释层且不升为高置信；shape coexistence 从“无目标核直接线索”修订为“同核有独立 HD 极小、但 thesis 带关系未建立”；chirality/wobbling 不升级。

## Next Actions

1. 用户独立 `131Ce` 实验数据本轮不读取、不与公开数据合并；未来先建立独立 manifest、数据身份和 band/transition mapping，再按具体问题启动更深入 L4。
2. 继续补齐 Figure 5.5 gated inputs、measured δ/偏振、伙伴带 absolute strengths 与 HD–ND linking 等能够改变竞争解释排序的证据。
3. 不把本 project 的 provisional conclusion 写入正式论文结论或提升为 high confidence。

## Related Sources and Pages

- **Day 3 model-route link (2026-09-29):** [[a130-model-choice-card]] maps model inputs and limits for the existing `131Ce` question; [[hara-sun-1995-projected-shell-model-high-spin]] `HS10-4` is an axial-code historical comparison only. Its seven `N=76–78` triaxial candidates, including the later `133La`/`135Pr` TPSM examples ([[sheikh-jehangir-bhat-2024-tpsm-wobbling]]), do not transfer to `131Ce` (`Z=58,N=73`) and do not change the current hypothesis ranking.
- Target baseline: [[alwaleedi-2013-band-structures-131ce]], [[singh-2016-lifetime-131ce-133pr]], [[li-2004-lifetimes-131ce]], [[131ce-negative-parity-yrast-reference-sequence]], [[131ce-positive-parity-reference-sequence]], [[petrache-1998-highly-deformed-lifetimes-131ce-nd]], [[131ce]]
- Static-moment/shape anchor: [[ionescu-bujor-1998-static-moments-129-131ce]]；其 `131Ce` `J=9−` moments and PTR shape parameters constrain the shape background but do not identify the high-spin collective mode alone.
- `133Ce`: [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]], [[ayangeakaa-2016-133ce-in-beam]], [[133ce]]
- N=73 configuration/wobbling controls: [[ding-2021-131ba-133ce-signature-splitting]], [[palacz-1991-high-spin-131ce]], [[bazzacco-1998-rotational-bands-133nd]], [[chakraborty-2020-multiphonon-longitudinal-wobbling-127xe]], [[chakraborty-2024-possibility-wobbling-129ba]], [[127xe]], [[129ba]]
- Mechanism controls: [[ding-2021-131ba-133ce-signature-splitting]], [[chakraborty-2023-131xe-wobbling-origin]], [[nomura-2022-questioning-wobbling-ibfm]]
- Synthesis: [[gamma-soft-vs-gamma-rigid-diagnostics]], [[wobbling-vs-signature-partner]], [[signature-splitting-mechanisms]]
