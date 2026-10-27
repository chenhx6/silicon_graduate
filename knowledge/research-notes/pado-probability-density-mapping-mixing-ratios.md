---
type: research-note
title: "基于无预设自旋取向度的概率密度映射法（PDM/P-ADO）提取多极混合比研究"
aliases: [PDM概率密度映射法, P-ADO混合比提取方法, probability-density-mapping-mixing-ratios]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chen-2026-pdm-probability-density-mapping, sensharma-2020-longitudinal-wobbling-187au, guo-2022-low-spin-wobbling-187au, lv-2022-evidence-against-wobbling-135pr, yamazaki-1967-aligned-angular-coefficients, der-mateosian-sunyar-1974-angular-coefficients]
created_from: raw/writing/pado research integration
promotion_target: angular-distribution
tags: [mixing-ratio, p-ado, pdm, angular-distribution, linear-polarization, spin-alignment, jacobian, marginalization]
---

# 基于无预设自旋取向度的概率密度映射法（PDM/P-ADO）提取多极混合比研究

## Research Trigger

在低能核结构高自旋能带的竞争解释甄别（如手征双重带、三轴摆动模式、签名伙伴态、三轴形状共存等）中，带间 Delta I = 1 连接跃迁的电多极混合比 delta(E2/M1) 是重要的判别量，但其结论仍取决于响应模型、对齐域和其它伴随观测量。然而，传统从角分布各向异性（R_ADO 或 R_ac）与康普顿散射线偏振度（P）提取 delta 的方法，强烈受制于发射态未知的自旋取向度参数 sigma/I。传统上固定预设 sigma/I（如假定 sigma/I = 0.25 或 0.30）的做法容易造成人为压缩误差或锁定错误解（如 187Au 中的横向与纵向摆动争议）。本笔记系统吸收 raw/writing/pado/（Chen et al., 2026）的概率密度映射法（Probability Density Mapping, PDM / P-ADO），解析其无预设自旋取向度、局部雅可比测度变换以及全局边缘化积分的数学物理机制。

## Grounded Evidence

直接方法源为[[chen-2026-pdm-probability-density-mapping]]；Au与Pr的观测输入分别转引[[guo-2022-low-spin-wobbling-187au]] G22-7及[[lv-2022-evidence-against-wobbling-135pr]] L22-17，方法重析不增加独立采集。

1. **有界角坐标 xi = arctan(delta)**：定义 xi in (-pi/2, +pi/2)，将无限实轴delta映至有界开区间，便于采样大模混合比。它没有自动消除有限网格截断；代码当前±89°只覆盖约±57.29，须检查尾部质量及域敏感性。
2. **局部测度守恒与雅可比行列式变换**：可观测量空间 O(R_ADO, P) 与参数空间 P(xi, sigma/I) 通过响应函数关联。由测量不确定度构建的可观测量联合概率密度，通过雅可比行列式转换为参数空间密度：f_P(xi, sigma/I) = f_O[F(xi, sigma/I)] * |J(xi, sigma/I)|，严格满足微分微元面积变换规律 dA_O = |J| dA_P。
3. **响应曲面的全局拓扑分类（Inside vs Outside 构型）**：在给定响应函数、参数域和数值网格下，各向同性极限点 o0 = (R_ADO, P) = (1, 0) 相对于响应曲线的相对位置决定了全局解的拓扑分化：Inside 构型下 o0 位于曲线内部，响应曲面呈直立帽子状；Outside 构型下 o0 位于曲线外部，响应曲面呈倾斜帽子状并在投影面发生全局折叠（Global Folding），同一对测量值可能与响应曲面相交于两个候选解。
4. **自旋取向度的边缘化积分与非对称区间**：在声明的域和权重下对sigma/I积分，得到条件映射密度f(xi)。两版原稿均先在xi中求68%最高密度区间与等尾区间，再映射至delta；HDI及mode依赖坐标，映射后的端点不能冒称在delta密度中重新求得的HDI。多峰时分别报告各分支模式与概率质量。
5. **一维观测误差概率密度模型库**：
   - **高斯分布（对称误差）**：$f_{\mathrm{G}}(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]$；
   - **偏态正态分布（Skew-Normal，非对称误差优先）**：$f_{\mathrm{SN}}(x; \Xi, \omega, \alpha) = \frac{2}{\omega} \phi\left(\frac{x-\Xi}{\omega}\right) \Phi\left(\alpha \frac{x-\Xi}{\omega}\right)$，通过拟合 0.16、0.50、0.84 分位数确定参数；
   - **连续分段正态分布（Continuous Split-Normal, CSn，备选）**：$f_{\mathrm{CSn}}(x; \mu, \sigma_l, \sigma_r) = \sqrt{\frac{2}{\pi}} \frac{1}{\sigma_l+\sigma_r} \exp\left[-\frac{(x-\mu)^2}{2\sigma_{l,r}^2}\right]$。
