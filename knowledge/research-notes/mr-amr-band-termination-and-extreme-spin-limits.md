---
type: research-note
title: "MR/AMR 高自旋闭合极限与非集体能带终止"
aliases: [MR AMR band termination endpoint, shears closure extreme spin limits]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, afanasjev-1999-termination-rotational-bands, roy-2011-cd110-systematics-antimagnetic, garg-2015-135pr-magnetic-rotation, agarwal-2007-137pr-magnetic-rotation-bandcrossing]
created_from: Day26 delegated MR/AMR shears termination and extreme-spin audit
artifacts: outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/shears-termination
tags: [magnetic-rotation, antimagnetic-rotation, shears, band-termination, high-spin, dynamic-moment-of-inertia]
---

# MR/AMR 高自旋闭合极限与非集体能带终止

## Research Trigger

本轮问题是：固定价核子组态的磁转动（MR）或反磁转动（AMR）在剪刀角
\(\theta\to0\) 时，何时真正到达该组态的最大角动量，何时则通过核芯转动、
准粒子对齐或能带交叉获得新的角动量。目标是把“剪刀闭合”“非集体能带终止”
和“组态交叉/剪刀重开”分成可检验的物理层，而不是把它们都归入跃迁强度下降。

本笔记使用 Clark–Macchiavelli 2000 的剪刀几何综述、Afanasjev *et al.*
1999 的终止综述和 Roy *et al.* 2011 的 Cd 反磁转动实验与模型。三篇来源在
Wiki 中均为 `review_status: unreviewed`；以下是带 locator 的 Codex self-audit，
不是人工审核或论文级认证。

## Grounded Evidence

### 固定组态和终止的文献事实

| 来源 | 直接支持的内容 | 定位与证据边界 |
|---|---|---|
| Afanasjev *et al.* 1999 | 能带终止是固定组态中价角动量逐步对齐、集体转动连续消失并趋向非集体对齐态；终止态通常接近扁椭/非集体极限。 | *Phys. Rep.* 322, 1–124, PDF pp.4–7, Secs.1–2。形状轨迹是 CNS/转动平均场解释，不是仅由一条 γ 线直接测得。 |
| Afanasjev *et al.* 1999 | \(J^{(2)}\) 是区分平滑与不平滑终止的敏感量；\(^{109}\)Sb 的 smooth termination 中 \(J^{(2)}\) 随自旋连续降低并在终止处很小。 | PDF pp.37–40, Sec.4.2.2；该段明确把平滑性和结构纯度联系起来，也指出不规则 \(J^{(2)}\) 可来自结构改变。 |
| Clark & Macchiavelli 2000 | MR 剪刀图像由高-\(j\) 质子粒子和中子空穴组成，叶片由近正交向闭合演化；\(B(M1)\) 随横向磁矩减小而下降。 | *Annu. Rev. Nucl. Part. Sci.* 50, 1–36, PDF pp.11–18, Secs.3–4；这是综述归纳和模型解释，非本文新实验。 |
| Clark & Macchiavelli 2000 | 核芯转动、组态交叉和多叶片重耦合会使简单固定叶片图像失效或需要扩展。 | PDF pp.30–34, Sec.6, Eqs.(18)及Figs.19–20。 |
| Roy *et al.* 2011 | \(^{110}\)Cd 的 16\(^+\)–24\(^+\) 寿命为 0.36(3)、0.23(3)、0.17(3)、0.21(7)、0.27(7) ps，表中 \(B(E2)=0.14(1),0.12(2),0.11(2),0.09(3),0.06(2)\ e^2b^2\)。 | *Phys. Lett. B* 694, 322–326, printed p.324 Table 1。阻止本领系统误差可能约 20%；22\(^+\) 的 1323-keV 与 20\(^+\) 的 1314-keV 线形重叠，故端点解释需保留实验边界。 |
| Roy *et al.* 2011 | 对称双剪刀 AMR 模型使用 \(I=I_{\rm sh}+\mathcal J\omega_{\rm sh}\)，并以 \(B(E2)=15(eQ_{\rm eff})^2\sin^4\theta/(32\pi)\) 描述纯 AMR 的四极强度。 | printed p.323 Eq.(1)、Eqs.(3)–(5)，pp.325–326 Fig.4与结论。\(\sin^4\theta\) 是该对称双剪刀模型的结果，不能升级成所有 MR 或所有 AMR 组态的普适定律。 |

