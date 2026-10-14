---
type: source
title: "NPTool 2019对象：反冲四动量、速度getter与单位"
aliases: [NPTool Reaction object contract, NPTool velocity getter provenance]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: public-software-code-object
reading_depth: deep-read
title_original: "NPTool Reaction/Nucleus kinematic object at pinned NPTool.2.dev revision"
authors: [Adrien Matta, Pierre Morfouace, NPTool contributors]
author_list_scope: source-file-headers-not-entire-project-contributors
year: 2019
upstream_repository: "https://github.com/adrien-matta/nptool"
upstream_branch: NPTool.2.dev
upstream_commit: 415ad50066f715ca1de312da1202201f9381e87e
upstream_committed_at: 2019-09-02T12:38:49Z
canonical_source: "https://github.com/adrien-matta/nptool/blob/415ad50066f715ca1de312da1202201f9381e87e/NPLib/Physics/NPReaction.cxx"
data_version: pinned-2019-public-Github-object-successor-not-read
citation_key:
raw_file: "raw/code/gpt/day13/nptool-2019/NPReaction.cxx"
raw_sha256: "e9babf556002357bfed1bb87dcd86efd66959f45779c425887536c3dd43d4d88"
raw_storage_status: reserved-unpopulated-public-code-copy-only
nuclei: []
methods: [two-body-kinematics, velocity-reconstruction, doppler-correction, unit-audit]
tags: [nptool, code-object, four-momentum, caller-contract, stage, historical-version]
---

# 计算对象不能替代测量与执行版本

## Bibliographic Record

来源是公开的软件对象，非实验论文：固定上述2019commit的`NPReaction.cxx/h`，并读相关`NPNucleus.cxx/h`、unit/constants、README与LICENSE。MainCPP的GitblobSHA为`8b0e4ac798b1a87eb607fed42cfa522ffd3e4691`，SHA256如上；每个取得对象均核Gitblobheader+bytes与SHA256。

GitHub README lines1–5明确迁往`https://gitlab.in2p3.fr/np/nptool`。本次GitLab API ConnectionError、landing ConnectTimeout，未读取新站代码；不能称这份2019对象为2026最新版本、e775s的实际commit或论文executiontrace。源仓库的GitHub阅读与Wiki的Gitee维护是不同对象，本任务未为Wiki建立GitHub维护链。

`raw_file`保留未填充。临时副本在`tmp/day13/reopened/nptool-public-object/`，文件名将斜线换为双下划线；未build/execute第三方source。RootLICENSE声明GPL2.0，GitHub自动SPDX给NOASSERTION；只记录直接notice，不补写or-later或当前GitLab许可。

## Scope and Reading Depth

- Covered scope：Reaction主CPP/header物理、输入、初始化、重建与graph逻辑；Nucleus选定Mass/转换/setter/getter、实际datafilepath；unit/constants与Beam继承声明；README迁移/许可。此source定义为这些代码对象的审计，不是整个NPTool仓库摄入。
- Not covered：最新GitLab代码、生产analysiscaller/e775s或2017设置、ROOT实际执行、完整Nucleus/Beam generator、mass-table数值及原2016方法论文全文。Dependency文件整体hash不等整体科学审核。

## Paper Question and Scientific Motivation

与[[zanon-2023-o20-high-precision]] ZA23-2的particle-assistedentry相连：proton测量经哪种数学/对象流程给重核初四动量？velocity/TOF字段的单位、producer、mass/state与referenceframe是什么？计算getter之间相符是否构成独立速度证据？

## Method and Design Logic

明确Beam/Target/Light/Heavy角色→按beam总动能与mass初始化四动量→以light动能/角重建heavy四动量/Ex→选择正确getter并转换坐标→另行处理target/emission/exithistory。API、caller与transport分别审计，不从通用库推断论文的实际使用路径。

## Key Evidence and Reasoning Chain

Source代码和byteidentity支持“本对象做什么”；论文报告支持“该实验利用什么数据”。两者还缺执行commit/config/caller绑定，不能合成为production证明。特别是多个由同energy/mass生成的速度/TOF/rigidity字段不增加独立measurement。

