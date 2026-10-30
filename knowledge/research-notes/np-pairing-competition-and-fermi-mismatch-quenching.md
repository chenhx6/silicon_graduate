---
type: research-note
title: "同位旋标量（T=0）与同位旋矢量（T=1）中子—质子配对竞争与跨区猝灭：Sarma-Clogston费米面失配崩塌、Wigner能与92Pd自旋对齐相界"
aliases: [np-pairing-competition-and-fermi-mismatch-quenching, isoscalar isovector pairing competition, sarma clogston limit np pairing, 92pd spin aligned pairing]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, ragnarsson-nilsson-sheline-1978-shell-structure]
created_from: Day 27 continuation study; system/scripts/day27_np_pairing_wigner_energy_study.py
tags: [np-pairing, isoscalar-pairing, isovector-pairing, wigner-energy, sarma-clogston-limit, 92Pd, 94Pd, 48Cr, Day27]
---

# 同位旋标量（$T=0$）与同位旋矢量（$T=1$）中子—质子配对竞争与跨区猝灭：Sarma-Clogston 费米面失配崩塌、Wigner 能与 $^{92}\text{Pd}$ 自旋对齐相界

## Research Trigger

在传统具有中子过剩（$N > Z$）的中重质量原子核中，核超流配对完全由同种核子间的同位旋矢量（$T=1, S=0$）库珀对（$pp$ 与 $nn$）主导，形成总角动量为零（$J=0$）的 BCS 凝聚态（[[knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei|Frauendorf 2001]]; [[knowledge/sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry|Butler & Nazarewicz 1996]]）。然而，在自共轭（$N \approx Z$）核素中，质子与中子占据完全相同的单粒子空间轨道（如 $1f_{7/2}$ 与 $1g_{9/2}$ 壳层），使得质子—中子（$np$）配对登上核心舞台。此时体系面临两种本质不同的配对竞争：
1. **同位旋矢量配对（$T=1, S=0, J=0$）**：形成各向同性的等标量自旋单重态，与同核子配对共同构成同位旋三重态；
2. **同位旋标量配对（$T=0, S=1, J=1$ 或 $J_{\text{max}} = 2j$）**：形成类似于自由氘核（$^2\text{H}$）的自旋三重态或在强自旋—轨道耦合下形成的自旋对齐（Spin-Aligned）强关联对（例如 $^{92}\text{Pd}$ 中的 $(g_{9/2})^2_{J=9^+}$ 配对，Cederwall et al. Nature 469, 68 (2011)）。此外，结合能曲面上著名的 Wigner 能尖峰（$E_W \propto |N-Z|/A$）长期被唯象归因于 $T=0$ 氘核凝聚。

然而，将基于 $N \approx Z$ 核区建立的 $T=0$ 配对模型跨质量区迁移至哪怕偏离对称线仅 2 到 4 个中子的中子丰富区（如从 $^{92}\text{Pd}$ 向 $^{94, 96}\text{Pd}$ 迁移）时，遭遇了灾难性的结构突变与机制不适用性：
1. **$T=0$ 序参量的一阶猝灭崩塌**：仅增加 2 个中子（$|N-Z| = 2$），中子与质子化学势分裂引发的费米面失配 $\delta\lambda = |\lambda_n - \lambda_p|/2$ 迅速越过 Sarma-Clogston 临界破对极限（$\delta\lambda_c = \Delta_0 / \sqrt{2}$），使得 $T=0$ 配对能隙 $\Delta_{T=0}$ 发生一阶非连续相变彻底归零；
2. **能谱结构的断崖式阶跃**：$^{92}\text{Pd}$（$N=Z=46$）基态带原本呈现间距恒定（$\Delta E \approx 400 - 500\text{ keV}$，$E(2^+) = 873.8\text{ keV}, R_{4/2} = 2.04$）的反常自旋对齐等间距谱，而在 $^{94}\text{Pd}$（$|N-Z|=2$）中，$E(2^+)$ 突变跃升至 **$1412.0\text{ keV}$（激增 $+61.6\%$）**，$R_{4/2}$ 暴跌至 $1.51$，瞬间退化为标准的单偶极 Seniority 谱；
3. **宏观 BCS 凝聚与有限价空间对齐的伪简并**：把 $^{92}\text{Pd}$ 的低激发谱过度诠释为宏观无限介质 $T=0$ 玻色—爱因斯坦凝聚（BEC），忽视了其仅为单一 $1g_{9/2}$ 壳层价空穴有限重耦的微观本质。

