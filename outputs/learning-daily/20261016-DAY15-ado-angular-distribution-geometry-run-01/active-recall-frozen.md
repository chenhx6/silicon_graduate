# Day15 主动回忆原答（冻结）

- frozen_at: 2026-10-16T22:17:56.981021+08:00
- session_id: 01a14510-aec7-7e00-aa23-f7c77a5124bc
- run_id: 2026-10-16-day-15-01
- 类型：primed recall，不是独立盲测。已读本次 prompt 的 Day14 预习摘要、Wiki index 和 active handoff/课程卡；尚未打开本次科学 source/raw 或 Day14 详细日报。启动文件的概述也构成提示。
- 冻结规则：本文件不回写；来源后的纠正另存日报/knowledge。不能沿用 Day14 分数或检查数量。

## 1. angular distribution、A2/A4、maximum/reference 和 alignment

Angular distribution 是已布居核态相对束轴的单个 γ 发射角分布。轴对称、无向取向且只保留到 k=4 时，我的原答是 W(θ)=A0[1+A2 P2(cosθ)+A4 P4(cosθ)]，A2/A4 是归一后的 Legendre 系数，无单位；实验有时把 A0 吸收，因此须核约定。Maximum/reference coefficient 是特定自旋路径、混合比和参考 alignment 所给的理论系数，实际系数会受未完全 alignment 衰减；我记得可写 Ak=αk Ak(max)，但不能把所有 k 的 α 当一个常数。核 alignment 是磁子态 |m| 的不均匀布居且 p(m)=p(-m)，不同于有向 vector polarization，也不同于转动能带 quasiparticle alignment。σ 是假设 m 布居的宽度，σ/J 与 σ 本身不同。

## 2. R_ADO、f_ADO、待测/门控、角组和效率

待测线 x 是比较两角组计数的跃迁；门控线 g 用于挑出符合级联。暂以 H=远离90°的角组、T=90°角组记号，我的原答 R_ADO=[N_x(H|g)/ε_x(H)]/[N_x(T|g)/ε_x(T)]。实际 Zheng 的 H/T 分子分母以及 f 修正方向尚不能从记忆保证，应回原件后更正而不改本文件。ε 的组计数必须对应整组效率之和而非不加说明的单台效率，且 gate efficiency 与 γγ response 可因 self-exclusion 影响。f_ADO 应是把符合计数对应的角比与本征单γ角比联系起来的修正因子；我不确信原文写 R=f R0 还是 R0=f R，核原式后才能套。只有两角净计数与待测线单γ效率比时，只能求实验角比，无法同时定本征角比与 f：一个约束有两个未知。需要独立单γ本征比、已知级联 response 或独立 gate/geometry 输入；用同一 R 定义 R0 再宣布 f=1 是循环。

## 3. alignment、feeding、有限立体角和门条件

alignment 改变统计张量和 A2/A4，弱 anisotropy 不必意味着另一多极性。上游 feeding 会改变被研究核态的磁子态分布，寿命/去取向也可能衰减。有限立体角要对 Pk 与实际方向效率积分，不能仅代名义中心角；角组探测器数和能量依赖效率必须与计数归一相配。符合门改变条件样本和 joint γγ distribution，换门可能改变 postselection；同母态不等于门后同 density matrix。单γ效率和角分布校准不够确定 joint response、多重度和 pair acceptance。

## 4. 失效观测与失败控制

固定已知自旋/多极性的校准线，如果换门、换角组或改变背景侧带后，效率修正角比不能在含 Cov 的误差内闭合，则当前可迁移的 f/几何假设失败。独立多角分布可检验 alignment 参数是否足够；对 E/M 候选还需线偏振或独立 ICC 等必要观测，ADO 单值不能定电磁性质。必须保留共享事件、共享背景和效率共同归一带来的相关；独立 Poisson 假设只能在数据结构支持时使用。若缺实际事件和 Cov，不把自设数或模拟统计当实验测量。
