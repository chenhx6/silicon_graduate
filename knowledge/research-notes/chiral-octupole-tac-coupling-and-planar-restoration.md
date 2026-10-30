---
type: research-note
title: "手征—八极角度势纠错：驻点、硬编码阈值与78Br的quartet证据边界"
aliases: [chiral-octupole-tac-coupling-and-planar-restoration, chiral octupole tac coupling, octupole chiral quenching, beta3 crit chirality]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, wang-2019-rat-prm-78br-octupole-correlations]
created_from: Day 27 continuation study; system/scripts/day27_chiral_octupole_coupling_tac_study.py
tags: [chirality, octupole-correlations, stationary-point, source-correction, model-boundary, Day27]
---

# 角度势是否真的导出“平衡角”

## Research Trigger

Day27旧版用一个角度公式宣称已求解3D-TAC、证明静态八极淬灭手征、得到五核素平衡角和势垒，并把78Br四条带称作已确证quartet。核验发现：给出的势能不产生脚本所用驻点，jν≥12截断是硬编码，quartet与实验上限归属也超出原件。随后追加provisional附录没有修复明确错误。

本页撤回这些结论；旧代码、正文、JSON及输入保存在本run `scientific-corrections-047/superseded-chiral-artifacts.json`，旧结果已标superseded。新脚本做明确的数学/来源审计，不预测核素角度或相界。

## Grounded Evidence

理论背景的手征转动与反射不对称自由度分别回链 [[knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei|Frauendorf 2001]] 和 [[knowledge/sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry|Butler & Nazarewicz 1996]]；78Br实验范围回链 [[knowledge/sources/liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br|Liu 2016]]，RAT-PRM实际模型输入回链 [[knowledge/sources/wang-2019-rat-prm-78br-octupole-correlations|Wang 2019]]，198Bi背景回链 [[knowledge/sources/pai-2014-198bi-multiquasiparticle-magnetic-rotation|Pai 2014]]。这些来源均不替代本页的toy势能纠错。

| 来源与定位 | 实际支持 | 边界 |
| --- | --- | --- |
| [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] L16-9/13/14与L16-D27-R047-1；PDF2/4/5 | 两对正/负宇称双带与八条Band1–Band3 E1连接，作者解释为MχD伴八极关联；PES对β30软；结论把稳定三轴/八极核中quartet列为未来搜索目标 | 当前四带不自动等于已建立的同一chirality–parity quartet |
| 同source L16-6/8及L16-D27-R047-2；PDF3–5 | 两个组态的β2/γ不同，effective angles为TPRM结果；β30软面不直接测固定非零静态β3 | 旧五核素表的β3、φ和势垒不能称为实验量 |
| 同source L16-D27-R047-3；正文PDF1–5与Figs.1–6 | 原文没有旧笔记所称的E3跨带确证或<10⁻³、99.9%置信的交叉支路上限 | 旧上限没有匹配counts/效率/背景/Cov，已撤回，不拿模型零值制造实验置信 |
| [[wang-2019-rat-prm-78br-octupole-correlations]] W19-D27-R047-1/2；v1 PDF6–7 | MDC-CDFT给β3=0且软，RAT-PRM采用β3=0.02，β2=0.28、γ=16.3°；有限核芯宇称分裂和惯量按同一实验谱调整 | 固定非对称输入不是静态八极的实测值；没有β3>0.1扫描，既不证明也不定量反驳0.1排除线 |
| 同source W19-D27-R047-3/4/6；PDF5–6、9、12–13 | 好总宇称基及具体M1/E2/E1算符；带头effective angles近90°也可属chiral vibration；E1/E2残差与负宇称组态重排仍有边界 | 需要具体波函数、量子化和算符，不能用一个角或简写群名保证所有精确transition zeros |

父代理回读Liu2016本地正文PDF1–5文字并视觉核PDF5 Fig.6及结论，原哈希不变。2019来源由独立worker读17页及五图，父代理另核参数/算符/角度/组态段；版本与阅读范围写在source，不声称复现其RAT-PRM数值。

## Provisional Reasoning

### 旧文字势的直接求导

记A=Kβ2 sinγ、B=Cβ3²，A、B为能量系数。旧文字写的是：

\[
V(\phi)=-\frac A2\cos(2\phi)+B\cos^2\phi
=\frac B2+\frac{B-A}{2}\cos(2\phi).
\]

因而：

\[
V'=(A-B)\sin(2\phi),\qquad V''=2(A-B)\cos(2\phi).
\]

在旧定义的角域 `−π/2≤φ≤π/2`：A>B时φ=0为极小，B>A时端点±π/2为极小（周期端点的两种表示）；A=B时整个角度势平坦。没有一般的内部双阱极小。尤其B=0时，这个A>0势也不在45°极小，不能用它产生旧脚本的零八极45°答案。

单独的正B cos²φ在φ=0曲率为−2B，是极大值而非所称平面恢复项。这个符号错误不能靠提高精度或添加“provisional”说明修复。

