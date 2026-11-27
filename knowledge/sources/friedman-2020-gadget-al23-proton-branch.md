---
type: source
title: "Friedman2020：GADGET低能质子、新相对强度与旧归一参考"
title_original: "Low-energy 23Al beta-delayed proton decay and 22Na destruction in novae"
aliases: [Friedman2020 GADGET Al23, FR20 low proton branching]
created: 2026-10-20
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
authors: [M. Friedman, T. Budner, D. Pérez-Loureiro, E. Pollacco, et al.]
year: 2020
journal: Physical Review C
volume: 101
pages: 052802
doi: 10.1103/PhysRevC.101.052802
citation_key: "friedman_2020_23al-energy-beta"
canonical_source: "Friedman PRC101052802 OSTI1726146 LANLacceptedmanuscript/arxiv191108783v2"
source_url: https://www.osti.gov/servlets/purl/1726146
raw_file: raw/papers/gpt/learning-daily/20261020-DAY18-dsam-lifetime-strength/friedman-2020-gadget-accepted.pdf
raw_sha256: 96ec0f4a4a7a89667a09a226b10695910509a120bb9a0f355ff19ac3fad19e9b
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [23Al, 23Mg, 22Na]
reactions: [23Al-beta-delayed-proton-decay]
methods: [gas-detector, gamma-coincidence, proton-branching, normalization]
tags: [GADGET, background, covariance, lifetime-companion, response]
---

# 新相对强度与旧绝对参考共同给出daughter分支

## Bibliographic Record

