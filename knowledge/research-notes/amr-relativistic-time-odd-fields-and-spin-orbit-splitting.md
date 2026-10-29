---
type: research-note
title: "CRMF反磁转动中的相对论时间奇场与自旋—轨道劈裂"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [Relativistic time-odd fields in antimagnetic rotation, CRMF AMR time-odd fields, 相对论时间奇场反磁转动]
tags: [antimagnetic-rotation, time-odd-fields, crmf, spin-orbit, dirac-equation]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 delegated CRMF time-odd-field, spin-orbit, and AMR four-blade proxy investigation
promotion_target: antimagnetic-rotation
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-first-page, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
---

# CRMF反磁转动中的相对论时间奇场与自旋—轨道劈裂

## Research Trigger

本轮问题是：反磁转动（AMR）在横向磁偶极矩相消时，为什么仍可有局域空间核子流；这些流怎样在协变密度泛函理论（CDFT）中诱发 ω、ρ 和光子空间矢量场；以及 Δh_odd 对高-$j$ 质子空穴、中子粒子、剪刀势能和 $\mathcal J^{(2)}$ 的可检验影响。用户要求一个关闭/打开时间奇场的数值对照。

现有三份指定来源支持推转平均场、双剪刀几何和 Cd 能谱/寿命观测层，但没有公开给出 $^{106,108,110}$Cd 的轨道分辨三维 CRMF 场解。因此本页把协变方程和对称性推导列为 grounded/model formalism，把计算结果列为 reduced-unit proxy；15–25% 的势能增强和 Cd 的 $\mathcal J^{(2)}$ 分担不写成实验或已发表 CRMF 结论。

## Grounded Evidence

| 主张 | 类型 | 证据与 locator | 边界 |
|---|---|---|---|
| 推转平均场使用 $h'=h-\boldsymbol\omega\cdot\mathbf J$；自洽解同时依赖形变、构型、频率和角动量取向 | model-formalism | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，PDF pp.467, 469–471 | 综述给出框架，不给本任务的轨道分辨空间场 |
| 磁/反磁转动由高-$j$ 粒子—空穴电流环和双剪刀取向产生；AMR 的两支横向磁矩在理想对称几何中相消，并与规则 $\Delta I=2$、小 $B(E2)$ 和大 $\mathcal J^{(2)}/B(E2)$ 联系 | review/model interpretation | [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]，PDF pp.487–490；[[rather-2014-104pd-antimagnetic-first-page]]，printed 061303-1 Eqs.1–2 | 这是宏观几何与模型判据，不是局域流或全带 $B(M1)=0$ 的定理 |
| $^{110}$Cd 的 16$^+$–24$^+$ 平均寿命为 0.36(3)、0.23(3)、0.17(3)、0.21(7)、0.27(7) ps，表列 $B(E2)$ 为 0.14(1)–0.06(2) $(eb)^2$ | experimental-fact | [[roy-2011-cd110-systematics-antimagnetic]]，PDF p.324 Table 1 | stopping-power 系统误差可达约20%；$1323$ 与 $1314$ keV 线接近，顶端含 effective lifetime 边界 |
| 110Cd 作者用双剪刀与核芯转动共同解释较大的惯量和缓慢的 $B(E2)$ 下降，并采用 $\mathcal J_m=19.5\,\hbar^2$/MeV | author-interpretation/model input | [[roy-2011-cd110-systematics-antimagnetic]]，PDF pp.325–326, Fig.4 | 粒子加转子参数不是裸两体矩阵元，也不等于 time-odd 场分解 |
| CDFT 空间场的结构是 $\mathbf V=g_\omega\boldsymbol\omega+g_\rho\tau_3\boldsymbol\rho+e(1-\tau_3)\mathbf A/2$，场方程空间分量由同一核子四流作源 | model-formalism | 本页由协变 Euler–Lagrange 方程写出；与 [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] 的推转框架相容 | 指定来源没有本核素的 $\omega/\rho/A$ 网格输出；需真实 CRMF 重跑才能升级为 direct numerical evidence |

