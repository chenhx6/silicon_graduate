# Day17 本 session 来源前主动回忆

- session_id: `01a1532e-0f21-7903-9bf6-8a9cc9ee9e17`
- run_id: `2026-10-19-day-17-01`
- 冻结时间、SHA-256：见同目录 `active-recall-freeze.json`；该 JSON 在打开本轮 source/raw 前生成。
- 性质：受既有知识和本 prompt 强烈 priming 的主动回忆；不是独立盲测，不沿用 Day16 的分数、程序检查或预习学分。

## 已暴露范围

用户的本轮 prompt 已逐条给出 ST99 勘误/灵敏度指数、SG98 C/S/η/294-keV closure、Morse/L26/L25/UC21/UCG/Riley/Co60、Jones/Ra/Go/Tsuzuki/Bizzeti、SU/FH/Hamilton、Garg/Palit/Rh/feeding/D66/GR97/Geant3 以及 Day16 最终综合。启动时仅读治理、课程卡、状态与近期报告；还没有打开本轮科学 source 页或 raw 原件。后面的答复已受这些提示影响。

## 先答，不回看本轮原件

1. 物理线偏振 P 是指定坐标轴下两正交光子偏振强度之差与和的比；轴若取反应面内还是法向，正号可翻转。角度、布居、门条件和多极混合共同决定它，单凭电/磁标签不能迁用任意 P 值。
2. A 是某一计数/调制估计量；Q 是这一估计量对 matching physical P 的探测响应，只有归一、接受与选择匹配时才能写 A=QP。polarimeter Q 不等于角关联有限立体角的 Q_k。
3. clover 的通常形式为 A=(a N_perp-N_parallel)/(a N_perp+N_parallel)，但 a 究竟为哪一计数比必须看原定义；若换命名却不换比值会产生伪不对称。
4. 已获提示 SG98 双分段为 A=(η C-S)/(sqrt(η)(C+S))。C/S 不是 clover 平行/垂直的裸替换；C 包含另一侧光峰/sideADCzero。η/Q/阈值依赖必须回原件确认，不能用旧数据误差调 η 去消印刷 closure。
5. 对 clover 定义，令 x=a N_perp, y=N_parallel：dA/dN_perp=2ay/(x+y)^2，dA/dN_parallel=-2x/(x+y)^2，dA/da=2N_perp y/(x+y)^2。Var(A)=g^TΣg；独立 Poisson 是明确设计极限，不适用于默认峰拟合面积。P=A/Q 的传播还含 A–Q Cov。
6. 对 SG98 的非标准分母，必须另推 dA/dC,dA/dS,dA/dη，不能借上式。若共享校准同时影响 η 和 Q，不能默认其 Cov=0；Table3 的 fit errors 不是 sqrt(counts)。
7. FOM 常见 εQ²，但 ε 可为每发射光子、每入射光子、每 full-energy event 或选中双击的比例。比较时间效率必须统一分母、角度选择、background 和 deadtime。
8. Klein–Nishina 给单次自由电子散射的能量/极角/方位依赖；90°附近高 analyzing power 不等于全阵列 Q。阈值、事件排序、多次散射、partial charge collection、门和背景改变有效响应。
9. 几何 null a/η 的校准不是 polarized Q 校准；若用同一 known transition 标定 Q 再回代自身，不能算独立验证。gate 参考和 target 的 roles 不能倒换；同数据的论文/评价/模型复用不能计独立证据。
10. parity/Jπ/δ/集体模式判断须与 AD/DCO/ICC/feeding 等相容；P/A 的正负最多在明确相位、布居和匹配响应下约束 EM 候选。必要 companion 是同母态、同门、同取向及响应可追溯的观测量。

## 本轮可证伪问题与预计新交付

连续性问题：两个原件的 A 归一/效率分母怎样改变同样“计数误差传播”的 Jacobian 与共同校准不确定度？先重新完整核 ST99 与 SG98，而不是重跑 Day16 Table3 JSON。

候选新颖性问题：在真实参考与 target 的匹配接受下，能否设计一套同时测 a/η、Q 并留出独立检查支路的最小计数方案？只允许一个不重叠 novelty 槽；若尚无真实输入，明确为 design exercise，不产生实验 CI。

新 artifact 应包含本 session 推导的两个估计量 Jacobian、带明确背景/校准共享结构的设计计数与数值交叉核验，以及 P/A/Q 分层表/一个独立校准输入。原件冲突和旧 corrections 保留；本轮不预填 card complete。
