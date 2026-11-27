---
type: source
title: "Bisoi et al. 2014 - High spin spectroscopy in 34Cl"
aliases: [Bisoi 2014 34Cl high spin]
created: 2026-09-21
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "High spin spectroscopy in 34Cl"
authors: [Abhijit Bisoi, M. Saha Sarkar, S. Sarkar, S. Ray, D. Pramanik, R. Kshetri, Somnath Nag, K. Selvakumar, P. Singh, A. Goswami, S. Saha, J. Sethi, T. Trivedi, B. S. Naidu, R. Donthi, V. Nanal, R. Palit]
journal: "Physical Review C"
year: 2014
volume: 89
pages: "024303"
doi: "10.1103/PhysRevC.89.024303"
citation_key: Bisoi_2014
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Bisoi et al., Phys. Rev. C 89, 024303 (2014)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf"
raw_sha256: "bc0af718ffb496f135abe2a51b82f87d208776fce155926a8604e8c05d126f85"
nuclei: [34Cl, 34S, 26Al]
reactions: [27Al-12C-alpha-n]
experiments: [INGA, DSAM, RDCO, IPDCO]
models: [large-basis-shell-model, sd-pf-cross-shell, two-level-mixing]
observables: [level-scheme, lifetime, B(E2), B(M1), RDCO, IPDCO, mixing-ratio]
methods: [gamma-gamma-coincidence, DCO, linear-polarization, Doppler-shift-attenuation]
tags: [34Cl, INGA, high-spin, DSAM, collectivity, shell-model]
---

# High-spin spectroscopy in `34Cl`

## Bibliographic Record