“总横向磁矩为零”与“每一点局域四流为零”是两个不同命题。磁偶极矩是空间积分及等价刃相消后的结果，而时间奇场的源是点对点的 $j^i(\mathbf r)=\sum_k\bar\psi_k\gamma^i\psi_k$。文献证据支持这种分层，但不提供本页工件的参数数值。

## Provisional Reasoning

### 1. 复合离散对称性不消灭局域流

在内禀坐标中取转轴为 $z$，两对高-$j$ 刃在 $x$–$z$ 平面成镜像排列。对空间矢量四流 $\mathbf j$，时间反演给 $T:\mathbf j\mapsto-\mathbf j$；绕 $y$ 轴转 $\pi$ 给 $R_y(\pi):(j_x,j_y,j_z)\mapsto(-j_x,j_y,-j_z)$（坐标同时作同一旋转）。因此复合操作 $S=R_y(\pi)T$ 在回到同一内禀坐标后允许

$$
S:\ (j_x,j_y,j_z)\mapsto(j_x,-j_y,j_z).
$$

保留 $S$ 的平面解可有 $j_x$ 和 $j_z$ 的非零局域分量；它只迫使反对称分量（例如取决于 $j_y$ 的部分）满足相应奇偶约束。对称的两刃贡献其横向磁矩

$$
\mu_\perp\propto\int d^3r\,[\mathbf r\times\mathbf j(\mathbf r)]_\perp
$$

在全空间积分后相消，但这不推出 $\mathbf j(\mathbf r)=0$。只要在某个开集 $\Omega$ 内 $\mathbf j\ne0$，有限程 Green 函数

$$
(-\nabla^2+m_a^2)\,a_i(\mathbf r)=g_a j_i(\mathbf r)
$$

就一般给出 $a_i(\mathbf r)\ne0$。只有逐点源恒为零，或发生精确的非局域抵消，才会使全部空间矢量场恒为零。

### 2. CDFT/CRMF 中的时间奇 Dirac 项

采用与本地 CRMF 研究笔记一致的度规和符号约定，旋转系单粒子方程写成

$$
h'\psi_k=\epsilon'_k\psi_k,
\quad h'=\boldsymbol\alpha\cdot[-i\boldsymbol\nabla-\mathbf V(\mathbf r)]+\beta[m+S(\mathbf r)]+V^0(\mathbf r)-\boldsymbol\omega\cdot\mathbf J.
$$

其中

$$
\mathbf V=g_\omega\boldsymbol\omega+g_\rho\tau_3\boldsymbol\rho+e\frac{1-\tau_3}{2}\mathbf A,
\qquad
\mathbf j_D=\sum_{k\in occ}\bar\psi_k\boldsymbol\gamma\psi_k.
$$

于是时间奇空间场进入

$$
\boxed{\Delta h_{\rm odd}=-\boldsymbol\alpha\cdot\mathbf V(\mathbf r)}.
$$

这里采用标准 Dirac Hamiltonian 约定；若从协变拉格朗日量写成 $\bar\psi\gamma^\mu V_\mu\psi$，则 $\beta\boldsymbol\alpha=\boldsymbol\gamma$，把空间项搬到 Hamiltonian 后就是上述 $-\boldsymbol\alpha\cdot\mathbf V$。某些文献把 $\beta$ 留在协变算符记号中，不能在未说明表示和度规的情况下直接把两种写法相减。

若采用相反的度规或把协变势定义成 $-\mathbf V$，整项会变号；可观测的自洽能量和流必须在同一约定中计算，不能仅凭字面正负号比较不同程序。

在弱场、正能投影下，消去 Dirac 小分量可得到熟悉的静态自旋—轨道基线

$$
H_{so}^{(0)}\simeq \frac{1}{2M_*^2r}\frac{d(V^0-S)}{dr}\,\mathbf l\cdot\mathbf s,
\qquad M_*=m+S-V^0,
$$

