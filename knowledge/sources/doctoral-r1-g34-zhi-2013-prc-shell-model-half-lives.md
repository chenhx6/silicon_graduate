---
type: source
title: 'Zhi et al. 2013: 包含首禁戒跃迁的大尺度壳模型r过程等待点核半衰期计算'
aliases: [Zhi 2013 PRC, Zhi 2013, 10.1103/PhysRevC.87.025803, 'arXiv:1301.5225']
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Shell-model half-lives including first-forbidden contributions for r-process waiting-point nuclei
authors: [Q. Zhi, E. Caurier, J. J. Cuenca-García, K. Langanke, G. Martínez-Pinedo, K. Sieja]
journal: Physical Review C
year: 2013
volume: 87
pages: 025803
doi: 10.1103/PhysRevC.87.025803
canonical_source: https://doi.org/10.1103/PhysRevC.87.025803
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G34/Zhi_2013_PRC_87_025803_SM_halflives_first_forbidden.pdf
raw_sha256: eaedbd4539854e3d1f0e7860ef7ab9c647d4fa44cd8144b4989ba220ec639333
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: [78ni, 130cd, 129ag, 131in, 199ta, 205au, 206tl, 207tl]
models: [large-scale-shell-model, nathan-code, kuo-herling-khhe, sieja-2010-interaction, cuenca-2007-interaction]
observables: [half-life, beta-delayed-neutron-probability, shape-factor, gamow-teller-strength, first-forbidden-strength]
methods: [lanczos-diagonalization, sum-rule-pivot, cvc-hypothesis, meson-exchange-enhancement]
tags: [beta-decay, gamow-teller, first-forbidden, r-process-waiting-point, quenching-factors, shape-factor, shell-model, fulltext-read]
arxiv: 1301.5225v1
---

# Zhi et al. 2013：包含首禁戒跃迁的大尺度壳模型r过程等待点核半衰期计算

## Bibliographic Record

Q. Zhi, E. Caurier, J. J. Cuenca-García, K. Langanke, G. Martínez-Pinedo, and K. Sieja, *Shell-model half-lives including first-forbidden contributions for r-process waiting-point nuclei*, Physical Review C **87**, 025803 (2013). DOI: `10.1103/PhysRevC.87.025803`。同源预印本：arXiv:1301.5225v1（`pdfinfo` 实测全文共 14 物理页，正文及图表延续至第 14 页）。本地归档 PDF 位于 `raw/papers/gpt/query/20261108-foundations-G34/Zhi_2013_PRC_87_025803_SM_halflives_first_forbidden.pdf`，文件大小 440,775 字节，SHA-256 为 `eaedbd4539854e3d1f0e7860ef7ab9c647d4fa44cd8144b4989ba220ec639333`。

## Scope and Reading Depth

