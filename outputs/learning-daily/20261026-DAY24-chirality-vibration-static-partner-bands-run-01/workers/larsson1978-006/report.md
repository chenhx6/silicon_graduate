# Larsson1978恢复结果：正文0页，程序与参数出处已进一步分层

本任务仅限Day24既有133Ce附属输入问题。`needs_review: true`，self-audit不是human review。没有修改005结果、canonical、raw、PLAN、Bib、凭据、配置、Git、session或课程学分。下载/运行数据仅在`tmp/day24-larsson1978-006/`；交付仅在本worker目录。目标明确为正文，不扩展SI或其它论文批次。

## 身份核定与实际阅读范围

独立新查Crossref及INSPIRE核定：S. E. Larsson, G. Leander, I. Ragnarsson, **“Nuclear core-quasiparticle coupling”**, *Nuclear Physics A* **307**(2), 189–223 (1978), DOI **10.1016/0375-9474(78)90613-9**。189–223为35页，INSPIRE也列35页、record1430142、NSR1978LA13。Crossref给1978年9月，Elsevier XML给1978-09-11；不以不同日期粒度制造出版日期冲突。

- Crossref：`https://api.crossref.org/works/10.1016/0375-9474(78)90613-9`，HTTP200。
- INSPIRE：`https://inspirehep.net/api/literature?q=doi:10.1016/0375-9474(78)90613-9`，HTTP200，命中record1430142。
- **1978 body取得：否；实际正文阅读：0页；正文版本：未得；正文SHA：不存在。**没有“全文精读”认证，没有原公式/页码/表图locator可给。
- 实际另读WK22原PDF49–50/77–78/87–88/120/124/128的相关正文和bibliography；视觉核49/50/78/120/124/128。读取RS88原PDF4/5/8/18，均fresh视觉核；没有重新声称读完RS88全部16篇正文页。
- WK22原文件SHA重新匹配`48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080`；RS88既有staging SHA重新匹配`af5b8588ac78f40ecb7ac5eb8f2dd8070c3457296e8fdcd63e9ea0d828a2fa6d`。

## 1978到底研究何种问题：只能给摘要级scope

INSPIRE的`metadata.abstracts[0]`明确标为Elsevier来源。该摘要说明：比较以Bohr Hamiltonian为基础的core-particle模型，特别是γ-unstable与rigid30°三轴芯；发展rigid triaxial rotor core的strong-coupling表述，应用185Re及75,77Se，讨论后者形状过渡和配对处理困难；并从strong-coupling basis看decoupled态的波函数/激发能及hexadecapole与j-mixing影响。

这能把本篇定位为**core-quasiparticle耦合formalism与应用**，不是2022代码包或actual GAMPN参数文件。上述内容只是**出版商摘要的研究范围**，没有核其正文推导、适用限制、Nilsson数值单位、能量零点、实际模型空间、惯量、BCS或EM显式公式。不得为其虚构具体方程号、引文页、配对处方或参数值。

RS88为另一个直接来源：其PDF8/printed430首段把odd case的显式M1/E2矩阵元指向Ref1；其PDF18/printed440 Ref1正是Larsson–Leander–Ragnarsson1978。这说明1978**是有价值的待读矩阵元来源**；但“RS88说其中有公式”不等于本worker已读/恢复这些公式。

## WK22原字面与Ref39/40/62/11逐项定位

WK22正文印刷页=PDF页−11。以下引用关系已回到原PDF，不能把source概括或相同作者名字当代码版本证据。

