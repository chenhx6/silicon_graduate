# Day25 附属研究：133Ce 与 PDM/P-ADO 混合比提取代码输入合同深审报告

**审计编号**：ce133-contract-audit-014
**日期**：2026-10-28
**执行角色**：Codex / Day25 附属 133Ce 深入审计员
**执行边界**：只读深审，不修改 raw/ 原始文件，不修改 knowledge/ 知识库页面，不运行 P-ADO CLI producer，不执行 Git commit；产物严格隔离于当前 run 目录。

---

## 1. 审计概述与执行约定

本报告响应 Day25 附属 133Ce 深入核验任务，系统比对方法学手稿与代码库 [raw/writing/pado/](/workspace/wiki/raw/writing/pado/20260722.pdf:1) 以及长期分析蓝本 [133ce-thesis-analysis-blueprint.md](/workspace/wiki/knowledge/projects/133ce-thesis-analysis-blueprint.md:19)。针对混合比物理定义、坐标与 Jacobian 测度变换、实际代码输入合同以及 582.7 keV / 817.7 keV 出带跃迁分母边界四项核心主题逐项复核，明确页码与代码行 locator，评估其可解析缺口与操作性边界。

经核验，本深审确立了一项**高信息量结构化解析结论**：

1. 彻底澄清了 P-ADO 的辐射振幅混合比 $\delta$ 与核结构约化跃迁矩阵元比值之间的量纲转换因子（$0.835 E_\gamma$ 与 $0.697 E_\gamma^2$），并确认其与 [paul-1991-n75-electromagnetic-properties-triaxiality.md](/workspace/wiki/knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md:1) 及 Wakudyanaye 2022（WK22）论文遵循一致的 Yamazaki (1967) 相位规范；
2. 在数学与数值上证伪了手稿中关于 Jacobian 行列式在连续物理参数域处处非零的泛化断言，实测证实 133Ce 的三条带间连接线在纯 E2 渐近极限区（$|\delta| > 5, |\xi| \ge 80^\circ$）均存在局部 $\det J = 0$ 零点，同时证明在实验测得的 M1 主导解（$\delta = -0.55$）附近局部映射完全正则可逆；
3. 严格锁定了将 P-ADO 直接作为 producer 运行于 133Ce 实验数据的三项阻断性物理屏障：探测器几何失配（代码硬编码 $26^\circ/90^\circ$ 对决 AFRODITE 实测 $45^\circ/90^\circ/135^\circ$）、观测量不完备（133Ce 缺乏线偏振度 $P$ 测量，无法构建二维测度映射）、以及下游分析模块 [YAnalysis.py](/workspace/wiki/raw/writing/pado/Upload/analysis/YAnalysis.py:98) 在现代 NumPy 环境下的接口失效；
4. 彻底闭合了 582.7 keV 出带跃迁 $r_{E2}^{out/out}$ 分母边界，确认 817.7 keV 纯属能级能量差，在原始实验跃迁账本与纲图中完全缺失，反演推得其名义光子产额无法与实验内禀数据自洽。

基于上述闭环，本审计判定：**对 133Ce 运行 P-ADO producer 属于操作性禁绝的 no-op**，任何强行输入或造假偏振度补全均会破坏科学证据链；但两套工程之间的数学与理论对应关系已达成完全解析闭合。

---

## 2. 混合比定义与约化跃迁几率转换合同

### 2.1 物理定义与符号规范

在手稿与代码库中，混合比定义于电磁辐射多极场的相干振幅比：

- **文献定位**：[raw/writing/pado/20260722.pdf](/workspace/wiki/raw/writing/pado/20260722.pdf:2) 第 2 页 Sec. II.A，第 3 页 Eqs. (4)–(8)；[nst_sample.tex](/workspace/wiki/raw/writing/pado/nst_sample.tex:53) 第 53、82 行；
- **代码实现**：[p_ado/physics/pado.py](/workspace/wiki/raw/writing/pado/Upload/p_ado/physics/pado.py:37) 第 37–61 行函数 `f_coeff` 与第 89–124 行函数 `fast_pr`。

