---
type: project
title: "135Nd手征伙伴带：实验、TAC/RPA与竞争解释证据图"
aliases: [135Nd chiral partner-resolved evidence map]
created: 2026-10-26
updated: 2026-10-26
status: active
review_status: unreviewed
confidentiality: public
project_stage: evidence-map-and-model-validity-audit
nuclei: [135nd]
tags: [chirality, partner-bands, tac, rpa, evidence-map]
---

# 135Nd手征伙伴带的逐量证据图

## Agent active summary

本页把[[nuclear-chirality]]中分散的Day24预习整理为可续接的正式研究入口。2007实验对伙伴带的支持保留；TAC/RPA的等强曲线、平均场临界点与实验最近接近点分别归类。绝对强度的逐线normalizer、同I/同family的完整EM块、相干信息及两partner的g向量仍缺。本页不改变Day21/22/23学分、人审或撤回；新综合全部`needs_review: true`。课程是否完成只由本日runner审计决定。

## Research Question

在锁定历史Band A/B身份后，哪些量直接支持135Nd的手征伙伴解释，哪些来自特定TAC/RPA动力学，哪些仍能由crossing、组态变化、γ-softness或band mixing重现？不能只凭同核名称将此三准粒子家族与低spin单νh11/2 TiP家族互换。

## Evidence Available

### 伙伴带观测账本

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] Table I（printed172501-2）的原打印量如下。τ为mean lifetime，B为该实验经寿命及分支推导的强度，不是直接计数；单位依次ps、μN²、e²b²。B列不自动绑定到作者未列出的逐条γ。小括号为原打印误差；不假设相互独立。

| Iπ | τA / τB | B(M1)A / B(M1)B | B(E2)A / B(E2)B | 证据属性 |
|---|---|---|---|---|
|31/2−|0.75(8) / 1.46(2)|2.5(3) / 2.7(3)|0.32(3) / 0.28(3)|同一DSAM/分支推导链|
|33/2−|0.44(2) / 0.87(6)|2.2(2) / 2.1(2)|0.32(3) / 0.28(3)|同上|
|35/2−|0.28(2) / 0.64(5)|2.4(3) / 2.2(2)|0.32(3) / 0.28(4)|同上|
|37/2−|0.23(2) / 0.48(3)|1.7(3) / 1.7(2)|0.32(4) / 0.29(4)|同上|
|39/2−|0.22(2) / 0.24(4)|2.1(3) / 1.9(3)|0.13(3) / 0.11(3)|同上；不单点命名静态阈值|

|量|实验/评价实际支持|模型与作者解释|本任务边界及必要输入|
|---|---|---|---|
|同I能量|原2003建纲图与MU07 Fig4能量点；既有官方snapshot在31/2…39/2的EB−EA中心为356.8/280.8/184.1/118.1/95.2keV（MU07-D24P-001、ZH03-D24P-001）|MU07把零/一声子带间差与RPA能量比较|评价字段不算第二次测量；要回原energy/assignment误差和谱系，不将最近接近点等同模型ωc|
|带内M1/E2及比|Table I与Figs2/3的实验点支持作者所称误差内相近；两种B的商不是δ²|TAC曲线供两带共同基线，谐振RPA不改期望值（MU07-D24-001）|等强理论曲线不能作为第二个独立验证；表内derivedB、B比与同τ不重复计票|
|跨带M1/E2|Fig2是M1，Fig3是E2；B→A open-circle图点是实验派生系列，不是RPA线|RPA波函数给带间率；原文承认带间E2偏低，M1 spin趋势也有差异|作者矢量图缩小转录误差，不补parent/Jf/component/absolute-vs-selected normalizer；MU07-D24P-004–010保持条件性|
|三轴角动量几何|τ/B没有直接测出三轴有符号分量；没有由图点单独确定左右手局域概率|FM97固定形状PRM/TAC奠基；MU07最低RPA模以取向涨落为主、有小γ振动混入|固定γ模型不验证实核γ刚性；需实际波函数、形状/取向联合分布及定义清楚的算符|
|g因子|本次已读MU07全文未报告两partner g；当前未获得可绑定向量|组态/算符可产生可检验g预报，但须独立定标|写unknown，不写0；128Cs bandhead测量不能搬入135Nd；g相近也不单独充分|
|采集与误差|175MeV、100Mo+40Ar、thick target Gammasphere；BLUE双门逐ring与LINESHAPE；5000 recoil histories、0.002ps步长、SRIM stopping、局部χ²寿命误差|理论形变/配对是另一条输入链|图/评价/综述复述不是新增采集；jointCov、逐门feeding/branch ledger仍缺|

## 模型有效域及所用输入

[[frauendorf-meng-1997-tilted-rotation-chirality]] FM97-D24-001/002：给定形状的h11/2粒子/空穴加三轴转子，irrotational惯量，TAC把I换经典J并作均场因子化；量子PRM仍有隧穿劈裂。Fig7带间强度抑制是该参数模型结果，不能把实核任何跨带线一概视作反证。文中134Pr高spin跨带未见同时受弱布居限制。