| 原件位置 | 原字面/实际引用 | 可支持什么 | 不能支持什么 |
|---|---|---|---|
| **PDF49 / printed38，§3.4首段** | 原文称 **“the QTR model codes of Ragnarson and Semmes [39, 40]”**，紧接依次列GAMPN、ASYMO、PROBMO，并叙述前后输出传递；EM计算段末另引[66] | WK22作者报告使用这个三程序链 | 句中作者归属与bibliography不能自行拼成某一公开版本；未给真实代码哈希/版本/input/output |
| **PDF124 / printed113，Ref39** | S. E. Larsson, **“The Nuclear Potential-energy Surface with Inclusion of Axial Asymmetry”**, *Physica Scripta*8(1–2),17–31(1973)，DOI10.1088/0031-8949/8/1-2/003 | Ref39是另一篇1973势能面方法文，与1978不同 | 不能把1973题名/内容归给1978，也不能把这条引用改写为Ragnarsson–Semmes1988 |
| **PDF124 / printed113，Ref40** | S. Larsson, G. Leander, I. Ragnarsson, **“Nuclear core-quasiparticle coupling”**, NPA307(2),189–223(1978) | 本次1978目标与WK22 Ref40身份一致 | 1978三作者中没有Semmes；该bibliography对应关系不是actual2022三程序的实现证明 |
| **PDF128 / printed117，Ref62** | I. Ragnarsson, P. B. Semmes, **“Description of nuclear moments and nuclear spectra in the particle-rotor model”**, *Hyperfine Interactions*43,423–440(1988)，DOI10.1007/BF02398323 | RS88是WK22另列的Ref62 | 不能把§3.4的[39,40]静默替换成[62]；RS88实际正文425–440，423–424是其publisher wrapper |
| **PDF49 / printed38，§3.4.1中段** | 明确 **“standard Nilsson parameters were adopted as in Ref. [11]”** | κ、μ数值来源另路由到Ref11 | 不因1978为formalism来源就把2022 κ/μ参数版本定为1978 |
| **PDF120 / printed109，Ref11** | T. Bengtsson, I. Ragnarsson, **“Rotational bands and particle-hole excitations at very high spin”**, NPA436(1),14–82(1985)，PII037594748590541X | Ref11的书目身份及1985参数来源路由 | 本worker未打开1985正文，也未核2022实际κ/μ表或GAMPN输入卡 |
| **PDF50 / printed39，§3.4.2** | ASYMO使用GAMPN输出的single-particle态/矩阵元，报告最多15态；惯量可由2+能量[51]或Harris参数[30,48]得到 | 方法可选项、程序数据流与截断限制的论文描述 | 不能把“最多15”当2022所有计算均用15态，也不能把惯量的历史来源统一归给1978 |

**分层判断（我们的证据审计推断）**：WK22程序归属的文字、其Refs39/40、另列Ref62和κ/μ的Ref11是不同层的记录。当前字面归属不完全对齐，但这不证明作者实际代码出错，也不授权我们替作者修正引用；实际代码来历与版本保持unknown。最有用的写回是将“历史formalism / 参数版本 / 程序分工 / actual job”分栏。

## 对ε、λ、模型空间、惯量、配对和EM的影响

| 项目 | 本轮直接核到的内容 | 仍未取得的actual-producer边界 |
|---|---|---|
| 单粒子能与零点 | WK22 PDF78/printed67 Table6.2表头ε(MeV)，数值约5.4502–6.4922；同页正文正宇称Ce λF=50.6 MeV。PDF87–88/printed76–77为Ba λF=51.0与Table6.4约5.4674–6.5126 | 未给这些列的共同零点、ħω缩放或跨程序转换。**不据相近8MeV尺度强凑，不改表单位，不把正宇称λ搬给负宇称。** |
| GAMPN的输入/输出 | WK22 PDF49要求Z/A、ε2/γ/ε4、valence配置、κ/μ和所选轨道空间；输出εν、矩阵元及NLJΩ展开 | 缺实际header、轨道编号全集、截断、符号/坐标规范、版本与输入卡。知道程序分工不足以计算BCS占据 |
| 空间 | WK22 PDF50报告ASYMO最多15轨道；PDF77/87应用为10个正宇称轨道。RS88 PDF8/430报告自己odd核10–15轨道的收敛经验 | 不是133Ce九负宇称轨道/特定γ参数点的独立收敛证书；不能拿RS88经验替当前空间误差 |
| 惯量 | WK22 PDF78有γ irrotational-flow与Harris J0/J1，其参数引用[48]；RS88 PDF8/430自己的应用用Grodzins关系 | 不同处方不同实例，不能因共有1978 formalism而称同一惯量；仍需2022实际Harris接口与coreR/总I/ω用法 |
| 配对 | RS88 PDF5/427给Bogoliubov态，core-H相关single-particle矩阵元乘UU′+VV′，另有off-diagonal ξ；PDF8/430说其方法的λF/Δ为derived quantities、参数源Ref14 | 不证明WK22的actualλ/Δ是同一求解方式，不恢复2022 λ/Δ数值与blocking。1978摘要的pairing difficulties不能代替其具体处方 |
| 物理/伸长坐标及EM | RS88 PDF4/426区分stretched单粒子势与physical算符，径向/ε4转换；PDF8/430将odd M1/E2显式矩阵元指Ref1 | 1978正文公式仍缺，actual PROBMO的operator、全波函数、phase、effective g/e与单位接口仍缺；不补signedδ或绝对B |