6. **八条基准实验跃迁提取对照表（Chen et al., 2026, Table 1）**：

| 核素 | 跃迁级联 | 偏振度 $P$ | 角分布比 $R_{\mathrm{ADO}}$ | 文献报道 $\delta$ | PDM 68% HDI | PDM 等尾区间 |
|---|---|---|---|---|---|---|
| $^{61}\text{Ni}$ | $5/2^- \to 3/2^-$ | $-0.15(3)$ | $0.70(1)$ | $-0.18(5)$ | $-0.15^{+0.03}_{-0.04}$ | $-0.15^{+0.03}_{-0.04}$ |
| $^{61}\text{Ni}$ | $7/2^- \to 5/2^-$ | $-0.10(3)$ | $1.67(2)$ | $2.46(15)$ | $2.79^{+0.16}_{-0.18}$ | $2.76^{+0.16}_{-0.17}$ |
| $^{61}\text{Ni}$ | $9/2^- \to 7/2^-$ | $-0.39(7)$ | $0.80(1)$ | $0.02(3)$ | $0.05^{+0.01}_{-0.02}$ | $0.05^{+0.01}_{-0.02}$ |
| $^{187}\text{Au}$ | $11/2^- \to 9/2^-$ | $-0.12^{+0.11}_{-0.12}$ | $0.39(5)$ | $-0.26^{+0.11}_{-0.15}$ | $-0.24^{+0.07}_{-0.15}$ | $-0.30^{+0.09}_{-0.18}$ |
| $^{187}\text{Au}$ | $15/2^- \to 13/2^-$ | $-0.09^{+0.17}_{-0.37}$ | $0.42^{+0.13}_{-0.16}$ | $-0.28^{+0.23}_{-0.69}$ | $-0.24^{+0.17}_{-0.34}$ | $-0.35^{+0.19}_{-0.57}$ |
| $^{135}\text{Pr}$ | $17/2^- \to 15/2^-$ | $0.04^{+0.08}_{-0.13}$ | $0.37(4)$ | $-0.47^{+0.09}_{-0.22}$ | $-0.42^{+0.11}_{-0.33}$ | $-0.55^{+0.17}_{-0.45}$ |
| $^{135}\text{Pr}$ | $19/2^- \to 17/2^-$ | $-0.07^{+0.09}_{-0.10}$ | $0.49(4)$ | $-0.31^{+0.10}_{-0.13}$ | $-0.26^{+0.07}_{-0.17}$ | $-0.33^{+0.10}_{-0.22}$ |
| $^{135}\text{Pr}$ | $21/2^- \to 19/2^-$ | $-0.03^{+0.05}_{-0.12}$ | $0.48(6)$ | $-0.37^{+0.10}_{-0.14}$ | $-0.29^{+0.09}_{-0.14}$ | $-0.33^{+0.10}_{-0.14}$ |

## Provisional Reasoning

### 1. 消除预设 sigma/I 偏差的统计优势
在固定取向度的分析中，单点拟合可能低估未知对齐度带来的不确定性。PDM在明确的响应函数、误差模型、对齐域和权重假设下传播sigma/I不确定性；所得区间来自条件映射密度，不应称为无条件客观结论。