### 最大角动量的代数边界

在无核芯角动量、固定两叶片且采用经典矢量长度的 MR 模型中，

\[
 I^2=j_p^2+j_n^2+2j_pj_n\cos\theta,
 \qquad I_{\max}^{\rm cl}=j_p+j_n \quad(\theta=0).
\]

对四叶片 AMR，若两支质子叶片以镜像方式贡献横向分量、两支中子叶片沿总
转轴排列，则

\[
 I(\theta)=j_{n1}+j_{n2}+(j_{p1}+j_{p2})\cos\theta,
 \qquad I_{\max}^{\rm cl}=j_{p1}+j_{p2}+j_{n1}+j_{n2}.
\]

这两个 \(I_{\max}\) 是固定组态的经典上限；它们不是任意核的实验终止自旋。
有限 \(j\) 的费米子反对称性会改变可用的耦合最大值，核芯角动量 \(R\) 也会使
总自旋超过价核子纯剪刀上限。例如本轮有限单粒子代数审计中，
\(\pi(g_{9/2})^{-2}\) 的最大耦合为 \(J_p=8\)，\(\nu(h_{11/2})^2\) 为
\(J_n=10\)，冻结该扇区时 \(I_{\max}=18\hbar\)，而把两个粒子简单当作
可交换经典矢量会给出不同的上限。该例是有限-\(j\) 边界，不是对 Roy 的
\(^{110}\)Cd 组态作一一对应的实验判定。

### 观测量与证据层

| 量 | 固定组态临界行为 | 能支持什么 | 不能单独证明什么 |
|---|---|---|---|
| \(B(M1)\) | MR 两叶片的理想几何给 \(B(M1)\propto\sin^2\theta\to0\)。对称 AMR 的带内横向磁矩可相消。 | 叶片闭合和 M1 主导的候选证据。 | 不能单独排除核芯转动、有效 \(g\) 因子变化或交叉。 |
| \(B(E2)\) | Roy 的对称双剪刀模型给 \(B(E2)\propto\sin^4\theta\to0\)。普通 MR 的 E2 幂次和绝对尺度取决于核芯、有效电荷及四极振幅。 | AMR 候选带内四极强度衰减。 | 不能把 \(\sin^4\theta\) 直接用于所有 MR 或不对称 AMR。 |
| \(\tau\) | 在能量和分支已知时，强度淬灭通常对应寿命变长；需结合 \(E_\gamma\) 的高次依赖反演。 | DSAM/RDDS 的绝对强度约束。 | 不能只用寿命趋势判定形状，因 feeding、stopping power 和线形会影响提取。 |
| \(J^{(2)}=dI/d(\hbar\omega)\) | 固定组态接近角动量上限时，模型轨迹的斜率可显著降低；Afanasjev 的 smooth termination 以连续降至很小为特征。 | 终止路径和结构连续性的动力学诊断。 | 负有限差分不是普适终止判据，可能来自交叉、带标记、线序或拟合问题。 |
| \(Q_t\)/绝对 \(B(E2)\) | 平滑终止要求集体四极矩沿固定组态连续塌缩。 | 非集体终止的形变证据。 | 一条弱或未观测 E2 线不等于 \(Q_t=0\)。 |

## Provisional Reasoning

### 1. MR 的闭合和 M1 淬灭

对两片固定长度的叶片，磁矩横向分量的半经典表达式为

\[
 |\mu_\perp|=(g_p-g_n)\frac{j_pj_n}{I}\sin\theta,
 \qquad
 B(M1)=\frac{3}{8\pi}|\mu_\perp|^2.
\]

