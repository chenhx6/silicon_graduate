---
type: system-vocabulary
graph-excluded: true
updated: 2026-07-03
---

# 双语术语归一化表

本表用于中文、英文、缩写、历史写法和实验口语之间的查询归一化，不替代概念页、模型页、方法页或原始来源。`canonical` 是检索入口，不表示 aliases 在所有语境中科学等价。

使用顺序：

1. 先匹配结构化 seed entry 和页面 `aliases`；
2. 按 `query_expansion` 扩展检索词；
3. 遇到 `ambiguity` 或 `do_not_merge_with` 时保留多个候选，不静默合并；
4. 科学主张仍回到知识页、source 和 locator，不能引用本表代替证据。

## Entry schema

- `canonical`：规范检索入口；
- `zh` / `en` / `abbreviation`：推荐中文、英文和缩写；
- `aliases`：历史写法、变体和口语；
- `category`：concept / model / observable / method / experiment / data-analysis；
- `scope`：适用语境；
- `ambiguity`：可能指向多个对象时的说明；
- `do_not_merge_with`：不得静默合并的术语；
- `query_expansion`：检索时使用的双向扩展；
- `notes`：上下位、原文用词或证据边界。

## Seed registry

### shell model

- canonical: `shell model`
- zh: `壳模型`
- en: `shell model`
- abbreviation: 无统一缩写
- aliases: `nuclear shell model`、`核壳层模型`
- category: model
- scope: 泛指基于壳层与组态空间的模型家族
- ambiguity: 用户说“壳模型”时可能泛指 shell model，也可能实际指 CSM、PSM、TPSM 或其他具体实现
- do_not_merge_with: `cranked shell model`、`projected shell model`、`triaxial projected shell model`
- query_expansion: `壳模型` ↔ `shell model`；同时把 CSM、PSM、TPSM 列为候选检索分支，但不视为等价词
- notes: 缺少上下文时列出候选并询问，或按候选分别回答

### cranked shell model

- canonical: `cranked shell model`
- zh: `推转壳模型`
- en: `cranked shell model`
- abbreviation: `CSM`
- aliases: `cranking shell model`、`推转壳层模型`
- category: model
- scope: 旋转参考系中的壳模型计算
- ambiguity: `CSM` 必须结合来源定义；不能仅凭“壳模型”自动选中
- do_not_merge_with: `shell model`、`cranked Nilsson-Strutinsky model`、`projected shell model`、`TPSM`
- query_expansion: `推转壳模型` ↔ `cranked shell model` ↔ `CSM`
- notes: 与 CNS 或其他 cranking 实现并列检索，保留模型假设差异

### projected shell model

- canonical: `projected shell model`
- zh: `投影壳模型`
- en: `projected shell model`
- abbreviation: `PSM`
- aliases: `angular-momentum-projected shell model`、`角动量投影壳模型`
- category: model
- scope: 对本征组态进行对称性恢复或角动量投影的模型
- ambiguity: `PSM` 是模型家族入口；是否包含三轴自由度需看原文
- do_not_merge_with: `shell model`、`cranked shell model`、`triaxial projected shell model`
- query_expansion: `投影壳模型` ↔ `projected shell model` ↔ `PSM`
- notes: TPSM 可作为相关专门候选，但不是所有 PSM 的同义词

### triaxial projected shell model

- canonical: `triaxial projected shell model`
- zh: `三轴投影壳模型`
- en: `triaxial projected shell model`
- abbreviation: `TPSM`
- aliases: `triaxial projected-shell model`、`三轴角动量投影壳模型`
- category: model
 - scope: 显式包含三轴本征组态的投影壳模型
 - ambiguity: 不应由泛称“壳模型”直接确定为 TPSM
 - do_not_merge_with: `projected shell model`、`cranked shell model`、`particle rotor model`
 - query_expansion: `三轴投影壳模型` ↔ `triaxial projected shell model` ↔ `TPSM`
 - notes: 与 PSM 保持上下位关系，不静默视为完全等价

### pseudospin

- canonical: `pseudospin`
- zh: `赝自旋`
- en: `pseudospin`
- abbreviation: `PSS`
- aliases: `pseudospin symmetry`、`赝自旋对称性`、`假自旋`（历史旧译，统一规范为赝自旋）
- category: concept
- scope: 原子核相对论对称性、单粒子能级简并与微观结构
- ambiguity: 赝自旋由量子数 $\tilde{n}=n-1, \tilde{l}=l+1, \tilde{j}=\tilde{l}\pm 1/2$ 定义（如 $2d_{5/2}-1g_{7/2}$ 双重态），与真实自旋不同
- do_not_merge_with: `isospin`、`spin`、`pseudospin doublet bands`
- query_expansion: `赝自旋` ↔ `pseudospin` ↔ `PSS` ↔ `假自旋`
- notes: 用户于 2026-11-07 明确指示规范中文译名为“赝自旋”，杜绝“假自旋”口语化表述