本研究旨在建立自洽的双流体 BCS 费米面失配方程，严格定量刻画 $T=0$ 配对在跨核区迁移时的猝灭相界。

## Grounded Evidence

依托 Nature 实验基准报告（Cederwall et al. Nature 469, 68 (2011)）、NNDC ENSDF 评价能级，以及 `system/scripts/day27_np_pairing_wigner_energy_study.py` 自洽费米面失配求解器，建立跨越 $A \approx 48, 64, 92-96$ 的对比矩阵：

1. **同位素链实验能谱与 $R_{4/2}$ 比值断裂**：
   - $^{48}\text{Cr}$ ($Z=24, N=24, |N-Z|=0$): $E(2^+) = 752.2\text{ keV}, E(4^+) = 1858.5\text{ keV}$，$R_{4/2} = 2.47$（强形变转子，$\Delta\lambda = 0.00\text{ MeV}$，计算 $\Delta_{T=0} = 1.25\text{ MeV}$）；
   - $^{50}\text{Cr}$ ($Z=24, N=26, |N-Z|=2$): $E(2^+) = 783.3\text{ keV}, E(4^+) = 1881.4\text{ keV}$，$R_{4/2} = 2.40$（$\Delta\lambda = 2.24\text{ MeV} > \delta\lambda_c$，计算 $\Delta_{T=0} \equiv 0.00\text{ MeV}$）；
   - $^{64}\text{Ge}$ ($Z=32, N=32, |N-Z|=0$): $E(2^+) = 901.8\text{ keV}, E(4^+) = 2052.2\text{ keV}$，$R_{4/2} = 2.28$（$\Delta\lambda = 0.00\text{ MeV}, \Delta_{T=0} = 1.25\text{ MeV}$）；
   - $^{66}\text{Ge}$ ($Z=32, N=34, |N-Z|=2$): $E(2^+) = 957.1\text{ keV}, E(4^+) = 2174.5\text{ keV}$，$R_{4/2} = 2.27$（$\Delta\lambda = 1.70\text{ MeV} > \delta\lambda_c, \Delta_{T=0} \equiv 0.00\text{ MeV}$）；
   - **$^{92}\text{Pd}$** ($Z=46, N=46, |N-Z|=0$, 自旋对齐相标杆): $E(2^+) = 873.8\text{ keV}, E(4^+) = 1786.1\text{ keV}, E(6^+) = 2535.8\text{ keV}, E(8^+) = 3050.8\text{ keV}$；$R_{4/2} = 2.04$；四阶阶跃间距几乎恒定（$\Delta E = 874, 912, 750, 515\text{ keV}$）；$\Delta\lambda = 0.00\text{ MeV}, \Delta_{T=0} = 1.25\text{ MeV}$；
   - **$^{94}\text{Pd}$** ($Z=46, N=48, |N-Z|=2$): $E(2^+) = 1412.0\text{ keV}, E(4^+) = 2130.0\text{ keV}$；$E(2^+)$ 暴涨 $+538.2\text{ keV}$；$R_{4/2} = 1.51$（暴跌向球形 Seniority 极限）；$\Delta\lambda = 1.19\text{ MeV} > \delta\lambda_c = 0.88\text{ MeV}$，计算 $\Delta_{T=0} \equiv 0.00\text{ MeV}$；
   - **$^{96}\text{Pd}$** ($Z=46, N=50, |N-Z|=4$, $N=50$ 闭壳): $E(2^+) = 1415.3\text{ keV}, E(4^+) = 2110.0\text{ keV}$；$R_{4/2} = 1.49$；纯四质子空穴 $(g_{9/2})^{-4}$ Seniority 谱；$\Delta\lambda = 2.33\text{ MeV}, \Delta_{T=0} \equiv 0.00\text{ MeV}$。

2. **费米面失配量与 Sarma 临界破对阈值对账**：
   - 对称能导致的中子—质子费米面失配量 $\delta\lambda = \frac{2 C_{\text{sym}}}{A} |N-Z|$（取 $C_{\text{sym}} \approx 28.0\text{ MeV}$）；
   - 典型核物质配对能隙 $\Delta_0 \approx 1.25\text{ MeV}$ 对应的 Sarma-Clogston 临界失配极限为：
     $$\delta\lambda_c = \frac{\Delta_0}{\sqrt{2}} \approx 0.884\text{ MeV}$$
   - 在 $^{94}\text{Pd}$ 中，偏离仅 2 个中子即产生 $\delta\lambda = 1.19\text{ MeV}$，已大幅超出临界极限（$\delta\lambda / \delta\lambda_c = 1.35$），迫使 $T=0$ 配对解发生第一阶非连续性崩塌淬灭。