- Completed reading_depth: deep-read（全文 14 页深入核验，涵盖 Sec. II 弱衰变相空间积分与形状因子展开、Sec. III 价空间截断、Lanczos 强度函数求和与不同 rank 算符唯象淬灭拟合、Sec. IV–VI 分别针对 $N=50, 82, 126$ 幻数等待点核的计算细节与图表，以及 Sec. VII 总结）。
- Covered scope:
  1. 运动学与端点能：电子总相对论能量 $W$ 与端点能 $W_0$ 均以电子静质量 $m_e$ 为单位（采用 $c=1$）。原文直接基于始末**核态质量差**定义端点能 $W_0 = Q/(m_e c^2) = (M_i^{\text{nuc}} - M_f^{\text{nuc}})/m_e$；若使用中性原子质量差 $Q_\beta^{\text{atom}}$ 换算，须包含电子静能零点，即 $W_0 \approx 1 + (Q_\beta^{\text{atom}} - E_x)/(m_e c^2)$。
  2. 相空间因子与比较半衰期定义区别：积分关系式 $f t = K = 6146\,\text{s}$ 中的相空间因子 $f = \int_1^{W_0} C(W) F(Z, W) (W^2 - 1)^{1/2} W (W_0 - W)^2 dW$ 显式吸收了形状因子 $C(W)$。常规比较半衰期基于纯费米积分 $f_0$，通过平均形状因子 $\overline{C(W)} = f/f_0$ 关联（满足 $f_0 t = K / \overline{C(W)}$）。
  3. 允许 GT 与首禁戒（FF）算符展开：GT 形状因子为能量无关常数 $C(W) = B(GT)$（已包含 $(g_A/g_V)^2$）；FF 展开为四项形式 $C(W) = k + ka W + kb/W + kc W^2$。
  4. 首禁戒算符多极分解与 CVC 约束：rank 0（时样轴矢 $\xi^\prime v$、轴矢相关 $w, w^\prime$）、rank 1（空样矢量 $x, x^\prime$、矢量速度相关 $\xi^\prime y$、轴矢相关 $u, u^\prime$）及 rank 2（轴矢相关张量 $z$）。在矢量流守恒（CVC）及同位旋良好对称性假设下，约束 $\xi^\prime y = E_\gamma x$（$E_\gamma$ 为同位旋模拟态到末态的能差）。
  5. 淬灭因子的唯象拟合属性：基于铅区与铟区 7 个母核共 20 项实验纯禁戒跃迁行（Table I）进行最小二乘拟合，报告振幅因子 $q(\xi^\prime v)=1.266, q(w)=0.66, q(x)=0.51, q(u)=0.38, q(z)=0.42$。原文未披露完整拟合权重与相关性；时样轴矢呈现表观增强（$>1$），空样各通道呈现不同程度压低。
  6. 校准输入与计算结果：$^{131m}\text{In}$ 属于首禁戒拟合集合，$^{130}\text{Cd}$ 寿命（当时旧实验值 $162(7)\,\text{ms}$）用于标定 $q_{GT} = 0.66$，二者均非留出预测；$^{78}\text{Ni}$ 壳模型计算 $0.15\,\text{s}$ 展现了跨壳组态混合解除泡利阻挡效应；$N=126$ 壳模型计算在 $Z \ge 70$ 核素中表现出 FF 贡献反超 GT。
- Not covered: 未包含 NATHAN 壳模型代码的原始对角化程序与双精密度 Lanczos 矢量输出；未展开超大型组态空间的三体有效核力推导。

## Summary

