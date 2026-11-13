import json, hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex'
with open(tex_path, 'rb') as f:
    tex_sha = hashlib.sha256(f.read()).hexdigest()

with open('raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json', 'r', encoding='utf-8') as f:
    ledger = json.load(f)

ledger['output_tex_sha256'] = tex_sha
ledger['recorded_at'] = '2026-11-13T20:30:00Z'
ledger['status'] = 'audited_and_reconciled_round2'

# Update notations
ledger['notations_and_conventions']['axis_convention_mapping'] = '显式区分几何主轴 (k1=m, k2=s, k3=l) 与第3.3节局部 FA 动力学展开坐标 (1=qp 沿短轴 s, 2=最大惯量沿中轴 m, 3=长轴 l)；展开常数写作 A_s, A_m, A_l，横向曲率 C_m = (A_m - A_s) + A_s j/I，C_l = (A_l - A_s) + A_s j/I，I_c = j / (1 - J_s/J_m)'
ledger['notations_and_conventions']['stability_condition'] = '区分定域能量极小与线性动力学稳定性：C_m, C_l > 0 为能量极小与正能声子基态；C_m, C_l < 0 为旋转系能量极大，陀螺力可赋予其线性稳定性，但不能作为声子激发稳定基态'
ledger['notations_and_conventions']['shimizu_frame_relations'] = 'omega_wob = omega_prec - omega_rot; omega_prec = hbar K / J_perp^eff; R_3=0 为形状冗余约束，具有固定内禀 K 的体系能谱仍为 E_K(I) = Eintr + hbar^2[I(I+1)-K^2]/(2 J_perp)，首间距 hbar^2(K+1)/J_perp 与大 K 渐近 hbar^2 K/J_perp 相差 hbar^2/J_perp'

# Update source inputs for Lv 2022 and Nomura 2022
for s in ledger['source_inputs']:
    if s['source_id'] == 'lv-2022-evidence-against-wobbling-135pr':
        s['text_anchor'] = 'PDF p. 3, Table 1: 747.3 keV is 17/2- -> 15/2- with P = 0.04(+0.08/-0.13), Rac = 0.37(4), delta = -0.47(+0.09/-0.22), M1% ≈ 82%; 813.2 keV is 21/2- -> 19/2- with P = -0.03(+0.05/-0.12), Rac = 0.48(6), delta = -0.37(+0.10/-0.14), M1% ≈ 88%; 450.2 keV is 15/2- -> 13/2- with Rac = 0.49(4), delta = -0.31(+0.10/-0.13), M1% ≈ 91%; B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5); model estimate R ~ 1 hbar at bandhead.'
        s['claims_supported'] = [
          "747.3 keV 跃迁实测 P = 0.04(+0.08/-0.13), Rac = 0.37(4), 小根拟合解为 delta = -0.47(+0.09/-0.22), 条件 M1 占比约 82%",
          "813.2 keV 跃迁实测 P = -0.03(+0.05/-0.12), Rac = 0.48(6), 小根拟合解为 delta = -0.37(+0.10/-0.14), 条件 M1 占比约 88%",
          "450.2 keV 跃迁实测 Rac = 0.49(4), 小根拟合解为 delta = -0.31(+0.10/-0.13), 条件 M1 占比约 91%",
          "采用已测 526.2 keV 多极性与相对强度导出分支比 B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5)，对纯 1-phonon 摆动声子图像提出强有力质疑",
          "带头模型估计核芯转动仅 R ~ 1 hbar，破坏简谐强转动近似；QTR 在固定形变 (gamma=26 deg) 下给出准粒子向转轴倾斜的平面转动"
        ]
    if s['source_id'] == 'nomura-2022-questioning-wobbling-ibfm':
        s['text_anchor'] = 'PDF p. 2, Fig. 1 caption and text: 134Ce core of 135Pr mapped from relativistic energy density functional DD-PC1 with separable pairing (Gogny D1M used for 132Ba/128Xe); reproduces low-spin bands with M1-dominated interband transitions without wobbling phonons.'
        s['claims_supported'] = [
          "微观泛函映射的 IBFM 计算 (134Ce 偶偶核芯映射自相对论 DD-PC1 泛函与可分离配对力) 自然重现 135Pr 能谱与 M1 主导带间退激，无需假定横向摆动声子",
          "135Pr 核芯处于 gamma 软势阱中，展现出动态玻色子--费米子相互作用特征"
        ]