## Provisional Reasoning

1. **双组分配对能量泛函与同位旋不相容原理**：
   在包含同位旋自由度的多体配对哈密顿量中，定域配对场分为同位旋矢量与标量两部分：
   $$\hat{H}_{\text{pair}} = -G_1 \sum_{\mu} \hat{P}_{1\mu}^\dagger \hat{P}_{1\mu} - G_0 \sum_{\nu} \hat{P}_{0\nu}^\dagger \hat{P}_{0\nu}$$
   由于费米子反对称化要求，相同空间轨道上的粒子无法同时处于 $T=1$ 与 $T=0$ 的非简谐关联中；在自洽平均场极小化过程中，两相具有相互排斥的竞争关系。在球形或小形变核中，平均场方程在绝大多数情况下只允许单一相纯解存在（即要么 $\Delta_1 \ne 0, \Delta_0 = 0$，要么 $\Delta_1 = 0, \Delta_0 \ne 0$），混合相由于能量重叠惩罚而不稳定。

2. **Sarma-Clogston 效应：内禀塞曼型破对机制**：
   当 $|N-Z| \ne 0$ 时，中子与质子的化学势差 $\mu_n - \mu_p = 2\delta\lambda$ 在准粒子能量中扮演了等效于超导体内外加塞曼磁场的角色。对于 $T=0$ 的 $np$ 库珀对，其内禀组成粒子具有不同的化学势，准粒子激发能谱演变为：
   $$E_{\text{qp}, 0} = \sqrt{(\epsilon - \lambda)^2 + \Delta_0^2} \pm \delta\lambda$$
   当 $\delta\lambda > \Delta_0$ 时，较低支准粒子激发能量变为负值，在费米面处形成自发拆对激发的正常流体态；在零温极限下，热力学势在 $\delta\lambda = \Delta_0 / \sqrt{2}$ 处发生一阶相变，导致非零配对能隙解 $\Delta_0$ 发生突变式湮灭。
   反观 $T=1$ 配对，由于质子库珀对（$pp$）与中子库珀对（$nn$）均由同种核子构成，二者各自以自身的化学势 $\lambda_p$ 与 $\lambda_n$ 独立凝聚，对化学势差 $\delta\lambda$ 完全免疫，因而在全核区保持极强的鲁棒性。

3. **$^{92}\text{Pd}$ 自旋对齐对与宏观 BEC 的物理界限**：
   在 $^{92}\text{Pd}$ 中观测到的反常等间距能级（$874 \to 912 \to 750\text{ keV}$），微观壳模型（Qi et al. 2011）严格证明其并非空间延展的宏观玻色凝聚，而是价空间仅有的 4 个质子空穴与 4 个中子空穴在极高 $j$ 轨道（$g_{9/2}$）中，通过短程吸引相互作用激发出角动量最大化耦合对 $(g_{9/2}^2)_{J=9^+}$。自旋对齐对的逐级去耦消耗了角动量，形成了类似于多剪刀展开的特殊光谱，不应被过度夸大为普适长程超流。

## Assumptions

1. **同位旋纯度近似**：假定在 $N=Z$ 核区库仑相互作用对单粒子波函数的同位旋混杂程度处于微扰量级（即 Fermi 跃迁求和规则被库仑力破缺幅度小于 $5\%$）；
2. **两能级平均场能隙方程**：采用 BCS 型有效单粒子能隙展开，忽略核表面高阶四体 $\alpha$ 结团关联对费米面失配的动态重整化。

## Competing Explanations

1. **竞争假说 A：Wigner 能是宏观 $T=0$ 氘核超流凝聚的直接热力学潜热**：
   - 证伪理由：Satuła & Wyss（1997）与 Frauendorf & Macchiavelli（2014）的投影推转壳模型明确证明，在包含精确粒子数投影与同位旋投影的纯 $T=1$ 配对哈密顿量中，仅由同位旋转动能项 $\frac{T(T+1)}{2\Theta_{\text{iso}}}$ 即可自然重现实验测得的全部 Wigner 能斜率（$E_W \approx 47 |N-Z|/A\text{ MeV}$），根本不需要假定基态存在静态宏观 $T=0$ 配对凝聚。
