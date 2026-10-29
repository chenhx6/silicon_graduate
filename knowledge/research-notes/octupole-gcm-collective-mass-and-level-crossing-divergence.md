---
type: research-note
title: "八极形变下微观集体惯量张量、避免交叉与绝热路径重整"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole GCM collective mass, ATDHFB octupole inertia, avoided-crossing mass divergence]
tags: [octupole, collective-mass, gcm, atdhfb, inertia-tensor]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 delegated study of ATDHFB/GCM collective inertia and octupole avoided crossings"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, bernard-2016-144ba-sccm-octupole]
outputs: ["outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-mass-tensor/octupole_mass_tensor.py", "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-mass-tensor/results.json"]
---

# 八极形变下微观集体惯量张量、避免交叉与绝热路径重整

## Research Trigger

本轮问题是：在二维形变坐标 $(q_2,q_3)=(\beta_2,\beta_3)$ 中，微观 GCM/ATDHFB 质量参数如何写出，八极驱动的 $\Delta l=\Delta j=3$ 轨道对在费米面附近的避免交叉如何影响绝热惯量，以及配对、残余相互作用和有限频率响应如何把小分母问题变成有限的动力学质量。重点核素是 $^{144,146}$Ba、$^{224}$Ra 和 $^{226}$Th。

“拓扑发散”在这里须谨慎使用：单粒子避免交叉本身没有已证明的拓扑不变量。真正可识别的是绝热坐标图中的小分母奇异性和绝热近似失效；只有当配对塌缩、能级真正趋于简并且矩阵元保持非零时，摄动推转表达式才显示发散标度。

## Grounded Evidence

| ID | 可复用事实 | 类型 | 定位与边界 |
|---|---|---|---|
| BN96-1 | 反射不对称的微观驱动与费米面附近的 $\Delta l=\Delta j=3$ 异宇称轨道对有关；静态八极极小、八极振动/软度、宇称恢复和 E1/E3 观测必须分层。 | 综述归纳 | Butler–Nazarewicz, RMP 68 (1996), Secs. II–VII, PDF pp.349–421；综述不是新的独立实验。 |
| BN96-2 | E1 对质子—中子位移和相消敏感，E3 更接近集体八极探针；强 E3 或低宇称劈裂不能单独证明刚性静态梨形。 | 综述归纳 | 同上，Secs. II.B, IV.C–D, VII；保留 `needs_review`。 |
| BE16-1 | 144Ba 的投影 GCM 先在 $(\beta_2,\beta_3)$ 上作 HFB，再恢复 $J,\pi,N,Z$ 并解 HWG；使用约 130 个内禀态，最低点约 $(0.2,\pm0.1)$，$\beta_3$ 方向较软。 | 原文模型结果 | Bernard–Robledo–Rodríguez, PRC 93, 061302(R) (2016), PDF pp.1–3, Eqs.1–5, Fig.1；未取得生产核和惯量网格。 |
| BE16-2 | 144Ba 二维投影 GCM 给 $0^+\leftrightarrow3^-$ 的 $B(E3)$ 约 25 W.u.；作者指出转动惯量偏小、谱伸展和缺少 cranking/配对响应是限制。 | 原文模型结果与限制 | 同上，PDF p.4 Table I 与讨论；不能当作实验 $B_{33}$。 |
| BU16-1 | 144Ba 直接库仑激发给出 $B(E3;3^-\to0^+)=48^{+25}_{-34}$ W.u.，但 $\beta_3$ 转换依赖转子、高阶多极和符号假设。 | 直接实验 | Bucher et al., PRL 116, 112503 (2016), PDF pp.3–4, Table I；[[bucher-2016-144ba-direct-octupole]]。 |
| BU17-1 | 146Ba 也给出中心约 48 W.u. 的基态 E3；小 E1 与中子轨道占据、偶极贡献相消有关，不能把 E1 小值当成惯量或八极集体性变弱的直接证据。 | 直接实验加模型解释 | Bucher et al., PRL 118, 152504 (2017), PDF pp.2–5, Table I, Figs.3–5；[[bucher-2017-146ba-direct-octupole]]。 |
| WR11-1 | 224Ra 的 Gogny-D1S HFB/ATDHFB-WKB 路径计算在基态附近约有 $\beta_2=0.18,\beta_3=0.14$；WKB 作用量同时依赖势能、ATDHFB 近似惯量、转动/零点修正和路径。 | 原文模型结果 | Warda–Robledo, PRC 84, 044608 (2011), PDF pp.3–5, 10–13, Eqs.2–7；[[warda-2011-actinide-cluster-radioactivity-gogny]]。该文不是低能 $B_{33}$ 系统学。 |
| NO20-1 | Gogny-D1M 映射把 224Ra 和 226Th 定位在八极关联较强的区域（模型 $\beta_3\sim0.15$），并保留核素依赖和软势边界。 | 原文模型结果 | Nomura et al., PRC 102, 064326 (2020), PDF pp.2–4, Fig.1；[[nomura-2020-ra-th-gogny-d1m-octupole]]。 |

