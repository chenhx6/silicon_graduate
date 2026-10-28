---
type: research-note
title: "奇奇核中平面剪刀到非共面手征：106Ag、134Pr与198Bi的证据边界"
aliases: [MR chiral topology odd-odd nuclei, 106Ag 134Pr 198Bi chiral transition]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [he-chuangye-2006-magnetic-chiral-106ag, rather-2014-ag106-transition-rates, tonev-2006-134pr-lifetime-chiral, tonev-2007-134pr-dynamic-chirality, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review]
created_from: Day26 independent odd-odd MR/chirality topology audit
promotion_target: magnetic-rotation-and-chirality
tags: [odd-odd, magnetic-rotation, shears, nuclear-chirality, chiral-vibration, static-chirality, 106Ag, 134Pr, 198Bi]
---

# 奇奇核中平面剪刀到非共面手征：106Ag、134Pr与198Bi的证据边界

## Research Trigger

目标是把“平面剪刀（MR）—软手征振动—静态手征双重带”写成可计算的拓扑演化问题，并核对 106Ag、134Pr 与 198Bi 的原件证据。核心警告是：近简并、相似 $B(E2)$、$B(M1)/B(E2)$ 相位或平滑 $S(I)$ 各自都只能构成候选信息；它们不能单独证明内禀三维手征。

## Grounded Evidence

| 核 | 原件/来源事实 | 直接定位与适用边界 |
|---|---|---|
| $^{134}$Pr | Tonev 2006 测量两带平均寿命；近简并区 Band 1 的带内 $B(E2)$ 约为 Band 2 的 2–3 倍，两带 $B(M1)$ 平滑且无奇偶交错；理想静态三轴 TQPTR 的电磁预言失配，作者转向动态手征/形状自由度 | [[tonev-2006-134pr-lifetime-chiral]] PDF pp.3–4 Fig.3；该页明确保留模型依赖与未列逐线协方差 |
| $^{134}$Pr | Tonev 2007 给出 Table I/II、偏振和模型比较：带内 $\Delta I=1$ 以 M1 为主，带间 $\Delta I=1$ 保留 mixed M1+E2 但缺足够统计确定 $\delta$；IBFFM改善主要 E2/M1 趋势但低自旋大 E2、能隙和 $I=15$ 交叉仍失败 | [[tonev-2007-134pr-dynamic-chirality]] PDF pp.8,12–14,25；作者总结为弱形状涨落与尚未揭示内禀对称性的条件解释 |
| $^{106}$Ag | 贺创业论文摘要将 Band 1 的 $\Delta I=1$、大 $B(M1)/B(E2)$、近零 signature splitting 与 TAC 剪刀联系；Bands 3/4 的同宇称近简并、平滑 $S(I)$ 与相位相同的比值摆动被提出为手征双带候选 | [[he-chuangye-2006-magnetic-chiral-106ag]] 摘要 pp.4–5、Chs.6–7；扫描编码损坏，精确轨道/能量和混合比须视觉复核，作者候选不升级为确证 |
| $^{106}$Ag | Rather 2014 直接 DSAM 原件报告两带 $B(E2)$ 在误差内相近，但 $B(M1)$ 自旋依赖不同；TPSM 在同一 $\epsilon=0.15,\gamma=30\degree$ 模型平均场上用不同准粒子 $K=4/K=2$ 重现能谱和跃迁趋势 | [[rather-2014-ag106-transition-rates]] PDF pp.3–11；Table I逐态寿命/强度受top-feed、side-feed、stopping与响应假设约束，Lieder另一原件未取得 |
| Pb区/198Bi | Clark 2000 综述记录 $191$–$202$Pb、$198$–$203$Bi 的大量 M1 带；198Bi在该综述中只是区域汇编入口，不是本轮得到的198Bi逐带原始寿命、三轴度或手征实验 | [[clark-2000-shears-mechanism]] p.5；本轮没有198Bi主实验原件，故不填入具体配置或静态手征结论 |

134Pr的正面和反面信息必须同时保留：Tonev 2006/07 的带近简并与动态解释属于同一实验谱系，不能重复计为独立实验。106Ag的 He 2006 候选与 Rather 2014 的 DSAM/TPSM 解释也不是自动独立裁决；后者的 Lieder 2014 primary 正文仍缺。

## Provisional Reasoning

### 1. 几何对象：什么叫平面、非共面与手征

在体坐标中取高-$j$ 质子粒子沿短轴 $s$，高-$j$ 中子空穴沿长轴 $l$，集体芯角动量 $\mathbf R$主要沿中轴 $m$。总角动量为

