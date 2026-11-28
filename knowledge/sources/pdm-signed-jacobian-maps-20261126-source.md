---
type: source
title: "P-ADO带符号Jacobian：两组注入几何与135Pr 747.3 keV"
title_original: "Signed P-ADO response Jacobian maps and derivative validation"
aliases: [PDM带符号雅可比二维图20261126]
created: 2026-11-26
updated: 2026-11-26
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized saved-response diagnostics with analytic and independent finite-difference derivatives"
raw_file: "raw/writing/pado/20261029_review_v1/revise_slide_figure/signed_jacobian_20261126/manifest.json"
raw_sha256: "5215edad3b6778a0ee6efb74c0fdf7362bb015a623ec5f87e07874856aa2cd05"
raw_storage_status: archived-local
archive_required: true
citation_key: PDMSignedJacobian20261126
evidence_sources: [pdm-two-geometry-recovery-20261125-source, pdm-report-figure-review-20261126-source]
tags: [pdm, jacobian, response-geometry, numerical-derivatives, finite-domain]
---

# P-ADO带符号Jacobian二维图

## Bibliographic Record

用户要求在既有幻灯片图目录新增125/90、26/90注入几何与135Pr 747.3 keV的带符号二维Jacobian。保存响应取自O01/N01/L04对应原始NPZ，全部P-ADO，不包含DCO/PDCO。本次没有PDM反演、误差调参或原报告修改。

## Scope and Reading Depth

横轴xi=arctan(delta)，单位rad；纵轴u=sigma/I。观测顺序严格定义为(R_ADO,P)，绘制正向J=d(R_ADO,P)/d(xi,u)。两注入参考自旋I=5、目标5->4；Pr参考自旋I=8.5、目标8.5->7.5。Pr采用原输入的加权角组，R=[2W(157.6)+W(133.6)]/[3W(75.5)]，P在75.5度，不采用占位的标量角字段。

## Summary

六张最终图包括三张独立线性色标map、一张共享线性色标三联图、一张共享对称对数色标三联图及一张原保存网格差分对照三联图。所有图保留正负、使用共同对称色限，没有逐图幅度归一或观测密度加权。黑线为插值得到的J=0等值线；两注入图标出全部10个真值位置，Pr仅标文献delta=-0.47的竖线，不补造宽度真值。

## Extracted Pages

本集合为独立PNG/SVG及单页PDF，不改变报告页码。首选`comparison_symlog`查看符号分区与小值，再看`comparison_linear`比较绝对幅度。独立图为`signed_J_injection_125_90`、`signed_J_injection_26_90`、`signed_J_135Pr_747p3`。

## Key Results

| ID | claim_kind | evidence_level | locator | 结论与边界 |
| --- | --- | --- | --- | --- |
| SJ26-1 | model-result | direct | `summary.json:settings`、各案例NPZ | J_RP_xi_u = R_xi*P_u - R_u*P_xi；交换观测顺序变号，改用sigma坐标则除以I |
| SJ26-2 | model-result | direct | `injection_125_90.json` | 解析J范围约[-1.046264,0.884431]，扫描网格存在正负分区 |
| SJ26-3 | model-result | direct | `injection_26_90.json` | 解析J范围约[1.9044e-8,2.661883]，本次全部扫描节点为正；不据此推断全局逆映射唯一或无偏恢复 |
| SJ26-4 | model-result | direct | `135Pr_747p3.json` | 解析J范围约[-0.058061,1.626959]，扫描网格存在变号区；理想权重几何不等于真实接受度重放 |
| SJ26-5 | software-audit | direct | 各案例JSON的`independent_derivative_checks`及`sign_disagreement_width_row_indices` | 全网格重构P/R与原数组在2e-12容差内一致；两级步长独立差分核对四个解析偏导，细步长最大绝对误差低于3e-9 |
| SJ26-6 | software-audit | direct | `injection_26_90.json`、`saved_grid_comparison_symlog` | 原单边差分在最小宽度第一行产生1781个微小负节点；解析导数消除此负带。原始差分另图完整保留，非静默裁切 |
| SJ26-7 | software-audit | direct | `rendered_qa.json`、各alignment/fonts/collision JSON | 六图的对齐、实际字形及碰撞检查均通过；逐图视觉检查由Agent完成，非human-reviewed |

## Derivative Definition and Verification

主图对原模型的精确二次辐射强度表达及Gaussian源布居求解析导数，再使用商法则得到四个偏导。令offset_m=m^2-min(m^2)，布居导数采用下面的终端可读表达，避免窄宽度下消减误差：

    d pop_m/du = I*pop_m*(offset_m-mean_offset)/sigma^3

响应强度对混合角的表达为：

    MM*cos(xi)^2 + 2*ME*cos(xi)*sin(xi) + EE*sin(xi)^2

独立差分使用公开`evaluate_response`，不复用解析导数实现，xi和u步长分别取1e-5与5e-6。主图使用全部原网格节点，不抽样、不平滑。原保存网格差分的绝对值另核对为I乘以原PDM的绝对Jacobian。

## Competing Interpretations and Limitations

主图给出响应模型的解析Jacobian，原保存网格差分另图展示，二者不混称。除第一宽度行的单边差分伪变号外，旧几何与Pr在零等值线附近还有少量离散根位置差异，完整行索引和计数见JSON。没有通过改绘图色限、裁掉小负值或改原核来消除差异。

三图统一色限约[-2.66188,2.66188]，对称对数颜色阈值约0.0266188，仅改变颜色映射，不改变J数值。未扫描的最小宽度以下区域用浅灰背景；该区域不被解释为J=0。真实观测误差密度没有进入本图，因此J的峰值不自动预言PDM恢复峰或实验精度。符号依赖约定，局部非零不保证全局唯一。

## Artifact Locators

- `README.md`：公式、输入、文件、边界差分与复现说明。
- 三个`<case>.npz`：完整响应、解析四偏导、带符号解析J、带符号原网格差分J及有效性。
- 三个`<case>.json`：输入、源哈希、数值范围、零线截面、标记及核验。
- `source_snapshots/`：精确绘图程序与当时使用的计算源码。
- 原响应网格和输入索引以原路径、大小与SHA-256登记，不修改原件。既有YAnalysis/YPlot和幻灯片Notebook未改写。
