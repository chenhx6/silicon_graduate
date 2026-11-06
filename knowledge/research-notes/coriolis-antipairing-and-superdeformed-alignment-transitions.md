---
type: research-note
title: "CAP 与超形变惯量：Day27 指定配对隙和带交叉示意的边界"
aliases: [coriolis-antipairing-and-superdeformed-alignment-transitions, CAP superdeformed alignment transitions, Day27 CAP SD ND]
created: 2026-10-30
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [book-bohr-mottelson-nuclear-structure-vol2]
created_from: Day 27 continuation study; system/scripts/day27_sd_vs_nd_pairing_cap_study.py
tags: [superdeformation, Coriolis-anti-pairing, CAP, backbending, dynamic-moment-of-inertia, Day27]
---

# CAP 与超形变惯量：Day27 指定配对隙和带交叉示意的边界

## Research Trigger

不同转动惯量曲线能否区分配对减弱、组态顺排和形变变化？Day27 程序只演示指定参数如何改变曲线，没有回答实际核素的排他机制问题。原笔记将 `160Dy_ND`、`152Dy_SD`、`194Pb_SD` 三组人为输入和输出写成核素实验事实，并宣称微观自洽地解决跨质量区争议；这些归属和裁决现已撤回。

旧正文的具体配对隙、壳隙、后弯峰值、惯量平台、涨幅、临界频率和 $Q_t$ 数值，没有本页可追溯的实验输入、误差和逐条 source locator，不保留为知识结论。旧称 DSAM 已排除形变拉伸、模型证伪无配对顺排的说法也撤回。历史输出 JSON 只保留原运行记录的身份，不是长期问答的实验事实源。

## Grounded Evidence

[[book-bohr-mottelson-nuclear-structure-vol2]] BM2-11（§4-3a，PDF64／printed42，编号1与前文）只支持配对减弱和可能转变的试探性解释，不支持普适平方根函数、固定临界自旋或统一二级相变。本轮读取既有 source 更正，没有新增原书页面或实验原件核验。

## Assumptions

`day27_sd_vs_nd_pairing_cap_study.py` 保留 `solve_cranked_pairing_bcs` 旧名称以兼容调用，但它**没有求解 BCS**。`G_pair` 只检验有限和非负，完全不参与结果；不从函数名推断存在 gap/number 方程。采用的曲线为

$$x=\hbar\omega\ [\mathrm{MeV}],\qquad
\Delta(x)=\Delta_0\sqrt{\max[0.04,1-(x/0.65\,\mathrm{MeV})^2]}.$$

0.65 MeV 和20%残余 gap 下限都是程序指定值。只要 $\Delta_0>0$，这条曲线就不会完全塌缩；它与 CAP engine 的零隙插值并非相同模型。

二能带示意另行指定

$$d(x)=2j(x_c-x),\quad P(x)=\frac12\left(1-\frac{d(x)}{\sqrt{d(x)^2+4V^2}}\right),\quad i_x(x)=2jP(x).$$

$j$ 是以 $\hbar$ 为单位的数值，$x_c$ 与 $V$ 单位为 MeV。交叉位置和混合强度均为输入；$d(x)$ 没有包含 $\Delta(x)$，不存在由 gap 自洽预测交叉或微观波函数重叠的计算。有限输入需 $x,\Delta_0,G_{\rm pair},x_c\ge0$，$j,V>0$；排除 $V=0$ 时交叉点的未定义退化。

集体响应和总自旋数值为

$$\mathcal J_{\rm rig}=0.0140 A^{5/3}(1+0.32\beta_2)\ [\hbar^2/\mathrm{MeV}],$$
$$\mathcal J_{\rm coll}(x)=\frac{\mathcal J_{\rm rig}}{1+(\Delta(x)/0.55\,\mathrm{MeV})^{1.8}},\qquad
I_x/\hbar=[\mathcal J_{\rm coll}/\hbar^2]x+i_x.$$

这些系数和指数是示意选择，没有本轮经验标定。限定 $A>0$、$\beta_2\ge0$。旧 `Q_t_eb` 字段按领先阶形变公式给出代理值，并假定 $A=152,160$ 时 $Z=66$，其它质量时 $Z=82$；这是遗留的电荷假定，不是通用核素识别或实测四极矩。

## Provisional Reasoning

在指定交叉点 $x=x_c$，$P=1/2$、$i_x=j$；交叉中心斜率为 $d i_x/dx=j^2/V$。因此峰宽由输入 $V/j$ 控制，不能据此宣称已推出配对相变阶数。

即使 $\Delta_0=0$，$i_x(x)$ 仍可变化，从而

$$\mathcal J^{(2)}/\hbar^2=\mathcal J_{\rm rig}/\hbar^2+d i_x/dx$$

仍可呈现非恒定响应。旧称“无配对必然得到恒定刚体线，因此惯量上升证明配对存活”的推理不成立。程序的 $\mathcal J^{(2)}$ 是对未舍入自旋与 $x$ 作中心割线差分；要求至少三个严格递增、非负、有限频率点，端点为 null。显示的舍入频率不能代替计算采样；尖峰高度和宽度可能依赖网格。

## Falsification or Reverse Tests

CLI 仍输出原核素标签和旧 `self_tests` 键，但明确标记为合成曲线阈值检查。通过只说明指定曲线达到内部阈值，不证明实验拟合、BCS 收敛或跨质量区机制。输出 `empirical_inputs` 为空，撤销未实际读取的经验文献归属。

## Competing Explanations

配对减弱、带交叉、单粒子顺排和形变变化均仍是待区分的解释。需要有逐带来源与误差的能量、寿命和电磁观测，以及独立约束下的模型比较，才能作核素判断；本任务没有开展这些工作。这里也不从三个合成预设推出质量区普适性或适用频率／形变阈值。

## Transfer Conditions

迁移这套曲线时必须保留其输入系数、单位、采样及遗留电荷假定，不把函数旧名或核素标签当成真实BCS求解／实验校准。

## Failure Conditions

将未使用的G_pair当成配对强度验证，将指定交叉归因于gap自洽，或将合成阈值测试写成结构确认，均使相应推断失效。

## Open Questions

实际核素中哪些具有独立误差和来源的能量、电磁与组态观测能够区分这些机制？本轮不新增实验拟合来回答。

## Human Review

没有新增真实用户科学审核事件；本次为源归属和条件模型合同更正。

## Promotion or Rejection History

- 2026-10-30 的“全微观／解决争议”历史声明撤回。
- 2026-11-06：冻结范围内修正代码说明、输入域、量纲和证据归属；未扩展为真实 BCS 模型，未改历史运行文件。
- [[book-bohr-mottelson-nuclear-structure-vol2]] BM2-11：试探性作者解释的来源边界。
- [[coriolis-anti-pairing-and-moment-of-inertia-expansion]]：不同的零隙条件插值及统一缩放轴比恒等式。
