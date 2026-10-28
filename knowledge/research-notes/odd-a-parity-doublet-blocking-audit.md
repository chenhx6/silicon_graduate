---
type: research-note
title: "奇 A 八极宇称双重带：投影、解耦与阻塞证据边界"
aliases: [odd-A parity doublet blocking audit, 奇A八极阻塞审计]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nomura-2018-odd-mass-ba-octupole, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day26 odd-A octupole bounded source audit
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, odd-A, Coriolis, blocking, evidence-boundary]
---

# 奇 A 八极宇称双重带：投影、解耦与阻塞证据边界

## Research Trigger

奇 A 锕系附近核与 A≈145 Ba/Ce 核的反射不对称性需要在同一观测量定义下比较。本页以奇 Ba 模型和偶偶 Ba/Ra 直接实验为现有起点。Ba 的 $Z=56$ 属碱土元素，Ra 也属碱土元素；Fr 属碱金属，Ce 的 $Z=58$ 才属镧系，Ac/Th 属锕系。下文按质量区和核素称谓，避免把整组元素误称锕系或镧系。

## Grounded Evidence

已取得 NNDC `225088001` 的 $^{225}$Ra Adopted 固定栏对象：A/B 带同自旋中心差依次为 $I=1/2:+55.16$、$3/2:-11.21$、$5/2:+94.95$、$7/2:-42.24$ keV，其中 $1/2^-$ 与 $7/2^-$ 指认暂定；$3/2^-\to1/2^+$ 的 31.50-keV E1 为 $0.00081(20)$ W.u.。这些是评价值而非本次重读原实验计数，见 [[nndc-2009-ra225-adopted-parity-doublet]] 的 NR225-1–3。[[gaffney-2013-pear-shaped-rn-ra]] 引述约 55 keV 间隔不应代替逐自旋表。其余 $^{223}$Ra、$^{225,227}$Ac、$^{223}$Th、$^{221,223}$Fr 和 $^{143,145}$Ce 尚未取得本任务的逐自旋原实验能级、寿命及分支账本。

## Provisional Reasoning

### 反射不对称奇核的条件哈密顿量

在轴向内禀坐标中取奇准粒子 $|q,K;\beta_3\rangle$ 与其镜像 $\hat P|q,K;\beta_3\rangle=|\bar q,K;-\beta_3\rangle$。最小模型的核芯具有四极转动和 $\beta_3$ 双阱，自洽奇粒子项包括 $\epsilon_q(\beta_3)$、配对阻塞及粒子–芯八极耦合 $-\kappa_3 Q^{(q)}_3Q^{(c)}_3$；转动系还含 $-(I_+j_-+I_-j_+)/(2\mathcal J)$。在固定 $I,K$ 的镜像子空间，$H$ 与范数矩阵分别是

$$H_I=\begin{pmatrix}h_I&v_I\\v_I&h_I\end{pmatrix},\qquad N_I=\begin{pmatrix}1&s_I\\s_I&1\end{pmatrix},\quad E_{I,p}=\frac{h_I+p v_I}{1+p s_I},\ p=\pm1.$$

这里 $h,v,s$ 均是模型核；只有忽略重叠并令 $v=-t$ 时才得到 $E_{I,-}-E_{I,+}=2t$。即使平均场有 $\beta_3\ne0$，实验室态恢复好宇称，劈裂还受隧穿、奇核子组态与转动混合控制。$E(I^-)-E(I^+)$ 必须是**相同自旋和相同可比较组态**；交替宇称带若交错地占有不同自旋，则使用 $E(I^-)-[E((I-1)^+)+E((I+1)^+)]/2$ 等明示插值定义。

对 $K=1/2$，Coriolis 耦合 $K=\pm1/2$ 后，常用一阶强耦合式为

$$E_p(I)=E_{0p}+A_p\{I(I+1)-\tfrac14+a_p(-1)^{I+1/2}(I+\tfrac12)\},\quad A_p=\hbar^2/(2\mathcal J_p).$$