# Update claims
for c in ledger['claims_and_derivations']:
    if c['id'] == 'CLAIM-4-4-2':
        c['derivation_steps'] = [
          "依据单粒子四极密度重叠分析：底壳粒子型倾向短轴 s=2，顶壳空穴型倾向长轴 l=3，半满壳对准中轴 m=1",
          "显式建立几何指标 (s, m, l) 与动力学展开常数映射：准粒子沿短轴 A_s，最大惯量在中轴 A_m，横向曲率 C_m = (A_m - A_s) + A_s j/I，C_l = (A_l - A_s) + A_s j/I，临界分叉 I_c = j / (1 - J_s/J_m)",
          "指出 FA 模型下 TW 摆动能量在低自旋可呈现先升后降，单一能量下降非充要条件",
          "区分定域能量极小与线性动力学稳定性：C_m, C_l < 0 虽可在线性近似下由陀螺力保持运动稳定，但属能量极大，不能作为声子基态",
          "澄清倾斜转动若局限在主平面内保持时间反演复合对称，不自动导致手征对称性自发破缺"
        ]
    if c['id'] == 'CLAIM-4-4-4':
        c['derivation_steps'] = [
          "分析在束角分布二次有理式代数方程，指出实数根可有 0、1 或 2 个，特定 Lv/Matta 分支需结合实际响应与误差评估",
          "核实 Lv 等人 2022 Table 1 实测数据：747.3 keV (Rac = 0.37(4), delta = -0.47(+0.09/-0.22)), 813.2 keV (Rac = 0.48(6), delta = -0.37(+0.10/-0.14)), 450.2 keV (Rac = 0.49(4), delta = -0.31(+0.10/-0.13))，明确 M1 百分比为 delta 的条件变换",
          "核实同母态分支比 B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5) 属于作者在采用 526 keV 参数下的解释，对纯摆动声子提出重要质疑",
          "带头模型估计核芯转动 R ~ 1 hbar 破坏谐振展开；阐明微观 IBFM (134Ce 偶偶核芯基于 DD-PC1 泛函映射) 与固定形变 QTR 平面转动竞争解释"
        ]
    if c['id'] == 'CLAIM-4-4-5':
        c['derivation_steps'] = [
          "推导三轴摆动在 gamma -> 0 轴对称极限下的连续演化：形状冗余约束 R_3 = 0，固定 K 能谱 E_K(I) = Eintr + hbar^2[I(I+1)-K^2]/(2 J_perp)",
          "给出 Shimizu 轴对称 RPA 参考系代数关系 omega_wob = omega_prec - omega_rot，明确 K 为无量纲单粒子投影",
          "严格区分带头首能级间距 hbar^2(K+1)/J_perp 与大 K 渐近频率能量 hbar^2 K/J_perp，指出其相差 hbar^2/J_perp 量度项",
          "剖析 187Au 纵向摆动宣称中存在的质子底壳对准短轴与中轴假设冲突，核查 Guo 2022 小根解与采用量依赖性",
          "阐明重核区 Os/Pt/Hg 的 gamma 软势能面与多重形状共存，明确扁椭或形状共存决非证实轴对称假设"
        ]