作为一般数学约束，BCS需要同一单位/同一零点的εν−λ及Δ；共同能量平移可相消，**两列未经证明的不同零点不能相消**。这是输入合同，不是本轮从1978正文提取的方程，也不提供作者真实换算。现有边界只被细化，没有关闭。

## 新入口访问记录与停止理由

先读前一轮`tmp/day23-theses/larsson1978-worker/access-probes.json`及`access-and-reading-notes.md`，未重试已知ScienceDirect403、anonymous API PDF406、Lund无附件、OpenAlex无PDF、Scholar MCP timeout或S2 429。

| 本轮新入口 | 实际结果 | 为什么不算正文 |
|---|---|---|
| Crossref exactDOI | 200，题名/作者/卷期页/DOI、TDM links | 元数据；TDM license标注不等于OA许可 |
| INSPIRE exactDOI | 200，35页/NSR/参考与Elsevier摘要，无documents附件 | abstract非body |
| Crossref提供的Elsevier **XML** TDM URL | **200，1780bytes，只有coredata** | 无originalText/body/ja:article。不是旧PDF406重试，也不因200就宣称取得全文 |
| OpenAIRE exactDOI | 200，Closed Access，唯一实例URL回DOI | 没有新repository PDF |
| CERN CDS exacttitle | 200 HTML，为Anubis验证页 | 没有搜索结果/正文，不绕过验证 |
| Bing exacttitle+pdf | 200，但返回核能/词典等不相关结果 | 不命中精确目标；不从搜索噪声认领PDF |
| OSTI title、DuckDuckGo、Google title/DOI、Internet Archive title | connection refused | 没有可读响应；不重试 |
| INIS legacy title search | DNS no address | 没有响应，不等于INIS从无记录 |

下载内容均留在指定tmp，未将HTML伪装PDF。没有修改凭据或申请/推断机构权限，没有走Sci-Hub、登录或付费墙绕过。实际新入口/状态见`access-ledger.json`，原响应在tmp；正文0页边界保持。

本轮已完成可得身份与引用出处分层，checked routes没有新正文候选；此处收口有界获取路线，不重复失败端点，不把摘要补成公式。下一高信息输入是实际GAMPN/ASYMO/PROBMO版本、header和输入输出合同，或日后出现明确合法1978正文链接后的定向原读。此为研究输入缺口，不自动变成用户待办，也不宣称全世界不存在可访问1978版本。

## 产物与检查

- `metadata-and-reading.json`：已核书目、摘要scope、body0页、null版本/hash。
- `access-ledger.json`：新入口与保留的旧失败边界。
- `checks.json`：Crossref/INSPIRE身份及35页算术、XML无body、WK22/RS88 SHA匹配。
- `report.md`：本报告，包含原字面/locator与输入出处分层，供root写回knowledge。

命令检查：Python requests的逐URL状态、content-type及真实响应体；JSON解析；XML body tag检查；hashlib SHA；PyMuPDF定向text/render；`view_image`原页视觉核。所有这些只检查身份、访问和转录，不认证历史代码或实验。一次辅助`tmp`递归文件发现未及时结束，已仅对自己的Python进程PID338051发送TERM；所有RS88文本/图已先生成，未影响来源、其它worker或daemon。本worker没有跑作者程序/用户events/统计拟合。