### particle rotor model

- canonical: `particle rotor model`
- zh: `粒子转子模型`
- en: `particle rotor model`
- abbreviation: `PRM`
- aliases: `particle-rotor model`、`particle-plus-rotor model`、`粒子-转子模型`
- category: model
- scope: 价粒子与集体转子耦合模型
- ambiguity: 用户说“转子模型”时还可能指纯 rotor、triaxial rotor 或 quasiparticle triaxial rotor
- do_not_merge_with: `rotor model`、`quasiparticle triaxial rotor model`、`triaxial particle-rotor model`
- query_expansion: `粒子转子模型` ↔ `particle rotor model` ↔ `PRM`
- notes: 泛称“转子模型”命中多个候选时必须列出候选

### quasiparticle triaxial rotor model

- canonical: `quasiparticle triaxial rotor model`
- zh: `准粒子三轴转子模型`
- en: `quasiparticle triaxial rotor model`
- abbreviation: `QTR`
- aliases: `quasiparticle-triaxial-rotor model`、`quasiparticle plus triaxial rotor`
- category: model
- scope: 准粒子与三轴转子耦合的模型表述
- ambiguity: 不同来源可能对 QTR、TPRM、PTR 使用不同命名；必须查看作者定义
- do_not_merge_with: `particle rotor model`、`triaxial particle-rotor model`、`triaxial rotor model`
- query_expansion: `准粒子三轴转子模型` ↔ `quasiparticle triaxial rotor model` ↔ `QTR`
- notes: 只有原文明确等价时才与 TPRM/PTR 合并检索结果

### tilted axis cranking

- canonical: `tilted axis cranking`
- zh: `倾斜轴推转`
- en: `tilted axis cranking`
- abbreviation: `TAC`
- aliases: `tilted-axis cranking`、`倾斜轴推转模型`、`倾斜轴推转方法`
- category: model
- scope: 旋转轴不受限于主轴的推转平均场框架
- ambiguity: TAC 可与不同微观框架组合，缩写本身不确定具体泛函或哈密顿量
- do_not_merge_with: `principal axis cranking`、`TAC-CDFT`
- query_expansion: `倾斜轴推转` ↔ `tilted axis cranking` ↔ `TAC`
- notes: 回答时保留原文的具体 TAC 实现

### multidimensional chirality

- canonical: `multidimensional chirality`
- zh: `多维手征性`
- en: `multidimensional chirality`
- abbreviation: `MχD`（歧义候选）
- aliases: `multi-dimensional chirality`、`多维手征`
- category: concept
- scope: 仅在来源明确使用该表述时作为概念入口
- ambiguity: `MχD` 在当前 Wiki 与部分文献中也用于 multiple chiral doublets；缩写不能脱离原文定义解析
- do_not_merge_with: `multiple chiral doublets`、`chiral doublet bands`
- query_expansion: `多维手征性` ↔ `multidimensional chirality`；`MχD` 同时检索两个歧义候选
- notes: 回答中应指出原文展开形式，不把缩写解析当作科学结论

### angular distribution

- canonical: `angular distribution`
- zh: `角分布`
- en: `angular distribution`
- abbreviation: 无统一缩写
- aliases: `gamma-ray angular distribution`、`γ-ray angular distribution`、`γ 射线角分布`
- category: observable
- scope: 强度随观测角度变化的分布及其拟合
- ambiguity: 实验口语中可能与 angular correlation 混说，但判据与归一方式需按原文区分
- do_not_merge_with: `angular correlation`、`DCO ratio`、`ADO ratio`
- query_expansion: `角分布` ↔ `angular distribution` ↔ `gamma-ray angular distribution`
- notes: 不得因都涉及角度而与角关联静默合并

### angular correlation

- canonical: `angular correlation`
- zh: `角关联`
- en: `angular correlation`
- abbreviation: 无统一缩写
- aliases: `gamma-gamma angular correlation`、`γ-γ angular correlation`、`方向关联`
- category: observable
- scope: 级联辐射方向之间的相关性
- ambiguity: 可能指完整角关联、DCO 或简化两点角关联；具体实现需看上下文
- do_not_merge_with: `angular distribution`、`DCO ratio`、`two-point angular-correlation ratio`
- query_expansion: `角关联` ↔ `angular correlation` ↔ `gamma-gamma angular correlation`
- notes: 与 angular distribution 分开检索，再按来源方法对齐

