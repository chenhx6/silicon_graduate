---
type: research-note
title: "R2 惯量证据矩阵与 163Lu 原表响应重建"
aliases: [R2 inertia evidence and band reconstruction]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hinohara-2010-local-qrpa-shape-mixing, sato-hinohara-2011-krypton-shape-mixing, washiyama-2024-five-dimensional-improved-inertia, xiang-2024-triaxial-pairing-collective-hamiltonian, sun-2025-iterative-atdhfb-rare-earth-inertia, prochniak-rohozinski-2009-bohr-collective-hamiltonian, hinohara-2015-nambu-goldstone-inertia-response, campaign-g07-gorgen-2004-163lu-quadrupole-moments]
created_from: "博士前置研学的跨来源比较、原表核查与可重放名义计算"
promotion_target: ""
tags: [doctoral-foundations, collective-inertia, band-energy, evidence-matrix]
---

# 原始案例怎样约束惯量，而不把模型当作测量

## Research Trigger

本页把 [[doctoral-r2-collective-inertia-response-crosswalk-20261108]] 的定义合同
落实到实际原作，保留可复用比较、源内边界和 163Lu 的真实表格变换。
候选和反方见 [[doctoral-foundations-research-question-register-20261108]]。

## Grounded Evidence

| 案例与 source | 本轮新增理解及 locator | 最强限制/竞争 |
|---|---|---|
| [[hinohara-2010-local-qrpa-shape-mixing]]、[[sato-hinohara-2011-krypton-shape-mixing]] | Se/Kr 的局域选模、惯量与转动局域化；H10 Sec. III，SH11 pp. 10–14 | P+Q 空间、有效电荷标定、E0 近似、76Kr 态对应 |
| [[washiyama-2024-five-dimensional-improved-inertia]] | 110Pd 的弱配对区，振动质量和转动惯量增强的坐标依赖不同；pp. 3–4 | 一个 EDF 应用不推出普适规律；激发带/E2 偏差仍存 |
| [[xiang-2024-triaxial-pairing-collective-hamiltonian]] | 128Xe 动态配对压谱与 ZPE 扩谱是不同操作；pp. 3–7 | 配对 +6%、cranking、节点及波函数条件截面；不唯一归因 TV |
| [[sun-2025-iterative-atdhfb-rare-earth-inertia]] | 166Er 三 EDF 的 β接近而惯量不同；v3 p. 4 | 同时改变了配对、单粒子谱和残余场；统计排除/包含两套样本 |
| [[prochniak-rohozinski-2009-bohr-collective-hamiltonian]] | 190Os 六个 B 函数的坐标依赖；pp. 36–39, Figs. 5–8 | 低自旋结果不能替所有高自旋组态固定核芯 |

Kr 的实验比较与 R1 CoulEx 有依赖，Sun/Petrík 与 Se/Kr/110Pd 之间有方法继承；
文章数不表示独立实验数。质量区是案例选择坐标，不能代替上述输入合同。

## Provisional Reasoning

### 出版版本、曲率与稳定性

[[hinohara-2015-nambu-goldstone-inertia-response]] 在 APS p. 9 给
142Nd 质子配对 TV=2.35、IB=6.13 MeV⁻¹；p. 8 的 116Sn 中子配对则为
5.95、4.71。它们反对通用固定因子，但不是空间 TV 张量的两个实验测量。
APS 在 m₋₁ 符号及常 Tz 路径的 1/4 因子上修订了 v1；
Eq. (61) 与冻结场 Eqs. (62)–(64) 的二因子内部差异仍隔离，不判定程序错误。

对作者所列 130Xe 参数，以其定义 \(C_{ab}=1/\mathcal J_{ab}\) 重建：

\[
C\simeq
\begin{pmatrix}0.08343&-0.23607\\-0.23607&0.34376\end{pmatrix}
\mathrm{MeV},\qquad
\det C\simeq-0.02705\ \mathrm{MeV}^2 .
\]

这是任务算术，不是新的实核计算。
\(\mathcal J_{np}=-4.236\ \mathrm{MeV}^{-1}\) 是交叉曲率的倒数，
不是逆矩阵的 np 元。重建矩阵不满足正定 Schur 补的条件，
但固定 N、Z 切空间的 HFB 稳定不要求所有放开粒子数方向都同样凸。
不能仅凭行列式排除原参考态或宣称新的核不稳定性；
实际二维曲率还需核查来源符号、约束路径和生产输入。
算术可由
[doctoral_r2_response_curvature_audit.py](../../system/scripts/doctoral_r2_response_curvature_audit.py)
重放；它只使用印出参数和非实核 Hessian，不执行 HFB/QRPA。

### 163Lu 的真实表格输入