# Update reader checks
ledger['reader_checks'] = [
  {"check": "半径余弦展开排序检查", "result": "逐项算出 cos(gamma-4pi/3) < cos(gamma-2pi/3) < cos(gamma) 导出 R_2 < R_1 < R_3，严格确立 s=2, m=1, l=3，修复旧稿代数符号错误"},
  {"check": "几何轴与 FA 动力学坐标映射检查", "result": "显式置换几何轴与局部展开指标：A_s, A_m, A_l，C_m=(A_m-A_s)+A_s j/I，C_l=(A_l-A_s)+A_s j/I，I_c=j/(1-J_s/J_m)，避免下标混淆"},
  {"check": "能量极小与线性稳定性区分检查", "result": "明确 C_m, C_l > 0 为能量极小与正能声子基态，C_m, C_l < 0 为旋转系能量极大，陀螺力可保线性稳定但不构稳定声子真空"},
  {"check": "163Lu 原件原表与采用量依赖检查", "result": "Table I 与 Table II 实测数据逐项核对，B_W(E2) ≈ 0.00530 e^2 b^2 导出 100–132 W.u.，注明 Table II 提取采用历史 delta=-3.10，注明核芯惯量为模型输出"},
  {"check": "135Pr 原件原表数值全面纠偏", "result": "核实 Lv 2022 Table 1：747.3 keV Rac=0.37(4), delta=-0.47(+0.09/-0.22); 813.2 keV Rac=0.48(6), delta=-0.37(+0.10/-0.14); 450.2 keV Rac=0.49(4), delta=-0.31(+0.10/-0.13)；分支比 0.7(+0.7/-0.5)；核芯转动 R ~ 1 hbar 为模型估算"},
  {"check": "Nomura 2022 核心泛函纠正", "result": "核实 134Ce 偶偶核芯映射自相对论 DD-PC1 泛函与可分离配对力 (Gogny D1M 用于 132Ba/128Xe)"},
  {"check": "Shimizu 高 K 进动参考系与能标检查", "result": "参考系代数式 omega_wob = omega_prec - omega_rot，K 无量纲，消除全带塌陷误断，确立首间距 hbar^2(K+1)/J_perp 与大 K 渐近 hbar^2 K/J_perp 的量度微商"},
  {"check": "187Au 对准几何与采用依赖检查", "result": "指出底壳粒子倾向短轴 s=2 与 LW 中轴假设分歧，带头 R ~ 1 hbar，采用 186Pt 导出带间 E2 仅数个 W.u.，澄清重区扁椭/共存非证实轴对称假设"}
]

