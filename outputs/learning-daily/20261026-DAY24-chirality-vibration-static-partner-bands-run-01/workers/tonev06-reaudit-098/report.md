# Tonev2006 原件与 canonical 源页再审（098）

本次为 Codex source/claim self-audit；不代表 human-reviewed 或论文最终准入。只写本 worker 目录；未修改 canonical、raw、PLAN、Bib 或 Git，未派生代理。审计时 canonical 行号以其 SHA-256 `cd52fa265def3167e20158debe5aafe59a429686f6ec28cc14489092967b48f9` 为准。

## 原件身份与可用性

实际原件 **存在**：`tmp/day24-tonev134pr-primary-090/body.pdf`，PDF 1.4，347,475 bytes，5 页；本次从文件字节独立计算 SHA-256 为 `eac94a5ff8402144aa66b003fbafada85e180126941063eb5bfc62be5b20d134`，与 090 identity/access 回执相符。`rg --files` 没列出被忽略 PDF 不能用作不存在判断。

canonical L21 `raw/papers/2006_Tonev_134Pr_Transition_Probabilities.pdf` 和 L24 `tmp/day24-tonev134pr-primary-090/10.1103_PhysRevLett.96.052501.pdf` 均不存在；原件缺失的结论不成立，是元数据路径写错。建议 L24 改成真实 `body.pdf`。L21 不应冒充已归档 raw；在 raw 尚未归档时，按源页 schema 留空/清楚标明拟归档路径，并保留 `raw_storage_status: public-staging-not-archived`。本审计不搬动或复制原始材料。

标题、DOI、PRL 96、052501、2006 及 published 2006-02-09 正确。**received 应为 2005-07-04**，源页 L38 的 2005-09-02 错误。定位：PDF1 / printed 052501-1，标题/署名下 `(Received 4 July 2005; published 9 February 2006)`。

**原件为 26 位作者**，与 090 identity 顺序相符；源页 L12 的 31 人名单错误。正确顺序：

D. Tonev; G. de Angelis; P. Petkov; A. Dewald; S. Brant; S. Frauendorf; D. L. Balabanski; P. Pejovic; D. Bazzacco; P. Bednarczyk; F. Camera; A. Fitzler; A. Gadea; S. Lenzi; S. Lunardi; N. Marginean; O. Möller; D. R. Napoli; A. Paleni; C. M. Petrache; G. Prete; K. O. Zell; Y. H. Zhang; Jing-ye Zhang; Q. Zhong; D. Curien.

源页多列 14 个不匹配名字，漏掉 9 个原件名字（其中 C. Petrache/C. M. Petrache 是署名精度冲突）；逐项见 `audit-result.json` 的 author_diff。标题页视觉已核，不是仅依 Crossref 或旧 identity 回填。citation_key 仍为空，不能编造其已完成状态。

## 七条 claims 逐项核验

| claim / 源页位置 | 本次判断与建议 | 精确原件位置 |
|---|---|---|
| TO06-D24-001 / L65 | 反应、阵列、87/83 MeV、13 个首次寿命支持。“13首次”与summary“14总计”不矛盾，但推荐统一为“共测得14态，其中13态首次确定，10+1有前值”。 | PDF1 abstract/末段；PDF2 左栏末段：10+1–18+1、13+2–17+2；except10+1 all first time |
| TO06-D24-002 / L66 | 所有寿命、误差及双方法脚注正确；**locator PDF2 TableI 应改 PDF3 TableI**。13+2/14+2方法见下表。 | PDF3 / 052501-3 左上 TableI及footnote a；PDF2左栏末段Klemme一致性；PDF5 Ref13 |
| TO06-D24-003 / L67 | 2–3倍与B(M1)无明显交错支持。“静态不支持”应归作者在该核两带和该实验/模型比较下的解释；“严重失败”改“该文采用的刚性TQPTR计算与数据明显不符”。 | PDF3 左栏 B(E2)14+–19+及pure chiral picture段；PDF4总结 |
| TO06-D24-004 / L68 | IBFFM较好再现B(E2)不对称、近乎常值趋势与无B(M1)交错，支持定性趋势比较。“成功再现2–3倍”不能当逐点精确拟合/唯一模型选择的认证。 | PDF3 Fig3；PDF4左栏顶部、右栏前两段及summary |
| TO06-D24-005 / L69 | 支持。保留“if it exists”，动态性质与形状自由度耦合是作者保持开放的解释；无独立手征识别证明。 | PDF4 / 052501-4 右栏最后summary段 |
| TO06-D24-006 / L70 | 支持：正文把lifetime analysis、branching ratios和linear polarizations coefficients细节留待Ref15。全5页不含完整逐线分支/ICC处理/Cov。缺Cov属于本次审计的完整性判断，不写成作者明确说不存在。 | PDF3左栏第1段；PDF5 Ref15 |
| TO06-D24-007 / L71 | PE06 Ref9/11角色分开支持；Tonev Ref15与PE06 Ref11署名对象不同支持。**不同引用不认证数据独立**。本条 `PDF4 Ref15` 错，Ref15在PDF5；PE06应定位PDF3 TableI caption/qualitative-agreement段和PDF4 Refs9/11。 | Tonev PDF5 Ref15；PE06 printed112502-3 TableI caption及qualitative agreement句、112502-4 Refs9/11 |

## Table I 寿命全表

全部 14 个数值和括号误差均与 canonical 一致，单位为平均能级寿命 τ 的 ps，不是半衰期。PDF3 TableI 的中央技术栏为两带共用；Band2 的13+2和14+2位于 RDDS 行组，对应源页 L86–87 的“RDDS/DSAM范围”应改成“RDDS（按共用方法栏）”。脚注 a 明确14+1、15+2均两法确定且误差内很好一致，表只报统计显著性更高的DSAM结果。

