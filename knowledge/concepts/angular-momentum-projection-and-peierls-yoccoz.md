---
type: concept
title: "角动量投影、非正交组态混合与转动惯量边界"
aliases: [角动量投影, AMP, 旋转对称性恢复, 重整化能谱, Peierls-Yoccoz惯量, 范数核, 哈密顿核, 高斯重叠近似, GOA, 投影壳模型]
created: 2026-11-02
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
tags: [angular-momentum-projection, amp, peierls-yoccoz, rotational-bands, symmetry-restoration, gaussian-overlap-approximation, goa, tpsm]
---

# 角动量投影、非正交组态混合与转动惯量边界

## Definition

### 物理全景：从破缺对称性内禀波包到实验室系纯自旋态

必须区分旋转不变的完整哈密顿量与破缺对称性的平均场参考态。
在这里的旋转不变框架下，完整 \(H\) 与旋转及角动量对易；
变形平均场 \(h\) 或参考态 \(|\Phi\rangle\) 可以不具有该对称性，
并不表示完整 \(H\) 被强制改成 \([H,J^2]\ne0\)。
Shimada论文PDF24的Eq.2.42明确使用 \([H,P^I_{MK}]=0\)
（[[shimada-2015-angular-momentum-projection-thesis]]）。

参考态一般包含多种自旋成分；哪些成分实际非零，由其连续与离散对称性决定，
不能先验写成必然含全部自旋。投影可构造好角动量态，不自动给出完整多体问题的精确本征解。

本轮直接依据Shimada原件PDF23–26、41–42的投影与变分定义；
旧稿所列教材和Peierls-Yoccoz原始文献未在本轮逐篇重核。
AMP的三个层次应分开：
1. **转动对称性投影算符 $\hat{P}_{MK}^I$**：
   Wigner D函数与旋转算符须按同一约定做群积分。一般的 \(P^I_{MK}\)
   是投影分量，满足 \((P^I_{MK})^\dagger=P^I_{KM}\)，不是每个分量各自都厄米；
   对角分量求和才给整个自旋I子空间的正交投影。K也不等于实验室M。
2. **投影能量与动力学**：
   单一轴对称K=0参考态的能量可写为
   \[
   E_I=\frac{\langle\Phi|HP^I_{00}|\Phi\rangle}
   {\langle\Phi|P^I_{00}|\Phi\rangle}.
   \]
   这不恒等于 \(E_0+A I(I+1)\)。非轴对称态通常还要K混合、求解
   \(H^I g=E_I N^I g\)，能谱取决于哈密顿核、参考态和试探空间。
3. **惯量与试探空间**：
   静态投影、推转态投影、多推转混合及线性响应的惯量不能不加条件互换。
   旧稿“Peierls-Yoccoz惯量必比刚体小30%”没有本页直接证据，撤回。
   时间反演奇分量（time-odd）不是空间负宇称分量；恢复旋转也不等于做了粒子数投影。

---

## Necessary Assumptions

### 严格投影数学积分与高斯重叠近似（GOA）

### (1) 轴对称K=0重叠核的约化
对于具有轴对称K=0的参考态，重叠核中的两个轴向角积分可先做掉。
在该核计算中，并采用 \(\hbar=1\) 及一致的旋转约定，有：
\[
\langle\Phi|P^I_{00}|\Phi\rangle=
\frac{2I+1}{2}\int_0^\pi d\beta\,\sin\beta\,d^I_{00}(\beta)
\langle\Phi|e^{-i\beta J_y}|\Phi\rangle.
\]
这里不是完整Hilbert空间中任意态都适用的一维算符替换。
整数I时 \(d^I_{00}\) 等于I阶勒让德多项式，不是始终为一阶：
$$d_{00}^I(\beta) = P_I(\cos\beta)$$

---

### (2) 范数核 $n(\beta)$ 与哈密顿核 $h(\beta)$
定义转动重叠函数：
- **范数核（Norm Kernel）**：
  $$n(\beta) = \langle \Phi | e^{-i \beta \hat{J}_y} | \Phi \rangle$$
- **哈密顿核（Hamiltonian Kernel）**：
  $$h(\beta) = \langle \Phi | \hat{H} e^{-i \beta \hat{J}_y} | \Phi \rangle$$

当 \(\langle J_y\rangle=0\)、小角累积量展开可控时，可以研究局部高斯重叠近似
（下式仍取 \(\hbar=1\)）：
$$n(\beta) \approx \exp\left( - \frac{1}{2} \langle \hat{J}_y^2 \rangle \beta^2 \right)$$
\(h(\beta)/n(\beta)\) 的小角系数还需由相应H与参考态确定；
不能只给 \(\langle J_y^2\rangle\) 就固定整个能量核，或把局部高斯近似
当作整个紧致转动群上的严格重叠。本文不重新认证旧教学toy所取的能量核。

---

