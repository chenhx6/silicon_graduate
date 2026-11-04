---
type: concept
title: "卢希庭第九章：核反应运动学、反应机制与光学模型的实验接口"
aliases: [核反应运动学与光学模型, Lu reaction kinematics, reaction-channel optical-model interface]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
tags: [nuclear-reactions, reaction-kinematics, optical-model, compound-nucleus, direct-reaction, in-beam-experiment]
sources: [book-lu-nuclear-physics-chinese, book-bertulani-nuclear-reactions, book-iaea-reaction-data-handbook]
---

# 卢希庭第九章：核反应运动学、反应机制与光学模型的实验接口

## Question and Scope

本页把《原子核物理（修订版）》第九章中最直接服务于实验设计和谱学分析的
内容整理成一条可检查的链：

```text
反应道与守恒量
    -> Q 值和质心系运动学
    -> 反应/分波/微分截面
    -> 光学模型的入射阶段
    -> 直接反应、复合核和预平衡过程
    -> 出射道选择与在束 gamma 谱学
```

本页只记录已从扫描原书页面图像核对的公式和物理结构。OCR 文本用于定位，
不作为复杂公式、上下标、图表和符号正负号的独立证据。章节其余内容仍按
`book-lu-nuclear-physics-chinese` 的 `skimmed` 边界处理。

## Definition

对靶核 \(A\) 和入射粒子 \(a\) 的反应，教材写成
\[
A+a\rightarrow B+b+Q.
\]
入射道由 \(A+a\) 定义，出射道由 \(B+b\) 定义。同一入射道可以对应多个出射道，
同一出射道也可以由不同入射道产生。因此，实验中的“反应”必须带有道标记，
不能把一个总产额直接当成某个唯一核素或唯一反应机制的证据。

教材区分：

- **核散射**：出射粒子与入射粒子相同；弹性散射保持靶核内部能量不变，
  非弹性散射使靶核进入激发态。
- **核转变**：出射粒子不同于入射粒子，例如转移、俘获或蒸发道。
- **低能核反应**：教材按入射粒子单核子能量低于核内费米能量的尺度讨论，
 其出射粒子数通常有限；中能和高能区需要额外的碎裂、介子和相对论处理。

## Necessary Assumptions

### 1. 质心系和实验室系

靶核在实验室系静止、非相对论近似成立时，入射粒子与靶核的约化质量为
\[
\mu=\frac{m_a m_A}{m_a+m_A},
\]
相对运动动能为
\[
E'=\frac{m_A}{m_a+m_A}E_a^{\mathrm{lab}}
\]
也就是常用的质心系能量
\[
E_{\mathrm{cm}}\equiv E'
\]
对核反应常用的质量数近似 \(m_a\propto A_a\)、\(m_A\propto A_A\) 给出
\[
E_{\mathrm{cm}}\simeq\frac{A_A}{A_a+A_A}E_{\mathrm{lab}}.
\]
这一关系是入射能量、库仑势垒、激发函数以及反应道比较的第一步；对重离子体系，
不能把实验室束流能量直接代入质心系截面公式。

### 2. Q 值、激发能和守恒量