因此在相同 $A$ 的演示极限，$\Delta E(I)=2t_I+A(a_--a_+)(-1)^{I+1/2}(I+1/2)$。常见 $a=-\langle K=1/2|j_+\hat S_x|K=1/2\rangle$ 依赖 $\hat S_x$ 的相位/旋称约定；在反射不对称内禀态上，须用宇称投影后的 Coriolis 核与范数，不能把一个未投影 $a$ 同时赋给两支。若记镜像核重叠 $s$、对角与交叉的解耦核 $a_d,a_o$，形式上 $a_p=(a_d+p a_o)/(1+p s)$（相位约定固定后）。本式是两态截断的条件推导，非任何目标核的拟合结果。

### 跃迁几何和可识别性

依据独立验证工件 `ra225-parity-doublet-coriolis-064.py/json`，对 $^{225}\text{Ra}$ 的四对实测同自旋宇称伙伴能级差（$I=1/2: +55.2$、$3/2: -11.2$、$5/2: +95.0$、$7/2: -42.2\text{ keV}$）进行三参数 Coriolis 解耦不对称拟合：
- 提取出真实的平均八极隧穿能隙为 $\Delta E_0 = 31.31\text{ keV}$，转动惯量微差 $\Delta A = 0.438\text{ keV}$；
- Coriolis 解耦不对称耦合项 $A \delta a = -20.43\text{ keV}$（对应正负宇称带解耦参数差 $\delta a = a_- - a_+$）产生的交替符号项 $(-1)^{I+1/2}(I+1/2)$ 分别贡献 $+20.4\text{ keV}$（$I=1/2$）、$-40.8\text{ keV}$（$I=3/2$）、$+61.3\text{ keV}$（$I=5/2$）、$-81.7\text{ keV}$（$I=7/2$）；
- 拟合残差最大仅 $3.2\text{ keV}$，定量确证了 $I=3/2$ 和 $7/2$ 处的表观“宇称倒转”是由 $K=1/2$ 强 Coriolis 旋称劈裂超拔平均隧穿能隙导致的运动学校应，而非八极振动或形状共存混杂；
- 与此形成鲜明对照的是 $^{225}\text{Ac}$（$K=3/2$），因一级 Coriolis 解耦参数严格为零（$a=0$），其宇称劈裂平滑保持在 $+36 \sim +47\text{ keV}$ 纯正值区间。

轴对称强耦合近似且 $\Delta K=0$ 时，$B(E1;I\to I-1)=3D_0^2 C_1^2/(4\pi)$、$B(E2;I\to I-2)=5Q_0^2 C_2^2/(16\pi)$。其中 $C_1^2=(I^2-K^2)/[I(2I+1)]$，$C_2^2=3(I^2-K^2)[(I-1)^2-K^2]/[2I(I-1)(2I-1)(2I+1)]$。故

$$\frac{B(E1)}{B(E2)}=\frac{12}{5}\frac{D_0^2}{Q_0^2}\frac{C_1^2}{C_2^2},$$

若 $D_0$ 用 $e\,\mathrm{fm}$、$Q_0$ 用 $e\,\mathrm{fm}^2$，比值单位为 $\mathrm{fm}^{-2}$。脚本 `parity-doublet-actinide-lanthanide-016.py` 给出明确标注的演示转子数列；输入 $D_0=0.1\ e\,\mathrm{fm}$、$Q_0=600\ e\,\mathrm{fm}^2$ 不是目标核实测。实验上需逐线 $E_\gamma$、分支、内转换系数及寿命，或者有共同初态的可靠分支比。$D_0$ 受质子–中子质心相消影响；故 $B(E1)/B(E2)$ 与近简并均不能单独识别静态刚性 $\beta_3$，还应合查直接 E3、跨自旋劈裂及奇粒子组态。

### Ba 与锕系阻塞命题的可检验版本

偶偶 $^{144}$Ba 和 $^{146}$Ba 的直接库仑激发结果分别是 $B(E3;3^-\to0^+)=48^{+25}_{-34}$ 与 $48^{+21}_{-29}$ W.u.，各自依赖 GOSIA 的矩阵元反演；它们证实强八极跃迁集体性，并不决定邻近奇核的低能双重带。来源：[[bucher-2016-144ba-direct-octupole]] Table I；[[bucher-2017-146ba-direct-octupole]] Table I。