而 $-\boldsymbol\alpha\cdot\mathbf V$ 通过动量替换和自洽波函数改变其一阶矩阵元、轨道占据以及 $M_*$ 和密度梯度。对一个未简并的轨道 $a$，一阶动态修正为

$$
\delta\epsilon_a^{odd}=\langle a|-\boldsymbol\alpha\cdot\mathbf V|a\rangle.
$$

因此质子和中子自旋—轨道差的修正分别是

$$
\delta\Delta_{so}^{(p)}=\delta\epsilon_{g_{7/2}}-\delta\epsilon_{g_{9/2}},\qquad
\delta\Delta_{so}^{(n)}=\delta\epsilon_{h_{11/2}}-\delta\epsilon_{h_{9/2}}.
$$

这两个式子是可计算定义；它们不是由 AMR 对称性决定的固定符号。空穴的能量解释还需保持“空穴能”与“被移走的粒子能”约定一致。

### 3. 数值工件和局域—整体对照

`workers/amr-time-odd-fields/amr_time_odd_fields.py` 在 $x$–$z$ 网格上用无散流函数生成四个镜像 Gaussian 环流，再用有限程 Yukawa 核求解 omega、rho 和 photon 的 reduced response。计算结果（$\theta=45^\circ$）为：

| 量 | proxy 结果 | 解释 |
|---|---:|---|
| 质子对的积分横向磁矩 | $0$ | 镜像刃的数值相消 |
| 中子对的积分横向磁矩 | $1.1\times10^{-15}$ | 浮点误差量级 |
| 总积分横向磁矩 | $1.4\times10^{-16}$ | 浮点误差量级 |
| 局域总流 RMS | $2.22\times10^{-2}$ | reduced grid units，非实验流密度 |
| 局域总矢量场 RMS | $6.49\times10^{-2}$ | reduced field units |

因此工件直接展示了“全局磁矩相消、局域流和场非零”的逻辑。接近闭合的 $1^\circ$ 对照中局域流 RMS 降到 $1.39\times10^{-3}$，说明该结果依赖镜像刃间距；它不是“任意 AMR 态局域流都必然同样强”的定量定理。

### 4. g9/2、h11/2 和自旋—轨道代理劈裂

在 45° 参考构型下，代码把 $-\boldsymbol\alpha\cdot\mathbf V$ 的局域期望写入 `level_shifts.csv`。结果为：

| 轨道/代理 | $\epsilon_{off}$ (MeV) | $\delta\epsilon_{odd}$ (MeV) | $\epsilon_{on}$ (MeV) |
|---|---:|---:|---:|
| proton $g_{9/2}$ hole | −3.200 | −0.0705 | −3.2705 |
| proton $g_{7/2}$ comparator | −1.100 | +0.0705 | −1.0295 |
| neutron $h_{11/2}$ particle | +0.800 | +0.0705 | +0.8705 |
| neutron $h_{9/2}$ comparator | +2.100 | −0.0705 | +2.0295 |
| proton spin–orbit proxy | 2.100 | +0.1410 | 2.2410 |
| neutron spin–orbit proxy | −1.300 | +0.1410 | −1.1590 |

这些 MeV 数值是人为归一化的 reduced expectation，不是某个已发表 CDFT 参数组的单粒子谱。它们展示了一个重要的可检验接口：同一个空间场对镜像轨道可产生相反一阶矩阵元，所以不能只给总磁矩而不输出轨道分辨的 $\bar\psi\gamma^i\psi$ 和能量差。

### 5. 剪刀张力和 15–25% 结果的准确含义

代码使用

$$
U_{off}(\theta)=V_2\sin^2\theta,
\qquad U_{on}(\theta)=U_{off}(\theta)[1+\eta(\theta)],
$$

