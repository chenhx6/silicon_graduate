---
type: research-note
title: "四部核结构书的阅读覆盖对账与 BM-II 带内 E2 连续单元"
aliases: [book-reading-coverage-reconciliation-20261106]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [book-corpus-coverage-ledger, book-bohr-mottelson-nuclear-structure-vol2, book-greiner-nuclear-models, book-casten-nuclear-structure-simple-perspective, book-petrache-chirality-and-wobbling]
created_from: user-authorized-library-reading-reconciliation
promotion_target: knowledge/synthesis/book-corpus-coverage-ledger.md
tags: [books, reading-coverage, source-locators, rotational-e2, particle-core, evidence-boundary]
---

# 阅读覆盖对账与一个实际完成的 E2 单元

## Research Trigger

Nov 2 的 [[book-corpus-coverage-ledger]] 固定了 33 个 PDF、12,076 个物理页和 **318 个 40 页工作包**，但不能代表 Nov 3–6 此后没有阅读。此次只核对 BM-II、Greiner、Casten 第一版和 Petrache 编著本的原件、后续阅读回执及知识记录；原账本不改写，留待 parent 整合。

本次新增完成的连续单元为 **BM-II 物理 PDF 66–71／印刷 44–49 页**，编号 `U-B25-002-E2-20261106`，属于原 `Q-B25-002`。六页全部读取并核图；其中 PDF66 与旧回执声明的范围重叠，67–71 五页位于此次找到的旧区间声明之外。没有据此核销整个 40 页包、§4-3b 后半、整章或整本。

## Grounded Evidence

**身份与分母。** 下列四个原件的实测 SHA-256、物理页数均与各自既存来源一致。B02／B10／B25 是原始账本的稳定 ID，不按当前目录重新排序。

| 原件 | 原队列身份／物理页数 | 实测 SHA-256 |
|---|---|---|
| BM-II：`raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf` | B25；772 页；20 包 | `46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a` |
| Greiner：`raw/books/Nuclear Models (Walter Greiner, Joachim A. Maruhn) (Z-Library).pdf` | B10；399 页；10 包 | `db5e43efaa80877822540bf0caae9be93d54d5499c5df89faae69769e6f77091` |
| Petrache：`raw/books/Chirality and Wobbling in Atomic Nuclei.pdf` | B02；339 页；9 包 | `787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2` |
| Casten 1990：`raw/books/Nuclear Structure From A Simple Perspective Casten.pdf` | B34-added-casten；391 页；另加 10 包 | `9028649fb9fad55d6d624b88ef8bf8487e8462c07596d9a42bd6117552fa3ea9` |

来源卡分别为 [[book-bohr-mottelson-nuclear-structure-vol2]]、[[book-greiner-nuclear-models]]、[[book-casten-nuclear-structure-simple-perspective]] 和 [[book-petrache-chirality-and-wobbling]]。本次完成单元直接绑定 [BM-II 原件](</workspace/wiki/raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf>)，定位为物理66–71／印刷44–49页；本页的公式与解释不以生成的技能卡为来源。

Casten 第一版**不在最初 318 包中**。既有 `20261102-casten-book-corpus-addendum.json` 单独追加 B34 的 10 包，使当时队列为 328 包。此次核对的目标交叉表为 **39 个原包＋10 个 Casten 增补包＝49 包**，并非全馆只剩 49 包。

当前 `raw/books/` 文件名盘点为 39 个 PDF，原 33 路径均仍存在；相较原快照新增 Casten 第一版、文件名标为 `edition2` 的 488 页英文 PDF，以及四个译本／排版衍生 PDF（369、369、472、140 页）。这六份新增文件的大小、页数和哈希已记录。不同版次和翻译不互相转移阅读学分；此处没有对原 33 份全部重做哈希盘点，也不把新的目录文件数自动变成新的课程分母。

**证据层级。** 本次检查了 33 条与目标书相关的回执／来源范围记录，采用以下区分：

- `record-verified`：原件身份及阅读记录的存在、范围或锚点得到核对；不等于本次重新读完所列区间。
- 全章阅读声明：保留回执中 full chapter、page-by-page 等实际措辞；区别于只列章名或只核公式页。若对象核查和习题／回忆记录不完整，不自动变成原账本六项标准下的 `chapter-complete`。
- 选段阅读与 `source-checked`：只对应明确页段、公式或图表；若范围是外包络，不假设其间每页都已读完。
- generated module／skill delivery／test pass：不产生阅读学分。Greiner Nov 4 的 `complete` 是技能交付完成；Casten 的整书文本抽取也只是访问与导航记录。
- 此次 `study-complete` 只授予新分配的六页单元；既有回执不因来源卡的 `updated: 2026-11-02` 或 `reading_depth` 标签而被忽略，也不被整体升级。