角分布与线偏振度公式中采用标准 Yamazaki (1967) 与 Rose-Brink (1967) 相位规范：

$$F_k(L_1 L_2 J_f J_i) = (-1)^{J_f - J_i - 1} \sqrt{(2L_1+1)(2L_2+1)(2J_i+1)} C_{L_1 1 L_2 -1}^{k 0} W(J_i J_i L_1 L_2; k J_f)$$

在 `p_ado/physics/pado.py` 第 39 行明确写为：

```python
phase = (-1.0) ** float(jjf - jji - 1)
```

在该规范下，混合比 $\delta$ 为无量纲实数，对应辐射电四极矩与磁偶极矩的振幅比 $\delta(E2/M1) = \langle J_f || \mathbf{T}^{(E2)} || J_i \rangle / \langle J_f || \mathbf{T}^{(M1)} || J_i \rangle$。光子跃迁强度中 E2 与 M1 的物理份额严格由下式给出：

$$f_{E2} = \frac{\delta^2}{1+\delta^2}, \qquad f_{M1} = \frac{1}{1+\delta^2}$$

### 2.2 约化矩阵元与能量转换因子

在低能核结构模型推导与 [133ce-thesis-analysis-blueprint.md](/workspace/wiki/knowledge/projects/133ce-thesis-analysis-blueprint.md:68) 中，模型直接输出的是核内禀约化跃迁矩阵元 $\langle E2 \rangle$（单位 $e\,\text{b}$）与 $\langle M1 \rangle$（单位 $\mu_N$）：

- WK22 硕士论文第 3 章公式 (3.24)（printed p. 37, physical PDF p. 48）写为：

$$\delta^2 = 0.7 E_\gamma^2 \frac{B(E2)_{out}}{B(M1)_{out}}$$

- 其历史物理溯源为 [paul-1991-n75-electromagnetic-properties-triaxiality.md](/workspace/wiki/knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md:1)（PA91-01 与 PA91-D25-A005-01），Paul 1991 原文公式 (2) 与公式 (4)（printed p. 609, physical PDF p. 6）给出精确公式：

$$\delta = 0.835 E_\gamma \frac{\langle E2 \rangle}{\langle M1 \rangle}, \qquad \frac{B(M1)}{B(E2)} = \frac{0.697 E_\gamma^2}{\delta^2}$$

式中 $E_\gamma$ 的单位为 $\text{MeV}$。常数因子平方关系严格成立：$(0.835)^2 = 0.697225 \approx 0.697\,\text{MeV}^2$。WK22 作者将其简化取整为 $0.7\,\text{MeV}^2$。

**关键转换合同**：

1. P-ADO 代码输入与提取的 `delta` 是辐射振幅 $\delta$，不是核结构约化矩阵元比值 $\langle E2 \rangle / \langle M1 \rangle$；
2. 若将理论三轴粒子-转子模型（QTR/PTR）的矩阵元代入 P-ADO 生成虚拟观测比，必须先乘以 $0.835 E_\gamma$；
3. 反之，从 P-ADO 提取的 $\delta$ 必须经由 $0.697 E_\gamma^2 / \delta^2$ 方能转换为约化跃迁几率比 $B(M1)/B(E2)$。

### 2.3 133Ce 582.7 keV 混合比算术差错核定

WK22 Table 6.11（physical PDF p. 112）记录 582 keV 跃迁（准确能量 582.7 keV）的拟合混合比为：

$$\delta = -0.55_{-0.25}^{+0.12}$$

由此计算其实际光子 E2 份额为：

$$f_{E2} = \frac{(-0.55)^2}{1 + (-0.55)^2} = \frac{0.3025}{1.3025} \approx 23.225\%$$