$$\mathbf I=\mathbf j_p+\mathbf j_n+\mathbf R.$$

三重积

$$\chi_g=\mathbf j_p\cdot(\mathbf j_n\times\mathbf R)$$

在体坐标中非零时，三矢量形成非共面三角架；其符号在镜像手性变换下改变。若三矢量共面，$\chi_g=0$，则是平面倾斜旋转/剪刀几何。$\chi_g\ne0$是**几何必要条件**，不是实验充分判据：量子态可为左右手性叠加，实验室观测仍需 partner-resolved 能谱和跃迁矩阵元。

### 2. 三轴粒子-转子能量与非共面极小

用最小经典粒子-转子泛函

$$E(\mathbf I)=\sum_{k=s,m,l}\frac{(I_k-j_{p,k}-j_{n,k})^2}{2\mathcal J_k},\qquad \mathbf I^2=I(I+1),$$

并取 $j_{p,s}=j_p$、$j_{n,l}=j_n$、其余内禀分量为零。拉格朗日极值条件可写为

$$\frac{I_k-j_k}{\mathcal J_k}=\lambda I_k.$$

平面解令 $I_m=0$。非共面解要求 $I_m\ne0$，因此 $\lambda=1/\mathcal J_m$，并给出

$$I_s=\frac{j_p}{1-\mathcal J_s/\mathcal J_m},\qquad
I_l=\frac{j_n}{1-\mathcal J_l/\mathcal J_m}.$$

由此得到清楚的动力学条件：$\mathcal J_m>\mathcal J_s,\mathcal J_l$，即中轴是最大惯量轴，才允许这种两高-$j$叶片与芯转动共同形成的 aplanar 极小。$\gamma$ 约30°附近的三轴流体动力学惯量常使中轴惯量最大，但具体方向取决于 $\gamma$ 约定、惯量模型和配对；不能把“$\gamma=30°$”直接当实验测量。

非共面解还必须满足总自旋高于临界组合

$$I_{\rm aplanar}^2=I_s^2+I_l^2+I_m^2,$$

其中 $I_m$ 是由角动量约束和旋转频率求出的芯分量。低自旋时 $I_m$不足，最低能量通常落在 $I_m=0$平面；随 $\omega$ 增长，若中轴极小稳定，系统可从平面向非共面软化。

### 3. 软手征振动到静态手征的Landau判据

取左右手性变换为 $\phi\to-\phi$，$\phi$为偏离平面的方位角，最低阶有效势为

$$V(\phi;I)=a(I)\sin^2\phi+b(I)\sin^4\phi,\quad b>0.$$

- $a>0$：$\phi=0$是单一平面极小，非共面运动是软的手征振动/零点涨落；
- $a=0$：平面模曲率消失，手征软模临界点；
- $a<0$：出现 $\phi=\pm\phi_0$ 两个经典极小，代表静态手征候选。

量子化后最低两态是左右波包的对称/反对称组合。静态手征需要势垒 $V_b$ 相对于方位零点能 $E_{zp}$ 足够大，使隧穿分裂 $\Delta E$ 小于实验分辨并且两带跃迁矩阵元呈稳定的 partner 结构。故“出现两个极小”仍只是模型条件；需要联合 $\Delta E(I)$、带内/带间 M1/E2、alignment、$\mathcal J^{(2)}$ 与配置证据。

本轮工件 `chiral-mr-topology-model.py` 采用合成 $a=0.42-x,b=1$ 画出单阱—临界—双阱演化；它没有对106Ag、134Pr或198Bi拟合。

### 4. MR与手征双带的观测量层级

| 观测量 | 平面MR/剪刀 | 手征双重带候选 | 解释边界 |
|---|---|---|---|
| 能带 | 单一 $\Delta I=1$序列，能谱可规则；配置交叉可 backbend/重开 | 同宇称、同构型候选的两条近简并 $\Delta I=1$带，能隙随I可减小 | 近简并不是充分条件；不同配置也能交叉 |
| $B(M1)$ | 单配置剪刀闭合时横向磁矩及B(M1)常下降；交叉改变叶片长度后可重开/反弹 | 理想手征伙伴有相近的带内M1及可比较的带间M1，随I可能出现相位/奇偶结构 | “恒定”不是普适硬门；需同母态、同口径的绝对率 |
| $B(E2)$ | 弱集体E2，常随闭合下降；芯贡献可改变趋势 | 相同三轴核芯应给相近带内E2，配合M1和能谱才有意义 | 134Pr的2–3倍差异正限制静态极限；106Ag相近E2也不唯一证明同形状 |
| 偏振/多极 | 带内$\Delta I=1$以M1为主、crossover E2 | 带间$\Delta I=1$ M1/E2混合、相位关系与选择定则可约束波函数 | 缺$\delta$与完整响应不能反演精确混合份额 |
| 动态惯量 | MR可有近似转动样 $\mathcal J^{(2)}$，配置交叉产生异常 | 三轴手征需要中轴惯量主导、alignment与$\gamma$在同一模型中自洽 | $\mathcal J^{(2)}$单独不能测量 $\gamma$或 $\chi_g$ |