**区间与重叠简表。** 下表全部为一基物理 PDF 页。页数是**记录范围的集合运算**，不是完成率；包含选页外包络、空白或参考文献的情况仍保留。

| 书 | 找到的阅读记录及范围 | 对账结论／重叠 |
|---|---|---|
| BM-II | Nov 3：高自旋选页 197、199、201、205、207、209、211–218；有限自旋核查 212–218；附录选页 219–230；M1 76–80；转动–内禀耦合 167–196；Nilsson 233–260、265–277；粒子–振动 438–457；振动／求和规则 383–437、64–66、620–656。 | 与 Nov 2 的 212–214 合并后，声明范围共 217 个不同物理页；212–218 七页重复出现。若干公式 locator 有冲突，不能据完整范围直接认证所有公式。新六页单元另列。 |
| Greiner | Nov 4 技能生成回执无连续阅读区间；当前 source 明记 Nov 5 重读 164–169／印刷145–150。 | 保留六页选段阅读记录；此次图像核对 164、166、169 证明页码／节标题对应。六张技能卡不是六章读完；未重做 parent 的转子矩阵核验。 |
| Casten 1990 | Nov 2：source 选段 32–42、201–245、262–285、290–335；回执 43–59、62–153、262–285、328–347。Nov 3 第10章回执 350–385。 | 声明范围并集 283 页；262–285 的24页及328–335的8页重叠。source 的“第8章”选段尾部跨入第9章。全书 `deep-read` 标签不覆盖这些缺口。 |
| Petrache 2025 编著本 | Nov 3 的16份回执涉及17章：1／8合在一份；2、3、6有章正文／逐页阅读描述；4、7–10、12–17等有 full-chapter 声明；5、11仍明确偏选图或选公式。 | 不能继续按 Nov 2 摘要说后续各章毫无记录。声明正文区间并集为20–91、94–337（316页）；92–93已明确分类为参考文献。与旧选段重复18页。保留全章声明，但本次只作记录核验和有限锚点检查，不新认证全书或所有图表。 |

逐回执的路径、文件哈希、范围类型、知识回写文件是否存在，以及全部49包的交叉表，保存在本次输出 `interval-evidence.csv`、`coverage-reconciliation.json`、`packet-crosswalk.csv`。这些是阅读审计凭据；科学公式仍以本页所列原书及 locator 为依据。

**实际发现的 locator 边界。**

| 记录 | 原声明与原件对照 | 应怎样保留 |
|---|---|---|
| `20261103-petrache-ch13-budaca-spin-dynamics.json` 的 `rendered_pages` | Fig.13.1–13.6 被标在“PDF259／260／261／264／266／268”。它们实际是**印刷页码**；物理页为278／279／280／283／285／287。PDF259 实为第12章、印刷240；PDF278 的图像明确为 Fig.13.1、印刷259。 | 第13章总体范围275–291正确；修正对象定位，不能据此断言整章文字从未读过。 |
| `20261103-casten-ch10-experimental-design.json` | 350–385 是所声明的阅读窗口；第10章正文实际为350–378／印刷335–363，379与385为空白，380–384为 References。 | 章节正文29页与36页阅读窗口分开计；不丢弃已声明的参考文献阅读，也不把它们算入章节正文。 |
| `20261103-bm2-particle-vibration-coupling-rpa.json` | 将 PDF450 配给 Eq.6-258–261、PDF456 配给 Eq.6-276；实际 PDF450／印刷428可见6-223c/d，PDF456／印刷434可见6-230。 | 438–457 的文字阅读声明保留；相关逐式“已核”说法不能直接继承，需重新定位。 |
| `20261103-bm2-collective-vibrations-and-sum-rules.json` | `rendered_pages` 另列483–485，但它不在该回执声明的64–66、383–437、620–656中。 | 作为额外对象核查声明记录，不把438–619之间自动补成连续阅读。 |

另核到了正向锚点：Petrache 物理146–147的 Table6.1、164的 Fig7.3、239的第11章开头及245的 Fig11.3；BM-II 的169含4-200–203、241含5-10、384含6-90、439含6-204–205。这些核查支持具体 locator，不扩张到整页或整章阅读完成。

## Provisional Reasoning

**新单元的完整阅读记录。** 物理66–71／印刷44–49，从 §4-3b 的 leading-order E2 intensity relations 读至 Fig.4-5 完整图注。物理65尾部仅用作前文上下文，72开头仅用于确认下一个小节；它们不计入本次完成单元。所有六页原生文本均读过，随后逐页核对图像：