因此在单一、孤立组态且叶片长度不变时，\(\theta\to0\) 给出
\(B(M1)\sim\theta^2\)。这支持“MR 终止前 M1 淬灭”的方向性推断。它依赖
有效 \(g\) 因子、核芯分担和组态不变；Clark & Macchiavelli 的 Eq.(5)及
PDF pp.13–18 已明确要求把核芯贡献从总自旋中单独估计。

### 2. AMR 的四极幂律和对称性边界

两支等价质子叶片的横向电四极振幅在镜像求和后是一阶横向项的相消，剩余
二阶张量分量随 \(\sin^2\theta\) 变化；其平方给出 Roy Eq.(1) 的
\(B(E2)\propto\sin^4\theta\)。理想等权双剪刀的横向磁矩也相消，因此带内
\(\Delta I=1\) M1 可被强烈压低。若叶片磁权重差为 \(\epsilon\)，则残余 M1
幅度为一阶 \(\epsilon\sin\theta\)，强度为二阶 \(\epsilon^2\sin^2\theta\)。
这说明“AMR 的 M1 为零”是对称极限，不是对奇 A、阻塞或混合组态的普适选择定则。

### 3. 终止附近的动态惯量

本轮脚本使用有界闭合轨迹
\(\cos\theta=1-\exp[-(\omega-\omega_0)/s]\)，并把 \(I(\theta)\) 代回
MR/AMR 几何。它得到：

- MR \(I_{\max}=15.5\hbar\)，AMR 四叶片示例 \(I_{\max}=20\hbar\)；
- 小角拟合的 MR \(B(M1)\) 幂为 1.9998，AMR \(B(E2)\) 幂为 3.9986；
- 固定组态路径的 \(J^{(2)}\) 从起始的 29.46（MR）和 55.38（AMR）
  \(\hbar^2/{\rm MeV}\) 降到 \(0.0125\) 和 \(0.0316\ \hbar^2/{\rm MeV}\)；
- 加入新叶片的平滑交叉代理模型在 \(\hbar\omega\simeq0.83\) MeV 产生
  \(J^{(2)}\) 峰（约 32.49 \(\hbar^2/{\rm MeV}\)），表示新组态重新提供
  角动量；它不是任何单个核的拟合。

脚本另设一个人为的局部轨迹回落反向测试，得到负斜率约
\(-18.48\ \hbar^2/{\rm MeV}\)。该数值只说明有限差分可以在轨迹回落、带标记
错误或未解析交叉时变成负值；它不证明稳定的终止态具有负物理转动惯量。
Afanasjev 的原文把 smooth/unsmooth 终止和结构改变分开讨论（PDF pp.37–40），
因此实验中出现负或强烈不规则的 \(J^{(2)}\) 应优先检查交叉和数据序列。

### 4. smooth termination 与 crossing/reopening 的判别

| 检验 | smooth band termination | crossing / shears reopening |
|---|---|---|
| 组态 | 同一固定组态、能级和 signature 连续可追踪 | 对齐增益、能级排斥或新 signature；需要新组态交叉证据 |
| \(I(\omega)\)、\(J^{(2)}\) | \(J^{(2)}\) 平滑下降至小值，\(Q_t\) 同时连续下降 | 局部峰、突变、回弯或不规则；新组态可使斜率重新增大 |
| 强度 | M1（MR）或 E2（对称 AMR）沿固定角度规律淬灭；寿命按相应强度增长 | 新带/新跃迁、混合强度或绝对 \(B(M1)\) / \(B(E2)\) 非单调反弹 |
| 形状 | CNS/TAC 的 \(\gamma\to60^\circ\) 扁椭非集体端是模型解释；需 \(Q_t\) 或多观测量支撑 | 形变、转轴倾角或核芯响应在交叉处重排；不能只用一条 \(\gamma\) 线归因 |
| 寿命和分支 | 固定分支、绝对寿命可连续拟合 | 交叉附近寿命、分支、偏振或对齐出现协同变化；需排除 feeding 变化 |