- A. Bisoi *et al.*, *Phys. Rev. C* **89**, 024303 (2014), DOI `10.1103/PhysRevC.89.024303`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/纲图/2014_Bisoi et al_High spin spectroscopy in 34 Cl.pdf`。

## Scope and Reading Depth

- PDF pp.024303-1–13 fully read: INGA/Pixie-16 experiment, RDCO/IPDCO/δ, level scheme to 10.6 MeV, DSAM line-shape lifetimes, Tables I–V, shell-model truncations/configuration mixing and conclusion.
- Not covered: raw event list and full shell-model code.

## Key Results

- `27Al(12C,αn)` at 40 MeV with 15 INGA clovers produced about `6×10^8` γ–γ events; the `34Cl` scheme was extended to 10.6 MeV. RDCO, IPDCO and δ assign multipolarities and parity, while DSAM provides lifetimes for selected states (PDF pp.1–4, Tables I–V).
- IPDCO confirms electric/magnetic character (e.g., 491-keV electric and 461-keV magnetic lines); DCO and Krane–Steffen δ values are listed for dozens of transitions under `σ/J=0.3` and clover `Q(E)` calibration (PDF pp.2–5, Table I).
- DSAM line shapes use 50,000 recoil histories, PACE4 momentum distributions and Northcliffe–Schilling stopping powers. Selected E2 transitions have `B(E2)≈8–20 W.u.`, indicating onset of collectivity; higher levels have larger E2 strengths and short lifetimes (PDF pp.5–9, Table V).
- Large-basis sd–pf shell-model calculations require cross-shell pf involvement for negative-parity and high-spin positive-parity states; two-level mixing is used for selected configuration admixtures (PDF pp.8–12, Tables III–IV).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BI14-1 | `34Cl` high-spin scheme reaches 10.6 MeV with RDCO/IPDCO/δ and DSAM evidence. | experiment-result | direct | PDF pp.1–9, Tables I–V | true |
| BI14-2 | Selected E2 lifetimes give `B(E2)≈8–20 W.u.` and evidence for emerging collectivity. | collectivity-result | direct | PDF pp.5–9, Table V | true |
| BI14-3 | sd–pf cross-shell configurations are needed to reproduce negative-parity/high-spin states. | model-result | mixed | PDF pp.8–12 | true |
| BI14-4 | DSAM feeding/stopping and `σ/J`/Q calibration limit lifetime and δ transfer. | limitation | direct | PDF pp.2–9 | false |

## Summary

Bisoi *et al.* connect a detailed multimethod level scheme to DSAM electromagnetic strengths in `34Cl`. The direct evidence supports a transition from single-particle to collective high-spin behavior, while pf-shell configuration mixing and two-level admixtures remain model interpretations.

## Competing Interpretations and Limitations

- DSAM lifetimes are sensitive to side feeding, stopping powers, recoil distributions and gates; upper limits are retained where statistics are insufficient.
- `B(E2)` enhancement indicates collectivity but does not uniquely determine a shape or deformation parameter.
- Large-basis shell-model truncations and effective interactions influence configuration mixing; model agreement is not a direct wave-function measurement.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BI14-AR-1 | Assignment chain | Coincidences → RDCO/IPDCO/δ → multipolarity/spin/parity; preserve weak/tentative levels. | PDF pp.2–5, Table I | self-checking |
| BI14-AR-2 | Lifetime chain | Doppler line shapes + PACE4/SRIM + side feeding → τ → B(E2)/B(M1). | PDF pp.5–9, Table V | self-checking |
| BI14-AR-3 | Model transfer | sd–pf shell-model and two-level mixing explain configuration content, not direct shape. | PDF pp.8–12 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[angular-distribution]], [[linear-polarization-asymmetry]] and light-nucleus collectivity comparators.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `BI14-P0-1`: Keep DSAM/model/lifetime boundaries explicit; `B(E2)` enhancement is not a unique deformation proof.

## Extracted Pages

- Methods/observables: [[doppler-shift-attenuation-method]], [[multipole-mixing-ratio]], [[angular-distribution]]。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from_page": 1, "to_page": 3, "sections": "I 引言、II 实验与数据分析、III.A 能级纲图开头，含式(1)–(3)及表I"}
- {"from_page": 4, "to_page": 8, "sections": "III.A 能级指认、III.B 寿命与集体性、IV 理论计算开头，含图1–8及表II"}
- {"from_page": 9, "to_page": 13, "sections": "IV 正负宇称截断、组态混合与跃迁强度、V 结论、致谢及参考文献[1]–[31]，含图9–10及表III–V"}
- 本次获取的具体覆盖：通读物理第1–13页的正文、图1–10图注、表I–V抽取文本、致谢和参考文献。建议接受既有条目的同版全文文字覆盖。条目中的方法和模型表述需更正，图表验收仍待目视核对。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | 40 MeV的¹²C束经²⁷Al(¹²C,αn)³⁴Cl反应布居高自旋态。15台INGA三叶草探测器记录约6×10⁸个γ–γ符合事件。作者在既有纲图中加入11条跃迁和6个能级，将3381 keV跃迁置于1935 keV跃迁之上，指认10 631 keV的11⁺态。 | 实验结果 | source-reported | 物理第1–2页§II、第3页表I、第4–6页§III.A及第5页图4。图4的宇称符号、标记及连线待核。 | true |
| A17-2 | DSAM线形拟合给出7250 keV能级平均寿命0.23(4) ps。7699、7800、8155、9392及10 631 keV能级仅给出寿命上限，其中10 631 keV为<0.04 ps。表V相应列出1935 keV跃迁的B(E2)为130(29) e² fm⁴，3381 keV跃迁为>51 e² fm⁴。 | 实验拟合结果 | source-reported | 物理第6–8页§III.B、第7页图6–7及第12页表V。表V的限值、误差及单位待核。 | true |
| A17-3 | 作者将所选E2跃迁约8–20 W.u.的强度解释为高激发区出现集体性，并对5.315、7.250、10.631 MeV序列估算β₂约为0.19–0.29。形变估计依赖所采用的关系式，且最高态寿命只有上限。 | 作者解释 | source-reported | 物理第7–8页§III.B及第12页表V。强度的限值方向待核对第12页。 | true |
| A17-4 | OXBASH的sdpfmw计算中，全sd空间较好描述至5⁺的谱，较高自旋正宇称态需要纳入pf空间。负宇称高自旋态对截断方案敏感，6⁻、8⁻在纳入1p–1h和3p–3h后改善，9⁻的能量在采用纯3p–3h并调整壳隙后改善。组态占比来自模型波函数。 | 模型结果 | source-reported | 物理第8–11页§IV.A–C，图8（第8页）、图9（第9页）、图10（第10页）及表III–IV（第11页）。图10与表IV的部分能量待核。 | true |

能级指认依赖符合关系、相对强度、DCO门条件及线偏振。δ由ANGCOR在σ/J=0.3下比较得到，偏振校准见物理第2页式(1)–(3)和第4页图1–2。DSAM采用PACE4初始反冲动量、改版LINESHAPE、50 000条反冲历史及经壳修正的Northcliffe–Schilling阻止本领。低产额迫使分析使用下方门，并引入旁馈假设。

- 将条目寿命链中的“PACE4/SRIM”改为“PACE4初始反冲动量、改版LINESHAPE与经壳修正的Northcliffe–Schilling阻止本领”。依据为物理第2–3页。
- 删除条目中的“Krane–Steffen”约定归属，改记ANGCOR和σ/J=0.3。正文称计算了20条跃迁的δ，线偏振测量覆盖超过25条跃迁，两项分别计数。见物理第2–4页。
- 将“两能级混合”从模型字段与摘要中删去，改为sd–pf空间的截断比较和按轨道占据数分解的组态混合。将寿命及跃迁强度的主定位改至物理第12页表V，把约8–20 W.u.定位在第7–8页正文并保留限值。
- 物理第11页表IV的11⁺实验能量抽取为10.618 MeV，第5页正文和第12页表V为10.631 MeV。第10页图10抽取的Theo-N4 9⁻能量与第11页表IV也不一致。能级纲图可按正文与表V记10.631 MeV，表IV及模型数值保留差异标记，待查原页。
- 物理第2页式(1)–(3)的偏振符号和平行计数下标有乱码，可依同页定义暂读为Δ_IPDCO及N∥。第9–11页的ℏω字形和第12页无编号粒子分区式的第二项指数亦需核原印。图1–10的图注均有抽取，第5页图4的部分宇称符号无法从抽取文本辨认。