| 物理页／印刷页 | 已读及视觉核查对象 |
|---|---|
| 66／44 | 上节结尾的 yrast 转动语境；§4-3b 假设；Eq.4-66 的 \(eQ_0\)、内禀密度积分、\(\nu=0\) 张量分量；脚注5。 |
| 67／45 | Eq.4-67 的内禀到实验室变换；4-68a/b 的 RME／B 归一化；4-69 的谱学四极矩；4-70 的 \(K=I\) 特例。 |
| 68／46 | 两种不同高自旋极限；4-71 的 \(\Delta I=0,1,2\) CG 渐近；固定形变假设；作者关于 \(^{20}\)Ne 高自旋偏离的讨论。所引外部表和图未因此获得阅读学分。 |
| 69／47 | 4-72、4-73 的 \(\delta\) 定义和均匀尖表面椭球条件；\(\delta\simeq0.95\beta_2\) 的领先阶条件；作者的形变系统学讨论。 |
| 70／48 | Fig.4-5：横轴质量数 A，纵轴 \(B(E2)/B(E2)_{\rm sp}\)，同位素链标号与图形；未数字化单点。 |
| 71／49 | 形变／配对竞争的文字；Fig.4-5 跨页图注、上行方向、single-particle 单位和引用来源。 |

**原书模型结论。** 采用轴对称、良好 \(K\)、固定内禀矩、领先阶强耦合近似，原书 Eqs.4-68b、4-69 给出

\[
B(E2;I_iK\to I_fK)=\frac{5}{16\pi}e^2Q_0^2
  \left|\langle I_iK\,20\mid I_fK\rangle\right|^2,
\qquad
\frac{Q_s(I,K)}{Q_0}=
\frac{3K^2-I(I+1)}{(I+1)(2I+3)}.
\]

这里 \(eQ_0\) 是内禀电四极矩；\(Q_s\) 是实验室伸展子态的谱学矩。\(Q_s=0\) 对 \(I=0\) 或 \(1/2\) 并不要求内禀形变为零。B 关系只有强度平方，不能据此恢复不同 E2/M1 张量间的相对相位。

**本次回忆与推导的实质增量。** 从分子／分母的最高次项，可明确区分：

\[
\lim_{I\to\infty,\;K\ {\rm fixed}}\frac{Q_s}{Q_0}=-\frac12,
\qquad
\lim_{I\to\infty,\;K=I}\frac{Q_s}{Q_0}=+1.
\]

前者沿同一固定 \(K\) 转动带；后者沿 \(K=I\) 的不同态序列。缺少这一区分时，“高自旋使谱学矩等于内禀矩”会给出错误的符号和归一化。两种极限均由原书印刷45–46页明说，本次以代数独立复核；不是新的核素预测。

对允许的同带向下 \(\Delta I=1,2\) 跃迁，由精确 CG 系数还得到

\[
\frac{B(E2;IK\to(I-1)K)}
 {B(E2;IK\to(I-2)K)}
=
\frac{2K^2(2I-1)}
 {(I+1)[(I-1)^2-K^2]}
\xrightarrow[I\gg K]{}\frac{4K^2}{I^2}.
\]

仅在两个末态都存在、分母非零时使用这个比值。该有限 \(I\) 有理式是本次重建，不是声称书中逐字印出的额外公式。它与 Eq.4-71 的 CG 渐近一致。取纯数学例 \(I=4,K=2\)，精确比为 \(56/25=2.24\)，而把它过早当作高自旋给出1，说明“高自旋”必须相对 \(K\) 量化。\(K=0\) 时 \(\Delta I=1\) 几何选择零保留。

**方向与单位回忆。** 同一 E2 算符下，\(K=0\) 极限有
\[
\frac{B(0\to2)}{B(2\to0)}=5,\qquad
\frac{B(4\to2)}{B(2\to0)}=\frac{10}{7},\qquad
Q_s(2,0)=-\frac{2}{7}Q_0.
\]
Fig.4-5 图注明确绘制上行 \(0\to2\) 强度，并定义
\[
B_{\rm sp}=\frac{5}{4\pi}e^2\left(\frac35R^2\right)^2
\simeq0.30A^{4/3}e^2{\rm fm}^4,
\qquad B_W=\frac15 B_{\rm sp}
\]
作为对应下行 \(2\to0\) 的单位。这个图中的单位和方向必须一起读，不能仅见 “single-particle” 就与另一表的下行 W.u. 混用。此处没有重新校准任何 Ba 核或改动 parent 的输入。

## Assumptions

范围核对依赖稳定的 raw 路径＋SHA，而不是文件排序、source 卡日期或技能名字。物理 PDF 页与印刷页分开处理；翻译和不同版次单独保留。

新 E2 单元只处理固定形变的轴对称领先阶模型。\(I,K\) 为以 \(\hbar\) 计的量子数，\(Q_0\) 的长度平方与电荷因子遵循上式；没有把此处 \(Q_0,\delta,\beta_2\) 无条件等同于软核不变量的有效形变。单粒子附加项、强 Coriolis 混合和非轴对称修正留给随后页段。

## Competing Explanations