[[campaign-g07-gorgen-2004-163lu-quadrupole-moments]] PDF2 Table I、
PDF3 Table II 给 15 条带内和 5 条带间跃迁。
总控核对全部 20 行，转录/原 PDF/producer/结果均登记哈希；
没有重新拟合寿命、核形状或对准组态。

以 \(I\to I-2\) 光子能量 e（MeV）为输入，声明 \(h=\hbar\omega=e/2\)。
半经典自旋中点取 \(I-1\)，
\(J_{\rm mid}^{(1)}/\hbar^2=2(I-1)/e\)；
量子转子约定
\(J_{\rm quant}^{(1)}/\hbar^2=(2I-1)/e\)。
两者的标签/近似不同。对 \(E(I)=aI(I+1)\)，后者严格返回 \(1/(2a)\)；
不能把定义差异叫成观测到的惯量改变。

同一路相邻两条 ΔI=2 跃迁给
\(J^{(2)}/\hbar^2=4/(e_{\rm upper}-e_{\rm lower})\)，
标在两光子中点的中心。TSD1 表值产生约 66.2–76.9、
TSD2 约 70.7–75.5 \(\hbar^2/\mathrm{MeV}\) 的名义结果。
原表能量经过四舍五入，以下小数不是测量误差或新精度：

| TSD2母态 I | \(e_{\rm out}\) keV | TSD1参考母态 | \(e_{\rm ref}\) keV | \(e_{\rm out}-e_{\rm ref}/2\) keV | 同母态 E2 out/in |
|---|---:|---|---:|---:|---:|
| 47/2 | 658.9 | 49/2 | 697.0 | 310.40 | .211 |
| 51/2 | 673.2 | 53/2 | 752.6 | 296.90 | .202 |
| 55/2 | 686.8 | 57/2 | 805.6 | 284.00 | .249 |
| 59/2 | 701.1 | 61/2 | 857.7 | 272.25 | .297 |
| 63/2 | 716.3 | 65/2 | 909.7 | 261.45 | .293 |

中点能量等于相应 TSD2 能量相对 TSD1 邻自旋平均值的差，
不单独确定横向摆动、静态刚性或微观流场。
同母态 E2 比的共同寿命消去；跨不同母态的 DSAM 误差不自动取消。
一般差分 Cov 为 \(D\Sigma_E D^T\)；
只有原 γ 能量误差独立时，共享线才产生常说的负邻点协方差。
原表未给完整能量误差/Cov，因此不生成置信区间。

可重放 producer：
[doctoral_r2_gorgen_band_response.py](../../system/scripts/doctoral_r2_gorgen_band_response.py)。
数值产物及回执在
[L4结果](../../outputs/l4/20261108-band-response-definitions/derived-observables.json)；
事实输入和解释在 source/本页持久化，不以 outputs 替代知识源。

## Assumptions

固定自旋、带和路径指认；两种 J(1) 只按所列定义比较。
E2 比使用同一母态；不同 B 的误差不可假设独立。
理论比较保留 EDF、配对、算符和实际坐标，不能只冻结一个平均 γ。

## Competing Explanations

配对、顺排、带混合、有效算符和实验门选都能改变响应指标。
一个下降的中点能量或相近 J(2) 不足唯一裁决模式。
参数化模型可以利用多个自旋点约束惯量；这不等于数据不带模型就唯一恢复一般张量。

## Transfer Conditions

迁移的是可声明的输入和响应合同。能量差分方法可用于其它区，
但具体核芯形变、准粒子取向、横向回复力和可布居窗口须逐核确定。

## Failure Conditions

缺能量顺序、步长、母态对应或共同误差时，不把曲率当精确响应测量；
底本公式存在未隔离差异时，不用其校准其它模型。

## Falsification or Reverse Tests

量子转子解析极限、独立标号算术和完整 20 行表核查已通过。
真实模式仍需同模型的未拟合 EM/磁观测，而不是把这些控制当成实验模式验证。

## Open Questions

哪些公开微观输入足以把 Lu 的沿带曲率、带间 EM 与横向频率响应放在同一计算中？
原实验完整能量/寿命 Cov、部分原 producer 和响应波函数仍不可得。

## Human Review

- Review scope: 用户授权研究；未发生逐项用户科学审核。
- Decision: 名义变换可重放，物理归因保持 provisional。
- Complete unresolved P0/P1 inventory: 版本及数学边界已隔离，所有核模式归因仍
  受共同模型与输入限制；不制造实验误差条。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 原件纠错与真实表重建 | worker drafts | provisional | 区分惯量对象、版本、约束与同母态依赖，撤回任意阈值 | doctoral-nuclear-structure-foundations |
