---
type: research-note
title: "反磁转动高自旋区配对相变塌缩与动力学转动惯量突跃机制"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [AMR pairing phase transition, AMR J2 anomaly, Mottelson-Valatin collapse in antimagnetic rotation]
tags: [antimagnetic-rotation, pairing-collapse, mottelson-valatin, dynamic-moment-of-inertia, cadmium110]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "delegated microscopic AMR pairing-collapse investigation, 2026-10-29"
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
promotion_target: ""
---

# 反磁转动高自旋区配对相变塌缩与动力学转动惯量突跃机制

## Research Trigger

本轮问题是：AMR带的中高自旋区若出现动力学转动惯量 `J^(2)=dI/domega` 隆起，能否把它归因于剪刀恢复势局域软化，或归因于推转场中质子/中子单极配对能隙的 Mottelson–Valatin 型塌缩？目标是把这两个机制放进同一可计算对象，逐项对照 110Cd 与 104Pd 的寿命、`B(E2)`、Eγ 和 `J^(2)/B(E2)`。

任务中的“110Cd 在 hbar omega≈0.50–0.55 MeV 达到 60–70 hbar²/MeV”的数值不能直接当作 Roy 2011 的原始报告。Roy 的 Table 1 直接给出寿命和 `B(E2)`；由印刷的 1075、1224、1323、1314、1358 keV 相邻差分得到的简单 `4/Delta E_gamma` 还包含一个负值。相同数量级的约 63.5 hbar²/MeV 峰可以由 Rather 2014 的 104Pd `J^(2)/B(E2)` 表和 `B(E2)` 相乘得到。因此本页把 60–70 区间作为机制控制的目标尺度和 104Pd 的派生实验尺度，而不把它升级成 110Cd 的直接测量。

## Grounded Evidence

### 110Cd：直接观测与有限差分边界

Roy et al. 2011 的 110Cd Table 1（印刷 p.324）给出：

| 初态自旋 | Eγ (keV) | tau (ps) | B(E2) (e²b²) |
| ---: | ---: | ---: | ---: |
| 16+ | 1075 | 0.36(3) | 0.14(1) |
| 18+ | 1224 | 0.23(3) | 0.12(2) |
| 20+ | 1323 | 0.17(3) | 0.11(2) |
| 22+ | 1314 | 0.21(7) | 0.09(3) |
| 24+ | 1358 | 0.27(7) | 0.06(2) |

这些是实验直接提取的寿命和强度，且 Roy 明确用对称双剪刀加核心转动解释 110Cd；模型采用 `J_core=19.5 hbar²/MeV`（Roy 2011，pp.325–326，Fig.4）。按 `hbar omega=E_gamma/2` 和 `Delta I=2` 的简单有限差分，四个相邻区间给出 `J^(2)≈26.9, 40.4, -444.4, 90.9 hbar²/MeV`，中心频率约为 0.575、0.637、0.659、0.668 MeV。负值来自 1323→1314 keV 的回弯，说明这一离散代理在该点失去平滑转子意义；它不能被删去以制造一个 60–70 的峰，也不能据此认证配对塌缩。

### 104Pd：有量纲的派生 J^(2) 峰

Rather et al. 2014 的 arXiv 全文版 Table 1（p.10）给出 `B(E2)=0.26(2), 0.22(2), 0.19(1), 0.13(1), 0.07(1), 0.02(1) e²b²`（16+–26+）和 `J^(2)/B(E2)=112.3(8.6), 140.9(12.8), 334.2(17.6), 282.3(21.7), 554.3(79.2)`。逐点相乘得到约 `29.2, 31.0, 63.5, 36.7, 38.8 hbar²/MeV`（16+–24+），所以 I=20 附近确实存在有限差分/派生意义下的隆起。这个峰依赖 DSAM、side feeding、stopping 和作者的 `J^(2)/B(E2)` 表，不能作为与 110Cd 独立的配对塌缩观测。

### 理论背景与配对证据边界

