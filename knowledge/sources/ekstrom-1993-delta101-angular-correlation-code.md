---
type: source
title: "DELTA1.01公开副本：相位、输入误差与分支输出合同"
aliases: [Ekstrom DELTA 1.01 1993, DELTA angular correlation code, PyNE DELTA101 content object]
created: 2026-10-18
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: software
reading_depth: skimmed
title_original: "DELTA Version 1.01, 15-Apr-1993"
authors: [L. P. Ekstrom]
year: 1993
version: "1.01 [15-Apr-1993]; original August1983, later header initials TWB"
source_route: PyNE-vendored-public-source
license: "Public PyNE source mirror; repository license retained in tmp; no upstream standalone-license certification or source redistribution"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "sha256:6e118b8c79784f67b33ea0388f84f5a187af33563653443076afe4cd568837fc"
source_url: "https://raw.githubusercontent.com/pyne/pyne/0.7.8/src/ensdf_processing/DELTA/delta.for"
raw_file: "raw/software-reference/day16-20261018/delta101-6e118b8c7978.for"
raw_sha256: "6e118b8c79784f67b33ea0388f84f5a187af33563653443076afe4cd568837fc"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [104Mo]
reactions: []
experiments: []
models: [Krane-Steffen, Rose-Brink, independent-Gaussian-chi-square]
methods: [angular-correlation, mixing-ratio-inversion, phase-convention, numerical-grid]
observables: [angular-correlation-coefficient, multipole-mixing-ratio]
tags: [software-reference, delta101, branch-topology, source-independence]
---

# DELTA1.01：generic producer与实际实验分析要分开

## Bibliographic Record