### 2. 解决多极性双解争端的实证范式（187Au 与 135Pr）
- **187Au 376 keV 跃迁（11/2- -> 9/2-）**：输入 P = -0.12(+0.11/-0.12) 与 R_ADO = 0.39(5)，PDM 边缘化计算给出 68% HDI 为 delta = -0.24(+0.07/-0.15)（等尾区间为 -0.30(+0.09/-0.18)）。条件概率质量高度聚集于小幅值区域，支持跨带跃迁以磁偶极成分为主；在给定输入误差、响应函数和对齐域下，大幅 E2 主导分支受到强烈抑制，但带身份仍需结合其它结构观测量。
  由 $f_{E2}=\delta^2/(1+\delta^2)$ 可得中心份额约 5.4%；将68% HDI端点映射到份额约为 2.8%–13.2%，因此只能表述为条件下 M1 主导，不能给出严格的统一 $E2<10\%$ 硬门。
- **135Pr 关键跨带线**：针对 17/2-、19/2-、21/2- 三条连接跃迁，PDM 条件密度给出一致的小负解（delta ~ -0.26 至 -0.42），与 Lv22 的联合 P-Rac 分析一致；它支持M1主导解释，但不是无模型排除其它机制。

### 3. 多峰多解诊断案例与概率质量分解
当偏振误差较宽（原稿19/2−→17/2−虚拟诊断输入R_ADO=.40(4)、P=.05(15)）时，条件映射密度可出现多个峰。等尾区间可横跨峰间低密度区，xi坐标HDI可保留断开的集合；各HDI分量质量合计68%，不是全部物理解的归一概率，也不是不同核结构模型的概率。数值须绑定稿件版本、对齐权重和域，不能跨图搬用。

## Assumptions

1. 假定反冲激发态的磁子能级布居遵循标准高斯对齐假定 P(M) prop exp[-M^2/(2 sigma^2)]；
2. 假定两角度角分布比 R_ADO 与线偏振度 P 的实验误差相互独立，联合概率密度采用因子化模型 f_O = f(R) * f(P)；
3. 假定探测器的有效几何衰减因子 Q2, Q4 与分段偏振灵敏度已经完成独立源刻度。

## Competing Explanations

1. **固定取向度拟合**：以单一典型值（如 sigma/I = 0.30）提取解，虽然计算简便但存在系统偏差风险；
2. **纯角分布 chi^2 扫描**：缺乏偏振约束时存在二次双解简并，容易误选大 |delta| 解导致物理机制误判；
3. **PDM 概率密度映射**：在声明的响应函数、误差独立性、对齐先验和校准假设下，通过参数空间映射与边缘化保留非对称尾部与多峰结构，是一种条件统计推断方案。

## Transfer Conditions

PDM的适用目标是：在融合蒸发反应布居、mixed M1+E2、Delta I=1且响应模型与对齐域可声明的对齐核态系统中使用；具体核素仍需逐项核对输入和假设。

## Failure Conditions

1. 在J=0处逆函数定理不能提供局部逆；数值加密可以检查收敛，但不能自动恢复缺失的可识别性，f_O|J|在该点也不等于发散；
2. 在各向同性极限 o0 = (1, 0) 处，响应曲面收缩为单点，可观测量完全丧失对混合比的敏感性，PDM 无法提供有意义的区间约束；
3. 若杂质峰、错误几何或校准使观测密度主要落在响应域外，归一化可能仅保留极小尾部并偏向边界；这需要检查域内质量和模型失配，不是一般的数学发散定理。

## Falsification or Reverse Tests

1. 原稿报告的8条基准线中，多数PDM区间包含文献值，但部分61Ni结果只有边界或部分重叠；该比较不是独立覆盖率检验。
2. 窄对齐权重可检验固定对齐附近的条件响应；极限仍含二维Jacobian权重，是否等于传统固定对齐提取需统一误差模型、测度与区间定义，目前未完成该等价性验证。

### 原件版本与辐射振幅合同（Day25 checkpoint009）

[[chen-2026-pdm-probability-density-mapping]] 保存15页版、11页版PDF与当前TeX各自哈希；原15页版Eq13/14、11页版Eq11/12不能混号。旧版Gaussian对齐宽度正文.02与Fig8 caption .1冲突保留，不能从后稿统一.1反填旧输入。

