**BM-II 历史条目引用归属已更正。** 修改仅涉及
[book-bohr-mottelson-nuclear-structure-vol2.md](/workspace/wiki/knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md)
及本审计目录；BM2-1–4逐字保留。此次是修订稿引用准确性核查，不授予新的课程、整章或整书阅读学分。

| 条目 | 处置 | 可保留的原书内容／撤回边界 |
|---|---|---|
| BM2-5 | 修正公式记号及机制归属 | 保留弱混合的 Mikhailov E2 有效强度关系。原书用 \(a_2,z_2\)，并明确相同自旋依赖可来自不同耦合；删除“唯一Coriolis机制＋普遍压低”的表述。PDF173、181／printed151、159。 |
| BM2-6 | 撤回正向物理断言 | 旧 Davydov–Chaban 四次式、参数和“成功解释多类能带”没有建立原书对应或可复现任务输出。旧§4-2页码实际指向§4-5起始及其后页段。 |
| BM2-7 | 收窄到条件模型 | 保留轴对称粒子–转子 Coriolis 项、\(\Delta K=\pm1\) 和 \(K=1/2\) 的签名项；删除一般三对角对角化“严格证明”K弥散／顺排的外推。PDF223–224／printed201–202，Eqs4A-7–4A-10。 |
| BM2-8 | 撤回正向物理断言 | 已核高自旋纯转子页不能支撑所写TSD/ND退激、穿透及低自旋终止计算。没有据此否定其它文献中的退激机制。 |
| BM2-9 | 保留多极矩展开，撤回惯量符号判据 | Eq4-190涉及电荷多极矩及四极分量二阶贡献；不提供旧惯量修正式或“正β4必然稳定TW”等结论。PDF161／printed139。 |
| BM2-10 | 保留定性方法，撤回固定数值 | 原书分离平滑能量与壳结构贡献，并强调壳能极小是否形成形状异能态还取决于平滑能量。旧固定自旋阈值和10–15 MeV降能未获支持。PDF620、627／printed598、605。 |
| BM2-11 | 改回作者的有条件讨论 | 原书说配对随旋转减弱，并提出可能较突发的转变；对当时A≈160、I≈20的联系仍是试探性的。删除普适平方根隙函数、30–40ħ阈值和统一二级相变。PDF64／printed42。 |
| BM2-12 | 修正参数字典及分支比 | 原书给 \(\epsilon_2,c(I),h_2\)；不可直接等同于 \(a_2,z_2\)。删除无来源换算及20%–35%普遍压低；条件分支比以本次代数推论标出。PDF181、183–184／printed159、161–162。 |
| BM2-13 | 撤回正向物理断言 | 固定PES极小坐标和交叉频率缺少核素、输入、输出或原书定位。一个可能的示意Routhian项不能证实这些数值。 |

因此是**六条保留可核部分并实质改写，三条撤回原正向断言**。没有仅调整 review 标签。也没有把找不到来源的公式改贴“任务模型”标签来保留为事实：本次未查得它们独立的模型定义或producer，至多是需另行定义、另行验证的历史模型设想。

**分支比更正。** 图像确认原书 Eqs4-230–4-231 为
\[
B=2M_1^2 C_{if}^2(1+a_2\Delta_{fi})^2,\qquad
a_2=-M_2/M_1,\qquad z_2=\frac{2a_2}{1-4a_2}.
\]
本次由此推得
\[
\frac{B(2_{K=2}\to0_{K=0})}{B(2_{K=2}\to2_{K=0})}
=\frac7{10}(1-6a_2)^2
=\frac7{10}\left(\frac{1-z_2}{1+2z_2}\right)^2.
\]
这不是声称原书另印了一条相同比值公式。精确阶乘CG求和给出两个几何因子 \(1/5\)、\(2/7\)；六组有理数检查及零修正极限通过。负、正小参数给出不同修正方向，不支持无条件压低。原书的耦合矩阵元关系则是 \(h_2=\epsilon_2\Delta E\)，其中 \(\epsilon_2\) 另有定义。

英文稿可保留的窄表述，例如：

> Within the effective band-mixing description, different couplings can produce the same spin dependence of the E2 matrix elements; this dependence alone does not identify a unique coupling mechanism.

定位：BM-II printed151，Eq4-211后文。此句是准确转述，不是书中逐字引文。配对、壳修正及多极矩内容应同样保留原书条件，不能继续引用被撤回的普适函数或无对象数值。

本次只作旧引用范围内的定位和选页复核；关键词扫描不计连续阅读。“未建立支持”不等于已经穷尽全书或外部文献，亦不意味着相关现象在其它模型中不可能。

审计材料：

- [claim-audit.json](/workspace/wiki/outputs/l4/20261106-odd-ba-manuscript-revision/bm2-source-attribution/claim-audit.json)：九条逐项旧稿、新稿、处置、物理／印刷页及图像核查状态。
- [mikhailov-algebra-check.json](/workspace/wiki/outputs/l4/20261106-odd-ba-manuscript-revision/bm2-source-attribution/mikhailov-algebra-check.json)：精确代数检查，无核素输入或参数拟合。
- `source-before.snapshot.txt`：被更正旧稿的追溯副本；其中旧断言已被本次更正取代，不得作为科学引用。
- `inspection/`：限定页图像；实际视觉核对与仅生成图像分开登记。

原件SHA-256保持
`46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a`。
其它知识页、历史回执、index、raw、PLAN和get-paper均未修改；未提交。
