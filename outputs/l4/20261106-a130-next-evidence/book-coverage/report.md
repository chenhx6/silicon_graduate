**四书阅读覆盖对账完成；新增一个实际完成的六页单元。**

长期知识与完整阅读记录见 [book-reading-coverage-reconciliation-20261106.md](/workspace/wiki/knowledge/research-notes/book-reading-coverage-reconciliation-20261106.md)。本输出是给 parent 的审计回执，原 `book-corpus-coverage-ledger.md` 保持原样。

核对了四部原件的 SHA-256、33条相关来源／阅读记录，以及49个目标分包。原始318包中，BM-II占20包、Greiner占10包、Petrache占9包；Casten第一版不在原分母内，由Nov2增补追加10包，当时总数变为328。当前目录39个PDF包括后来新增的Casten不同版次和译本，不据此自动迁移课程或合并学分。

| 书 | 原件物理页数 | 找到的声明范围并集 | 重叠页数 | 对账状态 |
|---|---:|---:|---:|---|
| BM-II | 772 | 217页，详见区间表 | 7 | Nov3已有多份选段／章节局部阅读回执；212–218重复。粒子–振动回执存在公式与页码错配。 |
| Greiner | 399 | 164–169，6页 | 0 | Nov5 source记录了实际定向回读；Nov4 `complete` 只是技能交付，未产生页段学分。 |
| Casten 1990 | 391 | 283页，含选段外包络／空白／参考文献 | 32 | 第一版独立增补；第10章正文350–378，与回执窗口350–385分开。 |
| Petrache 2025 | 339 | 20–91、94–337，316页 | 18 | Nov3回执涉及全部17章，应保留全章／逐页阅读声明；第5／11章仍偏选图或选公式。第13章对象页码须由印刷页转换到物理页。 |

这些是**记录范围并集与重复页位置**，不是科学阅读完成率。全章阅读声明、选段阅读、原文对象核查和生成模块在机器表中分别列出；本次没有仅凭回执给原40页包或整章新增完成状态。

具体定位修正：

- Petrache Fig13.1–13.6 的物理页是 **278、279、280、283、285、287**；回执写的259、260、261、264、266、268是印刷页。PDF259实际属第12章。图13.1及错页已视觉核对。
- Casten 第10章正文为 **PDF350–378／printed335–363**；379／385空白，380–384为参考文献。保留原36页阅读窗口，避免把它全计为章节正文。
- BM-II 粒子–振动回执把PDF450配给6-258–261、PDF456配给6-276；实际对应页面可见6-223c/d、6-230。回执存在不等于逐式定位已闭合。
- BM-II 振动／求和规则回执额外列出的483–485不在其声明阅读区间里，不能自动填满中间缺口。

**新增实际学习。** `U-B25-002-E2-20261106` 完整读取 BM-II **PDF66–71／printed44–49**；六张页面图像均检查，覆盖Eqs4-66–4-73、Fig4-5图轴及跨页图注。第66页与已有声明重叠，67–71位于已找到的旧范围声明之外。§4-3b后半和引用的外部例题仍未核销。

实质知识增量是固定 \(K\) 与 \(K=I\) 两条高自旋路径的区别：
\[
Q_s/Q_0\to-1/2\quad(K\text{固定}),\qquad
Q_s/Q_0\to1\quad(K=I).
\]
由精确CG平方复核了有限自旋 \(\Delta I=1\) 与 \(\Delta I=2\) 两支的E2强度比、其 \(4K^2/I^2\) 渐近、方向因子5、\(K=0\) 的 \(10/7\) 和选择零。对应推导与适用条件完整写入知识页；没有核素拟合或新实验结论。

首次SymPy导入失败后使用标准库精确有理数／阶乘求和，未安装依赖；代数检查内部耗时约0.0023秒，全部通过。草算分母的 \(I-1\) 已由独立CG和正确约分改为 \(I+1\)，记录为学习者修正。

下一连续未核销单元为：BM-II **72–75**；Greiner **170–175**；Casten第一版 **156–163**；Petrache **247–251**。Petrache该范围已有选公式记录，下一步是完成连续单元，不能宣称从未看过。

交付文件：

- [coverage-reconciliation.json](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/book-coverage/coverage-reconciliation.json)：原件身份、33条记录、范围并集／重叠、库存新增及下一单元。
- [interval-evidence.csv](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/book-coverage/interval-evidence.csv)：紧凑逐记录表。
- [packet-crosswalk.csv](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/book-coverage/packet-crosswalk.csv)：49包与阅读证据交叉表。
- [locator-audit.json](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/book-coverage/locator-audit.json)：实际锚点核查及新单元的视觉对象清单。
- [bm2-unit-algebra.json](/workspace/wiki/outputs/l4/20261106-a130-next-evidence/book-coverage/bm2-unit-algebra.json)：精确代数结果及失败／修正记录。
- `inspection/`：新单元六页与少量定位核查图像。

没有修改旧账本、原件、其它知识页、index、handoff或其它会话的数值工作，没有提交。目录名与实际文件时间分别保存；文件抽取、技能卡和测试成功均未替代阅读证据。
