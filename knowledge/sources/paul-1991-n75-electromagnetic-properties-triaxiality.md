---
type: source
title: "Paul et al. 1991 - Electromagnetic properties of N=75 isotones: evidence for triaxiality at low spin"
aliases: [Paul 1991 N=75 isotones, Paul 1991 133Ce triaxiality, 1991Pa04]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Electromagnetic properties of N = 75 isotones: evidence for triaxiality at low spin"
authors: [E. S. Paul, R. Ma, C. W. Beausang, S. A. Forbes, D. B. Fossan, J. Gizon, J. R. Hughes, Y. Liang, S. M. Mullins, P. J. Nolan, W. F. Piel Jr, R. J. Poynter, P. H. Regan, R. Wadsworth, N. Xu]
journal: "Journal of Physics G: Nuclear and Particle Physics"
year: 1991
volume: 17
issue: 5
pages: "605–617"
doi: "10.1088/0954-3899/17/5/009"
citation_key: Paul_1991
canonical_source: "https://doi.org/10.1088/0954-3899/17/5/009"
raw_file: "raw/papers/1991_Electromagnetic properties of N=75 isotones_evidence for triaxiality at low spin.pdf"
raw_sha256: "1c3859a03a76e200048b8e087e91131d7dc5f21fb8a683cd39155ab00e0818c9"
nuclei: [133Ce, 131Ba, 135Nd, 137Sm, 139Gd]
reactions: [120Sn-16O-3n-133Ce, 122Sn-13C-4n-131Ba, 112Cd-27Al-p3n-135Nd, 104Pd-37Cl-p3n-137Sm, 92Mo-50Cr-2pn-139Gd]
experiments: [stony-brook-tandem-angular-distribution]
models: [Donau-Frauendorf-semiclassical, cranked-shell-model, total-routhian-surface]
observables: [multipole-mixing-ratio, BM1-BE2-ratio, BE2-BE2-ratio, signature-splitting]
methods: [in-beam-gamma-spectroscopy, angular-distribution, directional-correlation]
tags: [133Ce, N=75, triaxiality, mixing-ratio, Donau-Frauendorf, BM1-BE2, A130]
---

# Electromagnetic properties of N=75 isotones: evidence for triaxiality at low spin

## Bibliographic Record

- E. S. Paul *et al.*, *J. Phys. G: Nucl. Part. Phys.* **17**, 605–617 (1991), DOI: `10.1088/0954-3899/17/5/009`.
- 本地原件：`raw/papers/1991_Electromagnetic properties of N=75 isotones_evidence for triaxiality at low spin.pdf`，SHA-256 为 `1c3859a03a76e200048b8e087e91131d7dc5f21fb8a683cd39155ab00e0818c9`。
- 本文献由用户提供，补齐此前 Day 24 遗留的 1991Pa04 原件缺口，为 [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] (WK22) 第 6 章带内混合比与三轴粒子-转子模型提供直接历史溯源。

## Scope and Reading Depth

- 全文 14 页（含封面）、图 1–6、表 1 与公式 (1)–(8) 完整通读；
- 重点核对 133Ce 在 Stony Brook 串列加速器上的角分布实验条件、多极混合比 delta(E2/M1) 符号约定、电磁跃迁几率比值定义，以及基于 Donau-Frauendorf 半经典模型对 133Ce 三轴形变（beta2=0.17, gamma=-20 deg）与有效 K 投影的理论计算。

## Summary

