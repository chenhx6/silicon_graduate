---
type: source
title: "multipolePDM 0.1.1：分组响应、角空间统计与注入验证"
title_original: "multipolePDM 0.1.1 grouped response and validation"
aliases: [PDM0.1.1验证, PDM大混合比覆盖率]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized local implementation and independently generated numerical controls"
raw_file: "raw/code/PDM/analysis/validation_v0_1_1/manifest.json"
raw_sha256: "7cba57eb032a4d41a863b9f3a841287e63159ac7fc8fc88af40583c5f5d7949e"
raw_storage_status: archived-local
archive_required: true
citation_key: MultipolePDM2026V011Validation
evidence_sources: [multipolepdm-20261120-synthetic-validation, multipolepdm-20261120-empirical-validation, pdm-20261120-error-geometry-grid-study, droste-1996-pdco-formalism, book-hamilton-electromagnetic-interaction]
tags: [pdm, pdco, validation, polarization, uncertainty, detector-geometry]
---

# multipolePDM 0.1.1：方法实现与验证边界

## 来源身份与定位

本页记录用户批准的程序改造及本地数值验证，不是新的实验测量，也不是已发表的独立验证论文。物理模型沿用 [[pdco-pdm-response-contract-20261118]]；程序规格见 [[pdm-three-mode-execution-contract-20261120]]。此前的误差模型、网格及135Pr权重研究见 [[pdm-20261120-error-geometry-grid-study]]，不能用研究原型替代正式程序验收。

集合根为 `raw/code/PDM/analysis/`。`validation_v0_1_1/validation.json` 汇总实际计数；manifest 登记本轮代码、输入、结果和测试日志。0.1.1已发布PyPI，公开制品哈希、实际安装路径/版本和三模式GUI均已核验。完整回归225项通过；完整源码ZIP解压后的三个Notebook运行通过。具体日志和公开元数据在同一归档集合，Windows/macOS原生GUI仍未实测。不能仅凭物理测试推断所有交互行为正确。

## 实现定义

- 三模式共用一个密度映射核。P_ADO使用单线偏振与角分布比；P_DCO使用单线偏振与DCO比；PDCO使用方向门条件偏振与DCO比。只有一个共同初态Gaussian宽度sigma，下游布居传播后不重新指定第二个Gaussian。
- 多行探测器组先加总强度，再取比或计算偏振。默认组内相对权重归一，原始加权和须明确选择。未选择方位表示固定极角下的方位强度平均，不是phi=0，也不是4pi积分。DCO与PDCO偏振可分别选择是否保留方位条件。
- 135Pr采用 `[2 W(157.6 deg)+W(133.6 deg)]/[3 W(75.5 deg)]`，其偏振角为75.5度；不能用代表角的函数值代替强度加权。正式实现对54个旧系数控制的最大绝对差为P约2.83e-15、R_ADO约6.22e-15，见 `validation_v0_1_1/logs/legacy-pr135-comparison.log`。
- 输入误差沿用显式中位数分侧高斯变换：每侧质量1/2，端点为标准正态Phi(-1)/Phi(1)，不等误差时中心密度跳跃。不自动把不可达的偏态正态分位目标拟合后再静默改成众数语义。此处是建模约定，不认证原实验误差的生成方法。

代码定位：`GUI/src/multipolepdm/physics/joint.py` 的组强度，`physics/detectors.py` 的方向与有效权重，`pdm/observations.py` 的观测密度。参考态和未观测传播条件仍须与相应原文模型一致。

## 区间与坐标口径

默认在arctan(delta)及sigma/I的边缘PDF上评估精确68% ETI和HDI。每个HDI连通分段分别记录质量及段内最高PDF位置；并列峰或平顶保留全部位置范围。各分段质量之和为0.68，不是每段各0.68。

delta的报告值由角区间端点、q50及各分段mode分别取tan得到。这是角空间HDI的delta表示，不称为重新按delta密度排序所得的HDI。均值与标准差按角PDF积分；报告 `tan(mean angle)` 和有效的 `tan(mean angle +/- SD)`，不把它们冒充delta的期望值与标准差。越界引导值有单独标记。另行导出的delta PDF保留坐标密度变换并作数值归一。

代码定位：`pdm/statistics.py` 的 `summarize_density`、`_hdi_segment`、`_moments` 和 `_delta_report`；测试见 `validation_v0_1_1/logs/statistics-tests.log`。网格采用实际坐标求导和积分；步长不能整除范围时保留较短的最后一格，不偷偷重调全轴步长。

## 正负混合比与大混合比注入

`benchmarks/sigma03_relP80_relR10/` 保存冻结工况、原始表和图数据：三模式，各取delta为正负0.1、0.5、1、5、10；真值sigma/I=0.3，反演仍扫描sigma。目标为5到4的M1/E2，门为4到2的E2；比值极角125/90度，P在90度，PDCO偏振门在125度，主工况作方位平均。误差为 `max(0.1075,0.8*abs(P0))` 和 `0.1*abs(R0)`；这是合成测试策略，不修改实际实验的不确定度。

