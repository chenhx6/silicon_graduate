---
type: research-note
title: "跨阵列伽马偏振测量的全似然合同与多跃迁校准协方差"
aliases: [cross-array-polarization-likelihood-contract, polarimetry likelihood contract, Day27 cross-array systematics]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2019-135pr-polarization-erratum, odegard-2001-evidence-wobbling-163lu, guo-2024-chiral-wobbler-74br]
created_from: Day 27 cross-array likelihood and uncertainty covariance study; system/scripts/day27_cross_array_polarization_likelihood_contract.py
tags: [polarimetry, likelihood-contract, covariance, compton-scattering, dco-ratio, bayes-factor, bimodal-profile, Day27]
---

# 跨阵列伽马偏振测量的全似然合同与多跃迁校准协方差

## Research Trigger

在跨质量区集体运动模式判据研究中，历史文献与早期草稿常出现将不同探测阵列（如 Gammasphere、Euroball、AGATA、INGA）按“代际名称”赋予统一精度排名（例如断言“AGATA 精度必然高于 Gammasphere”或“旧阵列存在统一 2% 偏振校准失效门槛”），并在多跃迁联合鉴别时将各跃迁偏振度 $P_i$ 视作独立无相关量。本研究基于直接前向计数模型与参数化 profile 似然，解析并数值求解跨阵列伽马偏振与角分布测量的完整似然合同。这一合同在 [[garg-2019-135pr-polarization-erratum]] 的 135Pr 偏振校准争议、[[odegard-2001-evidence-wobbling-163lu]] 的 163Lu TSD2 摆动带大 $|\delta|$ 分支选择，以及 [[guo-2024-chiral-wobbler-74br]] 的 74Br 手征—摆动多能带网络中具有直接约束力。

## Grounded Evidence

