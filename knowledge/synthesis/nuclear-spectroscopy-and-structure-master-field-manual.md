---
type: synthesis
title: "核结构与实验谱学工作入口：来源、模型与工具验证状态"
aliases: [核谱学实战全书, 核结构专家工作手册, 92模块闭环指南, 在束谱学实验手册, 三轴形变与高自旋实战手册]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
scope: "馆藏研学、低能核结构模型和实验谱学计算的证据边界"
confidence: low
sources: [book-petrache-chirality-and-wobbling, book-bohr-mottelson-nuclear-structure-vol2, cowan2011-asymptotic-likelihood-tests]
tags: [nuclear-structure, spectroscopy, book-study, scientific-validation]
---

# 核结构与实验谱学工作入口

## Active summary for agents

旧版“92 个生产级模块、全书吸收完成、全部科学验证”认证撤回。代码中有解析计算、经验参数化和合成示例，测试通过不使三者自动成为真实实验分析。当前入口按问题选择工具和已核验 source，先看下面的具体边界。未核验模块不能给其它模型提供确定性物理裁决。

## Question and Scope

目标是把全馆藏转成跨会话可检索、可复核的方法与研究知识。优先深入中文核物理基础、Bohr–Mottelson、手征/摆动专著、在束 γ 谱学、反应设计与实验统计。其它书不省略；Mathematica 侧重方法迁移到 Python。覆盖队列和逐页可读性见 [[book-corpus-coverage-ledger]]，不以模块数量计算阅读学分。

## Evidence Matrix

| 问题 | 可查原件/知识 | 当前核查所得 | 仍未闭合 |
| --- | --- | --- | --- |
| 谐近似何时适用 | [[book-bohr-mottelson-nuclear-structure-vol2]]，PDF 212–214 | 频率、横向涨落条件与轴约定已选段核对 | 完整 E2 推导、奇核 PTR 与目标核波函数 |
| 135Pr 是否已经终局裁定 | [[book-petrache-chirality-and-wobbling]]，Ch. 2/5/11 | 书中保留支持与反对解释 | 原始角关联/偏振数据、后续论文和共同分析 |
| 混合比能否直接选根 | [[wobbling-mixing-ratio-phase-and-transition-diagnostics]] | 理论最近根不构成独立证据；矩阵元与内禀 Q0 不等同 | 共同响应、校准和 nuisance likelihood |
| 稀疏峰能否称严格无偏 | [[poisson-maximum-likelihood-and-gamma-peak-fitting-bias]] | Poisson MLE 仍可有有限样本偏差；一次样本误差不是 bias | 真实背景/峰形不确定度、覆盖率与试验数校正 |
| 两本中文探测教材是否矛盾 | [[reconciliation-of-detector-dead-time-and-pulse-pileup]] | 需先分模型、适用环节及原文条件 | 逐页对照，不能用目录代替冲突证据 |
| 如何提出实验束流方案 | [[heavy-ion-fusion-evaporation-and-reaction-channel-design]] | 入口道、蒸发竞争、靶内能损及响应应分别约束 | 真实质量/激发函数、输运、探测与束流参数 |

以上多为方法核查或综述作者判断，不是新实验事实。重用同一数据的理论论文、专著章节和综述须标明依赖关系。

## Synthesis

### 沿观测到模型的研究路径

1. **反应与测量定义**：明确残核、反应道、入射电荷态、束流积分、靶组成/面密度、能损和探测几何；未测参数保留不确定度。
2. **计数与仪器响应**：原始计数、背景/控制窗、死时间、pile-up、能量/效率校准分别建模。背景扣除后的净谱通常不再是独立泊松计数。
3. **纲图与电磁性质**：先验证符合关系和能量闭合；混合比、分支比、寿命和 ICC 各有不同含义。能级强度不平衡还可能来自直接布居、未见支路和校准。
4. **模型比较**：以共同的带/跃迁身份比较 PTR/TPSM、IBFM/γ 软核、旋称伙伴、组态混合、TiP 与手征解释，写出各自能改变判断的观测预言。
5. **研究设计**：把关键证据缺口转换成有响应与统计功效依据的测量方案；不由一套示意高斯出射道权重直接批准束流能量或靶厚。

### 统一 CLI 的本轮用途