正式角域正负89.9度、步长0.1度，宽度比步长0.005；另有加密与正负89.99度扩域。输入、生成器、实际末格和代码哈希见 `frozen-job.json`、`frozen-policy.json`、`provenance.json`。

- 30条独立9j生成记录与30条同核记录完成反演。同核只能检查内部自洽；独立展开也仍共享声明的物理假设，不是独立实验。
- 33个有限或纯分量前向点的两生成器最大差为P约8.37e-16、比值约2.44e-15，见 `generator_agreement.json`。
- 每个生成器的30条无附加噪声注入中，角ETI包含真值20条、角HDI包含24条，宽度的两类区间均包含30条。不能把这些确定性包含比例当作重复实验覆盖率。
- 三个代表工况各用100个独立噪声向量，两个生成器成对使用同一噪声，总计600次反演、300个不同噪声对。`repeated_coverage.json` 同时保存分母和精确68%二项区间。
- **PDCO、delta=-10的重复控制存在明显不足：角ETI为0/100，角HDI为6/100，两个生成器一致。** 全部未包含、分支和边界告警保留。18项网格及范围对照通过数值判据，不能据此宣称真值恢复或统计覆盖已经可靠。

主要locator：`deterministic.json` 的 `arctan_delta.*_contains_truth`、`hdi_segments`；`repeated_coverage.json` 的 `case_id=PDCO_-10`；`grid_and_endpoint_sensitivity.json`。本轮没有为提高包含率调角度、缩小误差或固定反演sigma。

## 纯E2校准与退化响应

`GUI/tests/test_pure_calibration_v011.py` 直接检查共同理论手册的 `eq:e2-analytic-test`：完全对齐的2到0纯E2给出归一角分布 `(15/2) sin(theta)^2 cos(theta)^2`，45度处为15/8、P=+1；90度强度节点处不能定义偏振。各向同性初态给归一强度1与P=0。生产振幅与独立系数实现分别核验这些解析值。

选择定则禁止M1时，只作纯E2前向响应，不制造可自由扫描delta的二维PDF。另以允许M1/E2的5到4目标注入精确纯E2观测，检查混合模型的端点行为；有限扫描域不能直接包含无穷delta。36项校准/参考测试通过，其中新增纯分量控制见同名测试文件和归档日志。

对于本模型的轴对称初态，同一极角锥面及其镜像上的方向交换可产生严格常数DCO比。必须保留相应解析恒等式，不能把约1e-15的舍入Jacobian归一成假的二维密度。`physics/symmetries.py` 对全部有权重的方向检查精确条件，不以首行代替多组，也不靠任意删除小正Jacobian实现。其它非零小Jacobian仍只是诊断告警。

## 文献比较的范围

`cases/results_v0_1_1/` 和 `cases/followup/results_v0_1_1/` 共39项声明模型：30项混合反演、9项纯跃迁前向控制，另有8项加密。它们不是39个独立实验。输入覆盖80Se、135Pr、185Au、154Tb、164Yb、190Tl，按核素及能量识别，不依赖工作簿行号，不使用74Br作为本轮验证样本。

新几何快照保留原P/R及左右误差和文献原件哈希；135Pr改用强度加权，154Tb与190Tl的主模型采用不筛方位的理想环。185Au比值顺序假设和164Yb门/目标假设均保留，没有挑较吻合的一组当实验真值。文献delta、固定取向与校准取向只作事后对照，未作为反演约束。`literature_references.csv` 区分固定设置、报告误差及未报告误差；`intervals_68.csv` 保存所有HDI分量及各自mode。

## 可复用结论与开放问题

前向理论的一致性、密度归一和数值收敛，与反演的真值包含率是不同的检查。本轮已验证一套可复现的分组响应和角空间统计实现，同时明确暴露大混合比PDCO工况的包含率缺口。不能用通过的单元测试、纯E2解析值或文献中心值接近程度替代覆盖率结论。下一步物理研究应针对这类工况比较可辨识性、分支质量、扫描域和观测误差模型，而不是静默删去不利结果。

## 软件交付证据

公开版本为 https://pypi.org/project/multipolePDM/0.1.1/ 。`validation_v0_1_1/publication/` 保留API原始响应、获取元数据和两个发布文件的SHA-256核对。`logs/pypi-import.json` 记录从公开索引安装的实际路径与版本；`logs/pypi-gui-smoke.json` 记录三模式真实offscreen计算/保存。独立审查发现的退化方向组、单位切换与导图/失败重试问题均经修复和回归关闭，详细证据见 `logs/independent-review.md`。首次索引缓存尚未更新时的未验证回退运行不计入验收。
