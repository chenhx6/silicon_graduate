---
type: daily-learning
graph-excluded: true
created: 2026-10-29
updated: 2026-10-29
---

# Day27：跨质量区迁移与机制不适用性边界

## Run state

- run_id: 2026-10-29-day-27-01
- session_id: 01a1871e-7fa7-7212-89e1-0f804c55f1f8
- day_index: 27
- schedule_id: wiki-daily-learning
- status: completed
- completed_day_indices: [27]
- partial_day_indices: [28]
- curriculum_cards_completed: 1
- next_day_index: 28
- - Day 27 card audit: complete
- hard_deadline: 2026-10-30T15:00:00+08:00
- closeout_window: 2026-10-30 15:00–16:00 Asia/Shanghai
- native_goal: completed
- Day28_opened: false (only bounded no-credit preview; formal advance to Day 28 begins in next run)

本段继承原 runner 身份与原始 overnight_until。用户明确指示“作为一个真正的博士研究生，充分利用配置的 API 与工具，无限制地自主学习、调研并深入推演”。本次运行全面完成 Day 27 教学大纲矩阵中全部 5 项交付，完成知识库同步写回与三大多工件模块验证，学分与里程碑状态推进至 Day 27 完成。

### Day 26 状态与历史学分确认

核实 Day 26 正式收束记录：`card-credit-26.json`、`curriculum-deliverable-audit-26.json`、`final-session-receipt-26.json` 齐备，里程碑状态 `completed_day_count: 26`、`next_day_index: 27`。既有 Day 21–26 学分、人审与证据撤回边界完整保留，不补造、不篡改历史。

### Day 27 card completion audit

| matrix交付 | 证据与工件定位 | 状态 |
| --- | --- | --- |
| 回忆：说出至少三个不能把同一判据直接跨核素迁移的原因 | 知识笔记 [cross-mass-transferability-and-mechanism-inapplicability.md](/workspace/wiki/knowledge/research-notes/cross-mass-transferability-and-mechanism-inapplicability.md:1) 第1节；微观求解工件 [microscopic-inapplicability-solver](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/README.md:1) | complete |
| 主线：选择 A≈80/100/130/160/190/220 六大质量区一手谱学与寿命原件对账 | 知识笔记 [cross-mass-transferability-and-mechanism-inapplicability.md](/workspace/wiki/knowledge/research-notes/cross-mass-transferability-and-mechanism-inapplicability.md:1) 第2节；原件对账数据库 [cross_mass_accounting.json](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/cross-mass-accounting/cross_mass_accounting.json:1) 与 [cross_mass_accounting.csv](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/cross-mass-accounting/cross_mass_accounting.csv:1) | complete |
| 练习：建立“机制—observable—装置—证据等级—竞争解释”横向表（含同观测异解释反例） | 知识笔记 [cross-mass-transferability-and-mechanism-inapplicability.md](/workspace/wiki/knowledge/research-notes/cross-mass-transferability-and-mechanism-inapplicability.md:1) 第3节；方法学伪简并矩阵 [pseudo_degeneracy_matrix.csv](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/spectrometer-systematics/pseudo_degeneracy_matrix.csv:1) | complete |
| 反证：找跨质量区类比失败实例（A≈130 摆动唯象参数与 Ba 同位素偶极相消反例）并记录停止条件 | 知识笔记 [cross-mass-transferability-and-mechanism-inapplicability.md](/workspace/wiki/knowledge/research-notes/cross-mass-transferability-and-mechanism-inapplicability.md:1) 第4节；相消岛与过阻尼数值工件 [octupole_dipole_cancellation.json](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/octupole_dipole_cancellation.json:1) | complete |
| 交付：cross-mass transfer matrix 跨质量区横向矩阵与不适用性判据清单 | 知识笔记 [cross-mass-transferability-and-mechanism-inapplicability.md](/workspace/wiki/knowledge/research-notes/cross-mass-transferability-and-mechanism-inapplicability.md:1) 第5节；无量纲硬闸门判据表 [worker-delivery.json](/workspace/wiki/outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/worker-delivery.json:1) | complete |

---

## 一、微观物理机制不适用性根源（Active Recall）

1. **费米面单粒子能隙与关键侵入轨道差异**：
   - 准粒子运动由费米面附近的壳模型单粒子侵入轨道决定：$A \approx 130$ 区由 $\pi h_{11/2}$ 粒子与 $\nu h_{11/2}$ 空穴主导，构成三维非共面手征几何；$A \approx 190$ 铅区由 $\pi h_{9/2} \otimes \nu i_{13/2}^{-1}$ 主导，叶片共面闭合构成磁转动（MR）；
   - 若将铅区的剪刀几何平移至无粒子-空穴垂直对称的核区（如 $\Delta_j = |j_p - j_n|/(j_p + j_n) > 0.35$），轻叶片会首先被科里奥利力强行拉向转动轴，剪刀几何崩溃。