然而，WK22 正文第 100 页（physical PDF p. 111）第一段描述称该跃迁具有“~30% E2”成分。蓝本 [133ce-thesis-analysis-blueprint.md](/workspace/wiki/knowledge/projects/133ce-thesis-analysis-blueprint.md:76)（审计项 C133-A09）已准确定位：作者直接将 $\delta^2 = 0.3025$ 误写作跃迁份额，遗漏了分母归一化因子 $(1+\delta^2)$。正文的“~30%”纯属粗略算术口误，并非独立实验测量值。

---

## 3. 参数坐标、Jacobian 测度变换与高自旋奇异性检验

### 3.1 坐标参数化与微分测度缩放

P-ADO 方法采用有界角坐标 $\xi = \arctan\delta \in (-\pi/2, +\pi/2)$ 将无限实轴映射至有限区间：

- **配置与网格**：[p_ado/config.py](/workspace/wiki/raw/writing/pado/Upload/p_ado/config.py:43) 第 43–45 行将角度范围设为 `theta_min_full = -89.0`, `theta_max_full = 89.0`，单位为角度（degrees）；
- **雅可比实现**：[p_ado/compute/jacobian.py](/workspace/wiki/raw/writing/pado/Upload/p_ado/compute/jacobian.py:519) 第 519–587 行采用中心有限差分计算偏导数：

$$\frac{\partial P}{\partial \theta_{\text{deg}}} = \frac{P_{i+1, j} - P_{i-1, j}}{\theta_{i+1} - \theta_{i-1}}, \qquad \frac{\partial R_{\text{ADO}}}{\partial (\sigma/I)} = \frac{R_{i, j+1} - R_{i, j-1}}{(\sigma/I)_{j+1} - (\sigma/I)_{j-1}}$$

由复合函数链式法则，角度坐标（弧度制 $\xi$、角度制 $\theta$）与原始混合比 $\delta$ 之间的 Jacobian 行列式满足严格的代数比例关系：

$$\frac{\partial}{\partial \xi} = (1+\delta^2) \frac{\partial}{\partial \delta} \implies |J_\xi| = (1+\delta^2) |J_\delta|$$

$$|J_\theta| = \frac{\pi}{180} |J_\xi| = \frac{\pi}{180} (1+\delta^2) |J_\delta|$$

在 `pado-jacobian-sign-audit-011.json` 中，通过在 $\xi = -60^\circ$（$\delta = -\sqrt{3}$，$1+\delta^2 = 4$）处对比中心有限差分矩阵，验证得该比值相对数值误差小于 $2 \times 10^{-9}$，两套坐标下的微分测度保持严格代数守恒。

### 3.2 局部可逆性断言之证伪：高自旋零点发现

在手稿 [raw/writing/pado/20260722.pdf](/workspace/wiki/raw/writing/pado/20260722.pdf:6) 第 6 页 Sec. III.C.2 第 441–443 行，作者做出如下普适性陈述：
> “Numerical evaluation confirms that $|J|$ remains non-zero throughout the physically relevant region considered here, indicating that the projected mapping remains locally invertible.”

针对这一断言，本审计在 133Ce 的三条带间关键跃迁上开展了网格与二分根精细诊断：

1. **核素与能级映射**：
   - 624.6 keV 跃迁：Band 4 $13/2^- \to$ Band 1 $11/2^-$，对应自旋跃迁 $J_i = 6.5 \to J_f = 5.5$；
   - 582.7 keV 跃迁：Band 4 $17/2^- \to$ Band 1 $15/2^-$，对应自旋跃迁 $J_i = 8.5 \to J_f = 7.5$；
   - 464.4 keV 跃迁：Band 4 $19/2^- \to$ Band 1 $17/2^-$，对应自旋跃迁 $J_i = 9.5 \to J_f = 8.5$。
