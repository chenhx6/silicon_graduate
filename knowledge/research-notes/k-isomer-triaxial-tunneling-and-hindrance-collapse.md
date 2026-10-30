---
type: research-note
title: "高K衰变逐支纠错：宇称选择定则、部分γ半衰期与阻退度的迁移边界"
aliases: [k-isomer-triaxial-tunneling-and-hindrance-collapse, k-isomer gamma tunneling, reduced hindrance collapse, anomalous k decay]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [walker-dracoulis-2001-exotic-isomers, smith-2003-hf178-isomer-gamma-decay]
created_from: Day 27 continuation study; system/scripts/day27_k_isomer_triaxial_breakdown_study.py
tags: [k-isomer, parity, multipolarity, partial-half-life, internal-conversion, source-correction, Day27]
---

# 高K衰变的逐支身份与阻退度反演

## Research Trigger

Day27旧版把Hf的16⁺→14⁻及另外五个8⁻→6⁺支标为E2，再用预填fν值和自设指数公式宣称寿命塌缩、γ隧穿和统计混合被排除。这六条E2标记与宇称选择定则冲突；旧八核表又缺Eγ、绝对分支及内转换信息。统一provisional附录没有修正这些错误，本页现逐条替换。

旧笔记、脚本、结果和输入保存在本run `scientific-corrections-046/superseded-k-artifacts.json`，仅为撤回追溯。旧结果JSON已标superseded；“三千万倍实测寿命塌缩”“fν窄平台排他证明γ隧穿”撤回。

## Grounded Evidence

| 来源与实际定位 | 本轮核验事实 | 证据性质与限制 |
| --- | --- | --- |
| [[walker-dracoulis-2001-exotic-isomers]] WD01-D27-R046-1；PDF7/printed89 Fig.3和正文，PDF16/printed98 Sec.3.3 | Hf31年K=16异构态主要到K=8带I=13态，约13-keV、λ=3，ν=5；Sec.3.3明确E3，fν≈66 | 综述转述；本轮父代理文字/视觉回读对应页，不把它记为新实验 |
| 同source WD01-D27-R046-2；PDF16–17/printed98–99 Sec.3.3与Table II | fν=(Tγ/TW)^(1/ν)，Tγ为部分γ半衰期；TW取决于跃迁能量和多极性，Table II给keV/s单位的E1/M1/E2/M2例 | 不能拿能级总寿命或Ex直接代入 |
| 同source WD01-D27-R046-3；PDF17–18/printed99–100 | 保留Coriolis、γ隧穿和态密度等混合机制；某些低fν例原则上也能用基态带高K混合解释 | 低fν不独占γ隧穿，不能由自填窄分布排除其它机制 |
| [[smith-2003-hf178-isomer-gamma-decay]] SM03-D27-2/3/5；作者稿PDF3–7/printed1–5、Table I、Figs.2–3 | 13-keV E3主支与16⁺→12⁻ M4、16⁺→11⁻ E5具有不同多极阶和ν；直接γ弱支以符合确证 | M4/E5为该实验弱γ证据；E3主支和部分fν依赖既有转换信息，不能重复计独立证据 |
| Smith2003 SM03-D27-4；Table I及printed2归一段 | Iγ以325.5-keV支归一，弱支相对强度不等于绝对每次母核衰变的光子概率 | 本轮没有由原事件重提取bγ/转换系数/实验Cov |

父代理实际回读综述PDF7、16–18并视觉核PDF7/16/17，SHA-256与source一致。Smith公开作者稿共7页，视觉读正文PDF3–7及全部Figs.1–4、Tables I–II；原字体提取乱码未用于猜数。最终期刊版与作者稿身份分开，raw目录未写。

## Provisional Reasoning

### 电磁宇称与角动量先于K阻退

对通常具有良好宇称标签的核态，插入宇称算符得非零电磁矩阵元的必要条件：

\[
\pi_f\pi_i=(-1)^L\quad(EL),\qquad
\pi_f\pi_i=(-1)^{L+1}\quad(ML).
\]

实光子还须满足 `L≥1` 和 `|Ji−Jf|≤L≤Ji+Jf`。因此E2保持宇称；K混合、Coriolis或γ隧穿不豁免这个实验室选择定则。即使内禀反射不对称，带Jπ标签的实验态也不能因此任意发出跨宇称E2。

旧表中178Hf、176Yb、180W、130Ba、134Nd、188Pb六行不通过此必要检查。对这些既定初末自旋宇称，M2/E3等可能满足运动学，但不是这六条支已被实验指认的替代多极性，不能批量把E2改成E3。136Ce的10⁺→8⁺ E2和190Pt的7⁻→6⁺ E1只通过必要筛查；其存在、能量、K和强度仍未核，不因此成为真实数据。

Hf原综述与新读一手稿允许建立一个有来源的逐支锚点：

| 支路 | 电磁必要条件 | ΔK与ν | 处置 |
| --- | --- | --- | --- |
| 16⁺→13⁻ E3，约13 keV | 反宇称，ΔJ=3，E3允许 | ΔK=8，ν=5 | 与原件相符；报告fν≈66不等于本脚本独立提取 |
| 16⁺→12⁻ M4，309.5-keV | M4反宇称，ΔJ=4允许 | ΔK=8，ν=4 | Smith2003直接γ支与既有约束；不沿用ν=6 |
| 16⁺→11⁻ E5，587.0-keV | E5反宇称，ΔJ=5允许 | ΔK=8，ν=3 | 同上；不同ν对应不同阻退指数 |