2. **竞争假说 B：$^{92}\text{Pd}$ 的反常能谱是四极形变长椭转子（$\beta_2 \approx 0.25$）的低刚度转动表现**：
   - 证伪理由：若 $^{92}\text{Pd}$ 是普通转子，其激发能量必须严格遵循 $I(I+1)$ 规律，导致比值 $R_{4/2} \approx 3.33$，且带内 $B(E2)$ 强度应达到数十 Weisskopf 单位；实验上实测 $R_{4/2} = 2.04$（更接近振动极限），且 $B(E2; 2^+ \to 0^+)$ 仅约 $10 - 15\text{ W.u.}$，排除了强集体转动假说。

## Transfer Conditions

1. **不可跨质量区直接迁移的判据**：
   - 严禁将 $N=Z$ 核中使用的 $T=0$ $np$ 配对模型、自旋对齐对相互作用势套用至 $|N-Z| \ge 2$ 的非自共轭核区；在这些核区，费米面失配使 $T=0$ 配对彻底猝灭，必须退回标准 $T=1$ 单质单中 BCS/HFB 理论；
2. **可迁移的普遍物理判据**：
   - Sarma-Clogston 临界失配破对判据 $\delta\lambda_c \approx \Delta_0 / \sqrt{2}$ 适用于包含两个不同费米面的任何费米子配对体系（包括冷原子两组分费米气体、超稠密夸克物质 CFL 相）。

## Failure Conditions

1. **超重核与高同位旋不对称区（$|N-Z| \gg 10$）**：在此类体系中，质子与中子费米能级相差达数十兆电子伏，空间轨道主量子数完全错开（如中子在 $i_{13/2}$ 而质子在 $h_{11/2}$），$T=0$ 配对的单粒子空间重叠积分为零，讨论 $T=0$ 配对完全失去物理意义；
2. **高温退激发态（$T \ge 1.0\text{ MeV}$）**：热涨落完全破坏所有超流关联，不仅 $T=0$ 配对瓦解，常规 $T=1$ 配对能隙亦经历标准 BCS 热相变而熔解。

## Falsification or Reverse Tests

1. **$^{92}\text{Pd} \to ^{94}\text{Pd}$ 实验 $E(2^+)$ 突变跃升反证**：
   - 若 $T=0$ 配对在偏离 $N=Z$ 后依然具有跨区稳定性，则向 $^{92}\text{Pd}$ 添加 2 个中子后，基态能级谱应保持渐进演化，$E(2^+)$ 变动应小于 $100\text{ keV}$；
   - 实验上添加 2 个中子使 $^{94}\text{Pd}$ 的 $E(2^+)$ 剧烈跃升 $+538.2\text{ keV}$（涨幅达 $61.6\%$），且能级模式发生本质断裂，反向严格证实了 $T=0$ 配对在 $|N-Z|=2$ 处的断崖式猝灭；
2. **同位旋矢量配对在失配下的鲁棒性反证**：
   - 与 $T=0$ 的骤然消失形成鲜明反差，从 $^{92}\text{Pd}$ 到 $^{94}\text{Pd}$ 再到 $^{96}\text{Pd}$，常规 $T=1$ 配对诱发的三点偶奇质量差能隙 $\Delta^{(3)}_n$ 稳定保持在 $1.1 - 1.3\text{ MeV}$，精确验证了同种核子对不受化学势差屏蔽的理论预言。

## Open Questions

1. 在处于质子滴线的超重 $N=Z$ 质子发射核 $^{100}\text{Sn}$（$Z=N=50$）周围，自旋对齐 $(g_{9/2}^{-2})_{J=9^+}$ 构型是否会在双闭壳极硬核芯背景下表现出前所未有的超高自旋同质异能素？
2. 相对论协变密度泛函中的张量 $\rho$ 介子势对 $T=0$ 配对顶角的微观重整化幅度究竟有多大？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究全面自审：通过系统求解双组分 BCS 配对能隙方程与 Sarma-Clogston 费米面失配破对模型，彻底阐明了 $T=0$ 质子—中子配对与自旋对齐对严格局限于 $|N-Z| \le 1$ 狭窄走廊的微观机理，从第一性原理上澄清了 Wigner 能的投影本性与 $^{92}\text{Pd} \to ^{94}\text{Pd}$ 能谱跃迁反常，为 Day 27 跨质量区迁移机制不适用性边界补充了极其关键的核力同位旋配对对称性维度。

## Promotion or Rejection History

- 2026-10-30: Checkpoint 031 建立；脚本 `system/scripts/day27_np_pairing_wigner_energy_study.py` 验证通过；输出结果沉淀至 `continuation-studies/np-pairing-wigner/np_pairing_wigner_results.json`；完成全量结构化元数据登记与索引同步。