## Summary

核心contract是MeV总动能、radian角、beam+z/targetrest/默认reactionplaney0；反应四向量与Nucleus对象为不同状态容器。Nucleus速度以energy和其Mass重新计算，TOF字段为inverse-speed/per-length量。Mass含配置Ex，getter的独立性、更新次序与mass-shell一致性需要明确；本次静态审计没有指认真实实验错误。

## Experimental or Theoretical Setup

一个历史公开NPTool对象，无新实验。梁参数、groundmass/excitation、轻粒子能量校正和方向来自caller/config；该函数不自动提供真实beam分布、vertex、materialtransport、feeding或detectorresponse。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NP19-1 | 这份Reaction字符串constructor第一token A设为Beam、第二b设为Target，Light=c/Heavy=D；Print()另按target(beam,light)打印。不能仅凭字符串外观假设角色。 | experimental-criterion | direct | NPReaction.cxx lines98–150,378–393; NPReaction.h lines64–67 | true |
| NP19-2 | KineRelativistic与Reconstruct明确energyMeV、angle rad；初始化s=m1²+m2²+2m2(Tbeam+m1)，Tbeam为整颗beam的kineticenergy，非默认per-A。 | experimental-criterion | direct | NPReaction.cxx lines249–255,286–299,586–611 | true |
| NP19-3 | 重建设E3=m3+T3、p3=sqrt(E3²−m3²)，P4=Ptotal−P3，返回P4.Mag−Nucleus4.Mass；输入kinematics对应caller指定的interaction条件。 | model-result | direct | NPReaction.cxx lines286–299 | true |
| NP19-4 | 初始化beam沿+z、targetrest；重建light向量(p sinθ,0,p cosθ)，无φ参数。坐标/φ/worldrotation需caller处理，不从该方法自动获得完整worldvelocity。 | experimental-criterion | direct | NPReaction.cxx lines291–292,604–619 | true |
| NP19-5 | Reconstruct更新Reaction自身Lab3/4并returnEx；SetNuclei3额外调用两Nucleus.SetEnergyImpulsion并赋fThetaCM/fExcitation4；两getter路线不能视作同一次状态更新。 | experimental-criterion | direct | NPReaction.cxx lines286–299,621–632; NPReaction.h lines128,188–191 | true |
| NP19-6 | Nucleus.Mass=Au+massexcess/1000−Zelectronmass+Ex，包含该对象Ex；header/comment的nubtab03与实际SetUp读取nubtab12路径不同，数据文件版本需另验。 | experimental-criterion | direct | NPNucleus.h lines137–144; NPNucleus.cxx lines180–220 | true |
| NP19-7 | SetEnergyImpulsion保存P后取K=P.E−Mass并用energy/mass重算β等；scalarβ不是直接P.P/P.E。两者相同需对象Mass与P的invariantmass一致，更新Ex后cache还需按实际setter重建。 | experimental-criterion | direct | NPNucleus.h lines127–143; NPNucleus.cxx lines415–432 | true |
| NP19-8 | GetTimeOfFlight读取的转换量为1/(β cSI)，没有flightpath；GetVelocity的因子给cm/ns。它们从energy/mass等计算，不是rawdetectorclock测量。 | experimental-criterion | direct | NPNucleus.h lines111–116; NPNucleus.cxx lines394–431; NPSystemOfUnits.h lines32–40,101–115; NPPhysicalConstants.h line48 c_light | true |
| NP19-9 | EnergyToBrho/BrhoToEnergy缺省Q=-1000时取GetZ()，即默认核电荷值；ionicq信息必须按actual调用传入/配置，不能把模型Bρ当独立测量。 | experimental-criterion | direct | NPNucleus.cxx lines385–410; NPNucleus.h conversion declarations/setters | true |
| NP19-10 | DopplerCorrection以storedβ和suppliedθ做E_lab(1−βcosθ)/sqrt(1−β²)，标准inverse；没有在函数内用photon/recoil3Dvector决定相对θ或速度stage。 | experimental-criterion | direct | NPNucleus.cxx lines435–438 | true |
| NP19-11 | EnergyLabFromThetaLab是另一angle→energy helper；source警告某些双支情况下50/50随机取branch、超角范围返回−1，建议需要双支时用CMdistribution。 | author-interpretation | direct | NPReaction.cxx lines316–374 | true |
| NP19-12 | IsAllowed仅比较lab总energy与outputs restmass总和；实际two-body invariantthreshold还需s≥(m3+m4)²。后半为任务physicaldomain检查，未断言actualcaller未另作检查。 | our-inference | direct | NPReaction.cxx lines801–810; initialize lines587–605 | true |