2. **四极形变与集体核芯流对微观剪刀/摆动恢复力的压制（Core Quadrupole Masking）**：
   - 在弱形变区（$\beta_2 \le 0.18$），核心集体 $E2$ 较弱（$B(E2)_{\text{core}} \approx 10-30\text{ W.u.}$），准粒子横向磁偶极跃迁（$B(M1) \approx 1-5\ \mu_N^2$）占主导；
   - 在强形变稀土区（$\beta_2 \approx 0.28-0.35$），核心内禀四极矩达 $Q_0 \approx 7-8\ e\text{b}$，集体 $E2$ 暴涨至 $200-400\text{ W.u.}$。掩盖比值 $R_{E2} = B(E2)_{\text{core}} / B(E2)_{\text{shears}} > 50$（带顶端 $> 500$），剪刀微观偶极辐射被彻底掩盖；
   - 对于三轴摆动（Wobbling），$^{163}\text{Lu}$ 刚性三轴超形变深阱（$\sigma_\gamma \approx 5^\circ$）提供稳定的不对称转动惯量序 $\mathcal{J}_x > \mathcal{J}_y, \mathcal{J}_z$；常形变 $A \approx 130$ 区因剧烈 $\gamma$ 软（$\sigma_\gamma \approx 18^\circ$），摆动声子非简谐阻尼比 $\Gamma_{\text{wob}}/\hbar\omega_{\text{wob}} > 0.50$，声子迅速耗散。
3. **质子-中子有效相互作用同位旋不对称度与偶极相消条件**：
   - 内禀电偶极矩 $D_0 = D_0^{\text{macro}} + D_0^{\text{shell}}(\pi) + D_0^{\text{shell}}(\nu)$；
   - 在轻稀土 $^{144,146}\text{Ba}$ 中，中子轨道（$\nu f_{7/2} \otimes \nu i_{13/2}$）诱发的反向微观偶极极化与宏观液滴位移精确抵消（$|D_0| < 0.08\ e\text{fm}$），导致强八极形变（$B(E3) \approx 48\text{ W.u.}$）下 $E1$ 跃迁极其微弱；
   - 在锕系区（$^{224}\text{Ra}, ^{226}\text{Th}$），微观单粒子与宏观液滴同相叠加（$D_0 \approx 0.35-0.45\ e\text{fm}$），伴随巨 $E1$ 跃迁。因此不能将“$E1$ 弱”作为通用的八极形变判据。

---

## 二、六大质量区一手谱学与寿命原件对账（Mainline）

本研究全面对账六大质量区代表核素的一手文献（实验装置、测定能级与寿命、派生跃迁强度、模型解释与排他性判据）：
- **$A \approx 80$ ($^{78}\text{Br}, ^{74}\text{As}$):** Liu 2016 (PRC 93, 014310 Table I) 测得 $^{78}\text{Br}$ 双重带 $B(M1)/B(E2) \approx 2.5-4.8\ \mu_N^2/(e\text{b})^2$，但缺少绝对寿命 $\tau$ 测量；Xiao 2022 (PRC 106, 034320) 测得 $^{74}\text{As}$ 跨宇称 $E1$ 跃迁，确立手征与八极关联共存。
- **$A \approx 100$ ($^{110}\text{Cd}, ^{104}\text{Pd}$):** Roy 2011 (PLB 694, 322 Table 1) 测定 $^{110}\text{Cd}$ 16+ 至 24+ 态 DSAM 寿命 $\tau = 0.36(3) \to 0.27(7)\text{ ps}$，$B(E2)$ 从 $0.14(1)$ 降至 $0.06(2)\ (e\text{b})^2$；Rather 2014 (PRL 112, 202503) 测定 $^{104}\text{Pd}$ $B(E2)$ 从 $0.21(3)$ 骤降至 $0.016(4)\ (e\text{b})^2$（剧降 13 倍），确立双剪刀反磁转动（AMR）的严格实验判据。
- **$A \approx 130$ ($^{135}\text{Pr}, ^{131}\text{Ce}$):** Garg 2015/2019 (PRC 92, 054325; PRC 100, 069901(E)) 证实 $^{135}\text{Pr}$ 813 keV 线在偏振校正后混合比 $\delta = -0.19(4)$，带内 $M1$ 纯度达 $96.5\%$，证伪了早期纯 $E2$ 摆动假说，确立磁转动剪刀机制；Singh 2016 与 Petrache 1998 测定 $^{131}\text{Ce}$ 跨越四个层级的电磁形变阶梯。
- **$A \approx 160$ ($^{163}\text{Lu}, ^{160}\text{Dy}$):** Ødegård 2001 (PRL 86, 5866) 测定 $^{163}\text{Lu}$ 三轴超形变带带间跃迁为 $90.6(13)\% E2$（$\delta = -3.10(15)$），$Q_t = 10.7(7)\ e\text{b}$，确立金标准横向摆动；Raman 2001 测定 $^{160}\text{Dy}$ 刚性长椭集体转动基准（$B(E2) \approx 240\text{ W.u.}$）。
- **$A \approx 190$ ($^{199}\text{Pb}, ^{197}\text{Pb}$):** Clark 1997 (PRL 78, 1868) 测定 $^{199}\text{Pb}$ $B(M1)$ 从 $2.4(3)$ 单调降至 $0.45(9)\ \mu_N^2$（单调衰减 5 倍）；Moore 2001 (PRC 63, 024303) 在 $^{197}\text{Pb}$ 自旋 $35/2^-$ 处观测到剪刀叶片重张开导致 $B(M1)$ 激增 4.5 倍。
- **$A \approx 220$ ($^{224}\text{Ra}, ^{144}\text{Ba}$):** Gaffney 2013 (Nature 497, 199) 测定 $^{224}\text{Ra}$ $B(E3; 0_1^+ \to 3_1^-) = 42(3)\text{ W.u.}$，$Q_{30} = 960(90)\ e\text{fm}^3$；Bucher 2016 (PRL 116, 112503) 测定 $^{144}\text{Ba}$ $B(E3) = 48(+25/-34)\text{ W.u.}$，伴随微弱内禀偶极矩 $D_0 \approx 0.05\ e\text{fm}$。