Frauendorf 2001（RMP pp.466–471, 487–490）定义推转 Routhian `H'(omega)=H-omega J`，区分 `J^(1)=I/omega` 与 `J^(2)=dI/domega`，并把 AMR 描述为双剪刀横向磁矩相消、弱电四极跃迁的高自旋运动。该框架允许核心响应与剪刀角演化共同改变 `I(omega)`，但没有把某一个 `J^(2)`峰唯一归因于配对塌缩。

局部配对来源 [[zhang-2013-105106cd-pnc-superfluidity]] 与 [[zhang-2019-104pd-pnc-antimagnetic-rotation]] 支持 PNC-CSM 中配对、阻塞、占据重排和形变演化对 AMR 的共同作用：105Cd 模型中配对会推迟/平滑中子交叉，而 104Pd 的低频非对角 `J_x` 干涉使四根经典剪刀刃的分解失效。它们没有测量 110Cd 的 `Delta(omega)`，也没有证明 AMR 的 `J^(2)`峰一定是配对相变。

## Provisional Reasoning

### 自洽推转配对极小化

对每个核子种类 `q=p,n`，取残余主动配对空间中的时间反演轨道对 `k,bar{k}`，并把两质子空穴和两中子粒子作为显式阻塞的四准粒子背景。最小推转哈密顿量写成

$$
H'_q(\omega)=\sum_k(\epsilon_{qk}-\lambda_q-\hbar\omega j_{x,qk})n_{qk}
-G_q\sum_{k\ell}P^\dagger_{qk}P_{q\ell},\qquad
P^\dagger_{qk}=a^\dagger_{qk}a^\dagger_{q\bar{k}}.
$$

在固定 `lambda_q` 的最小控制模型中，

$$
E_{qk}=\sqrt{(\epsilon_{qk}-\lambda_q)^2+\Delta_q^2},
$$

$$
F_{qk}(\omega)=1-f(E_{qk}-\hbar\omega j_{x,qk})-f(E_{qk}+\hbar\omega j_{x,qk}),
$$

$$
\Delta_q=G_q\Delta_q\sum_{k\in\mathrm{active}}\frac{F_{qk}}{2E_{qk}}.
$$

这里 `F_qk` 是推转分裂对该对轨道的剩余相干权重；当准粒子分支被占据时，主动配对易感性下降。工件采用 `G_p=0.24 MeV`、`G_n=0.25 MeV`、有限展宽 `T=0.030 MeV`，主动空间为四个残余层，另行记录各自的两个被阻塞构型。它在约 `hbar omega=0.49–0.50 MeV` 附近把 BCS `Delta` 推到数值零。该阈值是本模型的壳间距、`j_x`、`G` 和固定化学势结果，不能外推成 110Cd 的实验临界频率。

固定粒子数时，`<aa>=0` 并不等于所有配对关联为零；可保留 `<P^dagger_k P_l>`、`<H_pair>` 或对转移振幅。PNC-CSM 与严格数投影因此不应被简化成“没有异常平均所以没有配对”。[[sheikh-2002-number-projection-pairing-comparison]] 在可精确求解的有限推转模型中也显示 HFB 的锐崩溃、LN 的平滑化和投影变分的残余关联可能不同。Mottelson–Valatin 在有限核中更准确地称为平均场分支的快速 crossover；没有热力学极限就不应宣称严格奇异相变。

### 从配对软化到 J^(2) 峰

将核心角动量写成 `I_core=J_core(omega) omega`，则

$$
J^{(2)}=\frac{dI}{d\omega}=J_{\rm shears}^{(1)}+J_{\rm core}(\omega)
 +\omega\frac{dJ_{\rm core}}{d\omega}.
$$

配对存在时取 Roy 型有效低频核芯惯量 `J_core≈19.5 hbar²/MeV`；完全塌缩的控制极限取题设要求的 `J_rigid≈45 hbar²/MeV`。工件把有限核响应表示为

$$
J_{\rm core}(\omega)=45-(45-19.5)S(\omega),\qquad
S(\omega)=\left[1+\exp\frac{\omega-0.40}{0.12}\right]^{-1}.
$$