“恒定 $B(M1)/B(E2)$”是某些手征候选的经验描述，不是对称性恢复的严格定理。反之，MR的单调下降也不是硬门；Clark与Hübel都记录Pb区交叉重开。

### 5. 三个案例的当前裁决

**134Pr：动态手征候选，静态极限受限。** Tonev结果同时具有近简并双带和模型化三轴背景，但带内E2 2–3倍差异、M1缺少理想奇偶交错，且IBFFM仍有能隙/交叉失败。因此可支持“平面/非共面自由度与形状涨落耦合的动态问题”，不能写成静态手征已证实，也不能把MR单序列和双带标签当作互斥。

**106Ag：共存/竞争候选，证据冲突而非单向转化。** He 2006把Band1视为MR、Bands3/4视为手征候选；Rather 2014则从寿命和TPSM指出相近E2与不同M1可由同一平均场形变上的不同准粒子组态产生。这个结果说明“同形变+近简并”可以同时容纳不同电磁结构，无法只凭E2和能隙宣称从MR转为静态手征。

**198Bi：本轮只能作为资料缺口。** Clark 2000 p.5只把198–203Bi列入Pb区M1带发现范围；没有取得198Bi的逐带原始EM数据、$\gamma$、$\mathcal J_m$或partner能谱。因此不做198Bi的静态/动态手征归属，也不把Pb区综述计作该核独立证据。

## Assumptions

粒子-转子推导使用刚性三轴惯量、质子/中子高-$j$内禀轴向阻塞、无显式两体电磁算符；Landau势只描述最低方位自由度。实际核需加入配对、形状涨落、配置混合、隧穿和芯极化。

## Competing Explanations

双带近简并可由不同准粒子配置交叉、两带混合、γ软形状、普通转动或测量分支偏差造成；相似E2可来自共同有效形变参数而非相同波函数；M1差异可由K组态、有效g因子和带混合造成。134Pr的IBFFM改善不构成唯一机制证明，106Ag的TPSM也不自动排除所有手征波函数。

## Transfer Conditions

欲把候选提升为静态手征，需要同一双带的绝对寿命与完整分支、带内/带间M1和E2、偏振/混合比、能隙及alignment一并与同一三轴PRM/TAC/IBFFM参数集比较；需要把统计与系统协方差、top/side feeding和实验响应保留在似然中。

## Failure Conditions

把 $\chi_g\ne0$ 当实验直接观测；把 $\gamma=30°$、相近E2或恒定比值当充分手征判据；把134Pr Tonev06/07重复计票；把106Ag He与Rather当独立同一实验；把198Bi综述目录当逐带原件，均越过证据边界。

## Falsification or Reverse Tests

1. 对同一双带测得明显不相近的带内E2或带间M1相位结构，降低静态手征解释；
2. 若两带绝对EM向量可由不同配置交叉在同一 $\epsilon,\gamma$ 下重现，不能再用近简并独占手征解释；
3. 若随频率出现清晰回弯而B(M1)在新配置重新增大，应优先检查MR重开；
4. 对198Bi先取得原始谱、寿命和三轴模型参数，再进行任何模式结论。

## Open Questions

134Pr双带的实际方位隧穿分裂及统一协方差仍缺；106Ag Lieder原件和历史带号映射仍缺；198Bi逐带原始数据未取得；流体动力学 $\mathcal J_m$ 与实际有效惯量的配对修正尚未在统一代码中计算。

## Human Review

Codex定向原件/self-audit，页面保持 `review_status: unreviewed`，未获得用户逐项人工审核。

## Promotion or Rejection History

2026-10-29：建立MR—手征拓扑笔记。`supports` [[nuclear-chirality]] 与 [[magnetic-rotation]] 的几何/观测分层；`revises` 把恒定比值、双带近简并和134Pr静态手征写成硬判据的历史措辞；`limits` 198Bi仅有综述目录证据。
