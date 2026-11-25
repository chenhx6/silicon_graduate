---
type: source
title: "PDM两组几何的正式响应注入、冻结PDF与0.1.2软件验证"
title_original: "PDM deterministic recovery in two detector geometries and software release evidence"
aliases: [PDM两组几何恢复来源20261125]
created: 2026-11-25
updated: 2026-11-25
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized local calculation and direct artifact/online-release verification"
raw_file: "raw/writing/pado/20261029_review_v1/PDM/figures/data/two_geometry_20261125/manifest.json"
raw_sha256: "0b08ab2e74b8813e097ad9371b0aaa2720118a2d696181732fc138e450173b3f"
raw_storage_status: archived-local
archive_required: true
release_artifact_file: "raw/code/PDM/analysis/validation_v0_1_2/release/artifact-archive/manifest.json"
release_artifact_sha256: "1a992dfd3e63de2d03cf797b9b28d2410c54d6d9bc6dd57240fa4c860b6c5dc3"
citation_key: PDMGeometryRecovery20261125
evidence_sources: [pdm-deterministic-report-revision-20261124-source, multipolepdm-20261120-v011-validation]
tags: [pdm, deterministic-validation, mixing-ratio, response-geometry, software-validation]
---

# 两组几何注入与软件验证原始工件

## Bibliographic Record

用户授权的2026-11-25本地模型计算、冻结PDF与直接软件验证集合。非新实验采集，非独立响应正确性论文；软件正式发布身份为PyPI multipolePDM 0.1.2，计算生成版本及代码哈希另按当时真实状态保存。

## Scope and Reading Depth

逐项读取60注入与30文献二维模型的输入/数组/统计，核对30新例的真实环条件；独立积分核查90套PDF，逐页视觉检查131页及修复页。不重新分析原始实验计数、不修改实验数据或汇总xlsx；9纯项仅前向，不制造二维反演。

## Summary

正式响应生成的确定性测试给出旧30复用与新30计算，共60主要案例；另保留30文献模型/15跃迁/9前向。新HDI成员计数改善，但大混合比的峰、ETI中位数及边界仍有限制。详见 [[pdm-two-geometry-recovery-20261125]]。

## Key Results

| ID | claim_kind | evidence_level | locator | 结论及边界 |
| --- | --- | --- | --- | --- |
| G26-1 | model-result | direct | `results.json:old_injections/new_injections`；新集合`ready.json:counts` | 旧30不重跑，新30为3张正式响应及30次独立映射；不是60种delta |
| G26-2 | model-result | direct | 新集合`aggregate_summary.json:all`、N01–N30的`statistics.arctan_delta` | 角HDI含真值30/30、ETI27/30；确定性成员关系，不是频率覆盖 |
| G26-3 | model-result | direct | `results.json:new_injections`的N30、N21 | PDCO正10的tan角mode6.04/中位数0.24，负10峰在有限角边界；新几何不保证无偏 |
| G26-4 | model-result | direct | 各行`statistics.*.hdi_segments`和`source_npz`；numeric-audit.json | HDI质量和.68、mass_fraction和1，各角/宽度边缘独立；tan端点与真实delta PDF不同 |
| G26-5 | synthesis | direct | `results.json:literature/forward_only_controls`；历史source | 30文献二维模型对应15跃迁，9前向另列，报道值不是真值 |
| G26-6 | model-result | direct | `full-pytest.xml`、`release/wheel-env_verification.json`、`release/wheel-gui.json` | 333测试及隔离包CLI/GUI通过；复用现有依赖且GUI仅Linux offscreen |
| G26-7 | synthesis | direct | `release/pypi-readback.json:files`及上传日志 | PyPI 0.1.2两制品与已验证构建SHA一致，不用本地build代替在线发布 |

## Extracted Pages

冻结main.pdf共131页；六张完整主表在18–20及56–58页，各一模式10行。O05/O18/O19/N04的修复图在29/42/43/65页已再次单页目视；两位worker覆盖1–131页，文献四联图与9前向表分别保留。机器locator优先行ID和原始数组，不以阅读版页数代替输入身份。

