---
type: system-governance
graph-excluded: true
created: 2026-11-04
updated: 2026-11-04
---

# 核结构与在束谱学实验数据分析工具箱 (Nuclear Spectroscopy Analysis Suite)

本目录包含一套纯 Python 编写的完整低能核物理与在束 $\\gamma$ 谱学分析工具链，主入口为 `nuclear_analyzer.py`。
该工具链专为从远端 Git 仓库拉取到实验室采集机、离线分析工作站或个人计算设备上直接运行而设计，完全取代对商业闭源软件（如 Mathematica）的依赖，严格基于统计学、误差传递与实验教材判据进行科学计算。

---

## 1. 跨设备快速部署指南

### 1.1 依赖与运行环境
只需标准 Python 3.9 或更高版本，核心科学计算依赖包括 `numpy`、`scipy` 与 `matplotlib`（均为通用开源标准库）：

```bash
# 1. 克隆或拉取仓库
git clone <repo_url> wiki
cd wiki

# 2. 创建并激活虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux / macOS
# 或 venv\\Scripts\\activate  (Windows)

# 3. 安装科学计算依赖
pip install numpy scipy matplotlib

# 4. 运行全套自检回归测试
python3 system/scripts/analysis/nuclear_analyzer.py selftest
```
若输出 `Regression checks passed.`，则表明 130+ 个物理分析子模块已在当前设备上完全就绪！

---

## 2. 核心子命令与功能矩阵分类

`nuclear_analyzer.py` 提供超过 120 个面向实验谱学与理论比较的专用子命令，按实验物理分析流程分类如下：

### (1) 重离子反应设计与运动学 (Reaction Kinematics)
- `kinematics`：重离子熔合反应运动学、质心系能量变换、反冲核初速度 $v/c$ 与最大多普勒位移；
- `fusion` / `wong`：基于 Wong 势垒穿透公式与抛物线势垒计算熔合总截面 $\\sigma_{\\text{fus}}(E)$ 及分波自旋分布 $P(\\ell)$；
- `evap`：复合核统计蒸发模型去激级联与 $xn, pxn, \\alpha xn$ 残余核产额预测；
- `rainbow` / `optrainbow`：重离子近弹弹性散射彩虹偏转函数、Airy 极小位置与相互作用半径反演。

### (2) 探测器物理与数字脉冲成形 (Detectors & Digital Pulse Processing)
- `hpgefield`：同轴高纯锗（HPGe）探测器反向偏压耗尽电场分布与 Shockley-Ramo 电荷收集时间；
- `hpge`：数字脉冲极零相消（PZC）、高频白噪声滤波与弹道亏损（Ballistic Deficit）评估；
- `mwdblr`：数字化移动窗口反褶积（MWD）与高计数率自适应基线恢复（BLR）递归算法；
- `cfd` / `tfawalk`：恒比定时（CFD）双极性信号过零点插值算法与定时走动（Walk）/抖动（Jitter）分离；
- `deadtime`：不可扩展型（非麻痹型）与可扩展型（麻痹型）死时间公式、计数损失校正与双根歧义预警；
- `pulserlt`：高频参考脉冲注入法（Pulser Injection）实时活时间（Live-Time）测定与二项-泊松复合方差传递；
- `psd` / `psdopt`：闪烁探测器电荷比较法（CCM）中子/$\\gamma$ 脉冲形状鉴别与短门最佳窗口 FOM 最优化。

### (3) 能谱解叠、符合矩阵与强度平衡 (Spectroscopy & Coincidence Analysis)
- `gslice` / `coinbal`：二维 $\\gamma-\\gamma$ 符合矩阵高斯切片、Radford 3点连续本底扣除与网格面积积分；
- `snip2d`：二维自适应敏感非线性峰剪切（2D SNIP）算法全自动自适应扣除二维散射背景；
- `gatedmult`：强重叠多重峰约束多高斯拟合与全协方差矩阵反演；
- `loopbal`：在束能级纲图能量闭合回路 Ritz 结合残差检验与跃迁强度平衡直接侧馈计算；
- `icc`：结合 BrIcc 数据表对内转换电子发射（ICC）进行绝对跃迁强度校正 $I_{\\text{tot}} = I_\\gamma(1+\\alpha)$；
- `tcs`：近距离测量真符合相加（TCS）全能峰损失（Summing-Out）与虚假峰（Summing-In）几何校正。