M. Friedman等，*Phys. Rev. C*101，052802(2020)，[DOI10.1103/PhysRevC.101.052802](https://doi.org/10.1103/PhysRevC.101.052802)。实际原件来自[OSTI1726146](https://www.osti.gov/servlets/purl/1726146)，9页包含LANL LA-UR-20-24094封面和作者稿8页，不是出版商VoR。封面提供24Nov2020归档身份，body带arXiv1911.08783v2/Jan2020和旧PLB投稿页脚，不据版式改真实PRC发表身份。

另取[arXiv1911.08783v2](https://arxiv.org/abs/1911.08783v2)作版本比较：8页，SHA256`7004bd908148695d1eb32b20b521e2360f753f4d23d8ed6bd95581730fdb8762`；与OSTI正文7页归一文本同，首页只见打印日期Jan2020/July2021差。再生日期不计新实验，两份来源不计独立采集。APS harvest401不绕过访问控制。[原件身份](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-osti_body-download.json)、[版本比较](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-accepted-arxiv-body-comparison.json)。

## Scope and Reading Depth

来源前已声明F23转引.65(.08)%与旧Si/GANIL priming。实际读OSTI封面及作者稿全部8页主线/refs、4图、2表，无编号公式；全页视觉核，Tables1/2另放大。原gas/pad事件、GEANT4输入/producer、两个estimator联合Cov、原γ馈入论文/学位论文尚未由此取得。[actual scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-reading-scope.json)。

## Experimental or Method Setup

NSCL150AMeV36Ar碎裂产生23Al，经A1900/RFFS约69%纯度、约2000pps；P10气体780Torr、125V/cm、40cm×10cm activevolume、MICROMEGAS与SeGA。束.5s植入/.5s测量。A–E pad合并与单padA响应不同；F/G/L/M未instrument，veto约50%，作者以高p稀少论其影响小。不是Si implantation原response或无任何背景的理想计数。

## Summary

新测I204/I866=.063(.004)，低于旧Si约.34(.06)。但I866abs=.41(.01)%仍采用旧工作，Iβγthrough7.79=3.95(.37)%也为旧输入；组合后I204abs=.0257(.0017)%、daughterBp=.0065(.0008)。新相对强度采集与旧参考分列，不能把gas新测误读为所有归一/γ数据已独立重测。旧τ与假J7/2再给omega.24(.08)，它与F23推荐强度有共享输入。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| FR20-1 | 实际OSTI封面+8页作者稿完整主线/4图/2表已读；arxivv2与正文只首页日期差，其它7页归一文本同，不当两次实验或VoR。 | identity-version-and-scope | direct-original | OSTI PDF1–9；body-comparison | true |
| FR20-2 | NSCL碎裂/A1900RFFS、23Al69%/2000pps、P10780Torr/MICROMEGASSeGA为新采集，区别旧TAMUSi/GANILα-tagged；后续旧reference依赖仍保留。 | independent-acquisition-and-boundary | direct | OSTI PDF3 Sec2 | true |
| FR20-3 | PadA减少β背景但高p效率急降；A–E event-sum效率高，F/G/L/M未instrument造成约50%veto，作者以>1MeVp分量小认为影响小。不能全volume/veto混用或称零背景/完美eff。 | actual-response-and-counter-boundary | direct-and-author-assessment | OSTI PDF4 Fig1/2 | true |
| FR20-4 | A–E低204峰仍用exponentialbackground，padA用linearbackground；GEANT4用于eff/形状选择。两谱不是同一个响应/两个完全无模型测量。 | background-and-companion | direct | OSTI PDF5 Sec3 | true |
| FR20-5 | 204/275/583/866效率.98/.98/.97/.93；沿束profile来自595p与583γ的drifttime，横向仅coarse所以不信padA高能eff。作者以profile变化给3%relative系统，sameMC不计独立response测量。 | actual-calibration-input-and-scope | direct-and-author-systematic | OSTI PDF5 Sec3 | true |
| FR20-6 | 583附近含595p→22Na第一激发态，由583γ coincidence识别而未能分峰；204只与511annihilationγ见coincidence，作者支持其到ground。不能把583归一支当单母态，也不把“没见其它γ”升级完整inventory证明。 | companion-observable-and-parent-identity | direct-and-author-association | OSTI PDF4–5 Figs3/4 | true |
| FR20-7 | A–E ratio .066±.005stat±.002sys；替代A(204/275)乘A–E(275/866)得.060±同尺度。作者称stat practically independent、effsys相同，合.063(.004)；共享pad/线/分母需实际Cov核，不能从两值相合证明独立。 | actual-estimators-and-shared-input | direct-and-readiness | OSTI PDF5–6 Sec3 | true |
| FR20-8 | 按作者stat独立/共同sys声明，平均scale≈.004062近打印.004；若声明statcorrelation0/.5/1，scale≈.004062/.004770/.005385。仅条件敏感性，不估真实rho或改实验CI。 | conditional-uncertainty-exercise | task-design | exercise conditional_ratio_combination | true |
| FR20-9 | Table1新204/275/583相对866为.063(.004)/.288(.010)/.685(.022)，旧Si204为.34(.06)而583约.69(.03)。新结果降低低p，并保旧高能reference可用；作者归因旧背景减除是解释，本session未查旧raw以量化错因。 | direct-intensity-and-author-interpretation | direct-and-author-interpretation | OSTI PDF6 Table1/Results | true |
| FR20-10 | I866abs=.41(.01)%采用Saastamoinen2011；新ratio→I204abs=.0257(.0017)%；Iβγ7.79=3.95(.37)%回旧Saastamoinen/Iacob/Zhai。故daughterBp新推断含旧gamma/normalization，不是完全独立pγ绝对重测。 | normalization-and-source-lineage | direct | OSTI PDF6 Results；Refs45/64/65 | true |
| FR20-11 | 打印.063×.41%=.02583%对报.0257保名义.00013个百分点差；用报p与gamma得Bp.0064643、独立scale控制.0007365，近报.0065(.0008)。原Cov/未舍入/全error处理未得，不强配或认新CI。 | actual-printing-check-and-covariance | task-derivation | exercise absolute_beta_proton/daughter_branch | true |
| FR20-12 | 作者adopt(7/2)+及旧meanτ10(3)fs得omega.24(.08)meV；本任务固定中心得.24289，若只取τ12端点则.20241。后者不是原Table2联合下界>.16/CL重建，τ上限95%与Tablecaption90%须角色分列。 | conditional-rate-versus-limit | direct-and-task-derivation | OSTI PDF6–7 Table2；exercise conditional_rate | true |
| FR20-13 | 本文并未新测τ或spin；shellmodelτ.6–1.7fs是模型，作者当时建议重测τ，偏好保守下界而非无条件推荐.24。F23后续新τ/推荐组合不能反写成本篇已完成的测量。 | time-dependent-interpretation-and-model | direct-author-boundary | OSTI PDF7 Results/Summary | true |
| FR20-14 | F23推荐Bp同时用本.65(.08)%与其新.68(.17)%；本文indirectomega又用J04τ。故FR20omega≈.24和F23recommended≈.24不计两个独立强度确认；两个采集的method差异仍有counter价值。 | cross-source-dependence | direct-primary-synthesis | FR20-10/12；F23-9/11 | true |
| FR20-15 | 旧thesisFig5.7两γ相对和×.433给3.53328%，本篇采用through-state3.95%，不是同一组printedinventory。需旧gammaoriginal/归一定义才能闭合，未把一个分母迁作另一个或补原Cov。 | denominator-version-boundary | actual-source-crosscheck | SA11-6；exercise old_thesis_gamma_denominator_boundary | true |
| FR20-16 | 12SHIVAruns的22Na yield/探测距离不确定性为模型输出，非天文检出/另一核branch实验。旧背景更可信与模型张力都是作者解释，原事件/response/fitCov仍未得。 | model-result-and-readiness | direct-author-model | OSTI PDF7；readingscope | true |
| FR20-17 | 后续实际TAMU三报告8页核2005采集与2006两次新run/高能标定/BGO改进，以及旧母态三γ比；它们未给本3.95(.37)%绝对馈入的完整原表。原PRC/thesis未取，不把后续run全当旧event转载，也不由相对比倒填绝对数值/Cov。 | actual-reference-lineage-and-readiness | direct-institutional-companion | TA07-1/2/3/4/6/7/12 | true |

## Analytical Reconstruction and Self-Audit

[算前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-exercise-before.md)、[打印输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-exercise-contract.json)、[程序](../../system/scripts/day17_friedman2020_branch_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/friedman2020-exercise-result.json)。没有用source图粗取新p计数/拟合数据，原数字与不闭合残差都保留。

写`p=r I866`、`g=Iβγ`，则`Bp=p/(p+g)`；其方差还含`2(dBp/dp)(dBp/dg)Cov(p,g)`交叉项，不能因采集不同就假所有reference独立。两个ratio估计共享pad/峰/分母，统计近独立是可检验近似，需要原事件划分和fitCov；本任务没有从一个假设rho生成新实验errorbar。

## Competing Interpretations and Limitations

气体低β背景显著改善低p辨识，仍保background形状/壁效应/beamprofile/efficiency假设。583/595doublet与204无伴随γ是必要companion，也各有分辨率/检出阈值边界。新低ratio可与旧高reference并存，不能从旧source某背景问题否定其全部校准值。

原event/pad histograms、GEANT4真实geometry/response与jointCov未得。下一若追ratio两方案独立性或新reanalysis，先取实际输入；若沿源链，精确γ馈入Iacob/Zhai或GADGET instrument primary提供更高信息，不能以更多toy替它们。

## Knowledge Impact and Learning Decision

`revises`新gasbranch意味着全部绝对归一已独立重测、或.24重合意味着两项独立强度确认；`supports`低背景探测与独立companionline控制；`limits`近独立stat、固定τ/J和打印mean对新CI保证。所有claim needs_review，无human-reviewed或本session新实验τ/Bp/spin/CI。仍仅Day17原窗口Day18无学分知识preview。

## Extracted Pages

[[fougeres-2023-mg23-velocity-difference-lifetime]]、[[saastamoinen-2011-thesis-al23-proton-response]]、[[kirsebom-2016-23mg-dsam-lifetimes]]、[[lifetime-strength-audit-165tm-136nd]]、[[linear-polarization-asymmetry]]。

## γ参考源链的机构原报告补充

[[tamu-2006-2007-al23-gamma-reference-reports]] TA07-1–12原读三个署名报告：2005实验与2006Sep/Nov新runs分开，后者BGO/高能24Al校准改进；不能统称同一批事件或完全独立标定。旧相对三γ比例可核S11转列表，却仍未给本absolute3.95的原完整分母/Σ，原IacobPRC/Zhai thesis未取，不冒source已完整闭合。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 1, "sections": "LANL 接收稿封面与出版版标识"}
- {"start": 2, "end": 3, "sections": "题名、署名、摘要、第1节引言及第2节实验装置"}
- {"start": 4, "end": 5, "sections": "第2节末及第3节数据分析，读图1阳极垫几何、图2质子谱、图3简化衰变纲图及图4符合谱的图注与正文说明"}
- {"start": 6, "end": 7, "sections": "第3节末、第4节结果与讨论、第5节总结、表1相对强度与表2共振强度、致谢开头"}
- {"start": 8, "end": 9, "sections": "致谢续及参考文献 [1]–[70]"}
- 本次获取的具体覆盖：逐页审读 PDF 第1–9页的提取文本，包括封面、全部5节正文、4幅图的图注、2张表的可读数值、致谢及参考文献 [1]–[70]。正文未见编号公式。图像、排版及符号原形待查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | GADGET 的 A–E 合并谱给出 204/866 keV 质子强度比 0.066，单垫 A 的 204/275 比与 A–E 的 275/866 比相乘给出 0.060。两者各报统计误差 0.005、系统误差 0.002。作者合并为 0.063(4)，表1所列旧硅探测器结果为 0.34(6)。 | 实验提取结果 | source-reported | PDF 第4页图2及第3节，第5–6页第3节，第6页表1与第4节。 | true |
| A17-2 | 作者根据 583 keV γ 与约 595 keV 质子的符合，将未分开的 583 keV 谱峰解释为含 583 和 595 keV 两条质子支路。作者另据 204 keV 质子只见 511 keV 湮没 γ 符合，将该质子支路指认为通向 22Na 基态。511 keV 符合来自正文报告，图4所示能区的边界待核。 | 由符合观测支持的支路指认 | source-reported | PDF 第4页第3节，第5页图3–4，待核第5页的箭头、坐标与符合区。 | true |
| A17-3 | 采用旧的 866 keV 绝对质子强度 0.41(1)% 和经 7.79 MeV 态的 βγ 强度 3.95(37)%，作者报 204 keV 绝对质子强度 0.0257(17)%、该态 Γp/Γ 为 6.5(8)×10⁻³。再采用 (7/2)⁺ 和文献寿命 10(3) fs，间接得 ωγ = 0.24(8) meV。表2另列使用寿命上限所得的 >0.16 meV，作者建议采用保守下限。 | 依赖既有输入的间接推算 | source-reported | PDF 第6页第4节，第7页表2及第4节末。待核第7页表注与限值栏。 | true |
| A17-4 | 12组 SHIVA 流体模拟给出 22Na 抛射物质量分数从约 1.1×10⁻⁴ 到 4.3×10⁻⁴。作者将此情景范围对应到约两倍的最大可探测距离差异。 | 新星模型输出 | source-reported | PDF 第6页第4节末及第7页表2下方的 SHIVA 模拟段。 | true |

A–E 合并谱的 204 keV 峰用指数背景，单垫 A 用线性背景。GEANT4 提供效率修正，作者对两种估计采用共同效率系统误差及统计近独立近似。两个估计共享谱与峰输入，本件无联合协方差。绝对归一取 [45]，γ 馈入取 [45,64,65]，寿命取 [41,63]，自旋采用文献指认。比较注所载 Fougères 2023 推荐组合复用本篇分支，数值接近的共振强度不能计作两项独立确认。

- FR20-6 的定位改为 PDF 第4页第3节及第5页图3–4。将 511 keV 符合归于第4页正文，并保留探测灵敏度限制。
- 归档著录保留接收稿身份和出版版 DOI。第1页抽取漏掉题名中的核素与 β，用第2页题名补齐。第5页效率符号有乱码，第6页 SHIVA 段末的白矮星质量和吸积率缺清晰的太阳质量符号，分别查原页。
- 第7页抽取写作 1.275-keV，疑有单位或小数点错误。查 PDF 第7页，确认后再规范为 1.275 MeV 或 1275 keV。第8页参考文献 [3] 的年份抽成 987，[31] 缺刊名，均待查该页，暂缓补写。
