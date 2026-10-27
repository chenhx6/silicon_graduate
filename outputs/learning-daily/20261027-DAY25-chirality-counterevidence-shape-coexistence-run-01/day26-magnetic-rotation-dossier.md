# Day26无学分preview：MR/AMR与条件剪刀几何

今日仍Day25，partial_day_indices:[26]；未开Day27。本文件为预习审计交代，可复用原文边界在[[garg-2015-135pr-magnetic-rotation]] GA15-D25P-A005-01/02及既有来源，不作第二知识源。旧稿由Git和tmp审计定位保留。

## 原文支持与缺项

Garg2015 PRC92,054325为135Pr负宇称高spin候选MR，谱学/角响应/线偏振结合TAC3qp/5qp支持作者possible解释；本篇有相对B(M1)/B(E2)，未给对应absoluteB/寿命。原文PDF7报告比值上升至约35/2，不是普适陡降。2019勘误正文未得边界GA15-9继续有效。

## 等长双叶的有界几何

忽略core、两叶长度固定且相等j、使用半经典横向磁矩：
$$I=2j\cos(\theta/2),\quad
\mu_\perp=(g_\pi-g_\nu)j\sin(\theta/2),\quad
B(M1)\simeq\frac{3}{8\pi}\mu_\perp^2.$$

在这些条件下随I的抛物线下降成立；不将其当135Pr实际拟合。一般两叶不等、core、g/形变及配置变化会改变趋势。闭合来自能量/推转平衡，不引无来源“有效摩擦力”；ω=dE/dJ也可随I变。

## 四模式辨识不能用硬门

|模式|可检验信息|不使用的普适断言|
|---|---|---|
|MR|指定配置下绝对M1/E2、自旋/形变/角动量演化|不规定所有候选必须M1纯100%、单调陡降或few W.u.|
|AMR|理想对称双剪刀的净横向磁矩相消、ΔI2序列与absoluteE2|不扩成所有量子/跨带M1严格禁戒，不要求强E2或必单调下降|
|wobbling|具体空间的跨带成分、声子有效域与能量/EM预报|不设普适out/in∝1/I|
|chirality|同pair内的几何模型与逐态EM/links比较|不把近简并或相同比值当充分条件|

Frauendorf2001 printed488–489的110Cd AMR近常数B(E2)≈.10e²b²是对普适单调门的原例；Frauendorf2014 PDF6 Eqs16–20还含自旋依赖x/y，临界附近HFA受限。常用wobbling energy须以相邻基准态平均插值，不能用单侧En(I)−En−1(I−1)替代。

## Learning Decision

revises旧摩擦/硬门与本带比值趋势；supports以actual时钟/分支/响应和固定模型可失败预报设计后续分析。寿命技术不限薄靶反冲，需按待测区间与响应选择。