旧脚本用 `φ=acos(B/A)/2`。在旧78Br自设输入下返回41.2477°，代回**它自己写的势**却有约0.380875 MeV/rad的非零梯度；136Nd/134Pr旧返回值同样不是该势驻点。这是代码—方程不相容的数学反证，不是对真实核素旋转几何的新测量或新解。

### 同一个反余弦必须来自不同的势

为显示不可静默换方程，另明确声明合成势：

\[
U(\phi)=\frac A2\cos^2(2\phi)-B\cos(2\phi),\quad A>0.
\]

它在 `|B/A|<1` 才有成对内部极小 `φ=±acos(B/A)/2`，曲率为 `4A[1−(B/A)²]>0`。经φ=0的势垒为 `(A−B)²/(2A)`，不是旧脚本的 `K(1−B/A)²/2`；后者还丢失A/K=β2 sinγ因子。

取**无核素身份的合成**A=1 MeV、B=0.2 MeV：相同反余弦角在V中的梯度约0.783837 MeV/rad，不是驻点；在U中梯度为零、曲率为正，过零势垒为0.32 MeV。U是另一个示意势，不是补齐了微观项的真实TAC；一维成对极小本身也不确证核手征性或四带结构。

### 硬编码阈值与不可识别输入

旧代码将jν=11.999改成12.0时，把约43.69°直接改成0。原文字势根本没有jν项，不能从它导出该截断。γ也只是固定输入，脚本未对γ求极小，因而不能宣称“八极项把γ推到0”。旧0.5°、β2=0.05/0.12、β3=0.06/0.1和jν=12等统一门均不再用于物理判决。

没有共同I/ω、组态、惯量张量、单粒子哈密顿量、角度坐标和八极耦合约定时，五核素均为not-ready；当前脚本输出真实核素φ、势垒、临界β3和quartet分类均为空。E1/E3强度不能在没有逆问题/响应与模型合同的情况下独立定出角度恢复系数C。

## Assumptions

- 数学审计使用旧文字势本来的φ坐标及能量系数；比较本身不认证这些坐标对应某一具体核素。
- 另一个合成势U与V保持不同身份，不用它拟合遗留核素输入。
- 数值网格只核极小值和导数，不能替代平均场/PRM的量子化、宇称恢复或电磁矩阵元。

## Competing Explanations

78Br的实验层、MχD解释、八极软性及quartet未来搜索保持分层。RAT-PRM中正宇称更接近平面而负宇称有手征解释，负宇称主组态与先前模型不同且要求进一步支持；不能把每条双带都套入同一几何。小八极关联与手征解释相容不推出所有大β3核素相容，也不证明大β3必然排斥手征。

## Transfer Conditions

可迁移的是“先验证源级身份和驻点，再作稳定性与可观测量比较”的方法。迁移到其它质量区须给出目标核素的完整模型及实验网络，不能复用本页自设A/B、角度阈值、所谓空间群简写或未读来源的精确零值规则。

## Failure Conditions

能量与求导公式不一致、返回角梯度非零、把固定γ输入当作已极小化γ、用if条件代替平面稳定性、或把八极软性/MχD写成quartet确证时，停止核素预测。缺计数、效率和背景时，不从未见支路制造上限或置信水平。

## Falsification or Reverse Tests

- 原V、其梯度/曲率及三角恒等式独立核对；零耦合、A=B平坦、两端曲率和φ反射控制通过。
- V/U分别作能量有限差分检验，最大梯度误差约3×10⁻¹¹（所选合成能标）；U网格从181点加密到1441点，最低能误差由约3.13×10⁻⁵降至2.00×10⁻⁷ MeV。
- 旧jν截断跳跃作为失败证据保存，旧核素solver入口禁用；不以新的假阈值替换它。
- Liu2016 PDF5的未来quartet措辞直接反证旧归属；Wang2019的β3=0.02不被夸大为>0.1定量反例。

## Open Questions

1. 取得目标组态的真实自洽能面与角度坐标后，平面驻点的Hessian如何随I/ω及八极自由度变化？需同时核自由度和稳定性，不能先决定结论。
2. 哪篇理想对称极限论文实际推导额外chirality–parity量子数及transition zeros？须读其哈密顿量和算符假设，不能借2019的78Br应用文代替。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为源级self-audit和条件数学验证，保持unreviewed/provisional。旧具体角度、势垒、β3排除线和虚构上限已撤回；本轮没有新实验、没有完整TAC/RAT-PRM谱复现，也不扩展原source的既有人审范围。

## Promotion or Rejection History

- 2026-10-30 checkpoint034及后续附录：旧正cos²恢复力、反余弦驻点、五核素预测、jν截断及78Br quartet/实验上限认证撤回；通用附录不足以修复方程和归属错误。
- 2026-10-30 checkpoint047：V/U不同角度势的独立导数与网格检查替代旧伪TAC预测；Liu2016源级quartet边界与新读Wang2019实际模型输入写回。结果为 `chiral_octupole_potential_audit_corrected.json`，整体Day27任务继续，不推进学分。