## Nuclear Structure Information

无新能级/寿命/强度或实验布居；Ex是以输入mass/beam/轻粒子量构造的invariant estimate。库getter不能代stateassignment、beam/targetcalibration、materialloss或feeding测量。

## Authors' Interpretation

Sourceheader将KineRelativistic用于simulation、Reconstruct用于analysis，angle-only函数有explicitbranchwarning；README声明迁站。这些代码注释作为本版本文档保存，不称实际e775执行说明。

## Model Results

源对象的重建公式与字段转换为model/算法关系。任务的mass/state、MeV/A与threshold数值sanity另在[[doppler-correction]]，不是NPTool第三方运行结果、实测beta偏差或论文生产bug。

## Competing Interpretations and Limitations

- 同一P有正确的fourvectorβ与不同restmass约束下的scalarβ；应明确估计器/mass-shellprojection及Σ，而不把差别当两次独立measurement。正确caller可使两者一致。
- Reconstruct与SetNuclei3/GetNucleus4/GetEnergyImpulsionLab4具有不同更新路径；未知actualcaller时不推断它取了stale/wrong字段。
- 坐标默认reactionplane、API rad与graph degree、总MeV与AMeV、velocity/TOF混合单位各有具体source依据；真dataset绑定/角旋转仍未得。
- `Mass()`已含Ex，其他层也可能加reactionExc，必须核配置/角色/缓存；不把ground/state质量混用或optionalrare-beam情况移植为本文数据偏差。
- IsAllowed的简单helper不是完整invariantphysicaldomain证明；可能有上游guard/高于threshold的工作域，actualusage未验。
- Github2019对象和当前GitLab/实验commit没有attestation；新站网络失败不等权限拒绝。只做历史对象scope，未build/execute或改第三方代码。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| NP19-AR1 | 数据与prior | measuredlight inputs经beam/mass/energycorrection假设给P4；这种约束有价值，仍非无prior的直接TOF。 | NP19-2/3/4; ZA23-2 | unreviewed |
| NP19-AR2 | getter独立性 | 字段必须记录producer、epoch、mass/Ex、units/frame；derivedvelocity/TOF同源不算independentinput。 | NP19-5/6/7/8/9 | unreviewed |
| NP19-AR3 | source versus production | 字节/source契约已核，actualcaller与运行commit仍unknown；保持L3 objectaudit与L4refit边界。 | NP19-1–12; ZA23-2/3 | unreviewed |

## Knowledge Impact and Learning Decision

写回[[doppler-correction]]及[[doppler-velocity-validation-contract]]的particle-entry/code-field契约，支持L3readiness判断；actualexperimentalrefit仍not-ready。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-context | [[zanon-2023-o20-high-precision]] | particle-assistedentry与NPTool引用；不证明相同commit/caller。 |
| methodological-context | [[assie-2021-mugast-agata-vamos]] | lightenergy/angle/beam与初四动量的条件依赖。 |
| methodological-bridge | [[doppler-correction]] | 反冲inputstage、Getter/Mass/单位、covariance与physicaldomain。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | source/caller/data绑定不能由库名代替。 |

## Human Review Triage

P0：pin/blob/hash/publiccopy/历史版本边界隔离，无第三方执行或raw改动。P1：NP19-2/4/5/6/7/8/9/10/12及actualcaller配置；保持unreviewed，不指认实验bug。

## Extracted Pages

MainReaction CPP/header完整physics/input/graph主线；Nucleus的Mass、SetUp、setters/conversions、units/constants与Beam继承选定对象。Mass-table数值、currentGitLab与实验caller未读。
