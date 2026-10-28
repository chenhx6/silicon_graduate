# 多带剪刀共存定向审计

已完成Pb综述级证据与141Eu第一手寿命证据的比较，并建立知识笔记和可运行的合成混合模型。139Sm保留全文缺口。页面均为unreviewed，不改变Day26学分、正式run/session/deadline或系统交接。

## 原件突破和修正

取得Podsvirova2004的6页出版商PDF，SHA-256 `31dd323d75f9a178e653bc88426482e3970a27183770dfd1771b514bbccdd503`，717914字节，PDF-1.4。其Table1报告DB1/DB2各三个寿命；原件中的“三个初始排列分支”属于模型可能性，不能计作三条寿命带。TAC的中子空穴配置与四极形变是作者假设；SPAC自旋依赖集体性方案较所试混合带交叉方案更好，故没有把两态混合写成实验已测机制。

## 工件

- 知识笔记：`knowledge/research-notes/multi-band-shears-coexistence-pb-141eu-139sm-boundary.md`。
- 来源页：`knowledge/sources/podsvirova-2004-141eu-dipole-lifetimes.md`，保留Table1不对称区间、比值边界与Monte Carlo众数含义。
- `multi-band-shears/`：出版商PDF/提取文本、Crossref身份登记、检索账本、模型Python/JSON/SVG。
- 合成参数W=0.040 MeV，Ic=24.5处能隙0.080 MeV；没有拟合任何核素。矩阵元用初末态各自的混合矩阵变换。

## 未完成边界和检查

139Sm的Crossref身份已核对；PDF路由HTTP406，没有补造全文覆盖。一次未经核验的arXiv候选实际属于无关论文，已按题名拒绝并移入tmp，其哈希与拒绝理由保留；未进入证据链。

仅执行本任务Markdown的定向diff空白检查与模型计算；未运行全库lint或测试，未commit/push。后续由父代理整合、运行发布门并自行发布。精确命令结果与工件哈希见相邻JSON。