### linear polarization

- canonical: `linear polarization`
- zh: `线偏振`
- en: `linear polarization`
- abbreviation: 无统一缩写
- aliases: `gamma-ray linear polarization`、`linear polarisation`、`γ 射线线偏振`、`偏振不对称`
- category: observable
- scope: γ 射线电磁性质相关的线偏振测量与分析
- ambiguity: polarization、polarization asymmetry 和具体不对称量并非总是同一字段
- do_not_merge_with: `angular distribution`、`DCO ratio`
- query_expansion: `线偏振` ↔ `linear polarization` ↔ `linear polarisation`
- notes: 回答时保留原文观测量名称与符号

### DCO ratio

- canonical: `DCO ratio`
- zh: `定向关联比`（常用写法仍保留 DCO 比值）
- en: `directional correlation from oriented states ratio`
- abbreviation: `DCO`、`R_DCO`
- aliases: `directional correlation ratio`、`directional correlations of oriented states`、`RDCO`、`DCO 比值`
- category: observable
- scope: 带有 gate 多极性与探测角组合条件的定向关联比
- ambiguity: 数值解释依赖 gate、角度和实验标定
- do_not_merge_with: `angular distribution`、`ADO ratio`、`two-point angular-correlation ratio`
- query_expansion: `DCO ratio` ↔ `DCO 比值` ↔ `R_DCO` ↔ `directional correlation from oriented states`
- notes: 检索与回答必须保留 gate 条件和原文定义

### ADO ratio

- canonical: `ADO ratio`
- zh: `取向核角分布比`
- en: `angular distribution from oriented states ratio`
- abbreviation: `ADO`
- aliases: `angular distribution of oriented nuclei ratio`、`angular distribution from oriented nuclei`、`ADO 比值`
- category: observable
- scope: 取向态或取向核条件下的角分布比值判据
- ambiguity: 不同实验可能采用不同角度组、归一和符号
- do_not_merge_with: `angular distribution`、`DCO ratio`、`angular correlation`
- query_expansion: `ADO ratio` ↔ `ADO 比值` ↔ `angular distribution from oriented states`
- notes: 以具体来源的定义、角度和 calibration 为准

### gamma-gamma coincidence gate

- canonical: `gamma-gamma coincidence gate`
- zh: `γ-γ 符合门`
- en: `gamma-gamma coincidence gate`
- abbreviation: `γγ gate`
- aliases: `coincidence gate`、`gamma-gamma gate`、`gate by <energy>`、`gated by <energy>`、`<energy> gate`、`用 <energy> 开门`、`拉 <energy> 门`、`开 <energy> 门`、`开窗`
- category: data-analysis
- scope: γ 谱学中的符合选门与 gated spectrum 语境
- ambiguity: `gate` 或“开窗”也可能指 energy、time、particle 或软件显示窗口；具体 gate 类型需看上下文
- do_not_merge_with: `time gate`、`particle gate`、`energy window`（无符合语境时）
- query_expansion: `开门/拉门/开窗` ↔ `gate/gated by` ↔ `coincidence gate` ↔ `gamma-gamma coincidence gate`，并保留能量与 gate 类型
- notes: 默认只在 γ 谱学符合语境中映射到 coincidence gating

### wobbling motion

- canonical: `wobbling motion`
- zh: `摇摆运动`
- en: `wobbling motion`
- abbreviation: 无统一缩写
- aliases: `nuclear wobbling`、`wobbling excitation`、`wobbling band`、`wobbling`
- category: concept
- scope: 原子核转动中的 wobbling 概念家族入口
- ambiguity: 泛称 wobbling 不自动指定 transverse、longitudinal 或其他模式
- do_not_merge_with: `signature partner`、`chiral doublet bands`
- query_expansion: `摇摆运动` ↔ `wobbling motion` ↔ `nuclear wobbling`；同时检索 transverse/longitudinal 作为下位候选
- notes: wobbling motion 是上位概念，不能由词面直接确定其下位类型

### transverse wobbling