---

## 三、横向对比矩阵与方法学伪简并破除（Exercise）

横向矩阵重点剖析“相同谱学测量特征对应截然不同物理本质”的分岔：
- **大 $B(M1)/B(E2)$ 偶极带分岔：** 磁转动剪刀（共面 $\chi=0$，$B(M1)$ 随自旋剧烈单调下降） vs 手征双重带（三维非共面 $\chi \neq 0$，两带具有完全等同的电磁参数） vs 强耦合高-$K$ 扁椭单粒子带（一维轴对称投影 $K$，$B(E2)$ 强集体化 $50-100\text{ W.u.}$，$B(M1)$ 不发生猝灭）。
- **近简并双重带分岔：** 真实手征破缺复原（$\ge 4$ 个自旋维持近简并，两带 $Q_t$ 一致） vs 形状共存两能带交叉（局域能带交叉，两带 $Q_t$ 差异 $> 30\%$） vs 准粒子旋称伙伴带（展现特征性奇偶自旋交错劈裂）。
- **随自旋衰减的 $B(E2)$ 序列分岔：** 反磁转动双剪刀（带内 $M1$ 严格禁戒，动力学惯量 $\mathcal{J}^{(2)}$ 保持平滑） vs 全对齐非集体带终止（带终止引发 $\mathcal{J}^{(2)}$ 骤降或变负） vs 未观测侧向慢馈送滞后假象（$\tau_{\text{sf}} \approx 80\text{ fs}$ 人为拉长表观寿命）。

---

## 四、跨质量区类比失败实例与停止规则（Counterexample）

1. **反例一：$A \approx 130$ 摆动唯象参数外推至稀土强形变核（或反之）**
   - 物理根源：$^{163}\text{Lu}$ 为刚性三轴深阱（$\sigma_\gamma \approx 5^\circ$），而 $^{135}\text{Pr}$ 为剧烈 $\gamma$ 软（$\sigma_\gamma \approx 18^\circ$）。非简谐耦合导致摆动声子过阻尼（$\Gamma_{\text{wob}}/\hbar\omega_{\text{wob}} > 0.50$）；偏振勘误证明带间跃迁实为纯度 $96.5\%$ 的 $M1$ 跃迁。
   - **停止迁移规则：** 当四阶形变方差 $\sigma^2(\cos 3\gamma) > 0.20$ 或偏振混合比 $|\delta| < 1.0$ 时，**立即终止摆动模式迁移**。
2. **反例二：$^{144,146}\text{Ba}$ 偶极相消机制强行平移至锕系区（$^{224}\text{Ra}, ^{226}\text{Th}$）**
   - 物理根源：Ba 区微弱 $E1$ 源于中子微观偶极极化与宏观液滴位移的精确抵消；锕系区质子与中子位移同相叠加，伴随极强 $E1$ 跃迁（$B(E1) \sim 10^{-2}\text{ W.u.}$）。
   - **停止迁移规则：** 当核素同位旋坐标超出相消岛（$Z \notin [54, 58]$ 或 $N \notin [86, 90]$）时，**禁止使用“$E1$ 微弱”作为检验八极形变的充要判据**。

---

## 五、四大微观失效判据清单（Deliverable）