现有来源没有给出四个核素在同一 EDF、同一坐标和同一惯量约定下的数值 $B_{22},B_{23},B_{33}$ 表，也没有给出统一的绝对表观转动惯量。因而本笔记不伪造这样的“对账表”。实验层的常用派生量是

$$
\mathcal J^{(1)}(I)=\frac{\hbar^2(2I-1)}{E_\gamma(I\to I-2)},\qquad
\mathcal J^{(2)}(\omega)=\frac{dI}{d\omega},
$$

但它们需从同一评价版本的能级和带标签重建；它们也不等于坐标依赖的八极质量 $B_{33}$。

## Provisional Reasoning

### 1. 二维集体动能与量子哈密顿量

取 $q_i=(\beta_2,\beta_3)$，经典集体动能写成

$$
T_{\rm coll}=\frac12 B_{ij}(q)\dot q_i\dot q_j
=\frac12\left(B_{22}\dot\beta_2^2+2B_{23}\dot\beta_2\dot\beta_3+B_{33}\dot\beta_3^2\right).
$$

这里 $B_{ij}$ 是质量张量；量子化时其逆矩阵 $B^{ij}$ 进入微分算符，且测度因子取决于坐标约定。例如在简单 Pauli–Podolsky 排序中

$$
\hat H_{\rm coll}= -\frac{\hbar^2}{2\sqrt{G}}\partial_i\left[\sqrt{G}\,B^{ij}\partial_j\right]+V_{\rm coll}(q),
$$

其中 $G$ 是相应集体度规行列式。$B_{23}$ 不是可任意删掉的“混合项”：它描述四极路径倾斜时八极响应的投影，只有在对称性或数值结果明确使其为零时才可忽略。

### 2. IB、GCM 和 ATDHFB 公式

令 $|\Phi(q)\rangle$ 为约束 HFB 真空，$E_\mu$ 为准粒子能量。切向量可写作

$$
\partial_i|\Phi\rangle=\frac12\sum_{\mu\nu}Z_i^{\mu\nu}\beta_\mu^\dagger\beta_\nu^\dagger|\Phi\rangle,
$$

并定义约束 HFB 哈密顿量导数的 20 分量
$F_i^{\mu\nu}=(\partial_i\mathcal H_{\rm HFB})^{20}_{\mu\nu}$。在 $\mu<\nu$ 求和且把共轭项显式对称化的约定下，Inglis–Belyaev 摄动质量可写成

$$
B^{\rm IB}_{ij}=\hbar^2\sum_{\mu<\nu}
\frac{F_i^{\mu\nu *}F_j^{\mu\nu}+F_j^{\mu\nu *}F_i^{\mu\nu}}
{(E_\mu+E_\nu)^3}
=2\hbar^2\,\mathrm{Re}\sum_{\mu<\nu}
\frac{F_i^{\mu\nu *}F_j^{\mu\nu}}{(E_\mu+E_\nu)^3}.
$$

