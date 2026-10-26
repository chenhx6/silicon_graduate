# 133Ce：原表网络与S(I)有界练习

来源为 Ignasio Wakudyanaye, *Triaxiality and Rotational Bands in 133Ce*。本批直接读原PDF并实际显示视觉核对PDF35/66/67/69（printed pp24/55/56/58），另读PDF63/64关于门控与双峰身份的正文。完整路径及SHA256见 `source-manifest.json`。没有使用outputs或现有知识页作为科学数据源。本练习只有表转录和条件代数，不认证signature partner、wobbling或其它模式。

运行：`python3 tmp/day23-theses/ce133-s-exercise/analyze.py`。脚本只写自身目录，使用Python标准库，无外部依赖。

## 表与身份

`nodes.csv/json` 给完整节点：Band1为13个能级，Band4为8个能级；另保留Table5.3的8个正宇称能级作歧义对照，共29个。`edges.csv/json`给Table5.1全部20边、Table5.2全部28边（13带内，15条去Band1），及Table5.3全部12边，共60边。每条保存初末节点/带、Jπ、初末Ex、Eγ、Iγ原样和括号误差、multipolarity、精确表行locator、能量误差caption规则及闭合残差。

Band1的9/2−能量不在Table5.1的Ei列单列。本练习由两条独立表边一致推得37.2keV（207.4−170.2；592.1−554.9），标记derived而非新实验值；Band1首个S因此为条件结果。Band4的13/2−=832.0在Table5.2后半部直接列出。未人为改变论文的能量零点。

`near-energy-identities.json`列出相差≤1keV的线对，阈值只用于人工复核队列，不用于合并。尤其608.3keV为Band4 19/2−→15/2−带内，608.7keV为Band4 15/2−→Band1 13/2−；能量近似不代表同跃迁。PDF63/printed52明确指出608/609双峰在门控中的交叉贡献，不能凭单门中209/399线就误判它们与608同路径。

缺失Band1 33/2−保留在 `S-results.json` 的not_evaluated列表，不插值、不延伸高自旋S。Table5.3两个19/2+（Ex2733.4/2739.5keV）有不同state ID并分别经881.2/886.8keV衰变，不自动合并为一个signature点。本批不算Band2的S。

## S中央值及设计矩阵

原文PDF35 Eq2.37为

S(I) = [E(I)−E(I−1)] − {[E(I+1)−E(I)]+[E(I−1)−E(I−2)]}/2

= ½E(I−2) − 3/2E(I−1) + 3/2E(I) − ½E(I+1)。

单位keV；不是Ewob，也没有除以spin。`design-matrix-L.json`提供显式14×21矩阵、行ID与列节点顺序，`S-central.csv`/`S-results.json`保存全部可用中央值：

| Band | I | S(keV) |
|---|---|---|
| 1 | 13/2 | 182.10（使用derived37.2锚点） |
| 1 | 15/2 | −216.15 |
| 1 | 17/2 | 277.30 |
| 1 | 19/2 | −318.60 |
| 1 | 21/2 | 345.25 |
| 1 | 23/2 | −342.50 |
| 1 | 25/2 | 351.35 |
| 1 | 27/2 | −369.60 |
| 1 | 29/2 | 410.30 |
| 4 | 17/2 | −175.05 |
| 4 | 19/2 | 49.60 |
| 4 | 21/2 | 100.55 |
| 4 | 23/2 | −166.80 |
| 4 | 25/2 | 247.65 |

其中两位小数是输入中央值线性组合的算术精度，不表示实验测量精度。终点外推、缺33/2所需窗口和其它不可评估位置均明确列出。

## 闭合与控制

`closure-summary.json`逐条列非零残差；Band1 29/2−→25/2−为+0.2keV；Table5.3前一个19/2+→15/2+为−0.5keV，后一个为0。其余零或0.1–0.3keV级差异保留，不按能量闭合强修原表。没有输入Ex协方差及其提取过程，不能把caption的Eγ误差上界当σ来做闭合χ²或宣判一致/不一致。

`controls.json`对14个S各完成：能级四项线性组合与中心间隔减两旁间隔均值的独立实现一致；加常数123.456keV的平移不变；理想E=A I(I+1)+C转子给S=0；逐能级有限扰动导数与L相同。`direct-gamma-gap-crosschecks.json`另用直接表列的相邻ΔI=1三线重算12个S，并与四能级结果精确相等；Band1高自旋缺失的两条ΔI=1线未造数。控制只检验公式和转录的内部条件，不证明能级身份或物理模式。

## 还需什么才能给实验Cov(S)

必须获得适用于同一level scheme的Cov(E)，然后Cov(S)=L Cov(E) Lᵀ。需要原能量拟合/校准统计和系统误差、共用参考跃迁和共享节点产生的相关性、双峰拟合协方差、网络约束及能量零点约定。`transition-incidence-A.json`给60×29 A，每边为+Ei−Ef，可用于在明确锚点/gauge后另做带Cov(Eγ)的网络拟合；本练习未做拟合，不将Ex中央值和Eγ当两组独立观测重复计权。

Table5.1 caption的Eγ误差依Iγ分组：Iγ≥10时within0.3keV，Iγ<10时up to0.7keV；Table5.2/5.3按Eγ<1000或>1000分组为within0.3/up to0.5keV。均未给完整逐线σ及相关矩阵，不应直接转换成高斯CI。Iγ统一相对170keV线，归一化有共享误差；这些强度误差不直接作为能级S的不确定度。

即使条件示例假定全部能级独立同方差σ²，Var(S)=5σ²且邻近S相关，这也只是代数假设，不能视为论文给出的实验误差。本批输出不含实验CI、模式概率、δ、寿命、g或beamtime。所有转录和派生结果保留needs_review:true；未修改canonical/raw/outputs/PLAN/Git。