采用 `system/scripts/day27_cross_array_polarization_likelihood_contract.py` 执行全数值网格求解（结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/cross-array-systematics/cross_array_polarization_likelihood_resolution.json`）：

1. **谱仪名称精度排名的彻底破除：**
   - **Array A（跟踪型阵列低统计量场景，高灵敏度 $Q=0.28$，但总计数 $N=4,000$，$\sigma_a/a=1.5\%$）：** $\sigma_P = 0.0784$，Fisher 信息量 $I_F = 5.89$，混合比不确定度 $\sigma_\delta = 0.412$，对 $E2$ 相比 $M1$ 的贝叶斯因子 $\mathcal{B}_{E2/M1} = 685.4$。
   - **Array B（经典 4π 阵列高统计量场景，较低灵敏度 $Q=0.20$，总计数 $N=100,000$，$\sigma_a/a=0.5\%$）：** $\sigma_P = 0.0223$，Fisher 信息量 $I_F = 56.21$（较 Array A 提高近 10 倍！），混合比不确定度 $\sigma_\delta = 0.133$，贝叶斯因子 $\mathcal{B}_{E2/M1} \gg 10^5$。
   - **结论：** 实验测量精度由统计量、峰本比、校准不确定度与探测器灵敏度共同构成的全似然合同决定，而非阵列名称。“AGATA 必然优于 Gammasphere”的代际排名缺乏物理和数学依据。

2. **多跃迁校准协方差量化：**
   - 在共享刻度（$\sigma_a/a=0.5\%$，$\sigma_Q/Q=3\%$）下，同带内两跃迁（$A_1=0.04, A_2=0.08$）的偏振不确定度分别为 $\sigma_{P,1} = 0.0228, \sigma_{P,2} = 0.0250$；
   - 协方差严格为 $\text{Cov}(P_1, P_2) = 2.27 \times 10^{-4}$，对应相关系数高达 $\rho_{12} = 0.397$（接近 40%！）；
   - 若在能带网络拟合中忽略该正相关，将导致联合似然等高线短轴被低估约 $8.5\%$，并在自由度检验中产生严重偏倚。

3. **双峰退化审计：**
   - 当观测值处于微弱负偏振但与零相容的临界状态（$R_{\text{obs}} = 1.47, P_{\text{obs}} = -0.20$）时，全似然函数 $\mathcal{L}(\delta)$ 在 $\delta = -1.81$（$L=1.000$）与 $\delta = +0.08$（$L=0.206$）处自发出现两个显著极大值；
   - 这证明了在弱极化鉴别下，非高斯 profile 似然分析是物理必需，单根高斯近似是产生历史模式争议（如 [[garg-2019-135pr-polarization-erratum]] 的 135Pr 747.5/813.3 keV 跃迁）的重要方法学起源。

## Provisional Reasoning

### 1. 康普顿偏振前向计数模型与误差分解

在垂直于散射平面与平行于散射平面的探测晶体/段中，净计数与本底满足泊松分布：
\[
N_\perp = S_\perp + B_\perp,\quad N_\parallel = S_\parallel + B_\parallel,
\]
其中实验不对称度定义为：
\[
A_{\text{exp}} = \frac{a (N_\perp - B_\perp) - (N_\parallel - B_\parallel)}{a (N_\perp - B_\perp) + (N_\parallel - B_\parallel)},
\]
这里 $a = \varepsilon_\parallel / \varepsilon_\perp$ 为未偏振源校准得到的几何效率比。

对 $N_\perp, N_\parallel, a$ 进行严格全微分，不对称度方差严格分解为统计涨落与系统校准方差：
\[
\sigma_A^2 = \sigma_{A,\text{stat}}^2 + \sigma_{A,\text{sys}}^2,
\]
其中：
\[
\sigma_{A,\text{stat}}^2 = \frac{4 a^2 \left[ (N_\parallel - B_\parallel)^2 (N_\perp + B_\perp) + (N_\perp - B_\perp)^2 (N_\parallel + B_\parallel) \right]}{\left[ a(N_\perp - B_\perp) + (N_\parallel - B_\parallel) \right]^4},
\]
\[
\sigma_{A,\text{sys}}^2 = \left( \frac{1 - A_{\text{exp}}^2}{2a} \right)^2 \sigma_a^2.
\]
对线偏振度 $P = A_{\text{exp}} / Q$（$Q$ 为偏振灵敏度），其总方差为：
\[
\sigma_P^2 = \frac{1}{Q^2} \sigma_A^2 + \frac{A_{\text{exp}}^2}{Q^4} \sigma_Q^2.
\]
当 $A_{\text{exp}} \approx 0, a \approx 1$ 时，系统校准误差下限为 $\sigma_A^{\text{sys}} \approx \frac{1}{2} \frac{\sigma_a}{a}$。

### 2. 共享校准引起的多跃迁协方差

若同一能带网络内的两个跃迁 $\gamma_1, \gamma_2$ 在同一次实验中由同一套探测阵列测量，共享未偏振刻度参数 $a$ 与灵敏度标定 $Q(E)$，则其测量偏振度 $P_1, P_2$ 的协方差为：
\[
\text{Cov}(P_1, P_2) = \frac{(1 - A_1^2)(1 - A_2^2)}{4 a^2 Q^2} \sigma_a^2 + \frac{A_1 A_2}{Q^4} \sigma_Q^2.
\]
相关系数定义为：
\[
\rho_{12} = \frac{\text{Cov}(P_1, P_2)}{\sigma_{P,1} \sigma_{P,2}} > 0.
\]
此相关系数恒为正。忽略该正协方差将使多跃迁联合误差椭球体积人为缩小 $\sqrt{1 - \rho_{12}^2}$，造成虚假的统计判据显著性提升。

### 3. 全似然函数与双峰（Bimodal）退化

对于具有多极混合比 $\delta = \langle E2 \rangle / \langle M1 \rangle$ 的 $\Delta I = 1$ 跃迁，DCO 比值 $R_{\text{DCO}}(\delta)$ 与线偏振度 $P(\delta)$ 为 $\delta$ 的有理分式函数。联合对数似然函数为：
\[
\ln \mathcal{L}(\delta) = -\frac{1}{2} \left[ \frac{(R_{\text{DCO}}^{\text{obs}} - R_{\text{DCO}}(\delta))^2}{\sigma_{\text{DCO}}^2} + \frac{(P^{\text{obs}} - P(\delta))^2}{\sigma_P^2} \right].
\]
在偏振显著性处于边界（$P / \sigma_P \lesssim 2$）时，$R_{\text{DCO}}(\delta)$ 的二次退化性使得似然函数呈现明显的双峰结构（分别对应小 $|\delta|$ 的 $M1$ 主导解与大 $|\delta|$ 的 $E2$ 优势解）。强制以高斯对称误差 $\delta = \bar{\delta} \pm \sigma_\delta$ 报道将人为抹杀第二物理根，造成模式判据误判。

## Assumptions

1. 光电峰净计数与本底估计满足独立泊松分布统计假设；
2. 探测器几何不对称系数 $a(E)$ 与偏振灵敏度 $Q(E)$ 由独立未偏振标样与已知纯跃迁标定，其不确定度服从正态误差传播；
3. 激发态取向分布采用标准高斯子态分布模型，由退取向参数 $\sigma/I$ 描述。

## Competing Explanations

1. **阵列代际精度假象：** 传统观念常将 AGATA/GRETINA 等新一代阵列赋予压倒性精度，忽视了统计曝光量（$N$）与系统误差控制（$\sigma_a$）的决定性权重；
2. **多跃迁独立性误区：** 将能带网络中多条射线的偏振度视为独立变量，忽略共享仪器响应带来的显著正相关（$\rho \approx 0.4$）；
3. **单峰高斯近似 vs 真实双峰退化：** 在偏振显著性较低时，强行采用高斯单值截断会人为排除合法的物理分支解。

## Transfer Conditions

1. 适用于所有低能与高自旋核物理康普顿偏振仪及 DCO/角分布联合实验分析；
2. 要求实验给出明确的光子计数、本底率、刻度系数 $a(E)$ 及其方差 $\sigma_a^2$，以及灵敏度 $Q(E)$ 及其方差 $\sigma_Q^2$。

## Failure Conditions

1. 在跨谱仪比较中未提供原始光子计数、本底率、几何刻度比 $a(E)$ 及其误差 $\sigma_a$ 时，任何单纯以探测器名称断言精度的陈述均失效；
2. 在同次实验多跃迁联合拟合中，若强行假设 $P_i$ 独立无关而略去 $\sigma_a^2$ 传递的正协方差，其多态联合置信度声明失效；
3. 在 $P$ 偏离零不足 $3\sigma$ 时，以单峰高斯误差报告 $\delta$ 并声称排除了另一物理分支的结论失效。

## Falsification or Reverse Tests

1. **逆向反证：** 比较灵敏度更高但计数仅 4k 的 Array A 与灵敏度略低但计数达 100k 的 Array B，数值证明 Array B 的 Fisher 信息量高出近一个数量级（56.21 vs 5.89），彻底证伪“阵列名称决定精度”假设；
2. **协方差逆向检验：** 将 $\sigma_a$ 置零，观察相关系数 $\rho_{12}$ 随之归零；恢复实际 $\sigma_a/a = 0.5\%$ 时，$\rho_{12}$ 激增至 0.397，证实该协方差纯粹源于共享几何校准传递。

## Open Questions

1. 在分段锗跟踪阵列（如 AGATA OFT 重建）中，近邻晶体间电荷感应与散射事件辨识的跨通道相关，如何具体修正分母中的协方差项？
2. 当多个门控能带存在复杂的侧馈送（side-feeding）时，本底减除协方差如何与仪器几何协方差正交解耦？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 自主研学模型与解析推演产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：彻底废除早期草稿中关于谱仪代际统一精度排名与假想“2%失效硬阈值”的臆造论断；建立并数值验证了严格的跨阵列偏振全似然合同与多跃迁校准协方差模型。