本文系统测量并汇总了 N=75 奇中子同中子素（131Ba, 133Ce, 135Nd, 137Sm, 139Gd）基于独特性宇称 nu h11/2 轨道的负宇称能带的电磁性质：
1. **实验测量**：在 Stony Brook 利用 120Sn(16O, 3n gamma)133Ce（69 MeV，厚铅衬靶）开展 5 角区（90, 115, 125, 135, 145 deg）角分布测量，利用 chi2 极小化拟合提取带内 Delta I=1 跃迁的多极混合比 delta(E2/M1)；
2. **符号与单位约定**：采用 Yamazaki 1967 符号约定；本文不另认证与其它相位约定等同，跃迁比率公式含因子 0.697 MeV^2；
3. **三轴性证据**：
   - 印612/Fig2的低spin约1、回弯后约5倍讨论的是同ΔI=1 E2分母；133Ce上升只称suggested且误差大，不能搬成Fig3的ΔI=2分母；
   - 竞争的非拉伸与拉伸电四极跃迁比值 B(E2; I -> I-1)/B(E2; I -> I-2) 围绕平均值 ~ 2 起伏，大于 1 的事实反映了波函数中低 Omega 组分的掺杂，是核具有非轴对称（三轴）形状的明确信号；
   - 采用 Donau-Frauendorf 半经典模型计算 133Ce：TRS 计算给出低自旋 (beta2=0.17, gamma=-20 deg)，高自旋三准粒子态 (beta2=0.17, gamma=0 deg)。在三轴形变下 K 不再是好量子数，有效 K=7/2 能更好地再现实验比值；
   - 依据 Hagemann-Hamamoto 三轴性检验（Delta B(M1)/<B(M1)> 与能谱旋称劈裂 Delta e_prime/hbar omega 的对比），在该检验的形状/近似条件下，作者将轻同中子素的电磁系统学解释为更明显的三轴性支持，非直接γ测量。

## Experimental and Method Contract

- **反应与靶**：120Sn(16O, 3n)133Ce，束能 69 MeV，靶厚 9.7 mg/cm2 120Sn，背衬 100 mg/cm2 Pb（完全阻止反冲核与束流）；
- **探测布局**：1 台反康普顿 HPGe 探测器（距离靶点 22 cm）在 5 个角度旋转测量，另 1 台固定在 -90 deg 作为束流强度与产额监测；利用 133Ba 与 152Eu 点源进行精确几何与探测效率刻度；
- **跃迁率合同（printed609 / physicalPDF6 Eqs2–6）**：
  能量用MeV；E1指该母态ΔI=1混合线能量，E2指ΔI=2纯E2线能量，不是电多极阶的缩写变量。

$$\delta=0.835E_1\,\frac{\langle E2\rangle}{\langle M1\rangle},\quad
\delta^2=T(E2)_1/T(M1)_1,\quad
\lambda_{\rm pure}=T(E2)_2/T(M1)_1.$$

$$\frac{B(M1)_1}{B(E2)_1}=\frac{0.697 E_1^2}{\delta^2},\qquad
\frac{B(M1)_1}{B(E2)_2}=\frac{0.697 E_2^5}{E_1^3\lambda_{\rm pure}}.$$

若另外定义经过效率/门接受度校正的光子分支Λ=Y2/Y1，Y1为整条混合线，则在同光子率合同下λpure=Λ(1+δ²)，从而：

$$\frac{B(M1)_1}{B(E2)_2}=
\frac{0.697E_1^2(E_2/E_1)^5}{\Lambda(1+\delta^2)},\qquad
\frac{B(E2)_1}{B(E2)_2}=
\frac{\delta^2(E_2/E_1)^5}{\Lambda(1+\delta^2)}.$$

原文说明ΔI=1强度作了内转换修正；尚未恢复原处理producer，不把总转换强度直接当光子yield。λpure是branching变量，不是BCS化学势。旧source漏E1²及混合份额的公式撤回；不改变论文原件或原实验δ。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PA91-01 | 120Sn(16O, 3n)133Ce 在 69 MeV 下测定负宇称带内 Delta I=1 跃迁的角分布，确立混合比 delta(E2/M1) < 0（采用 Yamazaki 1967 约定）。 | experiment-result | direct | PDF pp. 2–5, Fig. 1 | true |
| PA91-02 | 印612/Fig2中低spin约1及回弯后约5倍概括对应同ΔI=1 E2分母；133Ce上升仅suggested且误差大，不能转作ΔI=2分母的定量结论。 | observable-identity-and-qualified-author-summary | direct-original | physicalPDF9 printed612 §4.1 Fig2 discussion | true |
| PA91-03 | 非拉伸与拉伸四极比 B(E2; I -> I-1)/B(E2; I -> I-2) 约 2 > 1，反映三轴形变波函数中低 Omega 组分的非对角混合。 | triaxiality-indicator | mixed | PDF pp. 6–9, Fig. 4 | true |
| PA91-04 | Donau-Frauendorf 半经典模型以 TRS 参数 (beta2=0.17, gamma=-20 deg)、有效 K=7/2 与实测能谱旋称劈裂 Delta e_prime/hbar omega = 0.39(3) 较好地再现了 133Ce 的跃迁比率。 | model-interpretation | mixed | PDF pp. 9–11, Fig. 5 | true |
| PA91-05 | Hagemann–Hamamoto式下的轻重同中子素比较属于作者模型解释；Eq8将E2近恒假定用于从比值估M1不对称，不能直接独立测γ/刚性。 | conditional-cross-isotone-interpretation | direct-original-with-model-assumptions | physicalPDF12 printed615 Eq8 | true |
| PA91-06 | 确认 WK22 Figure 6.15(a) 采用的 133Ce Band 1 带内 delta 数据直接源自本篇，两文献形成确凿的谱系继承与互补关系。 | cross-source-lineage | direct | PDF p. 5, Fig. 1; WK22 PDF p. 113 Fig. 6.15(a) | true |