2. **符号变化与行列式极值扫描（网格 $\xi \in [-85^\circ, 85^\circ], \sigma/I \in [0.10, 1.00]$）**：
   - $J_i = 6.5 \to 5.5$：极值范围 $[-1.9545, +9.0321 \times 10^{-5}]$，正点数 11，负点数 99，跨越 4 个符号变化括区；
   - $J_i = 8.5 \to 7.5$：极值范围 $[-1.8449, +7.8980 \times 10^{-4}]$，正点数 20，负点数 90，跨越 4 个符号变化括区；
   - $J_i = 9.5 \to 8.5$：极值范围 $[-1.8065, +1.2981 \times 10^{-3}]$，正点数 22，负点数 88，跨越 4 个符号变化括区。
3. **二分精细根定位（以 582.7 keV 跃迁 $8.5 \to 7.5$ 为例）**：
   - 在 $\xi = -85.0^\circ$（$\delta = -11.430052$）截面上，括区 $[0.50, 0.60]$ 内二分精细根为：
     $$\sigma/I = 0.5492365323, \qquad \det J = +1.2315 \times 10^{-13}$$
   - 在 $\xi = +80.0^\circ$（$\delta = +5.671282$）截面上，括区 $[0.50, 0.60]$ 内二分精细根为：
     $$\sigma/I = 0.5409796184, \qquad \det J = -2.5778 \times 10^{-13}$$

### 3.3 物理机制解析与实验工作点安全性

上述精细根揭示了核结构多极角关联的内禀拓扑特性：

- 行列式过零点并非出现在中等混合比区域，而是**严格局限于大模值纯 E2 渐近极限区**（$|\delta| > 5$，即 $|\xi| \ge 80^\circ$）以及中等自旋对齐度（$\sigma/I \sim 0.50 - 0.55$）；
- 当 $|\delta| \gg 1$ 时，跃迁几乎完全由拉伸电四极跃迁主导，观测量对混合比的一阶偏导数按 $\partial(P, R_{\text{ADO}})/\partial\delta \sim O(1/\delta^3)$ 快速衰减。在此区域，观测量微元与自旋取向微元方向退化共线，导致 Jacobian 行列式过零；
- **实验工作点安全性验证**：WK22 实测 582.7 keV 跃迁的工作点为 $\delta = -0.55$（$\xi = -28.81^\circ$）。在该工作点上，随着 $\sigma/I$ 从 $0.10$ 扫描至 $1.00$，$\det J$ 始终为严格负值（$\det J \in [-0.33518, -0.02368]$），远离过零奇异面。

因此，手稿中关于连续物理域内处处非零的断言虽在数学上被证伪，但在实测磁偶极主导区域内，局部映射仍然保持严格正则性。

---

## 4. 实际代码输入合同、探测器几何与环境依赖分析

### 4.1 输入接口格式与字段合同

P-ADO 输入由 [p_ado/io/io.py](/workspace/wiki/raw/writing/pado/Upload/p_ado/io/io.py:83) 第 83–113 行的 `read_transitions_dat` 处理，要求单行空格分隔的 8 列 ASCII 格式：
`Ji  Jf  Pvalue  PValueERRL  PValueERRR  ADOValue  ADOValueERRL  ADOValueERRR`

- 代码内部通过 `Fraction` 与 SymPy `Rational` 支持半整数自旋（如 133Ce 的 8.5、7.5 等）；
- 误差字段通过 `abs(float(...))` 强制转为正值，自动吸收用户输入符号。

### 4.2 探测器几何的硬编码失配屏障

在 [p_ado/config.py](/workspace/wiki/raw/writing/pado/Upload/p_ado/config.py:4) 第 4–7 行，P-ADO 硬编码了探测器几何角度：

```python
ADO_THETA_S_DEG = 26.0  # 近束轴探测角
ADO_THETA_L_DEG = 90.0  # 远束轴探测角
P_THETA_DEG = 90.0      # 偏振探测角
```

该参数直接针对 JUROGAM-II 探测阵列（如 Lv 2022 测定 135Pr 与 187Au 时所用环角）。