阅读回执与 source 卡不同步，可能来自卡片更新滞后、后续摘要写回覆盖，或局部阅读被表述成了更宽的范围。本次不恢复编辑历史、不猜测实际执行者，也不把某条 locator 错配等同于整份阅读未发生。

同样，核结构观测量偏离领先阶 Alaga 比值，可能来自带混合、内禀结构变化、非轴对称分量或其它适用条件失效；本单元不能单独判别 wobbling、TiP、chirality 或 gamma softness。原书对历史实验的总结保留为作者报告，没有重新检查其原始计数或现代评价。

## Transfer Conditions

当前对原队列可安全转移的增量为：33条记录的身份／范围／重叠映射，以及一个实际完成的六页子单元。亲自核过的公式图像限于对象登记表；新单元的结果可供 E2 归一化、方向因子和渐近适用域核查使用。任何模型校准或真实核素推断仍需独立的数据与算符合同。

下一批明确的连续、尚未作为完整单元核销的范围：

| 书 | 下一单元：物理／印刷页 | 原包 | 原因 |
|---|---|---|---|
| BM-II | **72–75／50–53** | Q-B25-002 | 继续 §4-3b generalized intensity relations；本次停于71。仅看了72的开头定位，不算读完。 |
| Greiner | **170–175／151–156** | Q-B10-005 | §6.5.2 quantal Hamiltonian；170节标题已核，但仍需连续读取和公式核验。 |
| Casten 1990 | **156–163／141–148** | Q-B34-004 与005 | 第6章集体激发开头。有概念／技能引用，尚未找到对应完整连续单元的回执。 |
| Petrache | **247–251／228–232** | Q-B02-007 | 第11章 IBFFM-2 延伸。已有“选公式／结果页”记录，应补成逐页完整单元；不声称这些页从未被查看。 |

“未核销”指缺少满足原六项要求的连续单元完成记录；不能仅凭本次有限检索证明某人从未读过。Petrache 的全章回执应先修正具体 locator，再核对象覆盖与剩余排除项，不能直接重新安排成“全书零进度”。

## Failure Conditions

下列行为会使本次整合失效：以旧卡 `deep-read` 取代页段凭据；把章目录／整书抽取／技能数／测试数当学分；把 Petrache 的印刷页号作物理页；把 Casten 参考文献计为第10章正文；重复累计重叠页；把新六页单元升级成40页包；或将固定 \(K\) 与 \(K=I\) 的高自旋极限混合。

BM-II 粒子–振动回执的错配公式编号仍是未解决的定位项。本次没有全面复审它的全部科学结论，也没有改动它、原 source 或账本。

## Falsification or Reverse Tests

本次 `check_bm2_unit.py` 不调用书本提取、既有核模型或核素数据，以标准库 `Fraction` 和整数阶乘 Racah 求和独立计算 CG 平方。四个有限自旋例 \((I,K)=(4,2),(6,2),(20,2),(9/2,3/2)\) 的比值与上面有理式**精确相等**；方向因子5、\(10/7\)、\(K=0\) 选择零和两条不同极限均通过，内部运行约0.0023秒。

初次尝试使用 SymPy 时环境报告 `ModuleNotFoundError`，随后改为标准库精确运算，没有安装依赖。草算分支比曾把最后分母的 \(I+1\) 写成 \(I-1\)；精确 CG 求和与完整约分明确要求 \(I+1\)，已纠正。该项是学习者草算修正，不是原书勘误。

六页单元没有独立列出的课后习题；书中交叉引用的表4-4／4-6／4-8／4-10、图4-24／4-25及后半广义强度关系未据此计为本次完成。Fig.4-5 的图轴、单位、完整图注和数据出处已核，但未数字化或重新评价其中实验点。

## Open Questions

还需核对旧回执中的逐式／逐图错配、参考文献是否仅浏览，以及全章声明是否具有闭卷回忆和所有科学对象的记录。尤其需补全 BM-II 438–457 的实际公式序列，及 Petrache 第13章修正后的对象覆盖。Casten 第二版与四个翻译衍生文件尚未与第一版建立逐节对照，不能转移现有页码。

本次没有执行新全馆内容盘点，没有重读原318包，也没有进入 parent 的同核异能态 benchmark 或 Huygens 的固定形状转子数值工作。

## Human Review

本页是 Agent 的原件／记录对账及局部学习自审，没有 human-reviewed 事件。现有 review 标签保持原样；完成状态按范围与证据决定。

## Promotion or Rejection History

2026-11-06：新建本页，绑定四书原件，完成33条范围记录和49个目标分包的映射；新增 `U-B25-002-E2-20261106`。原 [[book-corpus-coverage-ledger]] 未改，等待 parent 按此页及审计输出整合可验证增量。当前只认定六页子单元完成，不新增整章、整本或原始40页包完成声明。