因此，判定终止至少需要“固定组态追踪 + \(J^{(2)}\) 连续趋势 + 绝对或相对
四极/磁强度 + 角动量上限”的组合。判定重开则需要“新组态指认 + 局部对齐增益
或能级排斥 + 交叉后新的电磁/寿命行为”。单独看到 \(B(E2)\) 变小，或单独看到
\(J^{(2)}\) 异常，都不足以二选一。

## Assumptions

- MR 计算采用两片固定经典矢量；AMR 计算采用两支等价质子叶片和两支轴向
  中子叶片，显式保留等权镜像假设。
- 角动量和 \(B(M1)\) 的数值为透明 toy 输入（\(j_p=5.5\)、\(j_n=10\)、
  有效 \(g_p=1.2\)、\(g_n=-0.2\)），不是 135Pr、110Cd 或其它单核素的拟合。
- AMR 使用 Roy 2011 的 \(Q_{\rm eff}=1.10\ eb\) 作为示例尺度；它不是本文从寿命
  分离出的独立静态四极矩。
- \(J^{(2)}\) 用 \(I(\omega)\) 的有限差分近似；实验中还需从正确的能级序列和
  跃迁频率构造，不能直接套用脚本的频率网格。
- \(\gamma\to60^\circ\) 取自终止综述的转动平均场形状语言；不把它当作独立的
  实验直接量。

## Competing Explanations

- 有限 \(B(E2)\) 或其平台可能来自核芯集体转动、频率依赖 \(\beta_2\)、有效电荷、
  四极振幅干涉或 feeding，而不是剪刀角没有闭合。Roy 2011 的 110Cd 正是 AMR
  与核芯转动耦合的案例（printed pp.325–326）。
- \(B(M1)\) 下降可能由有效 \(g\) 因子和核芯极化改变造成；它不能独立确定叶片角。
- 不规则 \(J^{(2)}\) 可能是组态交叉、能级排斥、配对坍缩、形状共存或跃迁排序问题；
  Afanasjev 1999 明确把不平滑终止与结构改变区分（PDF pp.37–40）。
- 奇 A 核的阻塞和镜像不对称会让理想 AMR 的 M1 相消失效；不能把偶偶 Cd 的
  \(\sin^4\theta\) 结果无条件迁移到 135Pr 等 MR 核。

## Transfer Conditions

可迁移的是：固定叶片几何下 \(I_{\max}\) 的矢量和边界；MR 横向磁矩的
\(\sin\theta\) 因子；以及对称双剪刀四极张量导致的 \(\sin^4\theta\) 角因子。

不可直接迁移的是：Roy 的 \(V_{\pi\nu}=1.2\) MeV、\(\mathcal J=19.5\hbar^2/{\rm MeV}\)、
\(Q_{\rm eff}=1.1\ eb\)，以及任何固定的 \(J^{(2)}\) 阈值。换到 A≈130 的
135Pr/137Pr 时，必须重新核对配置、对齐轨道、有效 \(g\) 因子、绝对寿命和核芯
响应。135Pr 现有证据中，Garg 2015 的 Fig.7 是相对 \(B(M1)/B(E2)\) 曲线，
交叉后缺少 crossover E2；高自旋“重开”应标为 TAC/几何解释，而非交叉后绝对
强度的直接测量（Garg 2015, PDF pp.7–8；见 [[pr135-shears-dynamics-bandcrossing-rebound]]）。

## Failure Conditions

若叶片长度随频率连续变化、存在强组态混合、核芯角动量不可忽略、镜像等权条件
破缺或四极振幅存在显著相干干涉，固定 \(\sin^2\theta\)/\(\sin^4\theta\) 轨迹
即失效。若终止候选没有足够长的同组态能级序列、没有寿命或 \(Q_t/B(E2)\) 约束，
只能写成“可能接近终止”，不能写成非集体终止已确立。若 \(J^{(2)}\) 的负值只在
删去交叉点或改动线序后出现，也不能把它作为终止动力学的独立证据。

## Falsification or Reverse Tests