| 命令 | 可使用内容 | 科学使用边界 |
| --- | --- | --- |
| `wobphase` | 有符号约化矩阵元换算；保留两个 δ 候选 | 缺模型矩阵元返回不足，不作 TW/LW 指认 |
| `poissonfit` | 固定峰位/宽度、已知本底的 bin 积分 Poisson 例子 | 局部渐近显著性与 LR 区间；不保证稀疏覆盖率或发现 |
| `deadtime` | 明示理想模型下的计数率与反演分支 | 模型需仪器校准；不把两本书的侧重点写成必然矛盾 |
| `fusion` | 入口运动学及明示的示意反应量 | 合成蒸发权重不是校准的 Hauser–Feshbach 截面 |
| `coriolis` | 理想单 j 耦合大小、合成能量序列的有限差分 | ξ 是输入；默认数据不是 131La 实测 |
| `gdr` | 经典积分标度及轴对称参数化的代数演示 | 非三轴完整响应；κ 与宽度非实测；正反演不认证精度 |
| `isg` | 明示假设的历史同位旋分支示意 | 未算真实约化矩阵元；份额与峰位不作测量或微观认证 |
| `fcoeff` | 任意初末自旋下 Yamazaki F 系数代数计算、理论 a2/a4、DCO 比值与 a2 双根反演 | 双根在数学上完全等价，需偏振度或内转换独立破除简并 |
| `decouple` | K=1/2 转动带解耦参数 a 与 A=hbar^2/2J 严格线性正规方程组反演及 Stephens-Simon 退耦带模拟 | 绝热转动近似下成立，大形变组态混合或三轴强进动需结合 PRM/TPSM |
| `alpha` | Alpha 衰变 Gamow 势垒穿透概率 WKB 积分、离心势垒阻碍及 Viola-Seaborg 系统学反演 | 势垒穿透模型假设预成几率 S_alpha，微观多核子团簇需结合壳模型/EDF |
| `triaxial` | 三轴核转子摆动（TW/LW）频率与临界自旋、Elena Lawrie 倾斜进动（TiP）判据及手征双带 B(M1)/B(E2) 奇偶交错 | 候选带必须具有显著 E2 优势方可定性为摆动；M1 主导时归属于单粒子进动或准粒子-γ 振动耦合 |
| `feldman` | 小信号测量的 Feldman-Cousins 统一置信区间与物理边界反演（泊松本底与正态截断） | 假设本底严格平稳已知；本底含系统误差时需结合 Profile Likelihood |
| `hpgefield` | HPGe 同轴探测器耗尽电压、电场分布、Shockley-Ramo 电荷收集、数字梯形平顶弹道亏损与 N 型/P 型快中子损伤调和 | 平面二维近似；闭端弹头区三维拐点需结合三维电荷漂移网格模拟 |
| `wong` | 重离子熔合 Wong 势垒穿透解析解、初态自旋分布 P(l)、RLDM 裂变截断与 xn 最佳束流能量规划 | 抛物线单势垒近似；重合道或强形变亚垒增强需结合耦合道（CCFULL） |
| `dsam` | 在束多普勒频移衰减法（DSAM）质心频移 F(tau)、LSS 阻止本领、Blaugrund 多次散射与皮秒核能级寿命反演 | 需结合上级跃迁侧馈时间去卷积；阻止本领基于 LSS 理论标度 |
| `vmi` | Mariscotti 可变转动惯量（VMI）模型 Cardano 三次方程解析求解、动态离心拉伸与 (J0, C) 反演 | 绝热连续拉伸假设；回弯（Backbending）对对齐不适用 |
| `seniority` | 原子核 Seniority (v) 代数方案、半满壳 n=j+1/2 处 B(E2) 严格相消与代数异能态寿命计算 | 纯单 j 壳层有效；多轨道组态混合与微观核芯极化需引入有效电荷 |
| `cfd` | 恒比定时甄别器（CFD）最佳延迟 t_d=tr*(1-f) 过零幅度游走消除与快速定时时间分辨 | 假设脉冲波形尺度不变；同轴 HPGe 漂移时间弥散需结合 ARC 定时 |
| `grodzins` | Grodzins 乘积定则 E(2+)*B(E2)、四极形变 beta_2 反演与 BCS 超流转动惯量淬灭比 | 轴对称 K=0 带头假设；双幻核壳封闭处 Grodzins 经验定则失效 |
| `csm` | 推转壳模型（CSM）双带回避交叉、相互作用矩阵元 |V_12| 反演与回弯/上弯分类 | 双态截断有效；多对准粒子多重交叉需全对角化 CSM |
| `omp` | 核光学模型势（OMP）Woods-Saxon 径迹积分、S 矩阵透射率 T(b) 与全反应截面 | 半经典直角径迹近似；极低能库仑偏折显著能区需分波偏相移求和 |
| `doppler` | 在束相对论多普勒展宽、有限张角 Delta_theta、速度弥散与中子反冲角离散预算 | 匀速直线发射假设；厚衬底慢化过程需结合 DSAM 连续谱积分 |
| `crank` | 高 j 单壳层三轴推转哈密顿量对角化、Routhian 能谱、对齐量 <jx> 与旋称反转 | 单 j 壳层截断；微观自洽多组态需结合三维推转 RMF 或 TAC-CSM |
| `pipeline` | 在束实验核谱学全流程数据处理流水线工作台（反应->多普勒->DCO->DSAM->模式仲裁） | 整合 7 大子模块；需提供对应阶段的关键输入观测值 |
| `schiffer` | Schiffer-True 普适两体相互作用矩阵元（TBME）、Pandya 反转与 Nordheim 手征带头自旋定则 | 纯两体短程势有效；多体有效作用需结合壳模型有效两体相互作用（如 G 矩阵） |
| `tac` | 三维倾斜轴推转（3D TAC）手征取向势能面 E(theta, phi)、分叉临界自旋与平面势垒 | 拟经典矢量耦合；低势垒大振幅涨落需结合投影壳模型（TPSM） |
| `zgamma` | Gamma 振动带 Mikhailov z_gamma 混合参数、Alaga 定则偏离修正与转-振耦合矩阵元 h_2 | 一级微扰假设；强非轴对称三轴大形变需采用 Davydov-Filippov 模型 |
| `loopbal` | 在束能级纲图 Ritz 闭合环能量残差、BrIcc 强度平衡与反应侧馈强度提取 | 瞬发符合假设；若中间态存在长寿命同核异能态需进行延迟门控校正 |
| `chaban` | Davydov-Chaban 非绝热三轴转子模型、离心 beta 拉伸比 p=beta/beta0 与能谱计算 | 假定三轴度 gamma 保持为常数极小；大振幅 gamma 涨落需结合 5D 玻尔哈密顿量 |
| `doubleroot` | DCO 多极混合比 delta(E2/M1) 双根轮廓极大似然、偏振/转换系数/单粒子极限物理仲裁 | 依赖实验角分布与偏振测量精度；对于纯多极跃迁（delta=0 或 delta->inf）需做退化处理 |
| `mchid` | 多准粒子多重手征双重带（MchiD）与 4-QP 非共面角动量空间几何测度分析 | 适用于偶偶核与奇 A 核多准粒子态；低自旋大振幅手征振动区域需结合微观量子投影 |
| `wilczynski` | 重离子深部非弹性散射（DIC）TKEL 能损、粘滞自旋转移与 Wilczynski 鸟嘴脊线模拟 | 假定二体反应机制；极高能区破裂（Breakup）与不完全熔合需引入三体运动学 |
| `octewsr` | 微观八极集体模式、IS-EWSR 求和定则耗尽率、内禀 D0 偶极矩与交替宇称能带分析 | 依赖 Alaga 几何分支假定；轴不对称八极振动需结合三轴八极微观混合模型 |
| `psdopt` | 数字化脉冲形状鉴别（PSD）、双门电荷比较法（CCM）门宽最优化与中子/gamma 分离 FOM | 假定双指数荧光衰变动力学；低能区（<100 keVee）受光电子泊松统计涨落限制 |
| `tacpair` | 自洽 3D TAC 微观配对能隙方程、Coriolis 反配对（CAP）淬灭与手征恢复相变动力学 | 依赖平均场单粒子态基底；大振幅非谐振量子涨落需结合角动量投影（AMP） |
| `cascadeuk` | 未观测中间级联去取向系数 U_k(I1, I2, L) 与级联角分布各向异性衰减修正 | 需假定未观测跃迁的多极性或混合比；若存在长寿命同核异能态需结合时间微分真空去取向 |
| `mwpc` | MWPC 与漂移室共形解析静电场、第一 Townsend 雪崩放大与饱和时空校准曲线 | 假定理想平行丝阵列；极端高计数率（>10^5 Hz/mm）下需引入正离子鞘空间电荷屏蔽修正 |
| `coriolismix` | 奇 A 变形核多带 Coriolis 耦合矩阵代数对角化、波函数混杂与签名交错度分析 | 假定轴对称拉长转子核心；三轴或超形变大形变核需结合非轴对称推转或三轴粒子转子模型 |
| `spontfiss` | 重核与超重核双峰势垒自发裂变（SF）WKB 量子穿透作用量积分与半衰期系统学 | 假定一维裂变裂开路径；高维断裂形变与颈缩动力学需结合多维微观自洽 HFB 势能面 |
| `ptrm` | 粒子-三轴转子模型（PTRM）完全代数对角化、摆动带激发谱与非简谐 R21 提取 | 假定单 j 壳层有效势；多准粒子组态需结合三维倾斜轴推转（TAC）或投影壳模型（TPSM） |
| `mwdblr` | 数字化移动窗口反褶积（MWD）与自适应基线恢复（BLR）高计数率滤波 | 假定单极性指数前放响应；复杂探测器电荷收集延迟需适度拓宽反褶积平顶 M_win |
| `gcd` | 在束超快电子学定时广义质心差分法（GCD）皮秒核寿命反演与 PRF 时间游走校准 | 需精确标定快闪烁体探测器的 PRF 能量依赖曲线；存在复杂多步侧馈时需结合微观退卷积 |
| `chiralg` | 手征双重带磁偶极矩 g 因子相等性定理检验与伪手征伪带排他性仲裁 | 依赖含自旋取向的超精细场或外加磁场 g 因子测量；低自旋大振幅手征振动区需计入量子相干修正 |
| `tcs` | 在束真符合相加（TCS）全能峰损失修正、相加峰产额与近几何立体角效率计算 | 需结合探测器全相互作用总效率与角关联 W(0)；极远距离低效率下相加修正可忽略 |
| `chiroct` | 三轴手征与八极反射不对称共存核四重能带（Chiral-Octupole Quartet）动力学分析 | 适用于奇奇核与多准粒子态；弱八极关联下四重带退化为独立手征双带与正负宇称能级 |
| `optrainbow` | 重离子核彩虹散射半经典偏转函数极小值、Airy 振荡结构与光学势深度反演 | 需高能量克服库仑势垒（E_lab >= 10-25 MeV/u）；强表面吸收可能部分削弱 Airy 极小振幅 |
| `timefit` | 在束电子学符合时间谱高斯-指数卷积解析线型拟合与激发态寿命解卷积 | 假定单指数核衰变与单高斯时间分辨（IRF）；复杂多路级联或时间抖动非高斯拖尾需多成分拓展 |
| `twoqpwob` | 偶偶三轴核两准粒子横向摆动模式（TW）激发能、频率斜率与带间 E2/M1 比率分析 | 假定两高-j 准粒子沿短轴刚性顺排（j_12 ~ 10 hbar）；受带交叉或高自旋三维取向转变限制 |
| `effcov` | HPGe / Clover 探测器全能峰效率曲线加权最小二乘拟合与严格全协方差误差传播 | 假定对数多项式在大于 80 keV 能区成立；超低能区（< 50 keV）吸收边缘需采用分段双幂律模型 |
| `gatedmult` | 在束符合矩阵门扣除本底重叠多重峰加权拟合与峰面积协方差反演 | 假定局部探测器能量分辨率为高斯线型；具有极强长低能拖尾的大晶体需扩展非对称卷积尾 |
| `tsddecay` | 三轴超形变（TSD）摆动带退激穿透、势垒隧穿与分支竞争动力学分析 | 采用 Hill-Wheeler 统计单势垒穿透模型；受正常形变态局部能级密度涨落与共振混合影响 |
| `mcintyre` | 重离子强吸收 S 矩阵 McIntyre 参数化、分波透光度与总反应截面半经典反演 | 假定平滑 Woods-Saxon 角动量吸收截断；极深能区或微细共振结构需微观光学模型展开 |
| `tacbifurc` | 3D-TAC 手征空间取向势能面、超临界叉式分岔临界自旋与手征势垒反演 | 假定两体单粒子角动量刚性对齐；高自旋微观配对波动与软核涨落需含时密度泛函微观校核 |
| `foldmult` | 在束多探测器阵列符合折叠数到多重度分布与复合核进入态自旋/能量反褶积 | 依赖阵列单光子效率与几何响应模型；受级联非统计电偶极与微弱转换电子竞争微扰 |
| `chirrules` | 手征双重带带内 B(M1) 奇偶交错同相性与带间 Delta I = 0 M1 跃迁极小仲裁 | 需双带精确电磁跃迁几率或分支比测量；低自旋大振幅手征振动区需结合隧穿波函数修正 |
| `timegate` | 在束多探头阵列瞬发-缓发时间门选与随机符合本底差分扣除 | 假定束流具有稳定 RF 微脉冲结构；极高计数率下需计入相邻束团重叠污染项 |
| `hexwob` | 非轴对称三轴核十六极形变 beta_4 微扰修正与摆动频率演化求解器 | 适用于高自旋或超形变能带；大振幅非简谐摆动需结合数值薛定谔方程对角化 |
| `chirasch` | 手征四次双阱势大振幅集体运动 1D 薛定谔方程有限差分对角化求解器 | 采用一维刚性质量参数近似；高自旋多维坐标混合需多维集体哈密顿量扩展 |
| `attneqk` | HPGe / Clover 探测器有限立体角角分布几何衰减因子 Q_2, Q_4 数值积分 | 假定探测器晶体为圆柱形对称体；前表面不均匀死层或异形切角需 Monte Carlo 补充校准 |
| `pulserlt` | 在束高计数率脉冲发生器注入法活时间测定与级联模拟堆积/ADC死时间补偿 | 依赖脉冲发生器频率绝对稳定性；极端超载（>150 kHz）下需检查前放直流偏置饱和 |
| `tsdpes` | 宏观-微观三轴超形变 3D (beta_2, gamma, beta_4) 势能面 Strutinsky 壳修正计算器 | 采用唯象液滴能与平滑高斯壳修正；极高同位旋非对称区需计入自洽微观泛函约束 |
| `capgap` | 科里奥利反配对（CAP）动态配对能隙淬灭与转动惯量超流向刚体相变求解器 | 采用 Mottelson-Valatin 单极配对单参量淬灭模型；存在高自旋准粒子顺排后弯时需计入阻塞效应 |
| `coineff` | 多探测器阵列 gamma-gamma 符合绝对探测效率矩阵几何与角度关联调制反演 | 需结合晶体有限立体角衰减因子 Q_k；极端宽开角（>30 deg）需开展非共轴三维 Monte Carlo 标定 |
| `tpsmproj` | 投影壳模型（TPSM）三维角动量投影矩阵元求解与能带 Hill-Wheeler 对角化 | 截断于多准粒子基底；包含高位闯入轨道的大振幅混合需扩展组态空间截断 |
| `rddsddcm` | 在束反冲距离多普勒频移法（RDDS）微分衰减曲线（DDCM）皮秒寿命反演 | 需平滑自适应样条对 R(d) 求导；飞行有效灵敏区外（R < 0.15 或 > 0.85）涨落较大需剔除 |
| `selftest` | 执行软件回归 | 不认证其余未审模块的模型、单位、证据或生产状态 |

