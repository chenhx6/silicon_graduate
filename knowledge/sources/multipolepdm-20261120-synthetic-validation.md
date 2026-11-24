---
type: source
title: "multipolePDM 20261120：独立响应与合成反演验证数据"
aliases: [multipolePDM三模式合成验证]
created: 2026-11-20
updated: 2026-11-24
status: ai-draft
review_status: unreviewed
source_type: research-code-and-synthetic-data
reading_depth: read
title_original: "multipolePDM three-mode synthetic validation"
year: 2026
canonical_source: "Local multipolePDM implementation, independent 9j reference and seeded synthetic validation"
raw_file: "raw/code/PDM/analysis/benchmarks/manifest.json"
raw_sha256: "3060ac4b8dcad5475236eb17d27be33c039df2c1b65d0658d5ebf7f174984f1b"
code_snapshot_file: "raw/code/PDM/archives/20261124-code-inputs/manifest.json"
code_snapshot_sha256: "de12a545155276455334b05626cdab32a9dc7874c47cbab7ff7c052d9a284b7b"
raw_storage_status: archived-local
archive_required: true
tags: [pdm, pdco, synthetic-validation, uncertainty, numerical-convergence]
---

# multipolePDM 独立响应与合成反演验证

## Bibliographic Record

2026-11-24整理软件基线时，将两项代码依赖改绑到固定快照，保留原条目的大小与SHA-256。旧`run_benchmarks.py`从0.1.0源码包恢复，逐字节匹配原记录；当前0.1.1工作源码不回退。原清单完整字节及恢复来源保存在`code_snapshot_file`集合，计算输入、输出和科学结论未改。

本项是经用户授权生成的本地计算证据，不是发表论文或新实验。原件集合位于 `raw/code/PDM/analysis/benchmarks/manifest.json`；代码、种子、网格、核态与几何由JSON、公开脚本及独立参考实现记录。公开代码根为 `raw/code/PDM/`。

## Scope and Reading Depth

已核对实际执行结果、独立参考与生产核桥接、JSON汇总和选定区间端点。测试覆盖允许M1/E2的输入及纯项前向极限，不认证任意核反应源模型、任意探测器响应或所有文献实验。三种模式各自保留偏振的条件定义。

## Summary

生产响应用显式光子振幅矩阵；独立响应由Droste广义9j系数与统计张量组装。两者共享标准角动量代数工具，但不共享生产振幅或拟合结果。输入delta采用KS/Droste约定，生产基底包含逐多极的 `(-1)^L` 相位；依据见 [[droste-1996-pdco-formalism]]、[[starosta-1999-pdco-experimental-test]] 与 [[krane-steffen-1970-cd110-mixing-ratios]]。

## Key Results

| ID | 计算结论 | locator | claim_kind | evidence_level |
| --- | --- | --- | --- | --- |
| PDM26-1 | 24项独立参考测试和7项生产桥接测试通过，包含两种发射次序、半整数、非相邻混合路径、非零相对方位角和两个偏振原始强度 | `GUI/tests/test_independent_reference.py`、`test_reference_bridge.py`；不是独立实验或原作者代码 | numerical-validation | direct-local-computation |
| PDM26-2 | 三模式共60条确定性生成／反演记录，正负delta包含0.2、1、3、10量级，另有零混合控制和6项纯分量前向控制 | JSON `deterministic`、`pure_forward`；正负delta不要求P反号 | numerical-validation | direct-local-computation |
| PDM26-3 | 三个代表工况各100个独立噪声样本，分别经同核和独立9j生成／反演，共600次反演；两生成器共用标准噪声流，不能当600个独立实验 | JSON `repeated`、`settings.error_model`，seed20261120 | numerical-validation | direct-local-computation |
| PDM26-4 | 默认3121x201网格加密至6241x401时，36项delta区间检查达到执行合同阈值；最大xi中位数位移约3.35e-5rad，最大端点位移约1.40e-4rad | JSON `convergence`；仅为所列工况的离散收敛，不证明积分域充分 | numerical-validation | direct-local-computation |
| PDM26-5 | 将xi边界从+-1.56扩到+-1.5705rad会改变大混合案例的部分HDI分支；P_ADO delta=+10的95%HDI从一段变成两段。六个+-10真值均仍包含在相应95%ETI及HDI内 | JSON `xi_bound_sensitivity`；保留域敏感性，不因加密收敛宣称截断无影响 | numerical-validation | direct-local-computation |

独立生成器的三个重复工况，delta的68%ETI/HDI经验包含率依次为P_ADO 0.64/0.67、P_DCO 0.69/0.64、PDCO 0.63/0.70；对应95%为0.96/0.96、0.95/0.95、0.95/0.96。sigma/I的包含率并不总接近标称质量：PDCO示例的68%ETI/HDI为0.97/0.83。各组只有100个噪声样本，不能把边缘PDF质量当作频率覆盖率保证。所有参数、误差及分支以JSON为准，不用摘要覆盖原始数值。

## Competing Interpretations and Limitations

- 同一程序生成再反演只说明内部自洽；独立代数组装补充物理核验，但仍不等于实验验证。
- 点响应与某些论文的阵列平均不是自动等价。此数据不能弥补实测案例缺少门线、路径或几何的输入。
- 网格加密与积分域扩展是不同检查；大混合比、边界和多分支必须保留实际结果，不能按文献delta选择分支。
- 经验包含率仅属于所给Gaussian独立观测误差和有限模型域，不推出所有实验误差模型的校准性；高于标称值也不能简单称为优越。
- 未加入chi-square拟合比较。Windows/macOS原生GUI未由该计算集验证。

## Extracted Pages

- [[pdm-three-mode-execution-contract-20261120]]：三模式、坐标、条件偏振与发布合同。
- `raw/writing/pado/20261029_review_v1/PDM/main.tex`：秘书手册中的理论、实现及图文核验。
- `raw/code/PDM/analysis/scripts/run_benchmarks.py`：可公开重跑入口。
