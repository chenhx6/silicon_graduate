---
type: research-note
title: "A130重写：附录A角动量与电磁张量约定审计与代数控制基准"
aliases: [A130 angular momentum appendix audit 20261113, 附录A角动量张量约定审计笔记, G94 附录A研学笔记]
created: 2026-11-14
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
authors: [G90 (Gemini Tiered/high)]
created_from: "A130博士论文重写五章39节工程：附录A角动量与张量约定审计（G94任务）"
promotion_target: doctoral-nuclear-structure-foundations
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, book-bohr-mottelson-nuclear-structure, lange-kumar-hamilton-1982-multipole-admixtures, book-hamilton-electromagnetic-interaction]
tags: [doctoral-thesis, angular-momentum, tensor-operators, wigner-eckart, 6j-symbols, electromagnetic-units, evidence-audit]
---

# 角动量约定：先查定义，再比矩阵元

## Research Trigger

附录A把多个章节使用的角动量、约化矩阵元、辐射幅度和命名单位放在同一张对照表中。审查发现的困难来自中间相位、相同名字的不同归一以及SI/高斯符号混用；这些问题需要具体公式和原件来区分。

## Grounded Evidence

| 原件与实际定位 | 本次可支持的内容 | 边界 |
|---|---|---|
| [[book-bohr-mottelson-nuclear-structure]]，PDF101/印82，Eq1A-60/63 | CG前有1/√(2If+1)；角动量矢量的RME为ℏ√[j(j+1)(2j+1)]。 | 与本地Suhonen的同归一可直接对照；没有由此核完Edmonds/Rose等全部版本。 |
| [[book-suhonen-from-nucleons-to-nucleus]]，PDF44–46/印29–31，Eqs2.27,2.30–2.34 | 所选WE归一、自伴球张量及其RME交换关系。 | 自伴性是附加条件，不由旋转张量性质或宇称本身推出；RME不必普遍实。 |
| 同书PDF48/印33 Eq2.54；PDF29–30/印13–14 | 张量积重耦合与6j三角、正交条件。 | 具体排列的9j→6j相位和单体式要配套；有限控制不代替全部恒等式推导。 |
| 同书PDF134–135/印119–120，Eqs6.7,6.9及脚注6 | SI μN=eℏ/(2mp)，电荷型磁算符M_S=M_μ/c；脚注明确高斯表达另有c。 | 高斯电荷e_G与SI电荷不能混填一个公式。 |
| [[book-hamilton-electromagnetic-interaction]]，PDF553/印542，Eqs12.184–185 | 本处混合比和Fk正干涉项配套；原文明确引用Krane–Steffen定义。 | 不是所有实验论文δ均已统一到此定义。 |
| [[lange-kumar-hamilton-1982-multipole-admixtures]]，PDF3–4/印121–122，Eqs2.4–2.11 | 所述发射情形的KS/RB变换，及发射与吸收区别。 | 原综述与后续勘误是不同载体；未获勘误不能当支持证据。 |

## Provisional Reasoning

本稿WE定义为
\[
\langle j_fm_f|T_q^k|j_im_i\rangle
=(-1)^{j_f-m_f}\begin{pmatrix}j_f&k&j_i\\-m_f&q&m_i\end{pmatrix}
\langle j_f\|T^k\|j_i\rangle
=\frac{C_{j_im_i kq}^{j_fm_f}}{\sqrt{2j_f+1}}\langle j_f\|T^k\|j_i\rangle.
\]
整数秩电磁张量改变CG耦合顺序时，必须同时改变对应相位，不能称两个裸相位普遍相同。

若$T_q^{k\dagger}=(-1)^qT_{-q}^k$，则
\[
\langle j_f\|T^k\|j_i\rangle=(-1)^{j_f-j_i}\langle j_i\|T^k\|j_f\rangle^*.
\]
$j=1/2,T=J,k=1$给出非零实RME $\hbar\sqrt{3/2}$，直接反驳交换式中额外乘$(-1)^k$的旧写法。该检查不要求所有电磁RME都实。有限空间与非正交基只要度规、态及伴随算符一致，也不因“投影”而自动失去正逆B的统计权互易。

SI磁单位分别是
\[
\ell_N=\hbar/(2m_pc),\quad \mu_N/c=e\ell_N,\quad
B_S=B_\mu/c^2=b_{M1}(e\ell_N)^2,\quad
b_{M1}=B_\mu/\mu_N^2=B_S/(\mu_N/c)^2.
\]
物理$B_S$不能丢电荷平方；命名单位归一后的数值也不能重复乘除$c^2$。混合比幅度的相位定义另需指定，并不由SI单位自动决定。

6j控制选取的三值为−1/10、1/6、1/15，加权平方和为1/5。另有非等底排指标与显式耦合基分量控制，用于辨别错误相位和指标；只说明所选例子。指标允许性函数χ与Racah三角系数Δ_R必须用不同名字，前者还要求角动量和为整数。

## Assumptions

固定本文的主动旋转、CG/WE相位与物理ℏ定义。电磁张量在相关公式中取整数秩；正逆B关系使用相容的伴随算符与归一。只在具体RME已选实数时省略共轭，不因时间反演或CS名称就声称所有态都有实基底。

## Competing Explanations

同一物理幅度可用不同RME归一、算符相位或命名单位表示。未完成定义桥接前的符号/数值差异不能直接判为不同物理预测。SI/高斯变换与KS/RB混合比相位转换是两个不同层次。

## Transfer Conditions

跨章节先给轴与参考系，再给态和张量定义，最后比较矩阵元。实际在束布居可有取向，角度计数需要密度矩阵与响应；标准B定义的磁态平均不等于要求每次实验都无极化。

## Failure Conditions

错原件SHA、未取得的文献被列为支持证据、多写$(-1)^k$、漏$e^2$、无条件$c^2$数值缩放，以及把一个有理数控制说成全附录证明，均会破坏此链条。

## Falsification or Reverse Tests

用$j=1/2,T=J$检查自伴交换；用两个不同耦合次序的非零CG分量检查相位；以显式张量积基求和核9j/6j。每例的输入与结果保持可重算，不能用结果一致替代实验验证。

## Open Questions

[[lange-1982-multipole-admixtures-erratum]]目前只有Crossref/OpenAlex题录及实际访问响应，无PDF正文。OpenAlex的bronze-OA标注与本地取得全文不同；403/401也不能证明收费。未得勘误内容前，不猜测它改动哪条式子，不用于当前公式支持。源本、题录和访问边界分别保存。

## Human Review

无新增真实用户人工审核事件；此处记录Agent原件核查及代数控制。

## Promotion or Rejection History

- G94执行T20八项返修后，父审重算四原件SHA，撤除两条假SHA与不可得勘误的支持关系，修正知识页里新的错误相位中间等式。
- 数学、原件和有限控制的边界写入本页及附录台账；不宣称全稿或全部文献版本认证。