### (3) 投影能谱积分公式
对偶自旋 $I = 0, 2, 4, 6, \dots$：
$$N_{00}^I = \frac{2I + 1}{2} \int_0^\pi d\beta \sin\beta \cdot P_I(\cos\beta) \cdot n(\beta)$$
$$H_{00}^I = \frac{2I + 1}{2} \int_0^\pi d\beta \sin\beta \cdot P_I(\cos\beta) \cdot h(\beta)$$

在上述单参考态K=0条件下，投影能量为：
$$E(I) = \frac{H_{00}^I}{N_{00}^I}$$
激发能为 $\Delta E_x(I) = E(I) - E(0)$。

---

## Discriminating Observables

联合比较能谱、定义明确的运动学/动力学惯量、B(E2)/B(M1)、配对和组态变化。
投影范数及GCM幅度是模型构造的一部分，不是直接测量的独立实验概率。

非正交生成基中的系数满足 \(g^\dagger N g=1\)，不是一般的
\(g^\dagger g=1\)。Shimada PDF26 Eq.2.59与PDF42 Eq.4.6使用
\(f=\sqrt N g\) 构造规范化集体幅度；该分布仍依赖所选生成空间。
精确零范数冗余与小而非零本征值的数值截断不同，后者需要稳定性检查。

## Supporting Evidence

### 原件案例而非普适惯量定律

Shimada PDF76–77、105–106比较了单态投影与multi-cranked混合：
164Er、40Mg、152Dy的自旋依赖有不同表现，混合可改善所测试的惯量行为。
164Er的g/s交叉在计算中约I=18，比实验高约3hbar，s带惯量也偏高；
不能把成功描述趋势写成所有状态和矩阵元都精确符合。
40Mg在该论文中没有可用于验证转动谱的实验数据（PDF54），它是模型预言案例。

### 三来源阶段综合：同一比较问题不等于同一输入

| 来源 | 输入与方法 | 可支持的比较及边界 |
| --- | --- | --- |
| [[li-2016-algebraic-collective-core-quasiparticle-thesis]]，PDF34、60–62 | QTR按奇核谱调整，QTD核芯取偶偶邻核约束 | 拟合对象不同；刚化是作者模型解释，不是直接势能测量 |
| [[gu-2007-tsd-tidal-waves-thesis]]，PDF57–65、79–80、92–94 | TSD倾斜解与粒子—空穴竞争；A110固定配对/化学势策略 | TSD不单独确认wobbling；能量和电磁量的比较精度不同 |
| [[shimada-2015-angular-momentum-projection-thesis]]，PDF24–26、41–42、98–101 | 对称性恢复、非正交混合；部分三轴参数为寻找双带而搜索 | 好角动量不保证唯一运动模式，参数搜索不等于盲预测 |

这是本轮三个理论来源的跨源综合，不把它们当三次独立实验或据此排名模型。
首先区分调参量与检验量、对称性与动力学、已测矩阵元与作者解释，再比较结果。

### 历史教学toy接口：本轮未执行

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/angular_momentum_projection_amp_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `amp` 命令。

以下保留调用入口，不是本轮新运行或对代码物理正确性的认证：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py amp --max-spin 10 --jy2 35.0 --a-rot 0.025 --json
```

旧稿所列0.0142、0.0958等数值及“泊松分布”未在本轮重验，
不再作为物理实证使用。以手选 \(A_{rot}\) 与重叠核构造的toy，
不能证明无需动力学输入就微观导出严格刚体谱。生产脚本本轮未改动或复验。

---


## Counter-evidence and Competing Interpretations

1. PAV是先变分再投影；VAP是对投影能量变分。后续K混合或有限生成坐标混合
   不自动等于完整VAP。旧稿中中英文顺序曾写反，此处订正。
2. GOA是近似而非严格高斯定理；弱形变、有限群角区间和多峰重叠都需另核。
3. 单参考态空间、配对处理、norm cut-off和所选生成坐标会限制结果。
   类声子谱或近简并双带需结合电磁量、组态及竞争解释，不由投影代数唯一确证。

## Our Current Position

AMP是恢复角动量与组织变分试探空间的方法。对称性可严格处理，
但能量、惯量和模式解释仍受动力学、截断与数据约束；不把方法名称当正确性认证。
本轮只核原件关键页及声明过的非正交矩阵代数例，没有运行作者HFB/AMP代码或PDM。

## Sources

- [[shimada-2015-angular-momentum-projection-thesis]] — PDF23–26、41–42、54、76–77、98–106，本轮直接来源。
- [[a130-rewrite-projection-selection-and-metric-truncation-20261113]] — K/M、离散选择定则、范数与能量平移的既有边界。
- [[tpsm-3d-angular-momentum-projection-diagonalization]]
- [[rotational-moments-of-inertia-and-spin-assignment]]
- [[nilsson-deformed-shell-model-dynamics]]