### 总分支、光子概率和混合乘性分量

设能级半衰期T，某支包括γ及内转换的总分支为bt，α=λIC/λγ。绝对光子概率为 `bγ=bt/(1+α)`，则：

\[
T_{1/2}^{\gamma}=\frac{T(1+\alpha)}{b_t}=\frac{T}{b_\gamma}.
\]

混合乘性时，若目标分量在全部辐射光子中的份额为fL，需再除fL，并使用整条支相应的有效α：

\[
T_{1/2,L}^{\gamma}=\frac{T(1+\alpha_{\rm eff})}{b_t f_L}
=\frac{T}{b_\gamma f_L}.
\]

如果已经给绝对光子概率，不能再乘转换修正。只有相对峰强度、只有Ex或只有总寿命时，输入未闭合；程序拒绝反演而不补常数。若输入为平均寿命τ，先用T=ln(2)τ。

纯乘性或分量定义明确后，`F=Tγ/TW`，`fν=F^(1/ν)`；ν≤0不在此“每阶K禁戒”定义域，不能强制取根。综述Table II只列E1/M1/E2/M2，本程序不由该表擅自发明E3 Weisskopf数值；Hf报告fν仅作source-reported记录。

误差传播也需同一约定。对z=(T,bt,αeff,fL)，`∇lnTγ=(1/T,−1/bt,1/(1+αeff),−1/fL)`，一阶方差为该梯度与实际Cov的二次型。无Cov或共享归一信息时不制造新置信区间。

### 独立事件率控制与错误寿命比

为校验实现，设置**无核素身份的合成输入**：T=10 s、bt=0.25、α=3。由λtot=ln2/10及λγ=λtot×0.25/4，独立算出Tγ=160 s；用绝对bγ=0.0625得到同值。再取辐射分量fL=0.4，Tγ,L=400 s。这些数值只是单位与归一控制，不是Hf或Ba新测量。

旧因子 `(60.5/3.44)^6≈2.95925×10⁷` 只重放自设同ν的阻退比例。真实部分γ半衰期之比还含 `TW,a/TW,b`，而TW随Eγ、多极性和A改变；能级总寿命比较还需分支/转换修正。因此它不是实测寿命加速比，也不说明真实Ba寿命应该为数天。

## Assumptions

- 选择定则筛查假定实验Jπ标签和通常电磁宇称规律适用；不研究极小弱作用宇称破坏。
- K与ν是所选内禀组态的近似标签，不能由Jπ筛查反推出K。旧表I=K仅为历史带头假设。
- 合成事件率为单支、无未记录feeding的控制。真实feeding和混合需单独建立数据合同。

## Competing Explanations

Coriolis混合、γ形变隧穿、局域态密度/近邻态混合和衰变末态组态差异均保留。原指数模型预设系数与 `max(2.5,...)` 下限，没有解隧穿方程或建立统计混合似然；用预填输入的窄分布不能排他检验这些机制。

## Transfer Conditions

可迁移的是逐支选择定则、能量/单位、绝对分支与内转换/乘性分量归一合同。跨核比较fν前须核Eγ、Jπ/K、纯/混合多极性、部分寿命定义和Weisskopf约定，不能把某一fν值或γ角阈值当作全核区寿命规则。

## Failure Conditions

来源或必要支路字段缺失、E2跨宇称、相对强度被当绝对概率、转换修正重复、平均寿命混成半衰期或ν≤0时停止阻退反演。某支未见但效率/求和/杂质边界未核时，不能声称物理禁戒或不存在。

## Falsification or Reverse Tests

- 六条旧E2跨宇称被明确拒绝；原Hf E3、独立M4/E5支通过必要条件，保留其不同ν。
- 合成事件率与两种分支约定给相同Tγ；分量份额、mean/half-life、重复转换、缺失α、零分支和实光子E0均有控制。
- 同E2条件下Eγ翻倍，Table II的TW变为1/32，防止把Ex和Eγ或能量单位混用。
- 所有八条旧核素输入停止实验fν反演和shape判决；旧巨量比例只作历史算术。

## Open Questions

1. 对旧Ba/Nd/Ce/Pb/Pt行逐支找到直接来源后，哪些真实支路及其乘性/分支存在，哪些原输入需彻底淘汰？
2. 在同一支路强度、转换系数和Cov约定下，哪些新的独立观测能区分Coriolis、γ隧穿与局域混合？先完成身份和归一，后比较机制。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为source定向self-audit与分析合同验证，保持unreviewed/provisional。子代理审计给出线索，父代理实际回读原页并复算；程序检查通过不自动认证旧核素数据或任何γ隧穿机制。

## Promotion or Rejection History

- 2026-10-30 checkpoint029及后续附录：旧E2表、千万倍“实测寿命塌缩”和统计混合排他认证撤回，通用边界附录未修复这些错误。
- 2026-10-30 checkpoint046：逐支选择定则与部分γ半衰期合同替代旧指数分类；新读Smith2003作者稿补一手M4/E5证据。旧工件保存，输出 `k_isomer_branch_audit_corrected.json`；不推进Day27/Day28学分。