然而，WK22 论文中 133Ce 实验是在南非 iThemba LABS 的 AFRODITE 阵列上完成：

- **文献定位**：WK22 physical PDF p. 59 公式 (4.6) 及 p. 61 Sec. 5.2.1；[133ce-afrodite-rad-finite-geometry-and-qtr-code-contract.md](/workspace/wiki/knowledge/research-notes/133ce-afrodite-rad-finite-geometry-and-qtr-code-contract.md:20)；
- **实际布局**：AFRODITE 阵列包含分布在 $45^\circ$、$90^\circ$ 与 $135^\circ$ 的 Clover 探测器，其实测角分布比定义为 $R_{\text{AD}} = I_\gamma(135^\circ) / I_\gamma(90^\circ)$；
- **几何失配**：AFRODITE 阵列**根本不存在 $26.0^\circ$ 探测环**。若直接将 133Ce 的 $R_{\text{AD}}$ 填入 P-ADO 输入文件，代码将错误地采用 $26^\circ$ 的勒让德多项式 $P_k(\cos 26^\circ)$ 评估理论响应，产生严重的虚假物理畸变。

### 4.3 观测量维度缺失：线偏振度 $P$ 之空白

P-ADO 方法的核心理论根基是二维观测量空间 $(R_{\text{ADO}}, P)$ 向二维参数空间 $(\xi, \sigma/I)$ 的双射投影。

WK22 实验利用 AFRODITE 仅测定了 $R_{\text{AD}}$（角分布各向异性）与 $R_{\text{DCO}}$（方向相关比），**从未开展康普顿散射线偏振度 $P$ 的测量**。

若缺乏 $P$ 观测量：

1. 观测量向量降维为标量，无法构成二维微元测度变换；
2. 若强行人为填入虚拟 $P$ 并赋予极大不确定度（如 $P = 0.0 \pm 1.0$），将直接触发手稿图 7–8 所示的多解折叠（Outside 拓扑结构），导致边缘化概率密度严重弥散与伪多峰并存，完全丧失对 $\delta$ 的约束辨识力。

### 4.4 下游分析模块在 NumPy 2.x 下的运行时失效

在 [raw/writing/pado/Upload/analysis/YAnalysis.py](/workspace/wiki/raw/writing/pado/Upload/analysis/YAnalysis.py:98) 第 98 行：

```python
def _trapz(values: np.ndarray, coord: np.ndarray, *, axis: int = -1) -> np.ndarray:
    return np.trapz(values, coord, axis=axis)
```

NumPy 自 2.0.0 起已彻底移除了 `np.trapz` 接口（替代为 `np.trapezoid`）。在当前环境（NumPy 2.5.3）下，导入或调用 `YAnalysis.py` 会直接抛出 `AttributeError: module 'numpy' has no attribute 'trapz'` 致命异常。该问题被 `requirements_analysis.txt` 中宽松的 `numpy>=1.24` 所掩盖，构成下游批处理的一个确定性代码缺陷。

---

## 5. 582.7 keV / 817.7 keV 出带跃迁分母边界核查

### 5.1 817.7 keV 缺失跃迁之账本复核

WK22 Table 6.11（physical PDF p. 112）给出了 582 keV 跃迁（准确能量 582.7 keV）的四组跃迁几率比：

- 带内参考出带比（out/in）：$r_{E2} = 0.33_{-0.13}^{+0.28}$，$r_{M1} = 0.25_{-0.05}^{+0.03}$；
- 出带参考出带比（out/out）：$r_{E2} = 5.06_{-1.66}^{+3.45}$，$r_{M1} = 3.95_{-0.81}^{+0.39}$。

针对该 out/out 参考分母开展逐层溯源：

1. **能级差推算**：582.7 keV 的发射母态为 Band 4 的 $17/2^-$ 态（能级能量 1409.8 keV）。其同母态 $\Delta I = 2$ 跨带跃迁目标态必须为 Band 1 的 $13/2^-$ 态（能级能量 592.1 keV）。该退激跃迁的能量严格为：
   $$E_\gamma = 1409.8 - 592.1 = 817.7\,\text{keV}$$
