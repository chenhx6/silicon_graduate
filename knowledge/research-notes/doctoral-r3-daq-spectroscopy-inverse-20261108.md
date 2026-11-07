---
type: research-note
title: "R3 实验解释：数字获取、联合接受度与电磁强度反演"
aliases: [R3 DAQ spectroscopy inverse]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G49/G50研学与总控原件复核、率方程推导"
promotion_target: ""
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, campaign-g07-gorgen-2004-163lu-quadrupole-moments, doctoral-r1-g27-clement-2007-prc-krypton-coulex, lange-kumar-hamilton-1982-multipole-admixtures]
tags: [doctoral-foundations, digital-daq, efficiency, dead-time, mixing-ratio, lifetime, covariance]
---

# 事件字不是γ强度，γ强度也不是核形状

## Research Trigger

吴鸿毅论文为电子学原始起点。本轮连接固件/选择逻辑、谱学计数、
寿命/分支和物理反演，补上只讲滤波器时会漏掉的实验因果链。
所有仪器数值只属于其原实验，未取得用户硬件配置或波形。

## Grounded Evidence

| 来源 | 实际locator | 学习对象 |
|---|---|---|
| [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] | PDF53–56/印刷41–44, Fig.2.8 | 事件字、时间戳、标准/定制缓存行为 |
| 同来源 | PDF104–109/印刷92–97 | 相位、上升沿、插值与定时 |
| 同来源 | PDF127–128/印刷115–116 | 两种死时间模型及随机输入前提 |
| [[campaign-g07-gorgen-2004-163lu-quadrupole-moments]] | PDF2–4, Tables I–II | DSAM、feeding、薄靶分支及平均δ依赖 |
| [[doctoral-r1-g27-clement-2007-prc-krypton-coulex]] | Tables V–VI,X–XI及矩阵元分析 | 多步干涉、对角矩阵元和混合推断 |
| [[lange-kumar-hamilton-1982-multipole-admixtures]] | 印刷121–122, Eqs.(2.1)–(2.11) | 光子混合比与相位约定 |

率关系和共同忙源例子为任务推导；不是原论文新增实测结果。

## Provisional Reasoning

### 1. 从电荷脉冲到有条件保留的事件

探测器脉冲经前放、ADC、触发/能量滤波、定时和堆积判别，才生成列表事件。
R1已经核PZC与CFD理想控制，本轮不换参数重跑同一个toy。
Fig.2.8给48位时间戳及后续16位CFD字段；
字段宽度说明编码容量，不直接说明实际时间分辨。
粗时间戳计数周期不必等于ADC采样周期；不同速率模块的细定时解释不同。
插值能给亚采样估计，精度仍受噪声、相位、上升时间、时钟/同步与算法影响。
经验“5Ts”不作所有仪器的定律。

标准/定制固件在波形FIFO满时行为有别（PDF55–56）。
保存事件头而丢波形，可提高某类事件可用性；
但需要离线波形才能完成的PSD、定时重算或堆积选择会受到另一种损失。
因此“触发已计数”“能量事件可读”“通过物理cut”是三个不同样本。

### 2. 单道 live 为什么不自动给双道符合 live

将一次真实事件条件写为 \(\xi=(E_1,E_2,\Delta t,\Omega_1,\Omega_2,\ldots)\)，
测量均值可写
\(\mu_a=\int d\xi\,R_a(\xi)\,s(\xi)+B_a\)。
R含效率、时间窗、堆积、触发/忙信号、读出和分析选择；
把R拆成各因子乘积，需要条件独立和校准依据。
以硬件live时间比例代替所有clean事件接受度并不普遍成立。

**任务反例：**令共同live指示C、两道各自指示U,V独立，
其概率为pc,p1,p2；两道live为L1=CU,L2=CV。
则 \(P(L_1L_2=1)=p_cp_1p_2\)，
而 \(P(L_1=1)P(L_2=1)=p_c^2p_1p_2\)。
共同忙源只计一次，不能由两个单道live相乘自动得到。
这是列明独立条件的例子，不是所有DAQ的通式。

吴论文附录给非延伸模型 \(r_{\rm obs}=r/(1+r\tau_d)\)、
延伸模型 \(r_{\rm obs}=r e^{-r\tau_d}\)的适用背景。
这些是特定随机到达/理想死时间模型；真实触发、堆积cut及缓存可更复杂。
延伸模型非单调反演需保留率分支，不从一个计数比唯一反推真实入射率。

### 3. δ 是无量纲光子振幅比

对指定约定的M1+E2光子发射，\(\delta^2=\lambda_\gamma(E2)/\lambda_\gamma(M1)\)。
它包含能量与单位换算，不是带不同单位的裸RME直接相除。
正确的相位约定转换可改δ符号及干涉项写法，保持δ²和预测不变。
单独任意改符号而不改几何系数会改变拟合。

角分布或DCO模型常给δ的二次有理式；
反演可能零、一、两实根，且要排除分母零点。
有限误差、取向、去取向、gate及探测器几何要进共同似然。
额外偏振可能分根，也可能仍有多个允许分支。
不声称“偏振只能定电磁类型”，也不声称“联立必双实根”。
同级联已知纯跃迁可以约束取向/响应，但不保证自动完全分离全部滋扰参数。

### 4. τ、总分支与光子分支不能混用

