---
type: source
title: "Geant3+VMC固定版本：无偏振Compton核与GR97重放边界"
aliases: [G3COMP pinned baseline, Geant3 VMC Compton component audit]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: software-source-code
reading_depth: skimmed
title_original: "Geant3 + VMC; G3COMP/G3FANG/G3DROT selected source"
authors: [Geant3 and VMC contributors]
year: 2026
citation_key: ""
citation_key_status: no-local-software-BibTeX-entry
canonical_source: "vmc-project/geant3@347fc6804dd116c66c2695df5d2c03d166a0364c"
source_url: "https://github.com/vmc-project/geant3/tree/347fc6804dd116c66c2695df5d2c03d166a0364c"
raw_file: "raw/data/gpt/day16-20261018/geant3-347fc6804d-gcomp.F"
raw_sha256: "a97226dc5ae5846cb038e9d2ca38f3591e183a652ff990dceec009a838042020"
raw_storage_status: public-staging-verified-vendor-not-redistributed
nuclei: []
reactions: []
observables: [Compton-energy-distribution, transport-cuts, polarization-interface]
methods: [source-audit, Monte-Carlo-component-benchmark]
tags: [software-provenance, Geant3, unpolarized-baseline, response-readiness]
---

# 代码字段、物理调用路径和历史producer分别核验

## Bibliographic Record