1. 在脚本中把两片 MR 叶片的有效磁权重改为 \(g_1=1.2+\epsilon\)、
   \(g_2=-0.2-\epsilon\)，验证 \(B(M1)\) 的端点系数改变但 \(I_{\max}\) 不变。
2. 把 AMR 一支叶片的电四极权重改为 \(q(1+\epsilon)\)，检查原本精确的
   \(\sin^4\theta\) 幂律和 M1 相消是否同时破缺。
3. 固定角度轨迹，只改变 \(Q_{\rm eff}(\omega)\) 和一个核芯 E2 底座，测试有限
   \(B(E2)\) 是否可以在不重开的情况下出现平台。
4. 对实验能级使用三点有限差分并保留所有交叉候选点；若负 \(J^{(2)}\) 仅由
   两条近能线互换产生，应把它归为排序/交叉问题而不是负惯量。
5. 用绝对 DSAM/RDDS 寿命、分支比、偏振和独立形变约束联合拟合；若交叉后
   \(B(M1)\)、\(B(E2)\)、对齐和寿命均保持同一固定组态的单调轨迹，则“重开”
   解释被削弱；若出现协同反弹且新组态可追踪，则“终止”解释被削弱。

## Open Questions

- 对同一 MR/AMR 带，能否同时获得交叉前后绝对 \(B(M1)\)、\(B(E2)\)、寿命和
  \(J^{(2)}\)，从而把“相对比值反弹”拆成分子与分母的真实变化？
- 如何在有限粒子数投影的 TAC/PRM 或 EDF 中同时处理反对称性、配对和核芯响应，
  得到量子化的 \(I_{\max}\) 而不是经典叶片和？
- 110Cd 的 24\(^+\) 端点和 26\(^+\) 有效寿命能否由新的多角度 lineshape/RDDS
  数据约束，以区分双剪刀闭合与核芯转动尾部？
- A≈130 的 135Pr/137Pr 交叉后能否补测 crossover E2 和绝对寿命，以验证“新增
  质子对导致剪刀重开”的具体组态而不是其它多准粒子重排？
- 能否用同时约束的 \(Q_t\)、\(\gamma\)、磁矩和对齐数据检验终止态是否确实
  接近 \(\gamma=60^\circ\) 的非集体扁椭端？

## Human Review

尚未进行人工审核。三篇核心来源页和本笔记均保持 `review_status: unreviewed`；
本轮只完成 Codex self-audit、公式边界检查和脚本复现。后续若用于论文或正式
项目决策，应按具体 claim 回到原 PDF、图表和实验原始论文，不把本页的自审状态
改写为 `human-reviewed`。

## Promotion or Rejection History

- 2026-10-29：新建本页和 `workers/shears-termination/` 工件目录。
- 接受为条件性结论：固定组态 MR 的 \(B(M1)\sim\sin^2\theta\) 端点；Roy 对称
  AMR 模型的 \(B(E2)\sim\sin^4\theta\)；固定组态终止附近 \(J^{(2)}\) 的连续
  下降；交叉可通过新叶片/新组态使 \(J^{(2)}\) 与强度轨迹重开。
- 拒绝为普适结论：所有 MR 的 \(B(E2)\sim\sin^4\theta\)；负 \(J^{(2)}\) 是
  终止的必要特征；经典 \(I_{\max}\) 等于任意真实核的终止自旋；仅凭弱 E2 或
  负有限差分即可排除能带交叉。

## Reproducible Artifacts

目录：`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/shears-termination/`

- `shears_termination_trajectory.py`：角度扫描、MR/AMR 闭合轨迹、幂律拟合、
  固定组态与交叉/反向测试的 \(J^{(2)}\)。
- `shears_termination_angular.csv`：\(\theta\)、\(I\)、\(B(M1)\)、\(B(E2)\)
  和镜像破缺代理量。
- `shears_termination_trajectory.csv`：\(\hbar\omega\)、\(I(\omega)\)、
  \(J^{(2)}\) 及重开/回落轨迹。
- `shears_termination_results.json`：参数、文献 locator、SHA-256、幂律和极值。

运行命令：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/shears-termination/shears_termination_trajectory.py
```