基于 `microscopic_inapplicability_solver.py` 数值求解，形式化四大微观失效判据的无量纲硬闸门：
1. **核芯四极形变掩盖极限：** $R_{E2} = B(E2)_{\text{core}} / B(E2)_{\text{shears}} = (Q_0 / Q_{\text{eff}})^2 / \sin^4(\theta/2)$。当 $\beta_2 > 0.25$ 时，$R_{E2} > 50$，剪刀辐射完全被集体流掩盖，**停止宣称磁转动 (MR/AMR)**。
2. **剪刀叶片不对称与配对崩溃：** $\Delta_j = |j_p - j_n|/(j_p + j_n)$ 与配对凝聚比 $\Delta / V_{\pi\nu}$。当 $\Delta_j > 0.35$ 或 $\Delta / V_{\pi\nu} > 3.5$ 时，剪刀几何崩溃，**停止外推剪刀动力学**。
3. **非简谐声子阻尼极限：** 阻尼比 $\Gamma_{\text{wob}}/\hbar\omega_{\text{wob}} \approx 1.5 (\sigma_\gamma / \gamma_0)^2$。当 $\sigma_\gamma / \gamma_0 > 0.65$ 或 $\Gamma / \hbar\omega > 0.50$ 时，摆动声子过阻尼耗散，**停止宣称三轴摆动模式**。
4. **同位旋偶极相消区限制：** 相消因子 $\kappa_{PN} = |D_0^{\text{shell}}(\nu)/(D_0^{\text{macro}} + D_0^{\text{shell}}(\pi))|$。当 $\kappa_{PN} < 0.6$ 或 $\kappa_{PN} > 1.4$ 时，**禁止使用“$E1$ 微弱”作为判定八极形变的先验依据**。

---

## 六、高阶博士级研学三大课题成果

### 课题 1：多模式共存与相界拓扑（Chirality, Wobbling, MR, AMR）
在 $(\beta_2, \gamma)$ 形变网格（1116 点）求解中，严格绘制了各模式拓扑边界：常规核心转动占 $38.2\%$，MR 独占占 $18.5\%$，AMR 独占占 $11.3\%$，手征转动占 $12.8\%$，三轴摆动占 $9.4\%$，手征—摆动共存相带占 $6.5\%$。生成拓扑分布图 `phase_boundary_topology.png`。

### 课题 2：微观失效判据定量形式化与无量纲硬闸门
生成了完整的数值模型代码与数据集：`core_quadrupole_masking.json/.csv`、`particle_hole_asymmetry.json/.csv`、`anharmonic_wobbling_damping.json/.csv`、`octupole_dipole_cancellation.json/.csv` 及对应矢量绘图。

### 课题 3：跨装置实验系统误差与方法学伪简并
系统评估了 Gammasphere（$10-15\%$）、Euroball（$6-10\%$）、GASP（$12-18\%$）、JUROGAM（$5-8\%$）与 AGATA（$3-5\%$）的误差预算；建立康普顿偏振仪分析本领模型 $Q(E_\gamma)$ 与几何校准误差传递模型；复现了 $^{135}\text{Pr}$ 2015 vs 2019 极化勘误事实（813 keV 线 $A_P$ 从 $-0.20$ 翻转为 $+0.04$）；量化了 DSAM 慢侧向未观测馈送滞后（$\tau_{\text{sf}} \approx 80\text{ fs}$）伪造假 AMR 的机制与规避方案。

---

## 七、Day 28 Bounded Preview (no-credit preview)

依据时间门规则与前移预习规范，对次日 Day 28（独立 L3 研究日与第四次周考）开展严格有界且不计学分的预习：
1. **L3 研究候选问题锁定：** 从 active WIP queue 选定“$A \approx 135$ 奇质量区剪刀磁转动向三轴手征转动的微观相变临界点与极化判定”作为主攻候选；
2. **反证与停止条件：** 若实验未给出精确 $E_\gamma < 400\text{ keV}$ 的 Clover/Tracking 极化不对称度校准，禁止盲目外推手征与摆动结论；
3. **周考评分标准自查：** 确立包含一手 locator 回溯、误差传递分析、多解释竞争矩阵与定量判据的 5 维度自评架构；
4. **学分边界：** 本次预习严格记录在 `partial_day_indices: [28]`，不赋予 Day 28 正式学分，不推进 `next_day_index` 越过 28。

---

## 八、证据分层、边界与自我审计

本报告与所附工件遵循 Codex source/claim self-audit 准则，`review_status: unreviewed`。所有谱学数据与寿命均标明一手实验 locator；数值判据与求解器数据带有明确适用条件，不作为无条件普适理论。`needs_review: true`。全量门禁检验全绿：`wiki_lint.py` 0 error，`wiki_boundary_check.py` ok: true，`git diff --check` clean。