`0.40 MeV` 的响应中心早于 gap 方程的约 0.50 MeV 数值塌缩，表示主动配对易感性先软化、随后发生快速重排；它是模型假设，不是额外实验事实。用 `I_shears=12+2j_pi omega/omega_shears`、`j_pi=4.5` 和 `omega_shears=0.82 MeV` 数值微分，含配对曲线在 `hbar omega=0.52 MeV` 给出 `J^(2)=70.8 hbar²/MeV`，随后回到无 `dJ_core/domega` 的约 `56 hbar²/MeV` 基线；完全无配对曲线从低频起即接近该基线。这个峰来自 `omega dJ_core/domega`，所以它是“配对控制的惯量响应峰”，不是单凭 `Delta=0` 就自动产生的定理。

### 剪刀恢复势的竞争机制

若只用角变量 `c=cos(theta)` 的剪刀能量 `V_shears(c)`，则

$$
I(\omega)=I_{\rm core}(\omega)+I_{\rm shears}(c(\omega)),
\qquad
\frac{dc}{d\omega}\propto\left[\frac{d^2V_{\rm shears}}{dc^2}+\text{core coupling}
\right]^{-1}.
$$

在 `d²V_shears/dc²` 局部变小的软点，剪刀角对频率的响应变大，同样的自旋增量也可产生 `J^(2)` 隆起。几何机制会同时改变 `B(E2)∝sin^4(theta)` 与 `B(M1)` 的角度趋势；配对机制则主要通过占据、准粒子阻塞、核心易感性和 `J_core` 的导数进入 `I(omega)`。两者都能产生峰，因此 `J^(2)` 单一观测量不具备可辨识性。

## Assumptions

- 主动配对空间是有限四层 toy 空间，化学势固定；没有做完整的粒子数约束、形变自洽、总角动量投影或 blocked-HFB/PNC 对角化。
- 两质子空穴和两中子粒子只作为阻塞背景记录，未把具体 `g_9/2`、`h_11/2` 多个签名轨道的真实 CMPC 权重冒充已知输入。
- `J_core=19.5` 来自 Roy 的唯象 AMR+core 拟合；`45` 是题设要求的刚体控制尺度，不是 110Cd 的独立实验测量。
- 0.40 MeV 的核心响应中心和 0.12 MeV 宽度是为了展示有限频宽的机制参数；它们不应与 gap 方程的 0.49–0.50 MeV 数值临界点混为同一观测量。
- 104Pd 的 `J^(2)` 数值由 Rather 报告的 `J^(2)/B(E2)` 与 `B(E2)` 相乘，仍是派生实验量；arXiv 全文与期刊第一页属于同一实验谱系。

## Competing Explanations

1. **剪刀势局域软化**：`d²V_shears/dtheta²` 变小导致 `dtheta/domega` 增大，并通过 `sin^4(theta)` 改变 `B(E2)`。它不需要配对塌缩。
2. **准粒子交叉和占据重排**：Zhang 2013/2019 所示 `g_7/2,d_5/2,h_11/2` 占据与非对角 `J_x` 干涉可改变对齐曲率，且可在配对没有完全塌缩时产生背弯。
3. **形变收缩**：104Pd 的固定 `epsilon_2` PNC 计算不能重现高频 `B(E2)` 快降，作者用随频率下降的形变拟合；若形变自由度未纳入，配对对 `J^(2)` 的份额会被高估。
4. **DSAM 与离散差分系统学**：stopping、side feeding、顶端 effective lifetime、Eγ 线重叠及分支归一会放大 `J^(2)` 的有限差分。110Cd 的 1323→1314 keV 回弯是直接的警示。
5. **组态交叉/重开剪刀**：不同 signature 或不同多准粒子构型的能级交叉能使 `I(omega)` 发生非解析分支交换；它不等同于 Mottelson–Valatin 配对相变。

## Transfer Conditions

可迁移的是推转 Routhian、`J^(2)=dI/domega`、配对 gap 方程、阻塞因子、`omega dJ_core/domega` 分解，以及用 `B(E2)` 和寿命分开检验电四极矩的逻辑。只有在同一单粒子空间、同一 `G_q`、同一阻塞方案和同一形变约束下，才可比较配对与无配对曲线。