并令 $\eta=0.20[0.75+0.25\,||\mathbf V||/||\mathbf V||_{45^\circ}]$。默认扫描给出 `enhancement_percent=16.95–20.28%`；另外显式扫描 15%、20%、25% 三个敏感性点。这个构造表达“时间奇场反馈可提高有效对准刚度”的研究假设，但 $\eta$ 是现象学闭合参数，不是由三份来源唯一确定的相对论场结果。

真正的 CRMF 检验应以同一组态的总能量曲率

$$
K_\theta=\left.\frac{\partial^2 E_{\rm CRMF}(\theta)}{\partial\theta^2}\right|_{\theta_0}
$$

比较 fully self-consistent 与 frozen time-odd 解，并同时固定配对、阻塞、网格、参数化和频率。只有在这些差分稳定时，才可把 15–25% 从 proxy 语言升级为特定参数化的模型结果。

### 6. 106, 108, 110Cd 的 $\mathcal J^{(2)}$ 对账

代码依照

$$
\mathcal J^{(2)}=\frac{4}{E_\gamma(I+2\to I)-E_\gamma(I\to I-2)}
$$

从本地 Cd 能量账本逐差分计算正值中位数，并保留 110Cd 的 1323/1314 keV 近重合导致的负有限差分。随后用 reduced response ansatz 比较 time-odd off/on：

| 核素 | $J^{(2)}_{off}$ proxy | $J^{(2)}_{on}$ proxy | 变化 | 实验正值中位数 |
|---|---:|---:|---:|---:|
| $^{106}$Cd | 22.50 | 25.15 | +11.76% | 22.60 |
| $^{108}$Cd | 22.50 | 25.37 | +12.76% | 22.47 |
| $^{110}$Cd | 42.00 | 47.78 | +13.76% | 65.66 |

实验中 $^{110}$Cd 的有限差分正值中位数受非规则能级间隔影响，不能被解释为一个稳定平台。表中 on/off 差值是场响应场景的定量输出，不是从寿命或能谱中唯一分离出的 time-odd 贡献；Roy 的直接实验量是寿命和 $B(E2)$，不是这种分解。

## Assumptions

- 四流在内禀 $x$–$z$ 切片由无散 Gaussian stream function 代理；没有三维自洽 Dirac 自旋or、密度和配对场。
- omega、rho、photon 采用周期盒 Fourier Yukawa response；耦合、质量、$V_2$ 和 $\alpha$ 尺度均为可见的 reduced parameters。
- g9/2 hole、h11/2 particle 只用局域密度与流向构造一阶矩阵元；比较轨道的基线能量为模型输入。
- `U_on/U_off` 与 `J2_on/J2_off` 使用现象学 response ansatz；没有把其百分比误写成实验误差或 published CRMF output。
- no-sea CDFT 的真空极化不拆成逐负能轨道流；代码也没有“Dirac 海”列。

## Competing Explanations

- $B(E2)$ 平缓下降和较大 $\mathcal J^{(2)}$ 可由核芯转动、频率依赖形变、配对重排、组态交叉或 side feeding 共同造成，不必由 time-odd 场单独解释。
- 单粒子劈裂的变化可能来自标量—时间分量、有效质量、张量耦合、构型混合和普通 Coriolis 项；$-\alpha\cdot V$ 的一阶代理不能单独识别它们。
- $\mu_\perp=0$ 只约束理想等价刃的期望值。刃长度、有效 $g$ 因子、配置混合或对称性破缺会恢复有限横向矩阵元，但不自动否定 AMR。
- 110Cd 的异常有限差分不应被强行归因于 time-odd 场；原 Table 1 已有线重叠和 effective lifetime 边界。

## Transfer Conditions

该结果可迁移到真实 CRMF/TAC-CDFT 的必要条件是：同一协变参数化和配对方案；明确 blocked configuration、轴排序、$\hbar\omega$ 和三维盒；逐轨道输出 $\bar\psi\gamma^i\psi$、$\omega_i$、$\rho_i$ 和 $A_i$；对 frozen time-odd 与 fully self-consistent 解计算同一 $E(\theta)$、$\mathcal J^{(1,2)}$、$B(E2)$ 和绝对 $B(M1)$；最后回到寿命、分支、ICC、DCO/偏振的共同实验合同。