- canonical: `transverse wobbling`
- zh: `横向摇摆`
- en: `transverse wobbling`
- abbreviation: `TW`
- aliases: `transverse nuclear wobbling`、`横向 wobbling`
- category: concept
- scope: wobbling motion 的一个下位类型
- ambiguity: 不能只凭出现“wobbling”或单一趋势自动归入 transverse
- do_not_merge_with: `longitudinal wobbling`、`signature partner`
- query_expansion: `横向摇摆` ↔ `横向 wobbling` ↔ `transverse wobbling` ↔ `TW`
- notes: 与上位 `wobbling motion` 建立层级关系，同时保留下位判据

### longitudinal wobbling

- canonical: `longitudinal wobbling`
- zh: `纵向摇摆`
- en: `longitudinal wobbling`
- abbreviation: `LW`
- aliases: `longitudinal nuclear wobbling`、`纵向 wobbling`
- category: concept
- scope: wobbling motion 的一个下位类型
- ambiguity: 不能只凭出现“wobbling”或单一趋势自动归入 longitudinal
- do_not_merge_with: `transverse wobbling`、`signature partner`
- query_expansion: `纵向摇摆` ↔ `纵向 wobbling` ↔ `longitudinal wobbling` ↔ `LW`
- notes: 与上位 `wobbling motion` 建立层级关系，同时保留下位判据

### signature partner

- canonical: `signature partner`
- zh: `旋称伙伴`
- en: `signature partner`
- abbreviation: 无统一缩写
- aliases: `signature-partner band`、`signature partner bands`、`旋称伙伴带`
- category: concept
- scope: 具有相应 signature 关系的伙伴带或序列
- ambiguity: partner 关系、splitting 观测量与 inversion 行为是相关但不同的对象
- do_not_merge_with: `signature splitting`、`signature inversion`、`wobbling motion`
- query_expansion: `旋称伙伴` ↔ `signature partner` ↔ `signature-partner band`
- notes: 回答时说明是在谈带关系还是能量劈裂

### signature splitting

- canonical: `signature splitting`
- zh: `旋称劈裂`
- en: `signature splitting`
- abbreviation: 无统一缩写
- aliases: `signature separation`、`signature staggering`、`旋称分裂`
- category: observable
- scope: signature 伙伴序列之间的能量劈裂或相应量
- ambiguity: 具体定义、公式和单位依赖来源
- do_not_merge_with: `signature partner`、`signature inversion`、`gamma-band energy staggering`
- query_expansion: `旋称劈裂` ↔ `signature splitting` ↔ `signature separation`
- notes: 不把观测量自动升级为特定物理机制

### signature inversion

- canonical: `signature inversion`
- zh: `旋称反转`
- en: `signature inversion`
- abbreviation: 无统一缩写
- aliases: `signature-order inversion`、`signature phase inversion`、`旋称次序反转`
- category: observable
- scope: favored/unfavored signature 次序随状态或自旋发生反转的表述
- ambiguity: 必须依据来源定义具体反转量与区间
- do_not_merge_with: `signature splitting`、`signature partner`
- query_expansion: `旋称反转` ↔ `signature inversion` ↔ `signature-order inversion`
- notes: 与一般 splitting 分开记录

### triaxial deformation

- canonical: `triaxial deformation`
- zh: `三轴形变`
- en: `triaxial deformation`
- abbreviation: 无统一缩写
- aliases: `gamma deformation`、`γ deformation`、`非轴对称形变`
- category: concept
- scope: 三个主轴不等价的形状或相应形变描述
- ambiguity: `γ deformation` 的数值与轴约定需跟随来源
- do_not_merge_with: `gamma-soft deformation`、`gamma-rigid deformation`、`superdeformation`
- query_expansion: `三轴形变` ↔ `triaxial deformation` ↔ `gamma/γ deformation`
- notes: γ-soft 与 γ-rigid 描述势能或动力学性质，不是三轴形变的自动同义词

### gamma-soft deformation

- canonical: `gamma-soft deformation`
- zh: `γ 软形变`
- en: `gamma-soft deformation`
- abbreviation: 无统一缩写
- aliases: `γ-soft deformation`、`gamma softness`、`γ softness`、`γ-softness`
- category: concept
- scope: 对 γ 自由度较软的形变或势能描述
- ambiguity: “soft” 的证据与模型定义需按来源判断
- do_not_merge_with: `gamma-rigid deformation`、`triaxial deformation`
- query_expansion: `γ 软形变` ↔ `gamma-soft deformation` ↔ `γ-soft deformation` ↔ `gamma softness`
- notes: 与 γ-rigid 并列检索，不静默合并

### gamma-rigid deformation