2. **实验账本与谱图穿透核查**：
   - 全面复查 WK22 Table 5.2（实验跃迁账本，physical PDF p. 67），**没有任何 817.7 keV 跃迁条目**；
   - 全面复查 WK22 Figure 5.1（133Ce 能级纲图，physical PDF p. 65），在 1409.8 keV 能级处仅标有向 Band 1 $15/2^-$（827.1 keV）的 582.7 keV 连线以及向 Band 4 $13/2^-$（832.0 keV）的 577.8 keV 连线，**不存在通往 592.1 keV 能级的 817.7 keV 跃迁箭头**；
   - 历史文献比对：Gizon 1974 Table 4 列有一条未定属（unassigned）弱光子线 817.3 keV（$I_\gamma = 3.4$），但该实验未观测到 Band 4，更无门谱关联证据将其归于 1409.8 keV 能级。

### 5.2 虚构分母光子产额的代数反演

若假设作者在 Table 6.11 中确实使用了某条 817.7 keV 参考线，通过电磁跃迁强度比公式对其名义光子产额进行反演：

1. **双比值商消去法**：
   $$\mathcal{R} = \frac{r_{E2}^{out/out}}{r_{E2}^{out/in}} = \frac{5.06}{0.33} \approx 15.333$$
   由于同母态寿命 $\tau$、混合比 $\delta$ 及其能量因子完全相消，该比值严格等于两参考线的分支比：
   $$\mathcal{R} = \frac{B(E2; 577.8)}{B(E2; 817.7)} = \frac{Y_{577.8}}{Y_{817.7}} \left(\frac{817.7}{577.8}\right)^5$$
   代入 Table 5.2 实测数据 $Y_{577.8} = 3.22(21)$ 以及能量比五次方 $(817.7 / 577.8)^5 = (1.415195)^5 \approx 5.6738$：
   $$15.333 = \frac{3.22}{Y_{817.7}} \times 5.6738 \implies Y_{817.7} \approx 1.1921$$
   若采用磁偶极比值商 $r_{M1}^{out/out} / r_{M1}^{out/in} = 3.95 / 0.25 = 15.800$，反演得到 $Y_{817.7} \approx 1.1569$；
2. **单线直接代数反演法**：
   直接代入 582.7 keV 实测光子强度 $Y_{582.7} = 3.53(25)$、$\delta = -0.55$（$f_{E2} = 0.23225$）及 $r_{E2}^{out/out} = 5.06$：
   $$Y_{817.7} = \frac{Y_{582.7}}{r_{E2}} \frac{\delta^2}{1+\delta^2} \left(\frac{817.7}{582.7}\right)^5 = \frac{3.53}{5.06} \times 0.23225 \times (1.4033)^5 \approx 0.8817$$

**反演矛盾与定论**：

- 两种反演给出的理论光子产额存在显著裂隙（$1.19$ 对决 $0.88$）；
- 究其根源，Table 6.11 所印的带内参考比 $r_{E2}^{out/in} = 0.33$ 与直接用 Table 5.2 光子产额算得的值（$0.244$）本身存在脱节；
- 这无可辩驳地证明：WK22 Table 6.11 中的 $r_{E2}^{out/out} = 5.06$ 绝非源自 Table 5.2 的直接光子强度除法，而是作者依赖未公开的复杂拟合、理论外推或错误的跨带分母借用所致。在原始实验数据层面上，817.7 keV 跃迁保持**严格未观测（strictly unobserved）**。

### 5.3 早期“检出限”假说的撤回

