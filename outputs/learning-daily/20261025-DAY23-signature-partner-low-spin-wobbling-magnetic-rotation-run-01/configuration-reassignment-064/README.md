# Day23 B槽：冻结实验层的组态重指派

本包给出可执行的**候选框架与窄条件控制**，未完成真实133Ce/Au作者producer比较。所有科学条目needs_review:true，不制造实验CI、δ、寿命或最终模式判决。

先读 [derivation.md](derivation.md)，数值和输入见 [verification.json](verification.json)，逐候选/逐观测可识别性见 [reassignment_matrix.json](reassignment_matrix.json)。执行：`python3 tmp/day23-theses/configuration-reassignment/verify_reassignment.py`。只使用Python标准库，119项检验通过；pass只针对给定代数，不认证模型充分性。

## 冻结对象与原带身份

- **133Ce Band4**：原Table5.2的832.0keV 13/2−到3616.2keV 27/2−、13带内+15带间边，全部保留；Band1及两带共21节点/48边的公开表转录保存在frozen-published-Ce-D.json。Iγ是相对光子强度，不等于原符合计数；原N、AD/P response和Cov未取得，不能声称重放了它们。原PDF和转录不改。
- 原九轨道QTR的Band1/4均主要#18≈ν[514]9/2−，Band4低spin有Kl≈13/2、额外Rl≈2的**模型**解释。#17≈ν[523]7/2−、#16≈ν[532]5/2−本来就在空间内，且原Band4已含其混合；另找它们主导的同H本征序列是待验证假说，不能给既有混合成分换名便称新解释。
- **187Au身份更正**：Sensharma Band2是原wobbling候选，Band3原本是associated unfavoured signature partner，而非原wobbling带。故实际B槽主对照采用已明确的Band2：同#19内禀组态的phonon解释，对QTR #21主导的轨道激发解释；Band3只作identity/SP/潜在Pt归属的附加对照。把Band3改核素为Pt会改变谱线身份，超出configuration-only。

## 候选可行性与需要新增的预测

| 候选 | 当前能支持什么 | 必须先过的门／可证伪向量 |
|---|---|---|
| Ce原九轨道TiP | 原能量/S及部分rE2支持；FA的某些δ更近，两模型rM1均有边界 | 原实际transition output、表图差异、完整振幅与全部分支；不能总称全观测通过 |
| Ce #17或#16主导轨道激发 | 轨道与π/半整数sector存在；形式可构造 | 同H本征态/wholeband的Ex与S、能量零点/λn/Δn、波函数/径向/EM振幅；裸ε差不能当带头预测 |
| Ce νh⊗π² 3qp | 数目奇偶/某些π和spin耦合允许，不代表低832keV能量可行 | proton pair breaking、blocking、残余力、相同Jπ/Ex和伴随3qp连接；超出原1qp空间，须明确新增模型 |
| Au Band2轨道激发对原wobbling | Guo已有#21对#19主导内容的源解释，不篡改已测计数/δ | 两发表模型H/shape/MoI/算符不同；先共同producer，不把二者称纯mapping受控对比 |
| Au Band3普通SP/其它配置/MR候选 | 只保原SP解释及归属争议；小δ不唯一指MR | 核素identity、同门全部伴随、完整实际particle/hole配置和B(M1)spin演化；没有新shears态或磁矩可填 |

## 数值控制最重要的结果

纯j Landé计算与独立CG自旋展开一致：选gs=.6free时，νh11/2的g_j=−.208691，**Ω5/2、7/2、9/2相同**。渐近Nilsson |ΛΣ⟩计算给出的不同gK属于另一个模型极限，不能当实际混合QTR磁预测。单hole的g_j不另翻号。

轴对称good-K的带内M1/E2比必须含K²；脚本以精确Fraction阶乘CG和闭式两路核对。采用人为Q0=1eb参考尺度的4个轴向控制，在I17/2给115.46、22.22、9.98、24.85 μN²/(e²b²)。它们仅说明可能的几何/磁算符敏感性和退化；不是实际Ce拟合，不可与Table6.11的**跨带**out/in直接对照。

真实δ符号/量级预测尚缺signed EM振幅，matrix中保持null。各候选冻结Jπ后，最低阶允许M1/E2的集合不会因换标签而改变；精确K禁戒只在另加轴对称good-K条件下成立。三轴混合/BCS可打开连接；3qp→1qp不是任意一体算符下的普遍零。

τ和绝对B是重要**联合**holdout候选，不能保证单独区分全部模式。完整BR/α、DSAM feeding/stopping、相对归一和δ的协方差不可缺；原用于调参的量不重复算holdout。下一可证伪问题为：在固定同一实验D与已冻结模型/算符下，替代态能否同时匹配原Ex网络，并对预先排除于定标的完整同母态退激/绝对强度或静态矩向量给出与原解释可分的预测？当前尚未取得这些实际数值向量，不虚报功效或CL。

## 来源与阅读范围

本次定向实际读原Ce PDF98/99/102/104/107/111/112；PDF99/104重新大图视觉核。此前Table5.1/5.2已直接读与视觉核；此次冻结其既有直接原表转录，未把日报输出当科学源。source_contract及精确locator在reassignment_matrix.json。

Guo/Sensharma原身份与模型空间沿既有canonical source/direct-reading合同，不新称全文重读。没有新外部source、raw修改、canonical/Git/PLAN改动，也不推进Day24或Day25。phys-model技能用于量纲、对称性和极限控制；用户限定本包仅tmp，故不运行Git或发布流程。
