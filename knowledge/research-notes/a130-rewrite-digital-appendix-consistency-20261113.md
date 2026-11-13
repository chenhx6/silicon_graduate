---
type: research-note
title: "A130重写：数字算法附录一致性与硬件实现边界"
aliases: [A130 digital appendix consistency 20261113, 附录E数字算法一致性研学笔记, G95 Appendix E 证据研学]
created: 2026-11-13
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
authors: [G95 (Gemini Tiered/high)]
created_from: "A130博士论文重写附录工程：附录E（数字算法）独占证据与科学推演"
promotion_target: doctoral-nuclear-structure-foundations
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing, doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync, wu-2021-general-purpose-digital-daq-waveform-analysis, wolff-1982-poisson-arrivals-see-time-averages]
tags: [digital-algorithms, trapezoidal-shaper, pole-zero-cancellation, cfd, linear-interpolation, pixie-16, pasta-theorem, joint-live-time]
---

# 数字算法先满足同一递推，再对照真实数据头

## Research Trigger

附录E与正文5.3/5.4/5.5共同连接模拟波形、离散算子、时间戳和事件流。问题既来自数学上不相同的差分式被写成同一个H(z)，也来自对原图字段、固件版本和参考测度的过度概括。

## Grounded Evidence

| 来源与实际定位 | 本页使用范围 | 边界 |
|---|---|---|
| [[wu-hongyi-2020-general-purpose-digital-daq-thesis]]，规范主件143页授权版；印20/PDF32、印25/PDF37 | 梯形成形、原式末项歧义及CFD记号，以正文5.3/5.4记录的公式桥为准。 | 沿声明的LTI输入延迟重建，不冒称取得作者勘误。 |
| 同书PDF55/印43 Fig2.8，已渲染逐格核对 | Word0 EventLength[30:17]、Finish Code bit31（1为堆积）；Word2[31:16]整体CFD Result；Word3 TraceLength[30:16]、OutOfRange bit31。 | 这是该图版本；不凭未知固件猜CFD强制触发子位。 |
| 同书PDF55–56/印43–44 | 标准固件波形缓存满时整事件损失；作者定制固件可仅存头、不记录波形。 | B115–116/PDF127–128讲死时间模型，不是这一缓存策略；没有在此取得统一高水位/溢出flag定义。 |
| [[wu-2021-general-purpose-digital-daq-waveform-analysis]] | 实际8页载体，波形处理与成形背景，按canonical来源既有选读。 | 不使用旧笔记虚构的PDF路径和哈希。 |
| [[doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing]] | 实际6页载体，Eq3及定时优化，与正文5.4的算子/输入/参数桥对照。 | 不能把其w与本文f直接同名等同，更不能把原文页号写成不存在的PDF45–52。 |
| [[doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync]] | 实际7页载体的多机箱同步背景。 | 同步背景不授权把所有现代模块都写成同一比特协议。 |
| [[wolff-1982-poisson-arrivals-see-time-averages]] | 10页本地载体，印223–226/PDF2–5，LAA及Theorem1。 | 到达前状态和长期极限条件；不是有限时间精确相等，也不自动处理依赖未来到达的双时函数。 |

## Provisional Reasoning

### 1. 同一个M、两个不同输出层次

\[
\alpha=e^{-T_s/\tau_d},\qquad M=\frac{\alpha}{1-\alpha}
=\frac1{e^{T_s/\tau_d}-1},\qquad\alpha=\frac{M}{M+1}.
\]
M与α同向变化，不能把M偏大同时写成α偏小。因果纯指数v[n]=Aαⁿu[n]取v[0]=A、负索引为零。单独的PZ阶跃递推vp[n]=vp[n−1]+v[n]−αv[n−1]给平台A。

组合梯形则用四延迟d[n]=v[n]−v[n−k]−v[n−ell]+v[n−k−ell]，随后p+=d、r=p+Md、s+=r。其H=[(M+1)−Mz⁻¹]BkBell本身是有限多项式；匹配输入时输出A(M+1)(bk*bell)，平台高Ak(M+1)。末项重建、参数ell≥k、平顶(ell−k)Ts及归一均与正文一致。

对本文四级梯形与正指数输入，M偏大可留负尾，偏小可留正尾；这一尾形不能直接套给单独的vp阶跃或任意基线算法。后续能量偏差还由取幅、基线估计与判弃共同决定。

### 2. 平顶与噪声不能只用一个“更长”描述

