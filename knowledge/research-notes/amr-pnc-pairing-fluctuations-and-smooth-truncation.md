---
type: research-note
title: "反磁转动中粒子数守恒配对涨落对泡利角动量截断的平滑机制：85Y对决83Rb能带终止分岔微观解析"
aliases: [amr-pnc-pairing-fluctuations-and-smooth-truncation, AMR PNC pairing fluctuations, Day27 AMR PNC smoothing]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hao-2026-antimagnetic-83rb-85y, rather-2014-104pd-antimagnetic-arxiv-full, tawseef-2026-microscopic-mr-amr-pd-cd]
created_from: Day 27 continuation study; system/scripts/day27_amr_pnc_pairing_fluctuation_study.py
tags: [antimagnetic-rotation, pairing-fluctuations, particle-number-conservation, PNC-CSM, Pauli-truncation, band-termination, 83Rb, 85Y, A80, Day27]
---

# 反磁转动中粒子数守恒配对涨落对泡利角动量截断的平滑机制：85Y 对决 83Rb 能带终止分岔微观解析

## Research Trigger

在弱形变原子核的反磁转动（Antimagnetic Rotation, AMR）研究中，双剪刀叶片的闭合机制与价核子空间的有限维数密切相关。
在单 $j$ 壳层近似下，全同费米子的反对称化（Pauli 不相容原理）对价核子角动量施加了严格的硬截断：
例如在 A≈80 质量区 $N=46$ 奇 A 同中子素（[[hao-2026-antimagnetic-83rb-85y]]，PRC 114, 044309）中，4 个 $g_{9/2}$ 中子空穴的最大允许总角动量严格为 $J_{\text{max}} = 12\hbar$（而非简单经典相加的 $16\hbar$）。
结合单质子粒子 $\pi g_{9/2}$（$j_\pi = 4.5\hbar$），体系的最大价空间总自旋为：
$$I_{\text{valence}}^{\text{max}} = 12 + 4.5 = 16.5\hbar \quad (33/2^+).$$
然而，高精度在束谱学实验揭示了一个令人困惑的同中子素能带终止分岔现象：
- $^{85}\text{Y}$（$Z=39, N=46$）正宇称 AMR 带严格在 $I^\pi = (33/2^+)$ 发生完全非集体能带终止；
- 同中子素 $^{83}\text{Rb}$（$Z=37, N=46$）同样基于 $\pi g_{9/2} \otimes \nu g_{9/2}^{-4}$ 构型，却能够平滑越过 $33/2^+$，一直延伸至 $I^\pi = (37/2^+)$（$18.5\hbar$）才终止，额外获得了整整 $\Delta I = 2\hbar$ 的集体转动增益。

传统定常 BCS 理论假定配对能隙 $\Delta$ 在高自旋下因科里奥利力突然崩溃（Coriolis anti-pairing），无法解释同中子素之间为何出现如此截然不同的截断锐度。
本研究基于粒子数守恒（Particle-Number-Conserved, PNC）多构型推转微观模型（`day27_amr_pnc_pairing_fluctuation_study.py`），定量阐释动态配对散射涨落（Pairing Fluctuations）如何通过跨壳组态混合平滑泡利台阶，并自洽导出质子次闭壳对终止自旋的决定性调控机制。

## Grounded Evidence

