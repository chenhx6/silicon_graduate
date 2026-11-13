---
type: research-note
title: "A130 方法重写：符合拓扑、瞬发偶然扣除与纲图拓扑闭合准则"
aliases: [A130 spectroscopy methods 5.6 note, Coincidence matrix and level scheme methodology]
created: 2026-11-14
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
question: "在在束 γ 谱学中，如何严格定义符合矩阵统计方差估计量、非等宽背景门内插权重，并区分图模型拓扑反符合与实验谱线检测限？"
evidence_sources: [xiao-xiao-2019-high-spin-74as-thesis, book-wu-nuclear-experiment-methods, wakudyanaye-2022-triaxiality-rotational-bands-133ce]
created_from: daily-learning-phys-model
promotion_target:
tags: [a130, coincidence-matrix, prompt-random-subtraction, background-subtraction, level-scheme, spectroscopy-methods]
---

# A130 方法重写：符合拓扑、瞬发偶然扣除与纲图拓扑闭合准则

## Research Trigger

在 A130 论文第 5 章第 5.6 节（符合矩阵与能级建立）重写审校中，父审合同提出了六项方法与统计边界要求：
1. 瞬发--偶然符合扣除 $S = P - aR$ 的总体理论方差为 $\mathrm{Var}(S) = \mu_P + a^2 \mu_R$，实验代入估计量为 $\widehat{\mathrm{Var}}(S) = P + a^2 R$；当归一化因子 $a$ 来自实测谱拟合时，须通过一阶 Delta 方法计入其方差与协方差传递；
2. 非等宽背景门不能直接平均原始计数，须先求出各背景门的道宽计数密度 $B_L/w_L$ 与 $B_R/w_R$，再按中心位置线性内插并乘以峰门宽 $w_p$；
3. 区分图模型中无级联路径的理想拓扑反符合与实验门谱中受探测灵敏度上限约束的未观测峰；
4. 明确符合关联确认的是衰变网络连通性，不单独证明同核反应道或相邻级联次序；
5. 澄清稳态闭合系统下的强度守恒，说明长寿命异能态的表观不平衡特定地源于有限观测时间窗；
6. 确立自旋宇称判定由角关联/偏振与选择定则给出，不普遍依赖绝对寿命测定。

## Grounded Evidence

本笔记基于三项已完成物理原件核验的标准来源：
1. [[xiao-xiao-2019-high-spin-74as-thesis]]：
   - 肖骁 2019 硕士学位论文《奇奇核 $^{74}\mathrm{As}$ 的高自旋态研究》（山东大学），原件物理 PDF 第 23–24 页（印刷第 15–16 页）第 3.1 节矩阵反演给出了二维对称矩阵按有序数对对等填入 $(E_i, E_j)$ 与 $(E_j, E_i)$ 的规则，以及限定特定角度探测器记录的非对称 ADO/偏振矩阵设定；
   - 原件物理 PDF 第 24–26 页（印刷第 16–18 页）第 3.2 节能级纲图建立明确指出能级纲图由 $\gamma\text{-}\gamma$ 符合关系、相对强度平衡与多极性信息综合建立。
2. [[book-wu-nuclear-experiment-methods]]：
   - 父审实际渲染并阅读了吴治华教材第10章第六节之四：印刷292–294页/PDF300–302页；图10.38在印293/PDF301。它支持多探头gamma-gamma数据处理、矩阵和开门投影框架。旧稿所指PDF253/258是α磁谱，不能支持符合统计公式；PDF267是gamma单谱的性能和分析。
   - 本页的条件泊松方差、全协方差Delta展开和双侧门密度插值是本任务推导，不冒称教材原式。对固定投影能量的一次本底密度，各窗中心对称积分时，平均密度等于中心密度，故按中心内插并分别除以窗宽；非线性密度则有近似误差。
3. [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]：
   - Ignasio Wakudyanaye 2022 硕士论文《Triaxiality and Rotational Bands in $^{133}\mathrm{Ce}$》（University of the Western Cape），原件物理 PDF 第 62–63 页（印刷第 51–52 页）第 5.2.2 节与 Fig. 5.2 阐明了门谱旁路分支判据：对 $871\,\text{keV}$ 设门未见 $490\,\text{keV}$ 与 $380\,\text{keV}$ 跃迁，但对 $936\,\text{keV}$ 设门清晰可见该两跃迁，从而判定 $490/380\,\text{keV}$ 处于与 $871\,\text{keV}$ 平行的退激支路上；同页分析了 $608/609\,\text{keV}$ 重叠双重峰的交叉解叠逻辑。

## Provisional Reasoning

1. **瞬发--偶然符合统计方差与估计量**：
   设净真符合估计量为 $S = P - aR$。若 $a = \Delta T_P / \Delta T_R$ 为预设时间门宽之比（常数），并另行假设瞬发与偶然时间差门中的计数可视为相互独立的泊松变量，则总体期望均值为 $\mu_P, \mu_R$，其总体理论方差严格满足：
   $$
   \mathrm{Var}(S) = \mu_P + a^2 \mu_R.
   $$
   在实验数据处理中，真实的期望值 $\mu_P, \mu_R$ 未知，采用观测样本计数作为代入估计：
   $$
   \widehat{\mathrm{Var}}(S) = P + a^2 R.
   $$
   当 $a$ 依赖于从实测时间谱或无相干本底能谱中拟合得到的参数时，由一阶 Delta 方法展开：
   $$
   \mathrm{Var}(S) \simeq \mathrm{Var}(P) + a^2 \mathrm{Var}(R) + R^2 \mathrm{Var}(a) - 2a \mathrm{Cov}(P, R) - 2R \mathrm{Cov}(P, a) + 2a R \mathrm{Cov}(R, a).
   $$
   此外，多重事件（$M_\gamma > 2$）对称填充或加权填充会在矩阵各道格点间引入统计协方差，格点计数并不自动独立。