记τ为母能级**平均寿命**，\(\lambda_{\rm tot}=1/\tau\)，
能量宽度为 \(\Gamma_{\rm tot}=\hbar\lambda_{\rm tot}\)。
若b_i为含内转换的总跃迁分支，ICC为α_i，则

\[
\lambda_{\gamma i}=\frac{b_i}{\tau(1+\alpha_i)},\qquad
T_{1/2,i}^{\gamma}=\frac{(1+\alpha_i)T_{1/2,\rm tot}}{b_i}.
\]

若a_i仅为相对光子强度归一，且所列γ/IC支路完整、无额外E0/粒子等竞争，
则改用
\(\lambda_{\gamma i}=a_i/\{\tau\sum_j a_j(1+\alpha_j)\}\)。
漏支路会改变归一；混合跃迁的总ICC也须用相应分量一致合成。
光子E2份额为δ²/(1+δ²)，M1份额为1/(1+δ²)。
所以固定相同τ、b时，改混合比分支会改两个分多极强度；
不能单凭某一个δ阈值命名或排除集体模式。

\[
B(XL;i\to f)=\frac{|\langle f\|\mathcal M(XL)\|i\rangle|^2}{2I_i+1},
\quad
\frac{B(XL;f\to i)}{B(XL;i\to f)}=\frac{2I_i+1}{2I_f+1}.
\]

RME(E2)单位e·fm²，B(E2)为e²·fm⁴；B(M1)常用μN²。
光子率含相应单位系数乘 \(E_\gamma^{2L+1}B(XL)\)；
上下行方向和单位先校对，再比较数值。0→2与2→0的B相差5倍。

### 5. 寿命测量提供什么独立信息

DSAM利用减速期间的连续Doppler线形，必须给速度历史、阻止本领、
feeding、取向/几何与谱重叠。Görgen明确未计入阻止本领选择的系统误差，
并用薄靶分支校正TSD2出带；Table II的绝对分多极强度还用既有平均δ。
新增寿命信息有实质价值，但多个结果不全部成为独立实验。
RDM/RDDS借飞行距离分辨发射时段，可降低某些连续减速依赖；
降速箔、feeding、距离零点和接受度仍须建模，不能称“完全不依赖阻止/响应”。

同母态两条校正光子分支的率比没有共同τ；
同阶E2强度比再乘各自 \(E_\gamma^{-5}\) 和混合份额即可。
这只消去代数中共同的τ，不保证分支测量的背景/门选误差同时消失。
跨母态的τ一般不消去；公共阻止参数也可对不同态有不同灵敏度。
一般误差传播用 \(V_y\simeq J V_x J^T\)，近似适用于局部可线性化分支。
乘性系统源可给 \(ss^T\)，不必是“全1矩阵加独立对角噪声”；
多根/边界用完整似然、profile或模拟保留非高斯结构。

### 6. CoulEx 网络为何增加信息而仍需要模型

多步CoulEx的干涉与重取向可约束相对符号、对角矩阵元及闭合环乘积；
单态重新定相会改若干RME符号，但闭合环不变。
有限网络的q2、q3与高阶闭合有截断及误差，
其比值是有权重的量子形状信息，不普遍等于未加权平均γ。
对角矩阵元的正负要结合I、K、转子映射才能转成prolate/oblate解释。

给定模型的V、质量张量、E2算符通过态与能谱影响CoulEx数据，
所以不能说CoulEx“对质量无一阶灵敏度”。
有限观测仍不能无模型唯一重建任意函数V(q)、Bμν(q)；
R1/T03展示了静态矩与动力学能标的区别，R2给具体响应实现。

## Assumptions

各率归一、ICC及分支的定义先固定。联合接受度和协方差需实际硬件/分析信息；
本页没有用未知配置计算机时或用户实验误差。

## Competing Explanations

弱支路、角各向异性或线形变化可同时受真实多极变化与选择/feeding/响应影响。
用独立标定、变化gate、距离/角度/率扫描等限制替代解释，
不默认某个核的已发表现象是仪器伪像。

## Transfer Conditions

从校准脉冲到列表事件，再到联合接受度、分支/寿命、RME和形状解释逐层迁移。
数学关系可复用；参数、固件、rate window和探测器几何须逐实验重验。

## Failure Conditions

把CFD位宽当分辨、live当clean比例、总/光子分支混用、
把所有Cov写成同一结构或用两声子2倍强度作无条件否决线，均失效。

## Falsification or Reverse Tests

独立观测应选能改变实际解释排序的逐态δ、绝对寿命、矩阵元或接受度控制。
不补造σ阈值、百分比系统误差或“测一项就确证”的规律。
数学多根与有限I非谐控制见[[doctoral-r3-quantum-labels-and-model-boundaries-20261108]]。

## Open Questions

实际用户采集是否有共同busy、波形条件丢失及母态相关的联合效率？
没有配置时这是后续应用问题，不阻止完成一般方法学习。

## Human Review

总控原件核查与条件推导，未记录用户人工逐项审阅。
G49/G50初稿中的固定率/σ门、必双根、刚性必谐和普适截断百分比均未采纳。

## Promotion or Rejection History

- 2026-11-08：将吴论文电子学推进到完整谱学反演链；保留源内应用依赖，不给用户仪器虚构性能。
