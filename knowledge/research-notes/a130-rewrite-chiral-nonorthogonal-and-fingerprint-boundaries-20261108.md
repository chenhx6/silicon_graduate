---
type: research-note
title: "A130重写研学：反幺正手征、复非正交两态与指纹对称性的区别"
aliases: [A130 antiunitary nonorthogonal and fingerprint boundaries]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "冻结G64-v1、Terra T09独立审计及总控原件/矩阵核查"
promotion_target: ""
evidence_sources: [frauendorf-meng-1997-tilted-rotation-chirality, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, book-bohr-mottelson-nuclear-structure-vol2, liu-chen-2016-78br-chirality-reflection-symmetry-thesis, koike-2004-chiral-bands-selection-rules, rohozinski-2011-cphc-s-symmetry-chirality, meng-2010-open-problems-nuclear-chirality, ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]
tags: [A130, doctoral-thesis, chirality, antiunitary, nonorthogonal, selection-rules]
---

# 合法的实对称近似，不等于反幺正对称性的普遍推论

## Research Trigger

G64-v1正确推导了\(\mathcal C=TR_y(\pi)\)的平方和重定相，
随后却将非正交重叠与耦合默认为同时实数，把有条件分支差写成通用能隙。
本页保存独立重推、源文的组合对称性和真实引用边界，服务3.5修订及附录。
冻结输入在`raw/writing/gpt/A130/review-inputs/G64-v1/manifest.json`，
不是正确核物理结论的证据源。

## Grounded Evidence