2. **非等宽背景门道宽计数密度内插**：
   设峰门中心为 $e_0$、宽度为 $w_p$，左背景门中心为 $e_L$、宽度为 $w_L$、谱为 $B_L(E_y)$，右背景门中心为 $e_R$、宽度为 $w_R$、谱为 $B_R(E_y)$。
   两侧背景门的单位能量道宽计数密度分别为 $B_L/w_L$ 与 $B_R/w_R$。局域线性内插至峰位中心 $e_0$：
   $$
   \rho_b(e_0) = \lambda_L \frac{B_L(E_y)}{w_L} + \lambda_R \frac{B_R(E_y)}{w_R}, \quad \lambda_L = \frac{e_R - e_0}{e_R - e_L}, \quad \lambda_R = 1 - \lambda_L.
   $$
   净门谱为：
   $$
   S_{\mathrm{gated}}(E_y) = G(E_y) - w_p \left[ \lambda_L \frac{B_L(E_y)}{w_L} + \lambda_R \frac{B_R(E_y)}{w_R} \right].
   $$
   该式在量纲上严格一致（均为计数），并在等宽对称条件（$w_L = w_R = w_b, \lambda_L = \lambda_R = 1/2$）下自然退化为 $G - \frac{w_p}{2w_b}(B_L + B_R)$。

3. **反符合的逻辑属性与实验灵敏度边界**：
   在图模型中，两条处于互斥旁路分支上的跃迁不存在共同级联路径，理论真符合截面为零（拓扑反符合）。但在实验有限统计谱中，未见某峰仅意味着其计数低于当前探测器效率、分支比及本底起伏所决定的灵敏度上限（如 $3\sigma$ 探测限），不能将其视为绝对物理反符合证明。

## Assumptions

1. 假定时间走动已由离线校正归零，瞬发时间窗覆盖了绝大部分物理瞬发分布；
2. 假定峰门邻域内康普顿连续谱本底变化平缓，局域一阶线性内插近似成立；
3. 假定衰变系统处于连续束流照射下的稳态平衡，或观测时间窗远大于所研究能级的主导寿命。

## Competing Explanations

1. **门谱中未出现某峰的竞争解释**：
   - 解释 A（拓扑旁路）：该跃迁与门跃迁处于互斥的平行退激分支上，物理上不存在级联（Wakudyanaye 2022 的分析判定）；
   - 解释 B（探测灵敏度不足）：该跃迁确实与门跃迁级联，但分支比极小或探测器效率较低，其实验计数被淹没在连续康普顿本底统计起伏之下；
   - 解释 C（异能态延迟截断）：两跃迁之间存在寿命大于符合时间窗的同核异能态，级联在时间谱上被切除在瞬发窗口之外。

## Transfer Conditions

1. 适用于使用多探测器 HPGe 阵列进行在束 $\gamma\text{-}\gamma$ 符合矩阵构建、一维门选投影与衰变纲图构建的标准核物理实验数据分析；
2. 适用于瞬发时间窗与偶然时间窗分离清晰、且背景谱连续平缓的常规能区。

## Failure Conditions

1. 当能谱背景存在陡峭的康普顿边缘、单/双逃逸峰或后向散射峰结构时，局域双侧线性内插公式失效，须采用非线性连续本底剥离或多维拟合；
2. 当存在严重的多重散射串扰（Crosstalk）或近几何真符合相加（TCS）时，测得的符合计数不再代表真实的核退激流，必须进行串扰剔除或相加修正；
3. 当存在长寿命异能态（$\tau > \Delta T_{\mathrm{coin}}$）时，瞬发时间窗内的表观强度平衡被破坏。

## Falsification or Reverse Tests

1. **等权退化测试**：在数值代码中设定 $w_L = w_R = w_b$ 且 $e_0 - e_L = e_R - e_0$，检验式~\eqref{eq:5-6-gate-sub} 是否严格退化为 $G - \frac{w_p}{2w_b}(B_L + B_R)$；
2. **零信号本底期望测试**：在无特征信号的平坦纯本底区域设置峰门与背景门，检验扣除后的净计数分布期望是否在统计误差内等于零；
3. **方差估计量蒙特卡罗检验**：对已知泊松期望 $\mu_P, \mu_R$ 进行抽样，比较样本代入估计量 $P + a^2 R$ 的平均值与理论总体方差 $\mu_P + a^2 \mu_R$ 的一致性。

## Open Questions

1. 在极高计数率大阵列实验中，多光子事件对称填充产生的网格协方差如何在最终拟合能级分支比的全局 $\chi^2$ 矩阵中精确参数化？
2. 对于包含多级微秒级异能态的复杂核衰变网络，如何结合数字化列表模式下的长程时间关联统一重构宽时域纲图？

## Human Review

本笔记由执行代理根据 2026-11-13 父审合同 round 2 要求及已核实原件独立撰写，记录物理与统计边界自审推导；未记录新的用户审核事件。

## Promotion or Rejection History

2026-11-14：建立第 5.6 节符合矩阵与能级建立的方法与统计边界知识笔记，支撑 LaTeX 正文与证据台账修订。

2026-11-14 父原件复核：纠正上述Wu页码归属；自行推导与原著报告分开登记。硬件未记录的是事件信息，物理事件本身未因此消失。