## Failure Conditions

- 把本页 16.95–20.28% 或 15–25% sensitivity scan 写成 Cd 的已发表 CRMF 结果。
- 把 `level_shifts.csv` 的 0.0705 MeV 或 0.1410 MeV 写成实测 g9/2、h11/2 单粒子能级移动。
- 用全局 $\mu_\perp=0$ 推出局域 $j^i(\mathbf r)=0$、所有 M1 矩阵元恒为零或所有 vector field 恒为零。
- 把 110Cd 的负有限差分或 65.66 的正值中位数称作稳定实验惯量平台。
- 把 no-sea 参数化和显式 Dirac 海流混写，或把场的符号约定当作可跨程序直接比较的物理符号。

## Falsification or Reverse Tests

1. 在同一三维 CRMF 构型中逐点积分每个轨道的 $j^i$；若 fully self-consistent 解的局域流在网格收敛后消失，撤回“time-odd field 必非零”的具体构型断言。
2. 逐步关闭 $g_\omega$、$g_\rho$ 和电磁空间分量；若轨道能级和 $E(\theta)$ 曲率变化低于数值误差，time-odd 场不是主要重整化源。
3. 改变轴排序、盒边界、网格和 Yukawa 范围；若 15–25% 只在单一 reduced 参数下出现，保留为 proxy sensitivity。
4. 对 $^{106,108,110}$Cd 同时拟合绝对寿命导出的 $B(E2)$、能级频率、alignment 和配置角；若 on/off 场差不能改善共同拟合，撤回“增强核芯对准刚度”的归因。
5. 将 time-odd correction 与标量场、Coriolis、配对和张量项逐一正交化；若 g9/2/h11/2 的劈裂符号随这些控制改变，禁止给出普适符号。
6. 对 110Cd 的 1323/1314 keV 线使用完整门控协方差和 feeding 模型；若差分平台消失，撤回由有限差分异常提出的动力学解释。

## Open Questions

- 是否存在公开的 $^{106,108,110}$Cd CRMF/TAC-CDFT 三维轨道分辨空间流、$omega/\rho/A$ 场和 frozen-time-odd 对照？
- 在同一协变参数化中，$-\alpha\cdot V$ 对 proton $g_{9/2}$ hole 和 neutron $h_{11/2}$ particle 的效应如何与标量场、张量耦合和配对重排分离？
- 真实四叶片构型中时间奇场对 $K_\theta$ 的响应是否仍落在 15–25%，还是随 $\gamma$、频率和占据发生符号变化？
- 106/108/110Cd 的 $\mathcal J^{(2)}$ 平台应由哪一组原始 $E_\gamma$、side feeding 和寿命协方差共同约束？
- no-sea 参数化中的真空极化如何与显式正能核芯极化在轨道分辨流账本中定义兼容的 observable？

## Human Review

页面保持 `review_status: unreviewed`。人工复核优先检查：复合对称性对四流分量的坐标约定；$\Delta h_{odd}$ 的度规符号；空穴能量的符号解释；三份指定来源能否支持迁移到具体 Cd CRMF 构型；以及是否允许把“15–25%”保留为模型敏感性而非物理结论。当前 self-audit 不等于 `human-reviewed`，也不改变指定 source 页的 review 状态。

## Promotion or Rejection History

2026-10-29：建立 provisional research note。完成三层分离：指定来源的推转/AMR/Cd grounded evidence；CDFT 四流—空间矢量场—Dirac 项的 formal derivation；以及 `amr-time-odd-fields` reduced-unit proxy。局域流与全局磁矩相消通过镜像流场数值对照；轨道劈裂、15–25% 刚度带和 Cd $\mathcal J^{(2)}$ on/off 分担均保留为 `our-inference`/model sensitivity，尚未晋升为正式 CDFT model 或实验 synthesis。