Zhi et al. 2013 在大尺度壳模型框架下建立了 Gamow-Teller 与一阶禁戒（FF）跃迁协同衰变的微观理论体系。该研究严格定义了将形状因子 $C(W)$ 纳入相空间积分核 $f$ 的计算方案，将首禁戒跃迁解构为 rank 0, 1, 2 的时样/空样矢量与轴矢量多极算符。通过对铅区和铟区 20 个已知纯一阶禁戒衰变跃迁行进行最小二乘拟合，获得了各 rank 算符的唯象淬灭参数，并以 $^{130}\text{Cd}$ 当时实验寿命（$162(7)\,\text{ms}$）标定了 $q_{GT} = 0.66$。文章计算了 $N=50, 82, 126$ 幻数等待点核的半衰期与中子发射几率，揭示了双幻核 $^{78}\text{Ni}$ 跨壳组态混合解除泡利阻挡以及 $N=126$ 丰中子核中 GT 遭遇泡利阻挡而使 FF 跃迁在特定高 $Z$ 核中占主导的微观机制。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZHI13-1 | 弱衰变相空间积分中，电子总能量 $W = E_e/(m_e c^2)$ 与端点能 $W_0 = (M_i^{\text{nuc}} - M_f^{\text{nuc}})/m_e$ 均以电子静质量 $m_e$ 为单位（$c=1$）；偏半衰期由 $f t = K = 6146\,\text{s}$ 给出，其中积分核 $f = \int_1^{W_0} C(W) F(Z, W) (W^2 - 1)^{1/2} W (W_0 - W)^2 dW$ 显式包含形状因子 $C(W)$，常规比较半衰期基于纯费米积分 $f_0$ 并通过平均形状因子 $\overline{C(W)} = f/f_0$ 关联（$f_0 t = K / \overline{C(W)}$）。 | theoretical-formalism | direct | p. 2, Sec. II, Eqs. (1)–(3), Eq. (14) | false |
| ZHI13-2 | 允许 Gamow-Teller 形状因子为能量无关常数 $C(W) = B(GT) = (g_A/g_V)^2 \frac{\vert \langle f \Vert  \sum_k \bm{\sigma}^k \bm{t}_-^k \Vert  i \rangle\vert ^2}{2J_i + 1}$；一阶禁戒跃迁形状因子呈现特征能量依赖 $C(W) = k + ka W + kb/W + kc W^2$。 | theoretical-formalism | direct | p. 2, Sec. II, Eqs. (4)–(7) | false |
| ZHI13-3 | 首禁戒算符分为 rank 0, 1, 2。rank 1 中矢量算符 $x$ 与轴矢量算符 $u$ 发生量子干涉（如 $(x+u)^2, (2x+u)^2, (2x-u)^2$ 等交叉项）；在 CVC 及同位旋对称性假设下约束 $\xi^\prime y = E_\gamma x$，其中 $E_\gamma = Q + \Delta E_C - (m_n - m_p)c^2$。 | theoretical-formalism | direct | pp. 2–3, Sec. II, Eqs. (7)–(13) | false |
| ZHI13-4 | 首禁戒各 rank 淬灭因子在铅区与铟区 20 项实测跃迁行中唯象拟合得到：$q(\xi^\prime v)=1.266, q(w)=q(w^\prime)=0.66, q(x)=q(x^\prime)=0.51, q(u)=q(u^\prime)=0.38, q(z)=0.42$；时样轴矢算符 $\xi^\prime v$ 展现表观增强（$>1$），空样算符呈现各向异性压低。 | model-calibration | direct | p. 3, Sec. III, Eq. (16), Table I, Fig. 1 | false |
| ZHI13-5 | $^{130}\text{Cd}$ 寿命计算并非留出验证，而是作为 GT 淬灭因子标定输入：采用 $q_{GT} = 0.66$ 时复现当时已知实验值 $T_{1/2} = 164.29\,\text{ms}$（实验 $162(7)\,\text{ms}$），此时首禁戒贡献约为 $13\%$。 | model-calibration | direct | p. 4, Sec. III; p. 7, Sec. V, Table III | false |
| ZHI13-6 | $^{78}\text{Ni}$ 壳模型计算寿命为 $0.15\,\text{s}$（实验 $0.11^{+0.10}_{-0.06}\,\text{s}$）；在单粒子模型下因质子 $0f_{7/2}$ 全满使得中子 $0g_{9/2} \to 0f_{7/2}$ 首禁戒跃迁完全泡利阻挡，而壳模型跨壳多体混合部分解除了阻挡。 | model-result | direct | pp. 5–6, Sec. IV, Table II, Figs. 4–5 | false |
| ZHI13-7 | 在 $N=126$ 等待点核模型计算中，随着质子数增加至 $Z \ge 70$（如 $^{196}\text{Yb}, ^{198}\text{Hf}$），因质子 $0h_{11/2}$ 轨道逐步填充，中子 $0h_{9/2} \to 0h_{11/2}$ GT 跃迁遭遇严重泡利阻挡，首禁戒跃迁贡献在计算中反超 GT。 | model-result | direct | pp. 8–9, Sec. VI, Table IV, Fig. 15 | false |

## Competing Interpretations and Limitations

- 淬灭因子的唯象拟合与有效算符重整化边界：
  1. $q(x) = 0.51$ 等参数是基于 20 个实验跃迁行的最小二乘拟合值。矢量流守恒（CVC）虽然保证了裸矢量荷 $g_V = 1$ 不淬灭，但在截断的有限价空间壳模型中，有效矢量算符同样吸收了未包含组态的微观重整化（如高阶关联、有限基底效应与相对论展开），不能断言其“完全源于芯极化”。
  2. 时样轴矢增强 $q(\xi^\prime v) = 1.266 > 1$ 在物理上与 Warburton 等人的软介子交换流（MEC）分析方向一致，但在本文大尺度壳模型中它依然属于有限空间下的唯象拟合参数，未在本文框架内由微观两体流自洽闭环导出，不能视作 MEC 的唯一证明。