### (4) 角关联、混合比与偏振双根仲裁 (Angular Distribution & Polarization)
- `dco` / `ado`：定向态方向角关联比值（DCO / ADO）与理论模型曲面计算；
- `clover`：四叶 Clover 探测器 Compton 散射反冲能量分辨与线偏振度（Linear Polarization）反演；
- `dualroots` / `doubleroot`：从单角关联二次有理式 $a_2(\\delta)$ 求解多极混合比 $\\delta(E2/M1)$ 两个数学实根，结合 Clover 线偏振不对称度进行双参数剖面似然比检验（Profile Likelihood $\\Delta\\chi^2$），彻底打破双根简并；
- `atten` / `cascadeuk`：在束核自旋取向高斯宽度 $\\sigma/I$ 衰减因子 $\\alpha_k$ 与未观测中间级联退取向张量 $U_k$ 计算；
- `deorient`：真空反冲超精细磁场退取向效应 $G_2, G_4$ 时间积分与角关联恢复。

### (5) 激发态皮秒寿命测量 (Picosecond Lifetime Inversion)
- `rdds` / `rddsddcm`：反冲距离多普勒频移法（RDDS / 活塞法 Plunger）微分衰减曲线法（DDCM）无偏反演 $1\\text{ ps} \\sim 1\\text{ ns}$ 寿命；
- `dsam` / `dsamzbl`：多普勒频移衰减法（DSAM）结合 ZBL 全能区电子/核阻止截面与 Blaugrund 空间散射多普勒线型反演 $0.01 \\sim 2\\text{ ps}$ 寿命；
- `feed`：有效慢侧馈时间延迟（Side-Feeding Delay）解卷积。

### (6) 三轴形变、手征性与摆动前沿判定 (Triaxiality, Chirality & Wobbling)
- `triaxial` / `wobbling`：Davydov-Filippov 刚性三轴转子本征能量、三态求和规则 $E(2_1^+) + E(2_2^+) = E(3_1^+)$ 与 Frauendorf 横向/纵向摆动模型；
- `wobstab`：奇 $A$ 核横向摆动临界失稳角动量与转动惯量模型分岔判定；
- `twoqpwob`：偶偶核两准粒子横向摆动（Two-quasiparticle Wobbling）微观能量与跃迁比率；
- `chiral` / `tac`：三维倾斜轴推转模型（3D-TAC）手征非共面取向势能面与叉式分岔势垒；
- `chirrules`：Koike-Starosta-Hamamoto 手征选择定则仲裁，检验带内 $S_{M1}(I)$ 奇偶交错同相性、带内 $B(E2)$ 相似性与简并点带间 $M1$ 跃迁深极小；
- `chiralg`：Grodner 手征双重带回旋比相等性定理 $g(\\text{Band 1}) \\equiv g(\\text{Band 2})$ 验证；
- `chirmep`：奇奇核手征大振幅集体运动最小能量路径（MEP）与瞬子（Instanton）量子穿隧能隙求解；
- `scissm1`：三轴双转子剪刀振动模式（Scissors Mode）激发能与 $M1$ 跃迁强度分布；
- `vmi`：Mariscotti 可变转动惯量模型（VMI）三次方程求解与离心拉伸拟合；
- `grodzins`：Grodzins 经验乘积定则由 $E(2_1^+)$ 反演四极形变 $\\beta_2$ 与内禀四极矩 $Q_0$。

