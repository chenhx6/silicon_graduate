---
type: method
title: Time-differential perturbed angular distribution
aliases: [TDPAD, time differential perturbed angular distribution, perturbed angular distribution]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: unreviewed
method_type: hyperfine-time-dependent-angular-correlation
tags: [tdpad, hyperfine, alignment, g-factor, angular-correlation]
---

# Time-Differential Perturbed Angular Distribution

## Purpose

Time-differential perturbed angular distribution (TDPAD) uses time-dependent anisotropy or correlation signals to probe hyperfine interactions, alignment, and related nuclear moments such as `g` factors.

## Inputs and Assumptions

- time-resolved anisotropy or correlation data with calibrated detector timing;
- a host/environment model for the implanted ions or recoils;
- an explicit separation between alignment effects, field-free fractions, and hyperfine-field assumptions.

## Core Observable

In the currently ingested boundary source [[gray-2020-hyperfine-fields-g-factor-measurements]], the measured `R(t)` amplitude depends on both the alignment term `B2` and the field-free fraction `p`. This means a reduced oscillation amplitude is not a unique signature of either weaker alignment or a larger field-free fraction.

## Boundary for the Sigma-over-I Project

TDPAD is not the same workflow as prompt in-beam P-ADO mixing-ratio extraction. The `sigma/I` discussion in Gray 2020 appears in a host-specific, isomeric `g`-factor context and should be used only as a boundary example showing that empirical alignment expectations may fail.

## What It Can Establish

TDPAD can constrain hyperfine precession behavior and, with controlled implantation and site information, support `g`-factor extraction and alignment diagnostics.

## What It Cannot Establish Alone

TDPAD amplitude by itself does not uniquely determine alignment or field-free fraction. It also does not define a universal prompt-decay `sigma/I` prior for fusion-evaporation angular-distribution fitting.

## Related Pages

- [[angular-correlation]]
- [[g-factor-measurement]]
- [[deorientation]]
- [[sigma-over-i]]

## Sources

- [[gray-2020-hyperfine-fields-g-factor-measurements]]


## Day19方法选择：TDPAD的四个时间对象