## Artifact Locators

本来源是软件计算与直接验证证据，不是独立实验或对响应核的独立证明。配套长期解释见 [[pdm-two-geometry-recovery-20261125]]。

- `results.json`：`old_injections`、`new_injections`、`literature`分别30条；各行input、source_npz、statistics、diagnostics、figure可还原输入与全部图表。旧数组只读恢复，PDM零重跑；新数据正式30例经独立观测映射。
- `final_report_snapshot_v2/main.pdf`：本次131页冻结报告，canonical阅读文件保持原PDM/main.pdf。六张主表页18、19、20、56、57、58横向，其余竖向；60注入及30文献二维模型各一张四联图。
- 新计算集合`analysis/benchmarks/geometry26_20261125/`：ready.json记录3张响应、30真值响应、30映射及27缓存命中；validation.json独立核积分/分位数/质量，provenance记录历史与源码身份。错误固定phi试算仅为隔离诊断，不计正式案例。
- `analysis/validation_v0_1_2/report/numeric-audit.json`：90套保存PDF的独立两节点Gaussian积分，归一化、mean/std、ETI16/50/84、HDI全部局部mode/mass/mass_fraction及tan转换通过，容差2e-12，无新反演。
- 同目录`report_final_typography/`有最终131页布局、两位worker覆盖全页的实际视觉检查及父代理密集三分支页复核。95幅最终图字体／碰撞均零失败；图下摘要默认两位小数，小非零用科学计数法，密集响应网格300dpi。静态源码预检零FAIL；三项通用期刊预设WARN由实际字形审计、PDF交付范围和300dpi下限逐项复核，不声称无诊断。
- `analysis/validation_v0_1_2/full-pytest.xml`：333项程序测试通过；GUI/JSON/幻灯片专项回执另存。全新依赖安装因9p工作盘大文件写入停滞停止；随后使用任务隔离包环境和现有科学依赖验证wheel、三模式CLI、Qt offscreen及包内示例，导入路径明确在wheel环境而非源码。
- `analysis/validation_v0_1_2/release/pypi-readback.json`：正式PyPI 0.1.2的wheel及sdist SHA-256与已测试构建一致。从PyPI安装确切0.1.2后，`release/pypi-env_verification.json`与`release/pypi-gui.json`再次核三模式CLI、Qt入口、v3导出及包内示例；不以本地build冒充在线发布。

## Competing Interpretations and Limitations

新角HDI含真值30/30，ETI27/30；旧分别24/30与20/30。新HDI分支1/2/3段分别20/8/2例。大绝对值12例的ETI中位数绝对值均小于真值。PDCO正10的角mode直接tan为6.04，中位数0.24；负10的角峰在有限角下边界，tan表示−57.29。新几何仍不保证无偏。

全部主要统计在arctan(delta) PDF评估68%，直接tan与真实delta PDF严格分开。角域±89.9°→±89°及PDCO方向门125°→90°同时变化，不能单因素归因。9纯项前向控制、30文献声明模型、15条不同跃迁与共享输入依赖继续区分；文献报道值不是注入真值。

## 保存与历史身份

本清单的报告主文件绑定最终快照而非持续编辑的canonical文件；数值源码另存固定快照。旧179项清单原字节保留，仅在新的历史绑定清单中将旧main.tex/main.pdf指向原哈希一致快照。计算的生成版本0.1.1与正式包0.1.2身份分别保存，不回填历史元数据。运行期间物理/映射/统计源码稳定，GUI/IO/版本维护漂移如实记录。

最终排版修订使用新快照与renderer_v2，前一渲染清单原字节和95幅图均保留，期望哈希未被改写；mean_endpoint_flags.json逐侧记录“--”的越域或正切奇点原因。无新增PDM反演。

0.1.2的wheel与sdist另以release_artifact_file副清单登记于GUI/dist固定版本文件，逐字节匹配PyPI SHA-256；不依赖tmp保留唯一发行制品。