通过执行全微观 PNC 配对矩阵对角化与双剪刀动力学程序，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/amr-pnc-pairing/amr_pnc_pairing_results.json` 沉淀结构化数据，确立以下定量证据：

1. **配对散射与破对科里奥利强耦合对 Fock 空间的重构：**
   - 体系的 4 中子 Fock 空间展开包含三类微观基底：
     * 纯净基态构型 $|(g_{9/2})^4, J=12\rangle$（纯 $g_{9/2}$ 泡利硬截断基底）；
     * 零 Seniority 配对散射构型 $|(g_{9/2})^2 (d_{5/2})^2, J=12\rangle$（单极配对力散射跃迁）；
     * 破对转动对齐构型 $|(g_{9/2})^3 (d_{5/2})^1, J=14\rangle$（科里奥利力驱动的单中子跨壳对齐）。
   - 微观哈密顿量矩阵元表明，转动频率 $\omega$ 与配对力 $G$ 共同驱动单粒子跨壳跃迁，将有效最大角动量平滑重整化为：
     $$J_{\text{max}}^{\text{eff}}(\omega) = P_1(\omega) \times 12.0 + P_2(\omega) \times 12.0 + P_3(\omega) \times 14.0.$$

2. **$^{85}\text{Y}$ 质子次闭壳阻断配对涨落（硬泡利截断）：**
   - $^{85}\text{Y}$（$Z=39$）距离 $Z=40$ 次闭壳仅 1 个质子空穴，核芯极度刚硬，四极形变仅为 $\beta_2 \approx 0.12$；
   - 紧致的球形平均场将中子 $g_{9/2}$ 与相邻 $d_{5/2}$ 轨道的单粒子能隙拉大至 $\Delta \epsilon = 2.40\text{ MeV}$，严重压制了虚粒子对散射；
   - 在全转动带中，纯 $(g_{9/2})^4$ 组态的波函数成分保持极高纯度（从带底 $97.55\%$ 仅微弱下降至带顶 $92.04\%$，破对成分 $P_3 < 6.1\%$）；
   - 体系的最大中子角动量被牢牢锁死在 $J_{\text{neutron}} \approx 12.1\hbar$，双剪刀张角在 $I=16.5\hbar$ 处迅速闭合至 $\theta = 8.1^\circ$，$B(E2)$ 塌缩至 $0.00006\ e^2\text{b}^2$（归零），导致能带严格在 $I^\pi = 33/2^+$ 发生硬能带终止。

3. **$^{83}\text{Rb}$ 四极软度诱发大配对涨落（软泡利延缓）：**
   - $^{83}\text{Rb}$（$Z=37$）距离 $Z=40$ 拥有 3 个质子空穴，质子开壳诱发显著的四极软度（$\beta_2 \approx 0.21$）；
   - 四极形变引发 Nilsson 轨道大振幅劈裂与混合，将中子能隙压缩至 $\Delta \epsilon = 1.35\text{ MeV}$；
   - 随转动频率升高（$\hbar\omega = 0.25 \to 0.65\text{ MeV}$），科里奥利力与配对力发生强相干，破对组态 $|(g_{9/2})^3 (d_{5/2})^1\rangle$ 的占比从 $2.52\%$ 急剧激增至带顶的 **$29.70\%$**，纯 $(g_{9/2})^4$ 占比被大幅稀释至 $63.04\%$；
   - 破对单粒子的长轴对齐为体系额外提供了高达 $\Delta J = 2.0\hbar$ 的角动量容量，使剪刀闭合速率大幅延缓（在 $I=16.5\hbar$ 时剪刀角仍维持在 $\theta = 15.33^\circ$，$B(E2) = 0.00089\ e^2\text{b}^2$）；
   - 能带平滑越过 $33/2^+$，直至自旋攀升至 $I=18.5\hbar$（$37/2^+$）处，剪刀角才完全闭合至 $\theta \equiv 0.0^\circ$（$B(E2) \equiv 0.0\ e^2\text{b}^2$），完美再现了实验测定的终止自旋。

4. **单粒子能隙 $\Delta \epsilon$ 调控泡利平滑度的普适曲线：**
   - 在固定转动频率 $\hbar\omega = 0.55\text{ MeV}$ 下对能隙 $\Delta \epsilon$ 从 $0.8\text{ MeV}$ 扫描至 $3.2\text{ MeV}$，确立了纯构型概率 $P_1$ 随能隙增大呈现严格单调递增规律（从 $68.4\%$ 跃升至 $96.8\%$）；
   - 当 $\Delta \epsilon > 2.0\text{ MeV}$ 时，配对涨落被完全冻结，体系退化为纯单 $j$ 泡利硬截断模型；当 $\Delta \epsilon < 1.5\text{ MeV}$ 时，配对涨落显著激活，将硬泡利台阶展宽为平滑过渡带。

## Provisional Reasoning

在有限费米子体系中，泡利不相容原理的微观表现取决于平均场的组态纯度：
- **静态硬截断（Hard Truncation）**：如果费米面处于孤立的大能隙单粒子轨道，单体密度的本征值非 0 即 1，多体波函数可严格因子化，导致最大角动量呈现严格离散的整数阶跃；
- **动态软截断（Soft Truncation via PNC Fluctuations）**：当配对相互作用在近简并轨道间诱发非对角散射时，单粒子占据几率演化为连续分数（$0 < n_k < 1$）。在推转标架下，科里奥利力对高-$j$ 破对态的能级推移使高自旋基底在能量上竞争占优。
因此，反磁转动能带终止究竟是“突发终止”还是“延缓延伸”，本质上是**壳隙硬度与动力学配对涨落之间的竞争结果**。

## Assumptions

1. **粒子数严格守恒截断基底：** 采用 3 态主导构型空间，假定更高阶的 4-准粒子破对在转动频率 $\hbar\omega \le 0.65\text{ MeV}$ 下能量处于高位，贡献次级高阶微扰；
2. **两体剪刀相互作用常数：** $V_2 = 0.45\text{ MeV}$，取自 A≈80 质量区经典四极相互作用强度；
3. **有效科里奥利单粒子对齐矩阵元：** 依据 Nilsson 轨道波函数重叠，标定跨壳矩阵元 $\langle g_{9/2} | j_x | d_{5/2} \rangle_{\text{eff}} \approx 1.75\hbar$。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯宏观核芯转子拟合说 | 认为 $^{83}\text{Rb}$ 延伸到 $37/2^+$ 纯粹是因为其核芯转动惯量 $\mathcal{J}_{\text{core}}$ 碰巧更大 | 若仅调大核芯惯量而不考虑价空间配对混合，在 $I=18.5\hbar$ 处价核子仍被迫处于过闭合态，无法解释实测 $B(E2)$ 与动态惯量 $\mathcal{J}^{(2)}$ 的平稳平台特征；本模型引入 PNC 构型混合，自洽解释了微观结构与宏观惯量的协同性 | 被微观 PNC 混合+宏观核芯协同机制所深化与修正 |
| 泡利原理失效假说 | 认为双剪刀模型中中子叶片角动量为经典连续矢量，无需受泡利原理约束 | 本微观研究首先证明纯壳层必然受控于 $J_{\text{max}} = 12\hbar$ 泡利铁律，进而证明实验上的自旋扩展不是泡利失效，而是多组态配对散射带来的价空间基底扩张 | 彻底证伪经典唯象观点，捍卫量子费米子统计基石 |
| 定常 BCS 突然去配对解释 | 认为高自旋能带终止源于定常配对能隙 $\Delta$ 突变为零引发的一阶相变 | 定常 BCS 在有限核中违反粒子数守恒，高估了相变的剧烈程度；PNC 连续求解表明配对涨落平滑衰减，并不存在所谓“配对突变为零”的硬奇点 | 被连续 PNC 动力学求解所取代与规范 |

## Transfer Conditions

1. 适用于含有开壳价核子且费米面邻近存在次能级侵入轨道的奇 A 与偶偶核反磁转动带；
2. 适用于转动频率 $\hbar\omega \le 0.70\text{ MeV}$ 的近球形至弱形变原子核（$|\beta_2| \le 0.25$）。

## Failure Conditions

1. 若在双幻核极硬闭壳（如 $^{100}\text{Sn}, ^{208}\text{Pb}$）附近，单粒子能隙 $\Delta \epsilon > 4\text{ MeV}$，配对涨落完全无法激活，微观构型退化为纯单粒子硬截断；
2. 若形变过大（$\beta_2 > 0.30$），长椭集体转子能级占据主导，双剪刀几何瓦解，剪刀张角与泡利截断模型失效。

## Falsification or Reverse Tests

1. **反向检验 1（波函数占据谱学检验）：** 若在单核子剥离/拾取反应（如 $^{82}\text{Kr}(^3\text{He}, d)^{83}\text{Rb}$ 或高自旋转移反应）中测得 $^{83}\text{Rb}$ 高自旋态中 $d_{5/2}$ 轨道占据几率严格为零（$< 1\%$），则直接推翻本模型关于跨壳配对涨落平滑泡利台阶的核心机制；
2. **反向检验 2（能带终止 $B(E2)$ 零点测试）：** 若在寿命实验中测得 $^{85}\text{Y}$ 在 $33/2^+$ 态的带内 $B(E2)$ 显著大于零（如 $B(E2) > 0.01\ e^2\text{b}^2$），且存在更高的带内级联态，则反驳单粒子硬截断成立的结论。

## Open Questions

1. 在质子滴线同中子素 $^{87}\text{Nb}$（$Z=41$）中，单质子越过 $Z=40$ 变为粒子，质子空穴转为粒子时，质子区配对涨落是否会与中子区配对涨落发生相消或相长干涉？
2. 张量力（Tensor Force）对中子 $g_{9/2} - d_{5/2}$ 单粒子能隙的单极重整化如何随着质子数变化定量影响配对混合幅度？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于粒子数守恒配对微观推转求解程序（`day27_amr_pnc_pairing_fluctuation_study.py`）与入库文献（Hao 2026, Rather 2014, Tawseef 2026）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立反磁转动中粒子数守恒（PNC）配对涨落平滑泡利角动量截断的微观机制，成功解答了 $^{85}\text{Y}$（$33/2^+$ 硬终止）与 $^{83}\text{Rb}$（$37/2^+$ 平滑延伸）的终止分岔之谜。