不同文献把 $\mu\nu$ 全空间求和、Kramers 简并和 $\hbar^2$ 因子放在不同位置；上式的求和约定必须随结果报告。用能量矩

$$
M_{-n,ij}=\sum_{\mu<\nu}
\frac{F_i^{\mu\nu *}F_j^{\mu\nu}+F_j^{\mu\nu *}F_i^{\mu\nu}}
{(E_\mu+E_\nu)^n},
$$

常用的扰动推转形式为

$$
B^{\rm GCM}_{ij}=\hbar^2\left[M_{-1}^{-1}M_{-2}M_{-1}^{-1}\right]_{ij},
\qquad
B^{\rm ATDHFB}_{ij}=\hbar^2\left[M_{-1}^{-1}M_{-3}M_{-1}^{-1}\right]_{ij}.
$$

这些式子是 perturbative-cranking 版本，不能与完整非局域 GCM 核自动等同。完整 GCM 要由 Hamiltonian kernel 和 norm kernel 解 Hill–Wheeler–Griffin 方程；Bernard 2016 的双坐标求和正是这种投影核层面的约束。

Thouless–Valatin 修正来自残余相互作用诱导场。线性响应层面可将每个 $F_i$ 代入 QRPA 矩阵方程

$$
\begin{pmatrix}A&B\\-B^*&-A^*\end{pmatrix}
\begin{pmatrix}X_i\\Y_i\end{pmatrix}
=\begin{pmatrix}F_i^{20}\\F_i^{02}\end{pmatrix},
$$

再用屏蔽/反屏蔽后的响应构造 $B^{\rm TV}_{ij}$。因此 TV 不是固定乘数；它依赖残余相互作用、配对、约束和是否包含粒子数/角动量的恢复。脚本中的 `TV_proxy` 只是显示这一层可能重整化的透明占位，不是 QRPA 计算。

### 3. 避免交叉、小分母与绝热失效

用二能级哈密顿量

$$
H_{\rm sp}(x)=\begin{pmatrix}ax&V\\V&-ax\end{pmatrix},
\qquad \epsilon_\pm=\pm\sqrt{(ax)^2+V^2},
$$

其本征态导数耦合为 $|\langle+|\partial_qH|-\rangle|=aV/\sqrt{(ax)^2+V^2}$。当 $V\ne0$ 时，普通单粒子避免交叉的导数耦合是有限的。若配对为 $\Delta$，相应准粒子尺度可示意为 $E=\sqrt{\epsilon^2+\Delta^2}$，所以有限 $\Delta$ 使 $(E_\mu+E_\nu)^{-3}$ 有上界。

真正的条件性奇异性在 $x=0,\Delta\to0,V\to0$ 出现：$F\to a$ 而 $E_\mu+E_\nu\sim2|V|$，故裸 IB 项满足

$$
B_{33}^{\rm IB}\propto\frac{a^2}{(2|V|)^3}\sim |V|^{-3}
$$

（若把导数耦合改写成不同规范，常见有效标度会呈 $V^{-1}$；发散幂次取决于保持不变的矩阵元和坐标定义）。因此“避免交叉必然导致发散”不成立；准确说法是“配对塌缩的近简并极限使绝热摄动展开失效，并产生对正则化极端敏感的伪奇点”。脚本在 `avoided_crossing_scaling.csv` 中固定交叉点展示裸曲线、配对曲线和有限频率曲线。

### 4. 非绝热/配对/粒子数响应的路径重整

平滑质量的三个机制可分开写：