代码的delta是无量纲辐射E2/M1振幅比，响应含2delta F12干涉与1+delta²归一。[[paul-1991-n75-electromagnetic-properties-triaxiality]] 的0.835 Eγ用于其RME到辐射振幅转换；不能把裸RME比直接输入PADO，也不能将输出再次乘此因子。能量通过实际Q(E)、ICC和强度换算进入合同；符号迁移另须核相位与偏振轴。若xi用degree，密度转换为 f_delta = f_xi,degree (180/pi)/(1+delta²)。同一个概率集合的质量可守恒，密度高度排序与HDI不保持。

### 局部面积守恒、折叠分支与统计解释（checkpoint009条件推导）

以下是对CH26-PDM-03/04的任务数学审计，不是原作者已报告的实验结果。设p=(xi,s)、s=sigma/I，F为分片局部可逆的光滑响应，J非零几乎处处。采用原方法的未归一权重 g(p)=f_O(F(p))|J(p)|w(s)，则面积公式给出

$$
Z_w=\int_{\mathcal P}g(p)\,dp
=\int_{F(\mathcal P)}f_O(o)\sum_{p_b\in F^{-1}(o)}w(s_b)\,do.
$$

因此局部变元公式不自动给全域唯一概率分配。归一化后推出的观测密度为 f_O(o)N_w(o)/Z_w，其中 N_w 是加权分支重数。若重数在支持域变化，即使w=1也会重新加权各观测区域；若要精确恢复原f_O，须另指定满足逐o分支权重和为1的分配合同，且处理域外质量。保留所有物理解并不决定它们的先验概率。

一个可解析控制取F(x,s)=(x²,s)、x∈[-1,2]、s∈[0,1]，观测矩形u∈[0,4]、v∈[0,1]上f_O=1/4。这里w=1给g=|x|/2、Z=5/4；负/正分支归一质量为1/5、4/5，重叠区u≤1的推出质量为2/5，而原观测质量为1/4。采用逐点1/N分支分配则恢复观测密度，负/正质量变为1/8、7/8。这不是PADO真实响应或数据，只证明全局归一、域边界和分支分配须声明。数值及分数控制见本run `pdm-measure-contract-009.py/json`。

若另以生成式likelihood L(o_obs|p)定义Bayes后验，公式是q(p|o_obs)∝Lπ。把f_O(F(p))当作该likelihood时，|J|w可对应一种隐式先验或测度，不能由测量单独决定，也不等于参数空间均匀先验。窄对齐权重极限保留f_O(F(xi,s0))|J(xi,s0)|，所以不自动等于固定对齐χ²提取。以上不判定原方法失效，而是要求将输出称作声明测度、权重和域下的条件密度；若称Bayes后验，应补齐likelihood/先验/分支合同。

### analysis 模块的复现边界（checkpoint010）

`raw/writing/pado/Upload/analysis/YAnalysis.py` 的投影、归一化、CDF和HDI全部经 `_trapz` 调用 `np.trapz`；当前NumPy 2.5.3已移除该接口，而 `requirements_analysis.txt` 的 `numpy>=1.24`允许该不兼容组合。当前包的24项测试不覆盖analysis模块。临时内存适配 `_trapz→numpy.trapezoid` 后，合成双峰密度的HDI分支质量和`mass`字段可对账；平顶常数密度在阈值二分下会把全域质量1记为请求的.68，故复现须另核各interval `mass`总和。默认`summary_transition`只计算delta，稿件要求的xi/AT-HDI须显式选择theta并把角度端点经tan映回delta；不能拿delta坐标HDI代替稿件结果。完整八条基准网格未取得，当前不做稿件重放。

## Open Questions

1. 当大探测器阵列给出多角度全矩阵（如 17 环或 39 探测器）时，如何将 PDM 推广至多维协方差不为零的高阶张量空间？
2. 如何在 PDM 中显式纳入上游未观测级联的退极化退取向张量 Uk 作为先验约束？

## Human Review

本笔记整合了 raw/writing/pado/ 原始手稿（Chen et al., 2026）的理论推导与算法定义，review_status 保持 unreviewed。文中涉及的方法比较未声明为 human-reviewed。

## Promotion or Rejection History

2026-10-28 由 Day 25 任务根据用户指令将 raw/writing/pado/ 的既有混合比研究成果纳入知识库，作为角分布与偏振方法学的核心补充，提升至 angular-distribution。