with open('raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

with open('outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-4.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print('Updated section-4-4.json successfully.')

# Update knowledge note
note_path = 'knowledge/research-notes/a130-rewrite-orientation-cross-region-conditions-20261113.md'
with open(note_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_note_content = r'''---
type: research-note
title: "A130重写：跨核区非轴对称取向运动的微观机制、证据基线与迁移条件"
aliases: [A130 orientation cross region conditions 20261113, 跨核区取向对照研学笔记, G90 Section 4.4 证据研学]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
authors: [G90 (Gemini Tiered/high)]
created_from: "A130博士论文重写五章39节工程：第4.4节独占证据与科学推演（G90返修R2版）"
promotion_target: doctoral-nuclear-structure-foundations
evidence_sources: [
  campaign-g07-gorgen-2004-163lu-quadrupole-moments,
  odegard-2001-evidence-wobbling-163lu,
  jensen-2002-second-phonon-wobbling-163lu,
  matta-2015-transverse-wobbling-135pr,
  lv-2022-evidence-against-wobbling-135pr,
  guo-2021-comment-transverse-wobbling-135pr,
  nomura-2022-questioning-wobbling-ibfm,
  shimizu-2005-high-k-precession,
  sensharma-2020-longitudinal-wobbling-187au,
  guo-2022-low-spin-wobbling-187au,
  frauendorf-2014-transverse-wobbling,
  matsuzaki-2004-nuclear-inertia-and-wobbling,
  book-bohr-mottelson-nuclear-structure-vol2
]
tags: [doctoral-thesis, orientation-motion, transverse-wobbling, high-k-precession, 163lu, 135pr, 187au, evidence-audit]
---

# 同样叫三轴，为何有截然不同的取向运动

## Research Trigger

在原子核集体运动模型中，非轴对称形变参数 $\gamma$ 或相近的跃迁四极矩 $Q_t$ 常被用作表征三轴性的标量指标。然而在跨核区谱学比较中，同样具有三轴特征的原子核却表现出横向摆动（TW）、纵向摆动（LW）、手征双重带、高 $K$ 进动以及平面转动/能带混合等截然不同的动力学表现。本笔记旨在建立跨越 $A \approx 130$、稀土区（$A \approx 160$）以及超铪/重核区（$A \approx 180$--$190$）的系统比较基线，剖析惯量主轴排序、准粒子对准几何与自旋相空间对取向模式的微观控制机制，确立取向模式跨区迁移的物理判据与失效边界。

## Grounded Evidence

| 物理体系 / 案例 | 原始文献与定位符 (Locator) | 证据性质与物理条件 | 边界与反例批判 |
|---|---|---|---|
| $^{163}\mathrm{Lu}$ TSD1/TSD2 经典摆动基准 | Görgen 2004 (PRC 69, 031301(R)), PDF pp. 2–3, Table I, Table II | 完全实测原表：Table I 测定 TSD1 (8态) 与 TSD2 (7态) $Q_t \approx 6.7$--$9.9\ \mathrm{b}$ 分布；Table II 测定 TSD2 $\to$ TSD1 连接线 $B(E2)_{\mathrm{out}} \approx 0.54$--$0.70\ e^2\mathrm{b}^2$ (按标准单粒子估计 $B_{\mathrm{W}}(E2) \approx 0.0594 A^{4/3} e^2\mathrm{fm}^4 \approx 0.0053\ e^2\mathrm{b}^2$ 换算约 $100$--$132\ \mathrm{W.u.}$), 采用历史平均 $\delta \approx -3.10$ | 建立在强超形变 ($\varepsilon_2 \approx 0.38, \gamma \approx +20^\circ$)、高自旋 ($R \sim 15$--$30\hbar \gg 1$) 与孤立 $\pi i_{13/2}$ 态之上；$n_w$ 标签属模型指派；Table II 中的 $B(E2)/B(M1)$ 分离依赖所采用的平均混合比 $\delta$；核芯转动惯量非实测量 |
| $^{135}\mathrm{Pr}$ 低自旋横向摆动宣称 | Matta 2015 (PRL 114, 082501), PDF pp. 1–3, 5 | 实验报道：基于 $\pi h_{11/2}$ 负宇称激发带 (Band 3)，角分布拟合选定大根 $|\delta| > 1$ (如 747.0 keV 提取 $\delta = -2.0(4)$)，测得正线偏振度，宣称低自旋 TW 与 $E_{\mathrm{wob}}$ 下降 | 忽略了角分布拟合固有的二次有理式代数双根多义性；正线偏振未能排他性排除小根；单一能量下降趋势不构成 TW 充要条件 |
| $^{135}\mathrm{Pr}$ 极化双根仲裁与摆动检验 | Lv 2022 (PLB 824, 136840), PDF p. 3, Table 1; Guo 2021 (arXiv:2111.14150) | 实验批判与新测：747.3 keV ($17/2^- \to 15/2^-$) 实测 $P=0.04_{-0.13}^{+0.08}, R_{\mathrm{ac}}=0.37(4)$，小根 $\delta = -0.47_{-0.22}^{+0.09}$ (条件 M1 占 $\sim 82\%$)；813.2 keV ($21/2^- \to 19/2^-$) 实测 $P=-0.03_{-0.12}^{+0.05}, R_{\mathrm{ac}}=0.48(6)$，小根 $\delta = -0.37_{-0.14}^{+0.10}$ (条件 M1 占 $\sim 88\%$)；450.2 keV 实测 $R_{\mathrm{ac}}=0.49(4), \delta=-0.31_{-0.13}^{+0.10}$；同母态分支比 $B(E2; 747.3)/B(E2; 526.2) = 0.7_{-0.5}^{+0.7}$ 挑战纯摆动声子图像 | 强角关联与偏振联合解出小根，M1 占比较高；同母态分支比反映能带混合；带头核芯转动估计仅 $R \sim 1\hbar$，微扰谐振子展开适用性受限 |
| $^{135}\mathrm{Pr}$ 玻色子-费米子与微观竞争解释 | Nomura 2022 (PRC 106, 064313), PDF p. 2 Fig. 1 caption; Lawrie 2020 (PRC 101, 034306) | 微观理论竞争：基于相对论 DD-PC1 泛函与可分离配对映射 $^{134}\mathrm{Ce}$ 偶偶核芯势能面 (Gogny D1M 用于 132Ba/128Xe)，IBFM 计算表明三轴 $\gamma$ 软核芯与价准粒子耦合自然产生低激发带与 M1 主导带间跃迁；固定形变 ($\varepsilon_2=0.16, \gamma=26^\circ$) QTR 模型放开 $j$ 冻结后呈现平面转动，TiP 框架给出倾斜进动替代解释 | 不同模型（IBFM, QTR, TiP）在同一实验谱线下的竞争表明低自旋核态具有丰富微观机制，摆动声子假说并非唯一相容理论 |
| 高 $K$ 进动：三轴摆动的轴对称极限 | Shimizu, Matsuzaki, Matsuyanagi 2005 (PRC 72, 014306), PDF pp. 2–3, 5–6 | 微观理论推导：在 $\gamma \to 0$ 轴对称极限下，形状转动冗余约束 $R_3=0$，绝热能带满足 $E_K(I) = E_{\text{intr}} + \frac{\hbar^2}{2\mathcal{J}_\perp}[I(I+1)-K^2]$；首能级间距为 $\frac{\hbar^2(K+1)}{\mathcal{J}_\perp}$，大 $K$ 渐近频率为 $\hbar\omega_{\mathrm{prec}} \simeq \frac{\hbar^2 K}{\mathcal{J}_\perp}$；参考系关系满足 $\omega_{\mathrm{wob}} = \omega_{\mathrm{prec}} - \omega_{\mathrm{rot}}$ | 统一了三轴摆动与高 $K$ 进动的角动量取向几何，明确区分随体旋转系与实验室固定 $K$ 参考系，首间距与渐近频率相差 $\hbar^2/\mathcal{J}_\perp$ |
| $^{187}\mathrm{Au}$ 纵向摆动宣称与实验检验 | Sensharma 2020 (PRL 124, 052501), PDF pp. 1–3; Guo 2022 (PLB 828, 137010), PDF pp. 2–4 | 实验争论：Sensharma 宣称 $\pi h_{9/2}$ 纵向摆动；Guo 2022 实测 376 keV ($11/2^- \to 9/2^-$) 与 462 keV ($15/2^- \to 13/2^-$) 支持小根 $\delta \approx -0.26, -0.28$，通过采用 $^{186}\mathrm{Pt}$ 核芯或带内 $B(E2)_{\mathrm{in}} \sim 100$--$200\ \mathrm{W.u.}$ 估算带间跃迁仅数个 W.u. ($B(E2)_{\mathrm{out}}/B(E2)_{\mathrm{in}} < 0.1$) | 奇质子处于 $h_{9/2}$ 底壳倾向短轴 $s$ 对准与 LW 要求的中轴 $m$ 对准产生模型分歧；带头估计 $R \sim 1\hbar$ 缺乏恢复力；支持长椭--扁椭形状共存与多构型混合解释 |
| 重区 Os/Pt/Hg 形状共存与 $\gamma$ 软度 | Prochniak & Rohozinski 2009 (JPG 36, 123101), PDF pp. 36–39 | 唯象与微观计算：微观势能面在 $\gamma$ 方向存在平缓软势与形状涨落，存在长椭--扁椭形状共存 | 不可简单给整个 $A \approx 190$ 区域贴统一固定扁椭或轴对称标签，扁椭/共存决不能当作证实了轴对称旋转假设 |

## Provisional Reasoning

### 1. 电荷几何主轴严格排序与局部 FA 动力学坐标置换

- **电荷几何半径严格展开**：在 Lund 约定下，$R_k = R_0 \left[ 1 + \sqrt{\frac{5}{4\pi}}\beta_2 \cos\left(\gamma - \frac{2\pi}{3} k\right) \right]$。在 $0^\circ < \gamma < 60^\circ$ 内严格导出 $\cos(\gamma - 4\pi/3) < \cos(\gamma - 2\pi/3) < \cos\gamma \implies R_2 < R_1 < R_3$。即**最短几何轴 $s = 2$；中间几何轴 $m = 1$；最长几何轴 $l = 3$**。
- **坐标置换与映射**：第\ref{sec:3-3}节 FA 展开指标中局部 1 轴沿准粒子顺排方向，局部 2 轴沿最大转动惯量轴。在横向摆动中，准粒子沿短轴 $s=2$，最大惯量在中轴 $m=1$。显式采用主轴标识 $(s, m, l)$：
  $$ C_m = (A_m - A_s) + A_s \frac{j}{I}, \qquad C_l = (A_l - A_s) + A_s \frac{j}{I}, $$
  $$ \hbar\omega_{\text{wob}} = 2\sqrt{(a_m I + A_s j)(a_l I + A_s j)}, \qquad I_c = \frac{j}{1 - \mathcal{J}_s / \mathcal{J}_m}. $$
- **刚体与无旋流惯量主轴机制**：刚体绕最短轴 $s=2$ 惯量最大 ($\mathcal{J}_s^{\text{rig}} > \mathcal{J}_m^{\text{rig}} > \mathcal{J}_l^{\text{rig}}$)；无旋流在 $\gamma = 30^\circ$ 处绕中轴 $m=1$ 惯量最大 ($\mathcal{J}_m^{\text{irr}} > \mathcal{J}_s^{\text{irr}}, \mathcal{J}_l^{\text{irr}}$)。微观配对相互作用使有效惯量具有频率依赖性，不必然受两者包络限制。

### 2. 第3章核心结论向第4章的贯彻：频率演化、稳定性与倾斜边界

- **TW 摆动能量非单调性**：在 $A_m < A_s \le A_l$ 下，$a_m < 0, a_l \ge 0$。在低自旋区间，由于因子 $(a_l I + A_s j)$ 随自旋线性上升，$\hbar\omega_{\text{wob}}$ 完全可能呈现**先上升后下降**的非单调演化。因此，**单一摆动能量下降不是 TW 的充要条件**。
- **定域能量极小与线性动力学稳定性的区别**：$C_m > 0$ 且 $C_l > 0$ 为势能极小处良定义的正能声子激发基态。若 $C_m < 0$ 且 $C_l < 0$，乘积为正且在陀螺科氏力下系统可具备线性稳定性（类似于刚体绕最小惯量轴转动的能量极大稳定态），但在物理上对应旋转坐标系的能量极大，不能作为集体声子激发的稳定真空。
- **倾斜转动不自动蕴含手征破缺**：角动量矢量偏离主轴若局限在主平面内（Planar Tilt），时间反演复合对称性 $\mathcal{T}\mathcal{R}_k(\pi)$ 仍保持，不破缺手征性；手征破缺必须在三个主轴上同时具备非零分量。

### 3. $^{163}\mathrm{Lu}$ 的实测原表数据分析与物理边界

- Görgen et al. (2004) Table I 中 TSD1 与 TSD2 的 $Q_t$ 分布在 $6.7$--$9.9\ \mathrm{b}$ 区间。Table II 实测 $B(E2)_{\mathrm{out}} \approx 0.54$--$0.70\ e^2\mathrm{b}^2$ 对应约 $100$--$132\ \mathrm{W.u.}$ 的集体增强。
- 明确 Table II 中的 $B(E2)$ 与 $B(M1)$ 提取依赖于采用的历史平均混合比 $\delta = -3.10_{-0.44}^{+0.36}$（外推假定）；模型惯量属于拟合或微观推转参数，非实测物理量。

### 4. $^{135}\mathrm{Pr}$ 的角分布双根与多元模型竞争

- Lv et al. (2022) Table 1 实测：$747.3\ \mathrm{keV}$ 跃迁 $R_{\mathrm{ac}}=0.37(4), \delta = -0.47_{-0.22}^{+0.09}$ (条件 M1 占 $82\%$)；$813.2\ \mathrm{keV}$ 跃迁 $R_{\mathrm{ac}}=0.48(6), \delta = -0.37_{-0.14}^{+0.10}$ (条件 M1 占 $88\%$)；$450.2\ \mathrm{keV}$ 跃迁 $R_{\mathrm{ac}}=0.49(4), \delta = -0.31_{-0.13}^{+0.10}$ (条件 M1 占 $91\%$)。
- 同母态分支比 $B(E2; 747.3)/B(E2; 526.2) = 0.7_{-0.5}^{+0.7}$ 挑战纯摆动声子图像；带头核芯转动模型估计仅 $R \sim 1\hbar$。
- 微观竞争模型：Nomura 2022 IBFM 基于相对论 DD-PC1 泛函与可分离配对力映射 $^{134}\mathrm{Ce}$ 软核芯势能面，天然重现 M1 主导带间退激；固定形变 QTR 模型放开 $j$ 冻结后呈现平面转动（Planar Rotation）；TiP 模型给出倾斜进动解释。

### 5. 高 $K$ 进动极限与重区形状共存边界

- Shimizu et al. (2005) 轴对称高 $K$ 进动参考系关系：$\omega_{\mathrm{wob}} = \omega_{\mathrm{prec}} - \omega_{\mathrm{rot}}$，其中 $\omega_{\mathrm{prec}} = \frac{\hbar K}{\mathcal{J}_\perp^{\text{eff}}}$。绝热转子能谱 $E_K(I) = E_{\text{intr}} + \frac{\hbar^2}{2\mathcal{J}_\perp}[I(I+1)-K^2]$ 的首能级间距严格为 $\frac{\hbar^2(K+1)}{\mathcal{J}_\perp}$，大 $K$ 渐近频率为 $\frac{\hbar^2 K}{\mathcal{J}_\perp}$，相差量度项 $\hbar^2/\mathcal{J}_\perp$。
- $^{187}\mathrm{Au}$ 质子处于 $h_{9/2}$ 底壳倾向短轴对准，与 LW 中轴对准模型设定分歧；Guo et al. (2022) 实测小根 $\delta \approx -0.26, -0.28$，采用 $^{186}\mathrm{Pt}$ 估算带间 $E2$ 仅数个 W.u.。重核区 Os/Pt/Hg 表现为软三轴与多重形状共存。

## Failure Conditions

- 将质量区名称作为排他互斥的物理机制标签。
- 忽略二次有理式代数方程的根数复杂性，单向采信符合模型偏好的解。
- 忽视小核芯角动量（$R \sim 1\hbar$）下简谐近似的局限性。
- 将模型拟合转动惯量参数误当作实验直接测量的物理量。

## Promotion or Rejection History

| Date | Event | Previous State | New State | Reason / Triggering Evidence | Target or Successor |
|---|---|---|---|---|---|
| 2026-11-13 | 建立第4.4节独占研学笔记 | none | provisional | 承接F02/F03合同与39节架构，全面固化跨核区取向对照微观证据链 | doctoral-nuclear-structure-foundations |
| 2026-11-13 | G90全面深化返修 R1 | provisional | provisional | 逐式推导Rk电荷半径排序R2<R1<R3，厘清惯量机制，结合3.2/3.3/3.6阐明TW非单调性 | doctoral-nuclear-structure-foundations |
| 2026-11-13 | G90精准修订 R2 | provisional | provisional | 响应父审意见：更正Lv表1数据(Rac=0.37/0.48/0.49, 813小根=-0.37)、更正Nomura DD-PC1泛函、区分定域极小与线性动力学稳定、消除全带塌缩并显式置换几何与FA展开坐标 | doctoral-nuclear-structure-foundations |
'''

with open(note_path, 'w', encoding='utf-8') as f:
    f.write(new_note_content)

print('Updated knowledge note successfully.')