理想匹配且取幅窗完整覆盖有限电流支撑时，足够长的平顶是消除收集形状依赖的一项足够条件；双指数渐近尾没有硬截断τcoll上界。线性固定滤波和平稳噪声下，能量方差由实际校准传递函数和噪声谱积分得到。

固定滤波形状、同比伸缩时间尺度的经典串/并联白噪声标度，不能无条件搬给“只增加平顶、上升段不变”。本文没有证明梯形对任意白噪声或平顶约束都最优，也没有把IIR结构等同为必然无限误差。

### 3. CFD算子、选根与误差方向

本文C[n]=F[n−d]−fF[n]，F是声明的快波形。若写成Ya[n]=F[n]−aF[n−d]，则在同输入/延迟下C=−fY_(1/f)，不是只改符号、保留同名分数。选负至非负根需先规定记录、前沿阈值和有效区间；不存在对任意F都适用的固定d与上升时间比例。

光滑非零斜率、Ts较小时，以估计减真值定义误差，领先项为
\[
\widehat t-t_\times\simeq-\tfrac12T_s^2\phi(1-\phi)C''(t_\times)/C'(t_\times).
\]
φ(1−φ)的中点极值只在相对曲率固定时提供主阶调制信息。小噪声抖动用经过滤波的σC/|C′|，不直接用原始ADC噪声，也不必要求噪声为白。

参考伪代码只处理一份已隔离记录，找到首个合格根即返回；连续多事件需另定义再装锁、迟滞、超时、堆积与holdoff，不能用注释假装已实现。定点位宽、舍入和饱和也不由浮点例子认证。

### 4. 数据头与二值概率的具体例外

Fig2.8的头长度是包含可选块的32位字数，最少4；Trace Length按采样点/16位字计，成对打包后占一半数量的32位数据字。单通道hit不是整次核碰撞，公共触发也可使通道hit相关；保头丢波形只减轻特定缓存瓶颈，不保证总接受度无损。

一般随机变量零Cov不保证独立，但固定参考测度、固定时差的一对Bernoulli指标Xi是例外：p11=L1L2后，其余三格由边缘概率相减便全部因子化。这不等于整个通道过程、其他标记或所有时差独立。

PASTA用于到达前状态，在所用长期极限与Poisson/LAA条件下比较平均。共享busy的正Cov例还需要零时差、free条件独立、0<fbusy<1与正free概率；不能把该符号推广到所有实际总线系统。

## Assumptions

- 纯指数/PZ解析结论先设零历史、线性匹配和声明的取幅方式；有限上升与基线估计另保条件。
- 传递函数的噪声积分采用平稳线性近似，不能把条件触发选择自动当原始平稳噪声。
- CFD连续延拓在选根邻域光滑且斜率非零，目标根分支稳定。
- 数据格式仅按已核论文版本，不替用户指定实际硬件或固件。

## Competing Explanations

波形失配、有限收集、基线估计和堆积均能移动峰位；参考时钟与共同噪声也能影响差谱。一个滤波名、码字位宽或代数恒等式不能唯一识别造成实验展宽的机制。

## Transfer Conditions

迁移算法须同步输入、延迟、归一与边界。迁移数据协议须对实际版本逐字段核验。以参考测度组织联合接受度时，也须说明它来自时间采样、pulser还是目标级联。

## Failure Conditions

虚构原件路径/SHA、错把B115定位为缓存策略、把16位结果全当有效时间细位、混用阶跃/梯形输出、把注释当状态机实现及遗漏Bernoulli例外，都会造成可检查的不一致。

## Falsification or Reverse Tests

canonical producer现含五项有限控制：纯指数递推与直接卷积、非零常基线、同形幅度缩放的CFD、M/α失配符号、已知零点二次曲线的割线领先误差。父实际运行的结果在outputs/l4/20261114-A130-digital-algorithms-controls/results.json，带producer SHA及Python/NumPy版本；最大平台相对偏离约5.24e−15、递推/卷积约5.60e−15，均为教学数值检查，不是实测能量或时间分辨。

## Open Questions

真实定点资源、计数率相关响应、非线性堆积、条件基线噪声及所用固件的全部状态机仍需各自证据；本页未虚构网表或用户装置验证。

## Human Review

无新增真实用户人工审核事件；为Agent原图、数学与有限输入控制复核。

## Promotion or Rejection History

- G95返修后父回PDF55图2.8及PDF56原文，修正父合同不准的页码导航和台账旧路径；同时纠正M/α反向、噪声最优性及Bernoulli限定。
- 与本次5.5窄修、附E及独立producer同步，原worker回执保留为历史输入，不充当最终物理认证。