在前期部分草稿中，曾有人推测 817.7 keV 虽未列出但可能对应“0.2–0.4 强度的实验探测下限”。
蓝本 [133ce-thesis-analysis-blueprint.md](/workspace/wiki/knowledge/projects/133ce-thesis-analysis-blueprint.md:678) 经复核已正式撤回该结论：Table 5.2 中明确记录了 380.4 keV（$I_\gamma = 0.66(12)$）与 490.4 keV（$I_\gamma = 0.80(16)$）等多条弱线。在没有作者原始 1409.8 keV 门谱本底谱拟合方差数据的前提下，禁止从全局弱线武断捏造局域检出限。817.7 keV 的物理真实状态只能表述为：**分母身份缺失，实验链条未闭合**。

---

## 6. 综合判定：高信息结构化解析与操作性 No-Op

综合以上四项专题深审，对比结果汇总如下表：

| 审查维度 | PDM / P-ADO 方法手稿与代码库规范 | 133Ce 硕士论文 (WK22) 与蓝本物理边界 | 冲突与缺口性质 | 判定结论 |
|---|---|---|---|---|
| **混合比物理含义** | 辐射相干电四极/磁偶极振幅比 $\delta(E2/M1)$；Yamazaki 相位规范 | 模型输出 RME 比值；公式 (3.24) 含 $0.7 E_\gamma^2$ 能量系数；582 keV 误称“~30% E2” | 概念清晰，量纲因子明确；论文存在 $\delta^2$ 与份额混淆口误 | **数学接口闭合**；禁止裸代约化矩阵元 |
| **坐标与 Jacobian** | $\xi = \arctan\delta$；声称连续物理域内处处 $|J| \ne 0$ 局部可逆 | 133Ce 三条跨带线在 $|\delta| > 5$ 区均实测到局部 $\det J = 0$ 零点 | 证伪原作者普适非零断言；但实验解 $\delta=-0.55$ 处于正则区 | **理论边界澄清**；明确多极极值区奇异性 |
| **探测器阵列几何** | 硬编码 JUROGAM 角度：$26.0^\circ$ 与 $90.0^\circ$ | AFRODITE 阵列实测角度：$45^\circ$、$90^\circ$ 与 $135^\circ$ | 核心角度完全不重合；AFRODITE 无 $26^\circ$ 探测环 | **代码输入物理阻断**；禁止直接运行 |
| **实验观测量完备性** | 必须具有角分布比 $R_{\text{ADO}}$ 与线偏振度 $P$ 构成的二维向量 | 133Ce 仅测定 $R_{\text{AD}}$ 与 $R_{\text{DCO}}$，线偏振度 $P$ 完全缺失 | 降维导致无法执行二维概率密度投影变换 | **方法适用性阻断**；强行填补属伪科学 |
| **代码运行环境** | 宽松依赖 `numpy>=1.24` | 运行环境为 NumPy 2.5.3，彻底移除了 `np.trapz` 接口 | 运行时抛出 `AttributeError` 致命崩溃 | **代码栈确定性缺陷**；需接口适配更新 |
| **582.7 keV 分母** | 假定实验输入具有确定的母末态与已知分支线 | out/out 所需 817.7 keV 跃迁在 Table 5.2 与纲图中完全缺失 | 实验跃迁账本缺失核心基准线，反演产额自相矛盾 | **科学事实缺失**；out/out 比值不可信 |

### 最终审计裁决

1. **非平凡 No-Op（Non-Trivial No-Op）**：本次深审绝非毫无科学增益的简单跳过，而是通过严格的数学推导与数值诊断，彻底理清了 P-ADO 算法应用于奇 A 核 133Ce 时的理论联系与物理边界；
2. **操作性禁绝指令（Strict Prohibition of Producer Execution）**：严禁在当前状态下对 133Ce 运行 P-ADO CLI producer，亦不得虚构线偏振度 $P$ 或强行借用 JUROGAM 探测角度；
3. **成果固化**：所有数学推导、反演产额与零点坐标均已完整记录于当前目录的 `ce133-contract-audit-014.json` 与本报告中，严格遵守仓库不改动 `raw/` 与 `knowledge/` 的自治安全红线。