```bash
python3 system/scripts/analysis/nuclear_analyzer.py wobphase --root1 -0.15 --root2 3.10 --json
python3 system/scripts/analysis/nuclear_analyzer.py poissonfit --area 60 --bg 2 --json
python3 system/scripts/analysis/nuclear_analyzer.py fcoeff -i 7.5 -f 6.5 -d -0.15 --json
python3 system/scripts/analysis/nuclear_analyzer.py decouple --preset 169Tm --json
python3 system/scripts/analysis/nuclear_analyzer.py alpha --preset 212Po --json
python3 system/scripts/analysis/nuclear_analyzer.py triaxial --preset 135Pr --json
python3 system/scripts/analysis/nuclear_analyzer.py feldman --preset faint_peak_2 --json
python3 system/scripts/analysis/nuclear_analyzer.py hpgefield --preset standard_coaxial_ptype --json
python3 system/scripts/analysis/nuclear_analyzer.py wong --preset 16O_122Sn --json
python3 system/scripts/analysis/nuclear_analyzer.py dsam --preset 134Ce_in_Au --json
python3 system/scripts/analysis/nuclear_analyzer.py vmi --preset 168Er --json
python3 system/scripts/analysis/nuclear_analyzer.py seniority --preset 130Sn_h11/2 --json
python3 system/scripts/analysis/nuclear_analyzer.py cfd --preset labr3_fast_timing --json
python3 system/scripts/analysis/nuclear_analyzer.py grodzins --preset 154Sm --json
python3 system/scripts/analysis/nuclear_analyzer.py csm --preset 164Er_neutron_crossing --json
python3 system/scripts/analysis/nuclear_analyzer.py omp --preset 40MeV_p_58Ni --json
python3 system/scripts/analysis/nuclear_analyzer.py doppler --preset 134Ce_in_beam --json
python3 system/scripts/analysis/nuclear_analyzer.py crank --preset h11/2_triaxial_chiral --json
python3 system/scripts/analysis/nuclear_analyzer.py pipeline --preset 135Pr_wobbling_audit --json
python3 system/scripts/analysis/nuclear_analyzer.py schiffer --preset pr134_chiral_bandhead --json
python3 system/scripts/analysis/nuclear_analyzer.py tac --preset 134Pr_chiral_tripod --json
python3 system/scripts/analysis/nuclear_analyzer.py zgamma --preset 168Er_gamma_band --json
python3 system/scripts/analysis/nuclear_analyzer.py loopbal --preset 134Ce_triaxial_scheme --json
python3 system/scripts/analysis/nuclear_analyzer.py chaban --preset 112Ru_triaxial_chaban --json
python3 system/scripts/analysis/nuclear_analyzer.py doubleroot --preset 135Pr_wobbling_candidate --json
python3 system/scripts/analysis/nuclear_analyzer.py mchid --preset 136Nd_4qp_mchid --json
python3 system/scripts/analysis/nuclear_analyzer.py wilczynski --preset 86Kr_166Er_703MeV --json
python3 system/scripts/analysis/nuclear_analyzer.py octewsr --preset 224Ra_pear_shaped --json
python3 system/scripts/analysis/nuclear_analyzer.py psdopt --preset EJ301_fast_neutron_psd --json
python3 system/scripts/analysis/nuclear_analyzer.py tacpair --preset 134Pr_chiral_tripod_pairing --json
python3 system/scripts/analysis/nuclear_analyzer.py cascadeuk --preset yrast_stretched_e2_cascade --json
python3 system/scripts/analysis/nuclear_analyzer.py mwpc --preset standard_mwpc_p10 --json
python3 system/scripts/analysis/nuclear_analyzer.py coriolismix --preset 159Dy_neutron_i13_2 --json
python3 system/scripts/analysis/nuclear_analyzer.py spontfiss --preset 238U_spontaneous_fission --json
python3 system/scripts/analysis/nuclear_analyzer.py ptrm --preset 135Pr_triaxial_wobbler_ptrm --json
python3 system/scripts/analysis/nuclear_analyzer.py mwdblr --preset standard_hpge_high_rate --json
python3 system/scripts/analysis/nuclear_analyzer.py gcd --preset 134Ce_fast_timing_2plus --json
python3 system/scripts/analysis/nuclear_analyzer.py chiralg --preset 128Cs_chiral_doublet_benchmark --json
python3 system/scripts/analysis/nuclear_analyzer.py tcs --preset 60Co_close_geometry_clover --json
python3 system/scripts/analysis/nuclear_analyzer.py chiroct --preset 78Br_chiral_octupole_quartet --json
python3 system/scripts/analysis/nuclear_analyzer.py optrainbow --preset 16O_16O_350MeV --json
python3 system/scripts/analysis/nuclear_analyzer.py timefit --preset 181Ta_isomer_decay --json
python3 system/scripts/analysis/nuclear_analyzer.py twoqpwob --preset 130Ba_two_quasiparticle_wobbler --json
python3 system/scripts/analysis/nuclear_analyzer.py effcov --preset clover_detector_152Eu_calibration --query-E 409,638,1332 --json
python3 system/scripts/analysis/nuclear_analyzer.py gatedmult --preset 133Ce_wobbling_candidate_doublet --json
python3 system/scripts/analysis/nuclear_analyzer.py tsddecay --preset 163Lu_TSD2_wobbling_decayout --json
python3 system/scripts/analysis/nuclear_analyzer.py mcintyre --preset 16O_208Pb_129.5MeV --json
python3 system/scripts/analysis/nuclear_analyzer.py tacbifurc --preset 134Pr_chiral_bifurcation --json
python3 system/scripts/analysis/nuclear_analyzer.py foldmult --preset 4pi_bgo_ball_fusion_evaporation --json
python3 system/scripts/analysis/nuclear_analyzer.py chirrules --preset 128Cs_chiral_doublet_benchmark --json
python3 system/scripts/analysis/nuclear_analyzer.py timegate --preset in_beam_134Ce_prompt_random_subtraction --json
python3 system/scripts/analysis/nuclear_analyzer.py hexwob --preset 163Lu_TSD_positive_beta4 --json
python3 system/scripts/analysis/nuclear_analyzer.py chirasch --preset 135Nd_chiral_vibration --json
python3 system/scripts/analysis/nuclear_analyzer.py attneqk --preset standard_coaxial_hpge_15cm --json
python3 system/scripts/analysis/nuclear_analyzer.py pulserlt --preset in_beam_high_rate_clover_130Ba --json
python3 system/scripts/analysis/nuclear_analyzer.py tsdpes --preset 163Lu_TSD_potential_energy_surface --json
python3 system/scripts/analysis/nuclear_analyzer.py capgap --preset 163Lu_TSD_superfluid_to_normal_phase_transition --json
python3 system/scripts/analysis/nuclear_analyzer.py coineff --preset 12_clover_array_60Co_cascade --json
python3 system/scripts/analysis/nuclear_analyzer.py tpsmproj --preset 130Ba_TPSM_triaxial_bands --json
python3 system/scripts/analysis/nuclear_analyzer.py rddsddcm --preset 134Ce_2plus_rdds_plunger --json
python3 system/scripts/analysis/nuclear_analyzer.py selftest
```