- 拟合集与标定输入说明：
  1. Table I 列出 20 个跃迁行，原文未披露详细拟合权重、协方差矩阵及数据挑选判据；$^{131m}\text{In}(1/2^-)$ 与 $^{129m}\text{In}(1/2^-)$ 明确属于首禁戒拟合集，$^{130}\text{Cd}$ 用于标定 $q_{GT}$，均非盲预测。
  2. Table I 内部自洽性疑点（参见 T04 独立审计 [[doctoral-r1-t04-first-forbidden-operator-audit-20261108]]）：针对 $^{205}\text{Hg} \to {^{205}\text{Tl}}(3/2^+_1)$ 与 $^{205}\text{Hg} \to {^{205}\text{Tl}}(3/2^+_2)$，原表理论列 $\sqrt{\overline{C}}$（$18.9$ 与 $10.3\,\text{fm}$）反算出的 $\log f_0 t$（分别为 $6.41$ 与 $6.94$）与原表所列理论 $\log f_0 t$（$7.26$ 与 $6.32$）存在倒置不一致，该现象在 PDF 与静态 `rp.tex` 中均存在，提示原文理论列存在疑似排版错配，不可将其作为无歧义基准。
- 标定输入演进与外部来源区分：
  1. 本文将 $^{130}\text{Cd}$ 当时实验寿命（$162(7)\,\text{ms}$）作为输入反调 $q_{GT} = 0.66$。后续 EURICA（Lorusso 2015）与 GRIFFIN（Dunlop 2016，参见 [[continuation-g19-dunlop-2016-cd-halflives]]）测定 $^{130}\text{Cd}$ 真实半衰期为 $126(4)\,\text{ms}$，从而促使后续大尺度壳模型将 $q_{GT}$ 重新标定为 $0.75$。这一后续调整属于外部谱学演进，不能直接归为 Zhi 2013 原文自身报告的内容。

## Extracted Pages

- 实际读取文献页码：arXiv:1301.5225v1 全文共 14 页（PDF pp. 1–14，其中 pp. 2–10 为核心理论、拟合表与讨论，pp. 13–14 包含图 16–17 及参考文献）。
- 关键公式定位：
  - Eqs. (1)–(3): 相空间积分 $f$、偏半衰期 $ft = K = 6146\,\text{s}$ 及电子总能量 $W$、核质量端点能 $W_0$ 定义（PDF p. 2）。
  - Eqs. (4)–(7): 允许 GT 形状因子 $C(W)=B(GT)$ 与首禁戒形状因子四项展开 $C(W)=k+ka W+kb/W+kc W^2$（PDF p. 2）。
  - Eqs. (8)–(13): 首禁戒各 rank 算符非相对论约化及 CVC 关系 $\xi^\prime y = E_\gamma x$（PDF pp. 2–3）。
  - Eq. (14): 平均形状因子定义 $\overline{C(W)} = f/f_0$（PDF p. 3）。
  - Eq. (16): 首禁戒各 rank 淬灭因子拟合值（PDF p. 3）。
- 关键表格与图形定位：
  - Table I: 铅区与铟区 20 项首禁戒拟合跃迁行的实验与理论 $\log f_0 t$ 及 $(\overline{C(W)})^{1/2}$（PDF p. 5）。
  - Table II: $N=50$ 等待点核理论寿命与实验对比（PDF p. 6）。
  - Table III: $N=82$ 等待点核理论寿命与实验对比（PDF p. 9）。
  - Table IV: $N=126$ 等待点核理论寿命预言（PDF p. 10）。
  - Fig. 1: 拟合平均形状因子理论与实验对比（PDF p. 4）。
  - Fig. 5: $N=50$ 各同中子素首禁戒贡献百分比（PDF p. 7）。
  - Fig. 10: $N=82$ 各同中子素首禁戒贡献百分比（PDF p. 9）。
  - Fig. 15: $N=126$ 各同中子素首禁戒贡献百分比（PDF p. 11）。