公开仓库[Geant3+VMC](https://github.com/vmc-project/geant3)的本轮固定commit为`347fc6804dd116c66c2695df5d2c03d166a0364c`，committer date2026-01-06，subject“Making version4.5”。README说明它包括Geant3.21与TGeant3 VMC接口。这个版本指针不是[[garciaraffi-1997-monte-carlo-compton-polarimeters]]的1997修改版身份。

## Scope and Reading Depth

完整读G3COMP、G3FANG、G3DROT、G3COMPI、G3TGAMA函数文件及所用头文件，G3INIT只定向读常量/默认cuts。树API明确truncated=false、1846条；不是全仓库内容审计。选中文件逐个核Git blob SHA-1与SHA-256，vendor只留repo内tmp，不纳入本Wiki发布；许可状态未由repository metadata确定，不作重新分发声明。

例如[gphys/gcomp.F](https://github.com/vmc-project/geant3/blob/347fc6804dd116c66c2695df5d2c03d166a0364c/gphys/gcomp.F)的Git blob为`aef13d0711c015aafccdc9ffb805d1d1f67b5199`，SHA-256见frontmatter。实际文件在`tmp/day16-geant3-producer/`。初gckmax下载ConnectionError后由同一固定blob API取得、核hash，未猜补参数；原header的MXGKIN为300。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| G3-1 | 当前固定仓库为Geant3.21+VMC/version4.5的公开快照；其历史注释不能独立认证1997 GCOMPOL/POLAR/GDROT3 producer与输入包。 | software-version-boundary | direct-metadata-and-code | README；commit347fc6804d | true |
| G3-2 | 所读G3TGAMA的Compton分支调用G3COMP；G3COMP按unpolarized KN抽样、phi均匀，函数体不使用POLAR。 | actual-callpath | direct-source | gtrak/gtgama.F:L219；gphys/gcomp.F:L108 | true |
| G3-3 | gctrak.inc有COMMON/GCTPOL/POLAR(3)，但字段存在不代表上述Compton路径实现偏振；本pin树未见GCOMPOL/GDROT3文件名，不证明所有文件内容或其它仓库中无该例程。 | interface-versus-capability | direct-source-and-scoped-search | geant321/gctrak.inc:L32；完整treefilenameaudit | true |
| G3-4 | EMASS默认double常量为.0005109990615，能量与GeV一致；G3COMP使用VECT(7)/EMASS。GR97 Table MeV输入须转换，不能按同数值直接喂入。 | units-and-kinematics | direct-source | geant321/gconsp.inc:L52；gphys/gcomp.F:L53–54 | true |
| G3-5 | G3INIT所读默认CUTGAM/CUTELE=.001，即1MeV；G3TGAMA对GEKIN≤CUTGAM直接停止。它们是transport cuts，不等同于GR97每晶体电子学阈值50/60/150keV；未声称GR97使用这些默认值。 | configuration-object-boundary | direct-source | gbase/ginit.F:L230–231；gtrak/gtgama.F:L43 | true |
| G3-6 | 本run原样编译G3COMP/G3FANG/G3DROT与原headers；harness显式提供确定性GRNDM和G3EKBIN空bookkeeping shim，不编译完整G3TGAMA/材料/几何输运。 | component-execution-scope | actual-build | geant3-component-benchmark-contract | true |
| G3-7 | 三能量各200000个组件MC事件的cosθ/phi分布与独立unpolarizedKN/均匀phi数值积分相容于预设诊断界；守恒、massshell和方向norm最大相对误差约4.64×10^-7。不是探测器Q或实验置信度。 | simulated-component-result | actual-execution | 本页组件结果；benchmarkanalysis | true |
| G3-8 | 同RNG下两正交初始POLAR给完全相同输出；旋转入射轴后能量相同、相对cos最大差约1.07×10^-7。它验证基线的无偏振/旋转语义，不验证polarizedresponse。 | interface-and-frame-control | actual-execution | benchmarkPAIREDcontrols；G3FANG/G3DROT | true |
| G3-9 | G3COMP在两种transport cuts均高于相应能量时本地沉积并停止；另有electroncut/ICOMP≠1沉积branch。能量仍闭合，不代表所需coincidence样本还存在。 | cut-failure-control | source-and-actual-execution | gphys/gcomp.F:L95–103/L156；benchmarkCUTcontrols | true |
| G3-10 | G3COMPI另需材料Z、能量表和bank指针；点核通过不恢复原GCOMPOL、材料response、geometry/cuts、原校准ledger和Cov，不能重放GR97的40%/10%或TableI。 | detector-readiness | direct-dependency-and-boundary | gphys/gcompi.F；GR97modified-producer boundary | true |

## Component Benchmark

冻结输入为0.0005、0.0015、0.004GeV（原Table能量0.5、1.5、4MeV）、原REAL4数据精度/double constants、zero transport cuts、ICOMP1。源码与headers保持原字节。GNU Fortran13.3.0实际compile0、execute0。

| E/MeV | MC平均E′/E | 独立KN平均 | cosCDF最大差 | phiCDF最大差 |
| --- | --- | --- | --- | --- |
|.5 |.65850816 |.65863344 |.001077 |.002290 |
|1.5 |.50517759 |.50531653 |.000894 |.001555 |
|4 |.39282534 |.39306439 |.001308 |.001410 |

每行200000事件，seed从20261019按行递增。独立KN积分用Gauss256/512核稳定性。预设六条CDF的DKW式抽样诊断界约.006384；它是本数值检查在理想iid解释下的保守诊断，不证明PRNG独立性，也不是实验CI。规范化bin的相关性仍由共同总数产生。

zero cuts只是隔离单个碰撞kernel；没有宣称它是GR97真实transport设置。控制中把两cut设为.001GeV后，.5MeV光子全作local deposit，photon能量为0且ISTOP2；能量守恒仍通过。另两个控制保留约.192542MeV光子、沉积约.307458MeV，改变的是tracking/stack对象，不是硬件门阈值。

## Summary

可重算的真实代码组件确认了无偏振KN抽样、单位、方向旋转及cut语义。POLAR字段和软件版本名不认证偏振物理，单碰撞分布/守恒通过也不认证完整探测器response。

## Competing Interpretations and Limitations

原GR97说明需要GCOMPOL、POLAR记录和GDROT3；当前读到的标准路径保持均匀phi且不消费POLAR，符合它作为unpolarized baseline的身份，不构成软件错误。不能把现代仓库或本harness称作原1997修改版重放。

G3COMP注释还明确忽略bound-electron效应。材料mean-free-path、photoelectric/pair channels、真实几何、电子学阈值和原采样/拟合Cov没有进入这个组件检查。相关原代码文件名在树中未出现，只是限定路径检索结果。

## Knowledge Impact and Learning Decision

`supports`自由电子基线与原GR97需要修改的理由；`limits`从POLAR字段、同程序名、正确守恒或unpolarized分布直接认证偏振校准；`revises`transport/electronics cuts可互换的隐含用法。这里只得到软件组件级可复算结果，完整experimental/原detectorMC仍not-ready；Day17仅partial预习。

## Reproducibility and Self-audit

[固定输入获取器](../../system/scripts/day16_fetch_geant3_component_inputs.py)按合同逐个核SHA-256/Gitblob、仅保存tmp；本次获取器actual0是十份已存cache的只读核验。再运行[组件程序](../../system/scripts/day16_geant3_compton_component_benchmark.py)、[冻结合同](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/geant3-component-benchmark-contract.json)、[实际build/执行/统计结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/geant3-component-benchmark-result.json)保存source hash、compiler、harness、seed、N、cut与全部失败控制。未发布vendor源码、未构造原GEANT3材料包或新核实验输入。

P0：未识别未隔离的来源/权限/路径问题。P1：版本、组件与历史producer必须分开，源码单位和cut只对这个pin/设置作证；所有新claims needs_review。

## Extracted Pages

[[garciaraffi-1997-monte-carlo-compton-polarimeters]]、[[gr97-stokes-response-and-merit]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]。