不能直接迁移的是本工件的 `G_p/G_n`、0.49–0.50 MeV gap 阈值、0.40 MeV 核芯响应中心、`J_rigid=45`、110Cd 的具体组态和 `J^(2)`峰。奇 A、四空穴 104Pd、三轴形变、PNC 固定粒子数或真实 EDF 需要重新求解；104Pd 的 PNC 四个部分占据空穴不能替换成 Rather 的有效两空穴图像。

## Failure Conditions

以下任一条件成立时，不能把峰归因于配对塌缩：

- 只由 `B(E2)` 或 `J^(2)/B(E2)` 单独反演 `Delta(omega)`，没有独立 pairing-sensitive 观测量；
- 把固定粒子数的 `<aa>=0` 解读为两体配对关联严格为零；
- 把 `J_core=45` 作为实验刚体惯量，而没有展示其形变和质量分布假设；
- 把模型施加的 0.40/0.12 MeV 核芯响应核写成 Roy 或 Rather 的原文参数；
- 忽略 Eγ 差分中的负值、DSAM side feeding、stopping 和 22+ 1100-keV 未确认分支；
- 把 104Pd 的派生峰或 Zhang 的 PNC 计算当成 110Cd 独立实验确认。

## Falsification or Reverse Tests

1. 在同一 blocked-HFB/PNC 空间中固定形变，分别保留完整 `G_q`、置 `G_q=0`、只改配对矩阵的非对角项，并输出 `Delta_q`、`<H_pair>`、`<P^dagger_kP_l>`、占据、`I(omega)` 和 `J^(2)`。如果峰在 `G_q=0` 仍存在且由 `d²V_shears` 变化重现，配对解释不具排他性。
2. 固定配对自洽解而扫描剪刀势曲率；若仅改变 `V_shears` 的四阶项就能重现实验峰和 `B(E2)` 下降，需把两种机制标为不可辨识，而不是选择配对解释。
3. 用独立寿命、绝对 `B(E2)`、带内 `B(M1)`/弱跨带 M1 和四极矩约束同时拟合。配对塌缩应与 `J_core` 增长、`B(E2)`趋势和占据重排保持同一临界窗口；几何软化应主要改变 `theta` 与 `sin^4(theta)`。
4. 对 Roy 的 Eγ、寿命和 feeding 协方差做 bootstrap/全局 lineshape 重算；若 60–70 峰只在端点差分或删去负差分后出现，则它是数据处理敏感量。
5. 以 rather 2014 104Pd 作为 holdout：同一微观参数不得只拟合 110Cd；若无法同时解释 Pd 的 I=20 派生峰和 Cd 的 B(E2)缓降，应拒绝跨核区的单一 pairing-collapse 叙事。

## Open Questions

- 能否取得 110Cd 原始 lineshape、side-feeding 和协方差，从 Table 1 之外直接重建连续 `I(omega)`？
- 是否存在 110Cd 的 PNC/blocked-HFB `Delta_q(omega)`、两体密度或配对转移信息，能与寿命区间同频率对齐？
- 用同一 Woods–Saxon/Nilsson 空间比较 PNC、LN、投影变分和 blocked-HFB 时，`J^(2)` 峰高、宽度和位置如何变化？
- 104Pd 的四空穴 PNC 形变路径与 Rather 有效两空穴 `J_core=5` 模型能否在同一电四极矩归一化下对账？
- 是否能用带内 `B(M1)`、弱跨带 M1 或电子散射四极矩把剪刀势曲率和核心惯量响应拆开？

## Human Review

页面状态保持 `review_status: unreviewed`。本页完成了 Codex source/claim self-audit：Roy 110Cd 的直接寿命/B(E2)、Rather 104Pd 的 Table 1 派生 J^(2)、Frauendorf 的推转框架和配对来源的适用范围已分栏；没有把模型峰写成人工审核或实验确证。

## Promotion or Rejection History

2026-10-29：建立为 `reasoning_status: provisional`。接受“配对塌缩可以通过 `omega dJ_core/domega` 产生 J^(2) 峰”的条件性模型推断；拒绝“Roy 2011 已直接测得 110Cd 在 0.50–0.55 MeV 的 60–70 峰”以及“该峰已排他证明 Mottelson–Valatin 塌缩”的表述。数值工件见 [amr-pairing-collapse worker](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-pairing-collapse/README.md)。