| Band | 态 | τ(ps) | 技术 |
|---|---|---:|---|
|1|10+1|4.93(15)|RDDS；与Klemme1999 Ref13一致|
|1|11+1|1.614(326)|RDDS|
|1|12+1|1.425(130)|RDDS|
|1|13+1|0.904(50)|RDDS|
|1|14+1|0.882(147)|DSAM；脚注a双法|
|1|15+1|0.608(68)|DSAM|
|1|16+1|0.562(47)|DSAM|
|1|17+1|0.422(30)|DSAM|
|1|18+1|0.249(10)|DSAM|
|2|13+2|1.443(50)|RDDS（共用方法栏）|
|2|14+2|1.280(50)|RDDS（共用方法栏）|
|2|15+2|0.887(47)|DSAM；脚注a双法|
|2|16+2|0.824(52)|DSAM|
|2|17+2|0.353(49)|DSAM|

## “静态排除”量词与 TQPTR/IBFFM 对照

PDF3原文：`Our results are incompatible with the pure chiral picture (static chirality) where the intraband B(E2) transition strengths must be almost equal ... the limit of static chirality is not reached in 134Pr and the nucleus stays in a very soft vibrational regime.` PDF4 summary：`our lifetime measurements and the theoretical analysis do not support static chirality in 134Pr`；随后明确 `chirality in 134Pr, if it exists, has mainly a dynamical character`，末句还开放two-quasiparticle/shape-degree coupling为prominent mechanism。

建议标题L34改为“134Pr寿命与理论比较不支持所分析双带的静态手征极限”；L94“决定性反证”改为“对所分析双带的理想静态手征解释形成强约束”。不能转述成所有手征模式、所有自旋、所有刚性三轴模型或任何手征几何残余被严格排除。动态手征也只是作者兼容解释，不能写为已独立证实。

源页L48 “TQPTR预言两带B(E2)相等”需要纠正。**Fig3中排两条计算曲线并非逐点相等**；PDF4左栏明确模型随自旋由dynamic趋近static，仍有substantial tunneling。almost equal是理想静态极限判据；该特定TQPTR计算产生较小伙伴差异和随spin上升的B(E2)，以及实验未见的B(M1)交错。应将“极限判据”与“这次模型曲线”分开。

IBFFM较好符合数据，作者认为shape fluctuations重要；该模型含γ≈30°附近/近轴构形混入且参数按134Ce数据调整（PDF3右栏）。Fig3和文字支持趋势对照，未给统计模型比较或排他的机制识别。原页也明确core ground-state/γ-band成分解释不必与chiral interpretation矛盾（PDF4左栏顶部）。

## “两组分支独立”的证据界限

已重新从PE06真正4页PDF抽取PDF3–4，SHA为 `ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f`。PE06 PDF3 TableI caption明确实验分支来自Ref11；同页寿命B(E2)不对称只称与其Q比结论 `qualitative agreement`，引用Ref9。PE06 PDF4 Ref9包含Tonev AIP764 p93及本PRL；Ref11列K. Starosta, D. B. Fossan, T. Koike, C. J. Chiara, A. J. Boston, H. C. Chandler, E. S. Paul, R. Wadsworth, A. A. Hecht（to be published）。Tonev PDF5 Ref15只列D. Tonev et al.（to be published）。

可支持的最强措辞是“分支数据和寿命定性参照在PE06中有不同引用入口；Tonev留待后文的Ref15和PE06 Ref11署名对象不同”。这不证明两套底层事件、探测器响应、校准、强度归一或误差独立。Tonev PDF2–3还明确其分支比修订旧Ref4，某些B(M1)/B(E2)与旧Ref16不同，说明既有分支文献间有继承/修订关系。未取得两份待发表文献对应的最终文献、实际run/输入谱系和Cov之前，不给“独立分支证据”计数。PE06是批判分析，不是新的寿命采集；其Q比2.0(4)是分支与两带模型提取，不能改写为Tonev寿命直接测得的Q比。

## 其余文字的收敛建议

- L54：RDDS DDCM是用S/U峰面积及直接馈入线在每个距离计算τ、在敏感区平均；“DDCM拟合”过于含混。门设在低于待测能级的depopulating transition的S/U成分上（PDF2左栏），建议按原文描述。DSAM才明确进行DESASTOP减速模拟和DDCM线形分析。
- L57：原文ΔI=1的M1主导判断专指**带内**；ΔI=2包括带内及带间，建议写全范围。
- L44/L70：ICC/Cov未提供可作为全篇检查后的缺口；“这些量留待后文”只对原文明列的寿命分析、分支和偏振细节成立，原文没有承诺后文一定提供Cov。
- SI：090回执支持“本次落地页扫描未识别SI链接”，不支持“论文绝无SI”。本次无需重下载已匹配完整原件。

## 审计交付与未完成边界

`audit-result.json`保存文件身份、当前canonical指纹、作者差异和逐claim判定；`table1-verified.json`保存14态原印数值；`tonev06-pdf01–05-fresh.txt`与`pe06-pdf03–04-fresh.txt`由实际PDF本次重新抽取，非沿用旧txt。已全文阅读Tonev5页文本，并视觉核PDF1/3/4的身份、TableI、Fig3和结论。未重拟τ、分支、模型producer或Cov；未声称完成底层数据独立性审计。结果应由父任务合并到canonical，当前worker按授权仅提供审计输出。