| 原作/本轮locator | 支持范围 |
|---|---|
| [[frauendorf-meng-1997-tilted-rotation-chirality]]，T09回PDF8–12 | 特定TAC/PRM的平面/非平面解与隧穿解释 |
| [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，PDF23–24/印刷485–486；T09另核34、42 | 粒子/空穴取向、手征与反射区别、模型演化 |
| [[book-bohr-mottelson-nuclear-structure-vol2]]，PDF212–215/印刷190–193 | 指定纯转子高自旋近似，不背书本页全部手征代数 |
| [[koike-2004-chiral-bands-selection-rules]]，PDF2–3 | 额外线性A对称与条件电磁选择规则 |
| [[rohozinski-2011-cphc-s-symmetry-chirality]]，PDF1、14；T09另核建模/结果页 | CPHC组合S对称的指纹、几何非唯一性边界 |
| [[meng-2010-open-problems-nuclear-chirality]]，PDF6 §3.1 | 本文所引S(I)的直接公式与主观/模型边界 |
| [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]，PR5 PDF1、3；T09读3–5 | 原实验与解释/寿命缺口，不从Fig.2替作者补公式 |

总控回读RMP上述页、Koike PDF2–3、CPHC PDF1/14、Meng PDF1/6和PR5 PDF1/3。
一般复两态公式与以下反例为任务推导，不冒引任何原文已给相同公式。

## Provisional Reasoning

### 1. 反幺正相关的两态能得到什么

令\(\mathcal C\)反幺正、\(\mathcal C^2=1\)，
厄米H满足\(\mathcal C H\mathcal C^{-1}=H\)，
取归一化且线性无关的\(|R\rangle=\mathcal C|L\rangle\)。
则两个对角元同为实数h：
\(\langle R|H|R\rangle=\langle L|H|L\rangle=h\)。
若有效H不保留该对称或两参考态并非如此相关，等对角元也须另加假设。

记\(s=\langle L|R\rangle\)、\(k=\langle L|H|R\rangle\)，一般都为复数。
保持C相关关系的重定相
\(|L\rangle\to e^{i\phi}|L\rangle,\ |R\rangle\to e^{-i\phi}|R\rangle\)
使s和k同时乘\(e^{-2i\phi}\)。
因此\(ks^*\)不变；s≠0时，同时实化的充要条件为\(\operatorname{Im}(ks^*)=0\)。
s=0时可以单独把k定相为实。
额外的线性幺正左右交换算符P、P²=1、[H,P]=0与R=P L，
可以保证相应矩阵实化，但这是附加条件，不由反幺正C本身推出。

### 2. 一个C=K的反例

以任意正能量单位ε写

$$
\mathcal C=K,\quad H/\epsilon=
\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
L=\begin{pmatrix}\sqrt3/2\\i/2\end{pmatrix},\quad R=L^* .
$$

H为实厄米矩阵、C²=1且保持H。
但\(s=1/2,\ h=0,\ k/\epsilon=-i\sqrt3/2\)，
\(\operatorname{Im}(ks^*)\ne0\)。
s已为实，k不能在保持s为实的同时一般性实化。
原正交空间的能量是±ε，非正交广义本征问题也给±ε；
硬套实分支式则产生复“能量”。这只是抽象二维控制，不是实际左右核态的计算。

### 3. 一般厄米矩阵铅笔与非负能隙

在所选基中

$$
\mathsf N=\begin{pmatrix}1&s\\s^*&1\end{pmatrix},\qquad
\mathsf H=\begin{pmatrix}h&k\\k^*&h\end{pmatrix},\qquad |s|<1 .
$$

求\(\mathsf Hc=E\mathsf Nc\)，而不是把非正交基当普通正交基。
久期式为

$$
(h-E)^2-|k-Es|^2=0
$$

即

$$
(1-|s|^2)E^2-2[h-\operatorname{Re}(ks^*)]E+h^2-|k|^2=0 .
$$

令\(a=1-|s|^2>0,\ b=h-\operatorname{Re}(ks^*)\)，则

$$
E_{\rm high/low}=\frac{b\pm\sqrt{b^2-a(h^2-|k|^2)}}a,\qquad
\Delta E_{\rm phys}=\frac{2\sqrt{b^2-a(h^2-|k|^2)}}a .
$$

s无量纲，h、k、b有能量单位，根号内为能量平方。
N正定与H厄米保证相应谱实；|s|=1时不能继续用二维分式。
若先定相使s为实，能隙还可写

$$
\Delta E_{\rm phys}=
\frac{2\sqrt{(\operatorname{Re}k-hs)^2+(1-s^2)(\operatorname{Im}k)^2}}{1-s^2}.
$$

进一步k为实时才回到
\(E_\pm=(h\pm k)/(1\pm s)\)；
其中“±”先标系数方向，不保证能量顺序，
\(E_--E_+=2(hs-k)/(1-s^2)\)可带号，
非负能隙为\(2|hs-k|/(1-s^2)\)。
这些系数符号不是C的规范不变量子数。

算符平移\(H\to H+c\,1\)在该基中表示为
\(\mathsf H\to\mathsf H+c\mathsf N\)，故h→h+c、k→k+cs，
能量都加c而能隙不变。若限制空间H=h1，则\(\mathsf H=h\mathsf N\)，
两本征值相等；不能把普通矩阵+cI与算符能量零点混同。

### 4. C的方向作用与参考态几何

选择y=m、x=s、z=l并注明主动变换，
\(\mathcal C\)对实角动量期望分量给
\((J_s,J_m,J_l)\to(J_s,-J_m,J_l)\)。
它保持选定主平面投影而翻转中轴分量；
J_m≠0时并未恢复完整J原方向。

总J三分量非零不是独自证明三矢量非共面或稳定手征解的充分条件。
例如声明的经典矢量
\(j_p=(1,1,0),j_h=(0,1,1),R=(1,2,1)=j_p+j_h\)，
总和三分量均非零而三重积为零。
在特定TAC模型中需要固定主轴、Hamiltonian/约束与对称性，
再检查相关参考解、稳定性和被变换解，而不是只读三个投影。

若子空间角动量相互独立，可定义厄米旋转标量
\(\chi=j_p\cdot(j_h\times R)\)，它对C为奇；
不独立时需先处理次序/厄米化。
C对称的非简并本征态有\(\langle\chi\rangle=0\)，
破缺参考态/选择的简并叠加与精确态不同。
半经典的均值三重积也不一般等于算符三重积期望。
涨落/相关或参考态几何与实验可观测量的关系仍需具体模型。

### 5. 额外线性对称产生的指纹

Koike2004的特定同j粒子—空穴、无旋转子模型有额外线性A对称，
其文中γ=90°与采用中轴量子化的Lund−30°等价，不能跨轴序只比较角数值。
PDF2明确电磁选择规则对该Hamiltonian的本征态成立，
不论手征几何是否已实现。其粒子—空穴交换C不是本页的反幺正C。

Rohoziński2011的线性组合\(\hat S=P_\alpha C_{\pi\nu}\)
关联核芯形变坐标的α-parity与价质子/中子交换；
Pα不是普通空间宇称。
作者在所考察CPHC模型中不预设角动量手征几何，
不同刚/软核芯可重现双带和部分电磁交错，
同时明确几何是否被唯一识别仍开放。
因此，未先假设几何不等于证明几何不存在，
也不能替该文补上未建立locator的“非绝热”归属。
线性A/S的±模型量子数与反幺正C本征相位不可合并。

### 6. 观测指标与版本身份

Meng2010 PDF6直接给
\(S_{\rm Meng}(I)=[E(I)-E(I-1)]/(2I)\)；
I无量纲时有能量单位，理想转子E=AI(I+1)给常数A。
这一算术不使它成为手征唯一指纹。
Ayangeakaa2013 PR5 Fig.2画S(I)，所核caption未印同式，
不能把另一文的定义自动归给它。
非正交重叠s、能差S(I)和CPHC算符S分别命名。

该2013论文实际有8页CHORUS accepted与5页出版reprint，
同题名/作者/DOI、非相同字节。当前优先PR5；
稿ledger中不存在的路径/未知哈希不能宣称实际已读，
也不能把AS8物理页照搬PR5。
相对B、组态指认、作者MχD解释和没有本核寿命的边界分别记录。

## Assumptions

标准T/旋转表示给C²=1及重定相结论，是否是某个约束Routhian的对称需另检验。
纯四极反射对称形状是一个参考，不排斥八极/反射不对称耦合。
无旋与刚体惯量不同；刚体椭球最大惯量绕短轴，不由纯转子极值直接指定实核J_m最大。

## Competing Explanations

相近能谱/交错/EM可受几何、额外线性对称、软核、组态和交叉共同影响。
多个模型路线可提供互补约束，不把寿命/δ/三维微观方法写成一条普适唯一认证路径。

## Transfer Conditions

跨区保留的是指定Hamiltonian/态/算符的条件。
粒子/空穴性质、同j、核芯α-parity、有效磁矩或对齐改变时，额外选择规则可改变；
不由此直接判该核区无手征。

## Failure Conditions

默认为实、把带号分支差当能隙、将参考态均值强加精确态、
同名C/S合并或混版本页码，会破坏本节。
自旋演化的势垒/t(I)趋势属于具体模型，无普适单调和必经阶段定理。

## Falsification or Reverse Tests

[`a130_rewrite_chiral_nonorthogonal_audit.py`](../../system/scripts/a130_rewrite_chiral_nonorthogonal_audit.py)
实际通过11项声明的有限矩阵/矢量检查，包括复重叠定相、H+cN、
常数算符、四个复矩阵铅笔及几何反例；产物/环境见L4回执。
它们不验证具体核的手征、势垒、寿命或EM。

## Open Questions

实际候选的额外线性对称与非共面相关能否由同一模型的未拟合量区分？
需要共同输入和可辨预测，不能仅凭多条“标准指纹”数目作判断。

## Human Review

T09独立审计与总控原件/矩阵核查；无新增人工审核事件。
旧稿3.5仍须同步条件和引用后才能纳入整稿。

## Promotion or Rejection History

- 2026-11-08：从实际初稿重建复非正交条件与指纹边界，原有合法实近似保留为受限结果。