### (7) 实验物理高级统计学 (Advanced Statistics)
- `stats`：实验不确定度传播、协方差矩阵反演与 MINOS 剖面似然非对称误差；
- `feldman`：Feldman-Cousins 统一似然比顺序求和置信区间，解决低计数本底下的物理边界（$\\ge 0$）区间构造；
- `poissonfit`：极弱峰泊松极大似然拟合（Cash 统计量），纠正传统 Neyman $\\chi^2$ 加权拟合产生的系统性负偏差。

---

## 3. 典型实验数据分析场景实操范例

### 范例 1：解决 $\\delta(E2/M1)$ 混合比双根并用 Clover 线偏振排他选解
当从方向角分布测得某一 $\\Delta I=1$ 跃迁的 $a_2 = -0.42(3)$ 时，存在两个数学实根：

```bash
# 1. 运行双根求解器与剖面似然分析
python3 system/scripts/analysis/nuclear_analyzer.py doubleroot \\
  --a2 -0.42 --a2-err 0.03 \\
  --pol -0.21 --pol-err 0.04 \\
  --spin-i 8.5 --spin-f 7.5
```
**输出**：系统将给出两个数学根（大根 $\\delta_1 \\approx -1.83$ 与小根 $\\delta_2 \\approx -0.47$），并自动代入 Clover 线偏振不对称度度量。由于大根预测线偏振 $P_{\\text{calc}} \\approx +0.35$ 与实测 $P_{\\text{exp}} = -0.21(4)$ 严重冲突（$\\Delta\\chi^2 > 100$），程序将以 $>11\\sigma$ 的置信度排他性锁定物理解为小根 $\\delta_2$（$M1$ 占优），直接证伪横向摆动假设！

---

### 范例 2：检验候选双能带是否满足核手征选择定则 (Koike-Starosta Rules)
对实验构建的双重能带运行电磁选择定则仲裁器：

```bash
# 针对 135Nd 3-准粒子手征双重带基准
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 135Nd_chiral_doublet_benchmark

# 或针对 134Pr 奇奇核手征双重带基准
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 134Pr_chiral_doublet_benchmark
```
**输出**：程序将自动提取带内 $B(M1; I \\to I-1)$ 的交错参量 $S_{M1}(I)$，对比两带的峰谷相位是否严格同相（In-Phase），检验带内 $B(E2)$ 相似度及简并点处的带间 $M1$ 压制程度，最终输出定量置信评分与仲裁结论。

---

### 范例 3：反冲距离多普勒频移法 (RDDS) 微分衰减曲线法 (DDCM) 提取皮秒核态寿命
利用柱塞靶（Plunger）装置在不同靶-阻挡箔距离 $d$ 处测得的未移位峰 $I_u$ 与移位峰 $I_s$ 面积：

```bash
python3 system/scripts/analysis/nuclear_analyzer.py rddsddcm \\
  --distances 10,25,50,100,200,500 \\
  --intensity-ratio 0.12,0.28,0.52,0.76,0.91,0.98 \\
  --recoil-beta 0.0185
```
**输出**：程序执行样条平滑并计算导数 $dR/dd$，在平坦响应区无偏反演本征核能态寿命 $\\tau$，彻底消除对未知侧馈模型的依赖。

---

### 范例 4：数字梯形滤波 (Jordanov) 与极零相消 (PZC) 离散递归处理
对前置放大器采样得到的离散波形运行数字梯形滤波算法以消除弹道亏损：

```bash
python3 system/scripts/analysis/nuclear_analyzer.py mwdblr \\
  --rise-steps 20 --flat-steps 15 \\
  --decay-time 50.0 --sampling-rate 100.0
```

---

## 4. 自动化测试与持续集成保证

本工具链中所有物理计算模块均由位于 `system/tests/` 目录下的 626 项单元测试进行逐一覆盖与约束：

```bash
# 运行全库单元测试套件
python3 -m unittest discover -s system/tests
```
测试覆盖了极端边界条件、简并点发散、物理守恒律、双根判据及真实高自旋在束文献数据，确保算法在任何设备上均保持数值精度与物理严密性。