1. **有限配对与配对振幅涨落：** $E=\sqrt{\epsilon^2+\Delta_{\rm eff}^2}$，其中 $\Delta_{\rm eff}$ 可包含静态配对和配对涨落的有效尺度；这避免把 $E_\mu+E_\nu$ 当成零。
2. **动态粒子数投影：** $N$ 投影改变 norm/Hamiltonian kernels 和集体度规，不能简单把平均粒子数约束代替为“再加一个 gap”。其方向是正则化配对塌缩，具体数值须由投影核计算决定。
3. **有限速度/有限频率：** 线性响应的零频展开可被有限频率响应替代。脚本采用示意尺度 $D_\omega=[(2E)^2+(\hbar\omega)^2]^{1/2}$，从而质量分母改为 $D_\omega^3$。这是平滑 proxy，不是有耗散的全频率 QRPA；真实响应还可能出现共振峰、相位延迟和摩擦项。

在二维路径上，$B_{23}$ 使最小作用路径偏离单纯的 $\beta_3$ 线。路径应由
$\int ds\sqrt{2B_{ij}(q)\,dq_i/ds\,dq_j/ds\,[V(q)-E_0]}$
最小化，而不能把某条静态 HFB 极小线直接当成动力学路径。

### 5. 核素系统学的现阶段可比量

| 核素 | 可核验的八极输入 | 惯量/转动层结论 | 当前缺口 |
|---|---|---|---|
| $^{144}$Ba | 直接 $B(E3)=48^{+25}_{-34}$ W.u.；投影 GCM 极小约 $(\beta_2,\beta_3)=(0.2,\pm0.1)$，$\beta_3$ 方向软。 | GCM 作者报告转动惯量偏小；实验能级可重建 $\mathcal J^{(1)}$，但本轮未生成同版评价表。 | 没有与 146Ba、Ra/Th 同 EDF 的 $B_{33}(\beta_2,\beta_3)$。 |
| $^{146}$Ba | 直接 $B(E3)=48^{+21}_{-29}$ W.u.；E1 强烈变化与 E3 强度解耦。 | E1 变化不能反推八极惯量变化；需能级/寿命和同一模型的路径响应。 | 没有发布的二维 ATDHFB/GCM 质量表。 |
| $^{224}$Ra | Gogny-D1S HFB 近基态约 $\beta_2=0.18,\beta_3=0.14$；ATDHFB 惯量进入团簇 WKB 作用量。 | WKB 对势、惯量、转动和零点修正共同敏感；不可把表观转动惯量替代 $B_{33}$。 | 低能八极振动专用 $B_{33}$ 与统一实验 $\mathcal J^{(1,2)}$ 账本缺失。 |
| $^{226}$Th | Gogny-D1M 映射在 $\beta_3\sim0.15$ 附近八极关联强。 | 只能说模型预期集体八极响应较强；不能给出本文未取得的数值惯量。 | 缺同一坐标、投影和 TV 修正下的惯量张量。 |

## Assumptions

- $\beta_2,\beta_3$ 采用同一无量纲轴对称坐标约定；不同来源的 $Q_\lambda$、半径和体积保持条件不能直接混换。
- 质量参数的公式采用 $\mu<\nu$ 求和和显式厄米对称化；若改用全空间求和，必须同步改变简并因子。
- toy 模型将未显式纳入的 2qp 通道压缩成小对角正则项，将配对涨落/粒子数投影压缩为有效响应尺度；这不等价于自洽 EDF。
- 大振幅周期使用一维对称双阱和坐标依赖的动态 $B_{33}$；没有声称重现某个核素的绝对能量或周期。
- 现有直接来源的 `review_status` 均为 `unreviewed`，本笔记保持 `ai-draft` 和 `provisional`。

## Competing Explanations

- 小分母峰可能是配对塌缩或坐标参数化造成的绝热伪奇点，也可能是真实的强非绝热跃迁；需要有限频率响应、Landau–Zener 概率和残余相互作用共同判定。
- 144/146Ba 的软性可以来自二维形状混合、宇称恢复和配对响应缺失的模型偏差；不能把强 E3 自动解释为刚性静态形状。
- 224Ra 的低能宇称结构可以是深双阱、宇称恢复后的软振动或转动—振动耦合；E1/E3 和能级必须联合使用。
- TV 修正可能增强或减小不同方向的质量，且 $B_{23}$ 的符号可随规范和路径方向改变；固定“TV=1.25 IB”不是可迁移规律。