## Competing Interpretations and Limitations

1. **谱线与带身份范围**：本篇仅研究负宇称 yrast 带（Band 1）及其高自旋 3-qp 延伸，未报告亦未涉及高激发 Band 4 及其跨带连接跃迁；
2. **寿命与绝对标度缺口**：本篇实验为厚衬靶角分布，未测定态寿命 tau，所有电磁量均为相对比值（B(M1)/B(E2) 或 B(E2)/B(E2)），无法单独给出绝对 B(E2) 或内禀电四极矩 Q0；
3. **有效 K 的唯象性**：在三轴形变下将 K 从 9/2 唯象调至 7/2 属于准粒子转子模型的参数化补偿，不能替代完全非谐微观波函数的严格对角化。

## Extracted Pages

[[133ce-thesis-analysis-blueprint]]保留本文带内混合比谱系与实际QTR输入缺口；不将旧实验的角响应或有效K转填现代Band4。checkpoint005仅补齐本页结构入口，原科学主张和needs_review保持，具体公式另按原件复核。

## Day25 checkpoint005：公式、比值身份与元数据复核

父代理定向读取physicalPDF2/3/4/6文字，独立代理视觉核2/3/6及公式7/8、WK22引用；不新增14页全文阅读声明。原SHA1c3859a03a76e200048b8e087e91131d7dc5f21fb8a683cd39155ab00e0818c9相符；旧公式/分母误认已在当前正文替换，旧字节由Git保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PA91-D25-A005-01 | Eq6的能量因子为.697 E2^5/E1^3，λ为纯M1分量的branching比；若改用全混合光子线分支Λ则须恢复(1+δ²)。旧source的(E2/E1)^5式漏E1²，E2/E2式漏混合份额。 | direct-formula-and-task-variable-dictionary | direct-original-plus-declared-algebra | physicalPDF6 printed609 Eq6 | true |
| PA91-D25-A005-02 | Table1反应为112Cd(27Al,p3n)135Nd、104Pd(37Cl,p3n)137Sm、92Mo(50Cr,2pn)139Gd；旧source114Cd/107Pd/52Cr撤回，原文件不变。 | direct-reaction-identity-correction | direct-original-and-visual | physicalPDF3 printed606 Table1 | true |
| PA91-D25-A005-03 | 低spin约1、回弯后约5倍段讨论Fig2同ΔI=1 E2分母，133Ce增幅仅suggested；不移为Fig3的ΔI=2分母。 | direct-denominator-and-qualifier | direct-original | physicalPDF9 printed612 §4.1 | true |
| PA91-D25-A005-04 | 作者尾明确R Wadsworth and N Xu，元数据补N.Xu；Yamazaki约定与Krane1975综述引用不是已核另一约定等同证明。 | direct-bibliography-and-convention-boundary | direct-original-and-visual | physicalPDF2 printed605 author list | true |

可复用branching字典与[[133ce-thesis-analysis-blueprint]]同母态部分相连；WK22 Fig6.15(a)引用Ref56只给Band1带内δ谱系，不补Band4跨带δ独立测量。