[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-D24-001/002：PQTAC用N=4、5两个major shells，QQ力及constant pair gap，以Strutinsky PES定参数；质子/中子gap分别取odd-even mass difference的50%/80%，是模型输入。RPA含取向、形状及两qp谐振自由度；最低模以取向为主，不等于模型完全删除γ涨落。well below transition时谐振可用；零频/非零φ的均场临界与实测最近接近点相差约1ℏ，临界区方法失效。没有由这些字面输入恢复原producer或从图推确切ωc。

## 近似阶次练习：等强来自什么

以下为本任务推导，来源背景为MU07 printed172501-3 Eq3后和printed172501-4非谐性段；不是作者原程序重放，也不是实核拟合。

用dimensionless小取向坐标q的谐振近似，H=p²/(2𝓜)+𝓜Ω²q²/2，令v=ℏ/(2𝓜Ω)。q为角度（radian），𝓜的量纲使𝓜Ω²为能量。取一个内禀算符分量F(q)=a+bq+cq²，则

$$\langle0|F|0\rangle=a+cv,\qquad
\langle1|F|1\rangle=a+3cv,\qquad
\langle1|F|0\rangle=b\sqrt v.$$

线性算符截断（c=0）下两态对角期望相同，同时允许非零带间振幅；保留曲率项后差为2cv。这说明“振动不改期望值”对应近似阶次。这里对角期望是内禀分量练习，**不是不同I间实验B的RME**；没有把它直接平方成135Nd带内率。实际带内/带间还需正确spin映射、EM张量、波函数和归一。

若Ω→0或a接近角几何零点，小振幅/相对修正展开可能失效；数学发散不能外推成实核测得发散。MU07的θ≈45°敏感性/非谐平均倾角讨论因而应和谐振等强基线同时保留。能隙变小、平均场分岔、有限体系隧穿与实验最小split是四个不同对象。

## Current Hypotheses

### 四条竞争路线与可证伪输入

以下是研究设计，均`needs_review: true`；未实际拟合，不给解释胜负或同等可信度。

|替代路线|可重现的局部特征|必须新增的可检验内容|能改变判断的检验/当前缺口|
|---|---|---|---|
|crossing|两同I候选能级靠近、alignment或能量斜率变化|指定crossing双方组态/形变、保持连续的state mapping，给跨区间全网络预测|单一spin近合不够；同reference能量/对齐、逐态τ与BR/ICC及两侧强度需联合核验|
|configuration change|不同组态也可能有相近能谱或B比|固定H/算符的本征态mapping须过能量、Jπ和全部links；若加入3qp空间须声明模型改变|只改标签不产生新预测；独立g/绝对B可作holdout，但当前双partner g与actual producer未得|
|γ-softness|形状/取向涨落可影响能隙和EM|联合shape-orientation动力学，说明刚性极限与混合、同算符的EM趋势|FM97固定γ范围不证明刚性；MU07小γ admixture也不量化实核完整γ分布|
|band mixing|近交叉时强度可重新分配，某些局部峰/谷可来自混合|同Ii/If完整RME块、相位/可用干涉约束、包含遗漏态的空间及归一|只看两条带不能证明封闭；MU07-D24P-008列缺失反向outlets，未观测不设0|

## Risks and Blockers

### What is established vs what is not

Established（本次已读来源范围）：MU07实验报告的伙伴电磁相似性及TAC/RPA总体比较，是135Nd手征解释的正支持；FM97给几何和量子恢复的理论基础。两篇原件的任务边界不同，不能互相冒充新实验。

Not established：模型无关的静态手征起始spin/硬阈值、全部branch/normalizer闭合、两partner g、唯一三维取向、排除所有crossing/组态/γ-softness/混合路线。既有Pr/Au争议不能自动否定本核正支持；本页也不恢复Qt代理CI、225.8keV正P、机时排他认证。

## Knowledge Impact and Learning Decision

`supports`既有135Nd实验支持链；`limits`把共享TAC带内曲线、RPA零频和实验阈值捆绑的推理。下一步优先完成既有原模型后续方法对取向/形状模和近临界非谐性的原文核对；只有具体endpoint/normalizer输入有进展时才重开强度库存问题。

## Next Actions

先核既有Almehed2011原方法的orientation/shape模和近临界近似合同；若缺原line/normalizer，不从图点再造branch。四条竞争路线须各自提供可冻结参数的预测及holdout，才进入实际比较。

## Agent self-audit triage

|级别/项|已核证据与本任务判断|未核验风险/后续|
|---|---|---|
|P1 实验支持与归一|原Table I/Figs1–4回读；支持链保留，逐线missing不伪补|图点identity与normalizer仍条件化；论文措辞逐claim回源|
|P1 理论等强与临界|MU07-D24-001/002原文；近似阶次推导明确标为任务推导|不可把谐振截断升格为普适等强/阈值定理|
|P1 竞争解释|FM97-D24-001/002支持适用域，其余为待检验设计|未拟合不分配胜率，不把列名当已有独立反证|
|P2 导航与信用|canonical链接到两source及概念，source反链已补|本页不授分、不更改原人审或撤回|

## Sources

- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]，MU07-D24-001/002；Table I、Figs1–4；既有D24P-001–010。
- [[frauendorf-meng-1997-tilted-rotation-chirality]]，FM97-D24-001/002；Eqs6–12、Figs1–9。
- [[zhu-2003-135nd-composite-chiral-pair]]，ZH03-D24P-001（既有谱系/端点定位，本轮未重读全篇）。