[[nomura-2018-odd-mass-ba-octupole]] PDF pp.6–10、Tables V–IX 的 $sdf$-IBFM **模型**给出 $^{143,145,147}$Ba 多数低能带小的 $f$ 玻色子成分，部分较高能态强 E3 预报；模型采用 DD-PC1/配对和对 $^{145}$Ba 低能谱拟合的粒子–芯耦合。原文没有给出“阻塞使八极响应下降 X%”的 QRPA 计算，也没有逐核穷尽实验双重态。特别是 $^{145}$Ba 计算 $11/2^+_1$ 在 705 keV，比较的实验候选约 670 keV；其 E3 预测不是实测。

可检验的微观工作假说是：八极两准粒子响应的一个通道按 $|Q^{(3)}_{ij}|^2(u_iv_j+v_iu_j)^2/(E_i+E_j)$ 加权，奇粒子阻塞改变特定磁子态的可用相空间，并可能重排配对与 $\beta_3$ 自洽势面。$^{145}$Ba 的 $\nu f_{7/2}\leftrightarrow i_{13/2}$ 具 $\Delta l=\Delta j=3$，Nomura Table II 球形输入 $\epsilon=0.552,3.378$ MeV、$v^2=0.243,0.028$；独立粒子占据/能隙代理量 $(0.243-0.028)/(3.378-0.552)=0.0761\,\mathrm{MeV}^{-1}$。这不是 QRPA 极化率或阻塞率，缺少角矩阵元、磁子态、相干残余相互作用和阻塞后的自洽解。

在锕系，候选八极驱动对为质子 $f_{7/2}\leftrightarrow i_{13/2}$、中子 $g_{9/2}\leftrightarrow j_{15/2}$；但“轨道密集协同强于 Ba X 倍”需要目标核相同方法的单粒子谱、配对、$Q_3$ 矩阵元和阻塞计算。脚本的双通道对单通道倍数只是显式假设下的灵敏度示例，不能写成区域实测差异。$^{143,145}$Ce 也尚无本任务原始基准账本。

## Assumptions

两态截断、轴向强耦合和 $K$ 守恒只用于推导核；电磁比值还要求相同内禀组态的 $D_0,Q_0$ 与同一转子约定。独立粒子代理量不含 QRPA 残余相互作用。

## Competing Explanations

低能双重态可受隧穿、组态混合、Coriolis 耦合和偶然能级靠近影响；较高八极态可由芯声子与奇粒子耦合形成。偶偶核的大 E3 可以对应软势能面或较稳定的反射不对称，须逐核比较。

## Transfer Conditions

跨区可迁移宇称投影、角动量代数和响应函数形式；不能迁移未经同方法核验的 $K$、配对隙、$Q_3$ 矩阵元或有效转动惯量。

## Failure Conditions

若无同自旋组态身份、寿命/分支/转换账本，任何数值 $\Delta E$ 或 $B(E1)/B(E2)$ 对账均失效。若不重算奇核阻塞后的平均场与配对，响应代理量不能解释真实淬灭比例。

## Falsification or Reverse Tests

对同一同位素链，比较奇核与两侧偶偶核的低能 E3、宇称位移和相同方法下的阻塞前后响应；若奇核低能 $f$ 成分或直接 E3 仍强，则简单完全阻塞叙述被反例限制。

## Open Questions

是否存在匹配的奇核 E3 与投影 GCM/阻塞 QRPA 计算，能把奇中子轨道占据与双重态劈裂作逐态对账？

## Human Review

本页是 Codex source self-audit 和条件推导，保持 unreviewed；论文级具体实验数值仍需原件定位。

## Promotion or Rejection History

2026-10-28：建立本页并撤回 Nomura 2018 来源页中未经原文量化的普遍泡利阻塞归因。

## Next Actions

当前仅取得 $^{225}$Ra 评价表，尚未重读其 1985Is03 等原实验正文；其他奇 A 核与 Ce 的 ENSDF/原实验逐级表、E1 寿命/分支和匹配的微观计算未完成同源核验。下一步按核素和 $K^\pi$ 建立母态–末态、寿命、分支、内转换和出处表，再计算同自旋 $\Delta E$ 或明示插值位移；微观部分做等约定的 odd/even 自洽阻塞 QRPA 或 GCM 响应差分。$^{225}$Ra 已有 E1 支线中心值低于 $10^{-3}$ W.u.，不能以 $10^{-3}$–$10^{-2}$ W.u. 范围充当本组奇核的通用已核实数据。