- canonical: `gamma-rigid deformation`
- zh: `γ 刚性形变`
- en: `gamma-rigid deformation`
- abbreviation: 无统一缩写
- aliases: `γ-rigid deformation`、`rigid triaxial deformation`、`gamma rigidity`
- category: concept
- scope: 对 γ 自由度较刚性的形变或势能描述
- ambiguity: rigid triaxial 的具体含义和参数约定需按模型来源判断
- do_not_merge_with: `gamma-soft deformation`、`triaxial deformation`
- query_expansion: `γ 刚性形变` ↔ `gamma-rigid deformation` ↔ `γ-rigid deformation` ↔ `rigid triaxial deformation`
- notes: 与 γ-soft 并列检索，不静默合并

## Additional canonical references

以下条目继续用于查重和名称对齐；若与结构化 seed entry 冲突，以 seed entry 的歧义和合并边界为准。

| canonical slug | 中文主名 | 英文与缩写别名 | 备注 |
|---|---|---|---|
| fusion-evaporation-reaction | 熔合蒸发反应 | fusion-evaporation reaction; fusion evaporation | 与具体蒸发道分开记录 |
| mass-region-a130 | A≈130 质量区 | A~130 mass region; A=130 region | “≈”不意味着固定边界 |
| collective-rotation | 集体转动 | collective rotation; rotational motion | 与单粒子转动表述区分 |
| nuclear-vibration | 原子核振动 | nuclear vibration; vibrational motion | 具体振动模式另建页 |
| chiral-doublet-bands | 手征双重带 | chiral doublet bands; chiral bands | “候选手征带”必须保留候选状态 |
| superdeformation | 超形变 | superdeformation; superdeformed shape; SD band | 不自动等同于三轴形变 |
| two-band-mixing | 两能带混合 | two-band mixing calculation; band mixing | 必须写明参与混合的具体两条带或两个同自旋宇称态 |
| linking-transitions | 连接跃迁 | linking transitions; decay-out transitions | 必须写明连接的是 SD-ND、SD-SD 或其他带结构 |
| flip-mode | 翻转模 | flip mode; FM | TW/LW 之间的 separatrix 区域 |
| gamma-band-energy-staggering | γ 带能量 staggering | γ-band staggering; S(J,J-1,J-2) | 与奇 A signature splitting 区分 |
| transition-quadrupole-moment | 跃迁四极矩 | transition quadrupole moment; Qt; Q_t | 与 spectroscopic quadrupole moment 区分 |
| triaxial-particle-rotor-model | 三轴粒子-转子模型 | TPRM; triaxial particle-rotor model | QTR 需按来源展开形式消歧 |
| cranked-nilsson-strutinsky-model | 推转 Nilsson-Strutinsky 模型 | CNS; cranked Nilsson-Strutinsky | 当前应用主要面向忽略配对的中高自旋 |
| covariant-density-functional-theory | 协变密度泛函理论 | CDFT; constrained CDFT; TAC-CDFT | 记录泛函、pairing 与约束 |
| two-point-angular-correlation-ratio | 两点角关联比 | Rac; R_ac; two-point angular-correlation ratio | 与依赖 gate 多极性的 DCO 分开 |
| multiple-chiral-doublets | 多重手征双重带 | multiple chiral doublets; MχD | 多对候选带不等于独立证据重复 |
| pseudospin | 赝自旋 | pseudospin; PSS; 赝自旋对称性 | 历史旧译“假自旋”，规范归一为“赝自旋” |

## 禁止自动合并

- `wobbling-motion` 与 `chiral-doublet-bands`
- `gamma-soft-deformation` 与 `gamma-rigid-deformation`
- `pseudospin`（赝自旋）与 `isospin`（同位旋）或普通 `spin`（自旋）
- 实验“近简并双重带”与理论“手征双重带”
- 某条带的观测标签与其组态或物理解读
- γ 带 staggering 与奇 A signature splitting
- wobbling energy 的趋势与 TW/LW 的完整拓扑定义
- DCO ratio 与两点角关联比 `R_ac`
- CSM、CNS 与 TAC-CDFT 的具体计算实现
- angular distribution 与 angular correlation
- shell model 泛称与 CSM、PSM、TPSM 等具体实现
- `MχD` 的 multidimensional chirality 与 multiple chiral doublets 两种展开
- coincidence gating 与未说明语境的 time/particle/energy window

## 待补充

- 用户常用的中文译名与符号约定；
- 理论模型及缩写；
- 实验判据、探测器阵列和分析方法；
- A≈130 区重点核素及带命名规则。