示例根和计数都是人工输入，不绑定真实核素。依赖以实际 import/environment 为准，旧“全套零依赖、任意设备即 pull 即用”承诺撤回；现有模块使用 NumPy、SciPy 等时需安装对应依赖。

## Counter-evidence

- 专著 Ch. 5 的两准粒子案例允许 M1 比 E2 更强，不能推广固定 E2 份额阈值。
- Ch. 11 的大 δ 可以来自 M1 小分母，不等价于大绝对 B(E2)。
- Ch. 2 与 Ch. 5/11 对同一候选可持不同立场；学科能力来自组织并检验这些分歧，而非抹去它们。
- 统计模块存在非负参数边界、未知本底/峰位与有限样本问题，不能用一个显著性数字替代核结构解释。

## Model Dependence

惯量、γ 参数和坐标轴编号都应随公式/模型记录。纯转子 yrast 稳态偏好最大惯量轴，不等于经典最小惯量轴一律不稳定。冻结对齐、小振幅、刚核与软核的物理假设分开，数值求得正频率不是完整动力学的替代。

## Limitations and Missing Evidence

- 全书逐章正文、例题、附录、图表和公式尚未完成覆盖，必须继续读取。
- 大批历史自动生成页面和脚本未做科学独立验证；本轮只核查指定范围。
- 全库结构 lint 当前存在历史问题，目录检查与自测通过不能掩盖它；发布按实际门禁结果执行。
- 已存在 farmer 进程仅负责特定暂时性故障恢复，不等于保证无限连续运行或学习已完成。

## Sources

- [[book-petrache-chirality-and-wobbling]]：版权页、Ch. 2/5/11 实际选段及争议定位。
- [[book-bohr-mottelson-nuclear-structure]] 与 [[book-bohr-mottelson-nuclear-structure-vol2]]：原件身份、前言方法论与高自旋近似。
- [[cowan2011-asymptotic-likelihood-tests]]：有边界单侧似然检验，PDF 公式版本已区分。
- [[wobbling-harmonic-limit-and-textbook-consistency]]：角度平方疑点，保持 provisional。

## Self-audit and revision

2026-11-02：撤回旧版普适“五道门”阈值、135Pr 争议终结、合成数据作为实测、工具数作为学习完成证明等结论。该历史已保留在 Git；本页给出当前有效认识和来源，不继续传播旧指令。无本轮 human-review 事件。P0 的自动选根已隔离；P1 的全馆藏和全模块独立验证持续进行。