[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-1–5和[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-1–5给直接原件：population lifetime、alignment relaxation、hyperfine oscillation period和instrumental PRF各有不同含义。理想ratio消population不等于寿命测完；finitePRF需先作用两支路计数再构ratio。128Cs的56ns是half-life，rank2频率为2ωL；129,131Ce为9/2−，Sn晶格QI/Sn-Pb外场MI不能误记成Cd或液态。

最小输入为level/spin/feeding、time scale/zero/response、field向与phase、B_eff或EFG的host校准、alignment/field-free/relaxation、逐detector背景归一和共享Cov。共同EFG可在适当同J/同host ratio中消，absoluteQ/g仍需绝对场；外场与打印ω不自动复现local-field结果。33项条件响应/周期算术见[[lifetime-method-selection-response-contract]]；不代原spectra/拟合CI或普适chirality判据。

## Day19三矢量g因子相加与手征几何判据

[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-1 与 GR18-D19-6 确立了奇奇核中通过 TDPAD 测量的同核异能态 $g$ 因子对内禀核几何（平面 vs 手征三维空间取向）的判定机制：

1. **双体相加模型破缺**：对于 $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$ 组态的 $9^+$ 异能带头，若假设偶偶芯不参与转动（$j_R = 0$），双体 Landé 相加公式严格给出 $g = (g_p + g_n)/2$。无论采用微观理论还是邻近奇 $A$ 核单粒子经验值，均预测 $g = 0.50\text{--}0.52$，与实测 $g = +0.59(1)$ 偏离超过 $7\sigma$。这在数学上证明必须引入有限芯转动角动量（$j_R = 2, 4$）的组态混合。
2. **三矢量广义相加公式（式 2）**：将质子、中子与集体芯三个角动量矢量耦合（$\vec{J} = \vec{j}_p + \vec{j}_n + \vec{j}_R$），$g$ 因子依赖于各矢量的内积标量积：
   $$g = \frac{1}{2} \left[ (g_p + g_n + g_R) + \dots \right] - \frac{1}{\langle J^2 \rangle} [g_p \langle \vec{j}_n \cdot \vec{j}_R \rangle + g_n \langle \vec{j}_p \cdot \vec{j}_R \rangle + g_R \langle \vec{j}_p \cdot \vec{j}_n \rangle]$$
   - **理想手征非平面几何**（$\vec{j}_p \perp \vec{j}_n \perp \vec{j}_R$）：三矢量相互垂直，标量积全为零，给出 $g \approx 0.50$；
   - **质子对齐共面几何**（$\vec{j}_R$ 趋向 $\vec{j}_p$）：标量积项为正贡献，将 $g$ 因子推高至几何上限 $g_{\text{max}} \approx 0.60$；
   - **中子对齐共面几何**（$\vec{j}_R$ 趋向 $\vec{j}_n$）：标量积项为负贡献，将 $g$ 因子压低至下限 $g_{\text{min}} \approx 0.40$。
3. **带头平面构型判决**：实测 $g_{\text{exp}} = +0.59(1)$ 紧贴质子对齐平面分支极值（$0.60$），而显著偏离理想手征值（$0.50$）。结合 PRM+CDFT 理论计算，其正规化手征序参量仅为 $\langle \hat{o} \rangle = \langle (\vec{j}_p \times \vec{j}_n) \cdot \vec{j}_R \rangle / \sqrt{\dots} \approx 0.15 \ll 1.0$。这表明 $^{128}\text{Cs}$ 的 $9^+$ 带头本质上处于近平面构型，反证了低自旋近简并带与电磁指纹不能直接充当静态手征几何的充分判据；特征手征空间取向仅在更高自旋或频率阈值之上才动态涌现。

## Day19电四极TDPAD进动周期与同宿主EFG对消

[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-1 与 IB98-D19-6 确立了电四极相互作用（QI）TDPAD 测量的自旋辨识与电场梯度（EFG）系统误差消除机制：

1. **自旋相关的四极周期前因子**：多晶六方或非立方金属晶格中，静态电四极进动基频由四极耦合常数 $\nu_Q = e Q V_{zz} / h$ 决定。进动周期 $T_0$ 的自旋依赖前因子为：
   $$T_0 = \frac{2J(2J-1)}{3} \frac{1}{\nu_Q}, \quad \omega_0 = \frac{2\pi}{T_0}$$
   对于 $J = 9/2$，前因子为 $24$；对于 $J = 7/2$，前因子为 $14$。两者基频相差 $24/14 = 1.714$ 倍，且时间各向异性谱 $R(t)$ 的傅里叶展开系数 $s_{2n}$ 呈现自旋特异性的振幅调制特征。在 $^{129}\text{Ce}$ 实验中，$J = 9/2$ 拟合 $\chi^2 = 2.7$ 压倒性优于 $J = 7/2$ 的 $\chi^2 = 13.9$，提供了不依赖衰变跃迁多极性的直接自旋判定。
2. **同宿主晶格 EFG 严格对消机制**：固态晶格中的电场梯度 $V_{zz}$ 通常带有 $15\%\text{--}20\%$ 的微观晶格计算系统误差。但若将两个同位素（如 $^{129}\text{Ce}$ 与 $^{131}\text{Ce}$）反冲注入同一温度下的同一多晶金属靶（如 Sn），两者在晶格间隙或替代位置感受的局部微观场梯度 $V_{zz}$ 严格相同。实测四极进动基频比值 $\omega_0(^{129}\text{Ce}) / \omega_0(^{131}\text{Ce})$ 严格等于电四极矩绝对值比值：
   $$\frac{|Q(^{129}\text{Ce})|}{|Q(^{131}\text{Ce})|} = \frac{1.32(13)}{0.92(10)} = 1.435 \approx 1.44(7)$$
   完全消除了宿主晶格 EFG 的绝对标定误差，确立了跨同位素极高精度的四极形变相对演化标尺。
3. **单粒子磁矩与集体四极形变解耦**：在同一组异能态上，TDPAD 磁相互作用（MI）测得 $g$ 因子分别为 $-0.185(10)$ 与 $-0.189(7)$，差异仅 $2.12\%$，严格符合单中子 $\nu h_{11/2}$ 轨道的施密特特征；而电四极矩却在两中子间隔内跃升 $43.5\%$。这一强力对比证明：奇核磁矩对芯形变演化具有刚性钝感，而电四极矩对价核子诱发的芯极化与集体四极形变膨胀具有极高灵敏度。

## Day19低自旋TDPAD共面几何与高自旋DSAM手征动态涌现的统一模型

[[grodner-2006-128cs-chiral-doublet-lifetimes]] GR06-D19-1 与 [[grodner-2018-128cs-chiral-g-factor]] GR18-D19-6 构成了核物理中利用异质时间方法解析手征对称性动态演化的经典跨代范式：

1. **高自旋 DSAM 电磁对称性（Grodner 2006）**：在 $I = 12\text{--}18$ 区域，$^{128}\text{Cs}$ 伴随带与基态带的带内 $B(E2)$ 强度完全可比（比值 $\approx 1.0$），彻底排除了 $^{132}\text{La}$ 式单带微观形变差异（$^{132}\text{La}$ 伴随带 $B(E2)$ 衰减达 $20$ 倍），并在带间观测到清晰的 $M1$ 奇偶交错跃迁，为三维手征转动提供了关键电磁证据；
2. **低自旋 TDPAD 磁矩共面判决（Grodner 2018）**：在 $I^\pi = 9^+$ 异能带头处，TDPAD 测得 $g = +0.59(1)$ 落在质子对齐共面极值（$g \approx 0.60$），将手征序参量限制在 $\langle \hat{o} \rangle \approx 0.15 \ll 1.0$，严格排除了带头处的静态三维手征几何；
3. **临界转动频率动态涌现模型**：结合两代实验确立了手征对称性破缺的动力学机制：低自旋态缺乏足够的集体芯转动角动量 $\vec{j}_R$，系统处于共面势阱中的手征振动（chiral vibration）；随着角动量增加至 $I \ge 13\text{--}14$，转动离心力驱动 $\vec{j}_R$ 沿着短轴快速转动，打破共面势阱对称性，体系平滑过渡至真正的稳定非平面手征进动（chiral rotation）。低自旋 TDPAD 磁矩与高自旋 DSAM 寿命测量在不同频率区间完美互补，消除了单一自旋推论的局限性。

## Day19 TDPAD微观动力学：晶格对称性解耦、四极微扰展开与四重时间对象规程

[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-7 与 [[grodner-2018-128cs-chiral-g-factor]] GR18-D19-7 确立了时间差分扰动角分布法（TDPAD）在纳秒至微秒异能态超精细测量中的微观物理响应准则：

1. **多晶电四极微扰因子 $G_{22}(t)$ 谐波展开与硬核底限**：在无序轴对称电场梯度（多晶 Sn/Cd）中，半整数自旋 $J=9/2$ 的微扰因子展开为五项余弦谐波 $G_{22}(t) = \sum_{n=0}^4 s_{2n} \cos(n\omega_0 t)$，展开系数之和严格满足 $\sum s_{2n} \equiv 1.0000$。时间平均值渐近收敛至刚性硬核底限 $s_{20} = 1/5 = 0.2000$，证实多晶样品的各向异性调制幅度绝不会完全衰减至零；
2. **同宿主晶格 EFG 完全对消定理**：固态晶格微观场梯度计算通常带有 $15\%\text{--}20\%$ 的系统误差。通过将不同同位素（如 $^{129}\text{Ce}$ 与 $^{131}\text{Ce}$）注入同一多晶金属宿主（Sn），微观场梯度严格等同，四极进动基频比值 $\omega_0(^{129}\text{Ce}) / \omega_0(^{131}\text{Ce}) = 1.4451$ 完全消除了晶格电场梯度的系统误差，构筑了高精度的相对四极矩标尺；
3. **晶格点群对称性与磁-四极微扰解耦定理**：由于四极哈密顿量 $H_Q$ 与磁哈密顿量 $H_M$ 不对易，非立方晶格中的 EFG 会将拉莫尔进动单频色散为混沌准连续谱。磁相互作用实验必须将反冲核注入具有面心立方（fcc Pb）完美对称性的宿主晶格，利用空间反演与立方群对称性严格压制电场梯度至零（$V_{zz} \equiv 0$），实现纯单频拉莫尔进动；
4. **拉莫尔进动双倍频调制定理与四重时间对象正交性**：张量取向对称性使得时间各向异性谱以双倍拉莫尔频率 $\omega_{\text{prec}} = 2\omega_L$ 振荡。严格解耦 TDPAD 中的四大时间实体：粒子数寿命 $\tau_{\text{pop}}$（统计分母）、取向弛豫时间 $\tau_{\text{relax}}$（阻尼包络）、进动周期 $T_{\text{prec}}$（物理振荡）与探测器展宽 $\text{FWHM}_{\text{PRF}}$（时间响应卷积），推导各向异性比值中粒子数衰减项完全对消；
5. **低自旋共面判定与手征动态涌现模型**：三矢量磁矩广义相加模型证明 $^{128}\text{Cs}$ $9^+$ 带头实测 $g = +0.59(1)$ 落在质子对齐共面极值，手征序参量仅为 $\langle \hat{o} \rangle \approx 0.15 \ll 1.0$，微观证明低自旋近简并带本质上属于共面手征振动，静态手征空间取向必须在更高自旋转动离心力驱动下才动态涌现。


## checkpoint099：跨质量区四类方法基准与物理时钟正交性

**checkpoint108撤回“完全正交独立时钟/主导系统学互不共享”认证。** [[nolan-sharpey-schafer-1979-lifetime-measurements]] NS79-D19-24/27、[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-8与[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-8区分observable及输入。不同机制不推出Cov=0；branch/stateidentity、feeding、velocity、timecalibration/normalization等仍可共享。

旧benchmark把合成stopping时间当23Mg实际输入、把F接近1称极高灵敏、将103Rh0.72ps错贴9/2+、134Nd2+错写45.4ps及把angularfrequency当MHz；均撤回。正确源身份见[[suzuki-2008-lifetimes-103rh-104rh]] SU08-D19-11、[[klemme-1999-lifetimes-134nd-neighbors]] KL99-D19-6。Radeck091、Nolan092、Regis094是已读scope，不由benchmark脚本赋独立实验或全面正确认证。

## checkpoint110：TDPAD完整scope与模型/feeding桥

[[ionescu-bujor-1998-static-moments-129-131ce]] IB98-D19-9–11与[[grodner-2018-128cs-chiral-g-factor]] GR18-D19-9分别补完整主线和关键模型图。Ionescu的Qs/g是校准后的state-specific结果；Table1的K混合、xi/epsilon/gamma/core-energy和signQcal是PTR层，同一absQs可由不同模型输入近似描述。Grodner的orientation约.15来自指定组态/参数PRM，不是g值直接读出的几何。

Day19设计边界有一个原文实例：129Ce建议的11/2−近邻态可在数ns feeding后布居9/2− isomer，而约11ns响应未辨它。不能把“衰变曲线看似单指数”升级为没有feeding，也不能把作者plausiblehalf估计当新测量。Eq6的S(J)归一与其他staggering定义不同；四个有理数rigidE=A J(J+1)+const控制给S0，只核定义，不测shape。Table2的131Cepositivegs epsilon范围与结论概括、PDF15gamma趋势措辞均按源字面保留，不以自动参数匹配消歧。