## Transfer Conditions

要把 toy 结果迁移到具体核素，至少需要同一 EDF 和配对方案的 $(\beta_2,\beta_3)$ HFB 网格、完整 2qp 谱和 $F_i^{20}$ 矩阵元；随后用同一投影约定计算 GCM/ATDHFB 惯量，并报告 $B_{23}$、正定性、网格和配对截断收敛。对 Ba/Ra/Th 的跨核比较还需统一能级评价版本、带标签、E3/E1 矩阵元和转动惯量定义。

## Failure Conditions

- 把普通有限间隙避免交叉写成必然拓扑发散，或把 toy 的无量纲质量写成核素的 MeV$^{-1}$ 数值。
- 在 $\Delta=0$ 或 2qp 截断未收敛时直接逆矩阵，产生数值正则化依赖。
- 忽略 $B_{23}$、粒子数/角动量投影和坐标测度，却把一维 $B_{33}$ 当作二维动力学。
- 将 Warda 的裂变路径 ATDHFB 惯量当作低能八极振动质量，或把 Bernard 的 GCM 转动惯量偏差当作实验转动惯量。
- 用单条 E3、单个宇称间距或 E1 小值排他决定静态梨形和惯量重整化。

## Falsification or Reverse Tests

1. **解耦极限：** 在脚本中令 $V\to0$，检查裸曲线只在交叉点尖峰而有限配对/频率曲线保持有界；若动态曲线仍无界，检查响应尺度实现。
2. **配对极限：** 扫描 $\Delta$，验证最小准粒子和的增加压低裸小分母响应；若趋势反转，检查矩阵元和简并因子。
3. **二维正定性：** 检查 $B_{22}>0$、$B_{33}>0$、$\det B>0$，并分别关闭 $B_{23}$ 比较大振幅周期。
4. **路径反检：** 用完整二维 $V(\beta_2,\beta_3)$ 和 $B_{ij}$ 做最小作用路径；若路径远离固定 $\beta_2$ 切片，拒绝一维周期外推。
5. **微观反检：** 对同一核素使用有限频率 QRPA/TV、粒子数投影 GCM 和扰动推转三种方案；若峰位和符号不稳定，只保留“绝热近似失效”而不保留定量发散主张。

## Open Questions

- 在同一 Gogny 或 Skyrme EDF 中，144Ba、146Ba、224Ra、226Th 是否能输出公开的二维 $B_{ij}(\beta_2,\beta_3)$ 和 2qp 贡献分解？
- 粒子数投影、配对振幅坐标和 TV 残余相互作用分别改变 $B_{33}$ 峰高多少？能否用同一有限频率响应区分它们？
- 144/146Ba 的 E3 强度相近而 E1 显著变化时，$B_{23}$ 或八极路径是否也发生可观测变化？
- 224Ra 与 226Th 的表观转动惯量、宇称间距和八极 WKB 惯量能否在同一带标签和评价版本下闭合？
- 避免交叉附近的 Landau–Zener 跃迁概率是否能解释高自旋八极带的非绝热路径，而不引入任意频率 cutoff？

## Human Review

本页为 Codex self-audit，尚未人工审核。公式中的整体因子、准粒子求和约定和 TV 响应需由熟悉具体 EDF 实现的研究者复核；来源页的实验和模型 claim 仍保持 `needs_review` 边界。Toy CSV/JSON 只证明代码路径可重复，不提升来源证据等级。

## Promotion or Rejection History

2026-10-29：创建研究笔记。接受“配对塌缩下的摄动推转小分母可产生条件性伪奇点、有限配对/频率/自洽响应可重整化”的工作命题；拒绝“所有八极避免交叉都有拓扑发散”“普通避免交叉必然使 $B_{33}$ 无穷大”和“现有论文已提供四核统一数值惯量表”的表述。已生成 `octupole-mass-tensor` 工件，运行结果含 4141 个二维网格点、80 个耦合强度点和 5 个大振幅周期点。