教材用动能差定义反应能：
\[
Q=(E_B+E_b)-(E_A+E_a),
\]
在使用原子质量时可写成
\[
Q=(M_A+M_a-M_B-M_b)c^2,
\]
电子质量因反应前后总电荷相同而相消，原子电子结合能通常在该层次忽略。
若出射残核处于激发态，质量差得到的 \(Q\) 与实验运动学中按基态假设得到的
\(Q'\) 的差给出残核激发能：
\[
E^*=Q-Q'.
\]

核反应的入口检查至少包括电荷数、质量数、总能量、动量、角动量和总宇称。
其中角动量和宇称约束会限制允许的相对轨道角动量 \(\ell\)，这直接影响角分布、
分波透射以及最终能带的自旋布居。

### 3. 光学模型的模型边界

光学模型描述入射粒子在靶核平均场中的第一阶段传播和散射。它用复势表示：
\[
U(r)=V(r)+iW(r)
\]
或等价的“实部势阱加负虚部吸收”符号约定。原书先用复矩形势阱说明：
\[
V(r)=
\begin{cases}
-(V_0+iW),&r\le R,\\
0,&r>R.
\end{cases}
\]
虚部使核内波函数衰减，代表入射通量被吸收到非弹性、转移和复合系统通道；
它不是一个可直接解释为核结构势能面的形变势。实际拟合通常使用 Woods–Saxon
体势、表面吸收项、库仑项和自旋–轨道项，参数需要由散射数据或经过验证的全局势给出。

## Discriminating Observables

### 1. 分波截面和透射系数

教材给出吸收截面的分波表示：
\[
\sigma_a=\pi\lambda^2\sum_{\ell=0}^{\infty}(2\ell+1)T_\ell
       =\sum_{\ell=0}^{\infty}\sigma_\ell,
\]
其中 \(T_\ell=1-|\eta_\ell|^2\) 是第 \(\ell\) 分波的穿透系数。
在复合核/直接反应的三阶段图像中，低 \(\ell\) 分波更接近靶核中心，
通常更容易贡献复合核形成；高 \(\ell\) 分波更偏向表面和掠射几何，
直接反应贡献可能更显著。教材随后用切断角动量 \(\ell_c\) 写出示意性的
复合核形成截面：
\[
\sigma_{\mathrm{CN}}=
\pi\lambda^2\sum_{\ell=0}^{\ell_c}(2\ell+1)T_\ell.
\]
这是一种反应机制分区图像，不能替代带耦合道、熔合概率 \(P_{\mathrm{CN}}\)、
裂变竞争和统计蒸发的完整计算。

### 2. 截面分解

卢希庭第九章给出平均截面之间的关系：
\[
\sigma_t=\sigma_{\mathrm{pot}}+\sigma_a,
\qquad
\sigma_a=\sigma_{\mathrm{CN}}+\sigma_D,
\]
\[
\sigma_{\mathrm{sc}}=\sigma_{\mathrm{pot}}+\sigma_{\mathrm{res}},
\qquad
\sigma_r=\sigma_{\mathrm{res}}+\sigma_D.
\]
这里 \(\sigma_{\mathrm{pot}}\) 是势散射，\(\sigma_{\mathrm{res}}\) 是经复合核形成的
共振散射，\(\sigma_D\) 是直接反应，\(\sigma_r\) 是去弹性散射/反应截面。
这些量的加和关系是实验报告中的记账约束；不同截面只有在明确是否做能量平均、
是否包含共振散射以及如何定义吸收时才可互相比较。

### 3. 直接反应与复合核的判别

教材将反应过程分为独立粒子阶段、复合系统阶段和最后分解阶段。直接过程保留
部分入射道记忆，常见特征是选择性较强、出射粒子能量较集中、角分布明显前倾或后倾。
复合核过程趋向统计平衡，出射粒子能谱更接近统计分布，角分布更接近各向同性，
但在有限自旋取向、角动量守恒和通道选择下仍可能出现非各向同性。
预平衡发射位于两者之间，不能仅凭一张角分布图强行归类。

## Experimental Interface

对于在束 \(\gamma\) 谱学和重离子反应分析，建议按以下顺序记录输入和证据：

1. 以靶核、弹核、束流 \(E_{\mathrm{lab}}\)、目标出射道和质量评价表为入口，
   先算 \(E_{\mathrm{cm}}\)、\(Q\) 和残核 \(E^*\)；质量数近似只能作为快速检查。
2. 将实验室系的带电粒子能量和角度转换到质心系，再与 \(d\sigma/d\Omega\)、
   激发函数或光学模型曲线比较，同时记录 Jacobian、靶厚能损、探测器固角和效率。
3. 将低能量角分布中的前倾/后倾、离散出射能量、激发态选择性与统计能谱作为
   机制判据的候选项；把“候选”与“已证实”分开写。
4. 对熔合蒸发实验，把复合核入口的 \(E^*\) 和角动量分布作为后续蒸发、
   \(\gamma\) 级联和 Yrast 线馈入的条件输入；不可用单一几何截面替代残核产额。
5. 对 A≈130 三轴形变课题，反应设计的直接任务是控制入口自旋/激发能、
   选择目标蒸发道并减少邻道污染；三轴、手征或摆动结论仍必须回到能级、
   分支比、DCO/ADO、偏振、寿命和模型比较的联合证据。

## Supporting Evidence

- 《原子核物理（修订版）》第九章开头与 §9.1：印刷 pp. 227–230 / PDF
  pp. 237–240，核反应定义、反应分类、反应道和守恒量；PDF p. 237、p. 239
  进行了页面图像核对。
- §9.2：印刷 pp. 230–233 / PDF pp. 240–243，\(Q\) 值、原子质量表达式和由
  出射粒子运动学求残核激发能；PDF p. 243 的示例页进行了图像核对。
- §9.3：印刷 pp. 233–253 / PDF pp. 243–263，实验室系/质心系、相对运动、
  分波和散射截面；PDF p. 244 的 \(E'=\frac12\mu v_a^2\) 关系进行了图像核对。
- §9.7：印刷 pp. 253–254 / PDF pp. 263–264，三阶段描述、直接作用/复合核、
  预平衡边界及截面加和关系；PDF p. 264 的截面分解图进行了图像核对。
- §9.8：印刷 pp. 254–259 / PDF pp. 264–269，复势、虚部吸收、平均截面、分波
  透射和复合核形成的切断角动量；PDF pp. 264–265、p. 269 进行了图像核对。
- §9.9：印刷 pp. 259–278 / PDF pp. 269–288，复合核形成/衰变独立性、
 统计衰变和 Breit–Wigner 共振；本页只使用已定位的模型结构，未宣称整节公式审计。
- §9.11：印刷 pp. 279–286 / PDF pp. 289–296，重离子反应总截面和经典/抛物线
 近似；PDF p. 291 的 \(\sigma_r=\pi\lambda^2\ell_{\mathrm{gr}}^2\) 与
  \(\sigma_F=\pi\lambda^2\ell_{\mathrm{cr}}^2\) 页面进行了图像核对。

## Counter-evidence and Competing Interpretations

- **光学模型的平均场描述不等于机制分解的唯一实验事实。** 同一虚部势可以把多个
  非弹性、转移和复合通道的平均吸收合并在一起；要分辨通道，仍需角分布、出射粒子、
  \(\gamma\) 级联、反冲质量和独立效率信息。
- **低 \(\ell\)/高 \(\ell\) 机制划分是有条件的。** 通道耦合、形变、库仑激发、
  预平衡发射和不完全熔合会改变简单切断图像；\(\ell_c\) 不能直接当作实验得到的
  复合核自旋上限。
- **统计性不能由各向同性单独证明。** 有限寿命、角动量取向、探测器接受度和
  反冲运动学都可能改变角分布。复合核、直接反应和预平衡过程可以叠加。
- **质量数近似不适合最终的 Q 值和产额。** 最终分析应使用评价质量、核素存在性、
 结合能/分离能及其不确定度；现有 `heavy_ion_kinematics.py` 的质量数近似适合
 入口量级检查，不能替代质量表和统计模型。

## Our Current Position

本页将 Lu 第九章作为中文反应术语、实验室/质心系接口和模型边界的基础来源。
现有 `system/scripts/analysis/` 中的 `heavy_ion_kinematics.py`、
`optical_model_potential_reaction_cross_section_calculator.py` 和
`compound_nucleus_evaporation_calculator.py` 可以作为可重复的量级检查工具，
但输出必须保留其代码中声明的“质量数近似、唯象势、单势垒或示意统计”边界。
下一步应把评价质量、能损、探测器响应和通道级不确定度接到同一输入对象，
再用于 A≈130 的具体实验方案比较。

## Sources

- [[book-lu-nuclear-physics-chinese]]
- [[book-bertulani-nuclear-reactions]]
- [[book-iaea-reaction-data-handbook]]
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]
- [[heavy-ion-deflection-functions-and-rainbow-scattering]]