实际取得的是[PyNE0.7.8所存DELTA源码](https://raw.githubusercontent.com/pyne/pyne/0.7.8/src/ensdf_processing/DELTA/delta.for)，207603bytes/2563行，GitblobSHA1 `9fd195047cfbaa293be46c26c5702d7b7580334a`、SHA256见frontmatter。source header标August1983/L.P.Ekstrom(Lund)，以及Version1.01/15-Apr-93/TWB修订记录；没有由initials扩写未知修订作者，1993也不是PyNErelease日期。namedtag0.7.8与retrieveddevelop对应文件**逐字节相同**；Gitlsremote因网络失败未得具体commit，因此用固定内容hash/文件版本作身份，不假报固定repoHEAD。

本次NNDC首页的Analysis/UtilityCodes指到IAEA公开目录，但该页403challenge；EL18所列旧NNDC DELTA地址404。GitHubAPI检索rate-limit、orgpage超时；均记录边界且不绕验证/改凭据。合法独立PyNE路径先从实际`src/CMakeLists.txt`发现DELTA/delta.for，再取上述namedtag与同taglicense.txt；本地构建只用此文件，未运行PyNE自动下载器/setup。这个副本不是已从NNDC核同hash的officialfile，也不自动等于EL18在2018使用的binary。

raw_file是未填归档槽；源码、原license、binary与运行目录都只在repo tmp，未将第三方代码或二进制进入Wiki Git。原PyNElicense文本保留，不声称原Ekstrom standalone程序为publicdomain；本页属于内容地址的研究核验。

## Scope and Reading Depth

读完header用途/级联/限制、输入cards与output合同，沿MAIN/OPENFI/WORK/RMINIM/DIPS/SETUP/SETCOF/SETVAL/SQRES/AK/SRK/SUK/QUADIN/CREAD/CLEAR主线，并查CG/Wigner/factorial数值保护。没有逐分支认证每个format、全部CGprimitive或PyNE其它程序，whole2563行定向状态skimmed。实际GNUFortran13.3使用`-std=legacy -O0 -ffixed-form -x f77`，无源码改动、无额外依赖安装；compileexit0，五项初始card和两项由purefailure触发的步长followup均processexit0。**exit0不自动表示科学控制成功**，下文保留首pure插值失败。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| D101-1 | 该内容对象声明KS70signconvention，使用首/末两δ和最多3个fixed未观测δ；角系数输入应已校正finitegeometry，内部扫描atanδ默认2度、每轴最多181点。此函数不是任意beam-orientedρ/sigma的DCOproducer。 | source-code-identity-and-domain | direct-code | header records01 00170–01210；WORK/SETUP/CLEAR | true |
| D101-2 | header与SQRES均按各dataitem独立/误差统计处理，目标是sum[(value−theory)/error]²；没有jointΣ、Gcalibration covariance或pureICCtheoryerror输入。带共享系数的数据不能只因此代码可运行便当独立。 | error-model-contract | direct-code | header01 00560–00600；SQRES programunit14 | true |
| D101-3 | AK以RK表示且显式说明δKS=−δRB，first/last线性符号与SETCOF的spinstates交换需一起读；代码中first“+”/last“−”不是KS70普通F的B/A公式可直接替换。实际printedgrid核与本任务发射kernels相容于F9.3精度。 | phase-role-and-kernel-check | direct-code-and-execution | AK unit22；SETCOF unit12 SRKcalls；SRK unit23；本任务grid audit | true |
| D101-4 | header明确忽略mixed未观测跃迁的internalconversion对deorientation影响，并引Anicin1972；SUK实际按δ²混合U。若目标是全部γ/ce未观测，须核Martin的totalICC权重，不能把generic默认自动当all-decay正确。 | unobserved-channel-model-boundary | direct-code | header01 00710–00740；SUK unit24 | true |
| D101-5 | DIPS按三点抛物线求minimum，采用absolutethreshold SIGMA=max(SQmin+1,SQmin*(1+F(NFREE)/NFREE))，F表标F(1,N,.683)。ERRL/ERRR初值1000、找不到scan内crossing便保留；此SIGMA不是δ标准差、1000不是有限measureduncertainty或完整wrappedCI。 | numerical-interval-and-sentinel-contract | direct-code-and-execution | DIPS unit10 records10 00740–01500；F unit19；DELOUT entry | true |
| D101-6 | 实际printed104MoA2only card在2度输出δ≈−.151/55.9，一度−.151/55.8；并给大支右error1000sentinel。A2+A4诊断仍保留smallpoorfit与largebranch，但程序给smallχ²≈8.727/absoluteSIGMA16.362，不是任意默认Δχ²1。不是EL18实际input/producer重放。 | bounded-public-program-execution | task-execution-on-published-summary | DAY16-DELTA101-PUBLIC-FORTRAN-01 cases Mo104_A2_only/A2_A4 | true |
| D101-7 | 已知pure4→2→0控制的exactgridχ²=0，但默认2度三点插值移动后报告χ².199/δ约.001；同input改1度χ².012，限定local±8度/.1度后printedχ²0。源未改，首失败保留；这验证header的细网格必要性，不是新实验修正或笼统代码正确/错误。 | failure-control-and-numerical-refinement | task-execution | pure_4_2_0与followupcards；DIPS/QUADIN；header01 00610–00630 | true |
| D101-8 | A2/A4 error≤0时DATA被关；Dcard uncertainty≤0时把对应δ固定，内部变量名PURE=true可以是固定非零mixing，不自动指physicalpuremultipole。读取codeflag或output须按真正输入语义。 | API-input-semantics | direct-code | MAIN A2/A4/D datarecords01 04730–05150；SETUP | true |

## Summary

公开genericproducer已从“没有代码”推进到一个内容hash明确、真实编译/执行的版本，可核相位/分支/误差合同。它仍没有EL18 unroundedcoefficients、G/response/Σ、原input文件或2018确切binary；同一个程序名称不消除这些证据层。普通独立误差、变步长、poorfit规则与sentinel均应作为输出解释的一部分。

## Numerical Exercise and Reproducibility

[输入五组card](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta-code-execution-input.json)在执行前冻结SHA256`49681494c95d56016327462751ce16642dbc2b9f04503fd199a0fdcca8b0b371`，actualbuildbinarySHA256`3c506ab2653509708b393a4f3708c08d1cc9ac06456f076f72334fc0f251f92d`；二进制hash依本构建环境。代码只在tmp编译；stdin使用工作目录内`input.dat/output.txt`，不超过Fortran80字符文件名边界，不覆盖raw。

[actual execution receipts](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta-code-execution-results.json)保留每组input/output全文与hash；首pure不闭合触发[预先冻结followup](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta-pure-followup-input.json)而非改source。1度全范围为181点，.1度只在已知pure点的local±8度，**不称全局scan**。

原创[输出审计](../../system/scripts/day16_delta101_output_audit.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/delta101-output-audit.json)逐gridrow以source literalRADS=.0174532和独立KS/D96kernels核printedA2/A4，最大差.000499891处于F9.3打印半步附近；没有用更宽任意容差掩盖差异。它通过完整性/declaredkernel检查，同时明确**initialpureminimumtest失败**。编译/七caseexit0与精确pure数值控制不是同一验收。

## Competing Interpretations and Limitations

- DIPS不会提供无限域精确posterior，profilethreshold也不恒为χ²min+1；内部NFREE按sourcecounter计数，不能悄然替换成通常Ndata−Nfit后解释输出“reducedχ²”。
- all-dataindependent假设不适用于EL18 groupG校准共享、KS70重复门或同derivedδ/ICC值重复输入。真正joint分析需独立Σ/likelihood或有依据的nuisance模型。
- 模型限制、有限scan/单精度RADS、三点插值和polarization/更高multipole输入范围须各自核。更多运行不补原counts、response、Cov或2018binary身份。
- 程序可接受fixednonzeroδ，而PURE布尔名只是实现细节，不可直接改写为一项experimentallyknownpureE2reference。

## Knowledge Impact and Learning Decision

`supports`KS/RB角色与双分支数字核验；`revises`SIGMA/1000/内部PURE的自动物理解释；`limits`默认步长、一项compiledcodeagreement或方法文citation替代actualexperimentalproducer。所有新claims true、pageunreviewed，无新δ/Jπ/g/shape结果。

## Extracted Pages

- [[eldridge-2018-gamma-band-mixing-ratios]]：source实际用名与currentgenericcopy边界。
- [[dco-pdco-ambiguity-worksheet]]、[[angular-correlation]]：allroots/纯极限/误差与producer对象。
- [[martin-1987-ensdf-mixing-ratio-phase-conventions]]、[[internal-conversion-analysis]]：被忽略的conversion权重条件。


## 原F表函数的实际执行与JT74处方比较

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| D101-9 | 代码F unit19明确引Gill1975 AppendixA Table7，16项FF与JT74 Table3不同；抽取未改F unit实际编译运行，ν1返回3.38000011、ν16返回1.07000005、ν17/20/30及ν≤0均返回1。DIPS的max绝对阈值结构可与JT74处方代数对应，但不能混其F值、把注释.683当所有ν的精确coverage，或据此认证EL18实际CI。 | source-code-and-statistics-contract | direct-code-and-execution | source lines1713–1733，unit19 F；1333–1336，DIPS；JT74-5/8/9 | true |

[[james-twin-butler-1974-angular-correlation-statistics]] JT74-5/8/9把R=minS、固定θ仍profile其它参数的S_h、增量E与绝对Scrit分开。源代码实际

```fortran
      SIGMA=SQ+1.0
      SIGMA1=SQ*(1.0+F(NFREE)/NFREE)
      IF(SIGMA1.GT.SIGMA) SIGMA=SIGMA1
```

等于`Scrit=R+max(1,R*F/ν)`。这个结构对应不表示作者采用相同F表：JT74印ν1=3.69、ν20=1.11；此代码按Gill引文表给ν1=3.38、ν>16默认1。精确标准F计算下，程序ν17/20/30的上尾约.33133/.32926/.32531，不能不经检查统一叫精确31.7%上尾。ν≤0的孤立函数返回1只是fallback，完整程序的zero-DOF警告与统计无意义边界仍保留。

[原unit实际编译/概率核验](../../system/scripts/day16_jt74_statistics_audit.py)读取本页同hash的公开代码对象、逐字节抽出F unit，无上游修改，compile/run均exit0；[完整结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jt74-statistics-audit.json)与冻输入保留原表、代码表和现代quantile三层。不从这些差异修正2018结果、取得新实验学分或宣称wholeproducer已认证。
