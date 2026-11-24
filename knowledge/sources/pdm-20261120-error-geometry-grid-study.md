---
type: source
title: "PDM：不对称误差、探测器组权重与网格对照研究"
title_original: "PDM asymmetric-error, weighted-geometry and grid-resolution study"
aliases: [PDM不对称误差的处理方案, PDM网格寻优研究]
created: 2026-11-20
updated: 2026-11-24
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-supplied legacy code, archived publication observations, unchanged multipolePDM0.1.0 core and local controlled studies"
raw_file: "raw/code/PDM/analysis/research/manifest.json"
raw_sha256: "33bf30cacda00eba542beaeeea01974b425dcc5a6bd71fac4fa6de9a28428ce8"
code_snapshot_file: "raw/code/PDM/archives/20261124-code-inputs/manifest.json"
code_snapshot_sha256: "de12a545155276455334b05626cdab32a9dc7874c47cbab7ff7c052d9a284b7b"
raw_storage_status: archived-local
archive_required: true
citation_key: MultipolePDM2026ErrorGridStudy
tags: [pdm, uncertainty, pdco, numerical-convergence, detector-geometry]
---

# PDM不对称误差、加权几何和网格研究

## Bibliographic Record

2026-11-24整理软件基线时，将18项代码与说明文档依赖改绑到固定快照，保留原条目的大小与SHA-256。旧`pdm/statistics.py`从0.1.0源码包恢复，逐字节匹配原记录；当前0.1.1工作源码不回退。原清单完整字节及恢复来源保存在`code_snapshot_file`集合，计算输入、输出和科学结论未改。

这是用户明确要求的本地计算研究，不是新实验或新发表论文。原件与输入清单见raw_file；代码、配置、数组、CSV/JSON与原文哈希一并保存。秘书手册中的“不对称误差的处理方案”及网格章节是这组数据的可读报告，不能反向代替原始数组。

## Scope and Reading Depth

三个互不覆盖写域的研究：asymmetric_errors、grid_resolution、geometry。已发布GUI核心未改，也没有发布新PyPI版本。135Pr观测量回原文TableI核对；用户135Pr脚本按实际2:1权重和P75.5deg读取。实验误差条的生成语义没有从三个数字中推定。

## Summary

偏态正态可因初值和接受规则而未充分拟合，但其分位不对称程度也有族限制。光滑或三点匹配好不意味着更真实。加权组强度不能由平均角替代。不选phi需平均强度而非设phi=0。当前样本的稳妥网格候选为0.1deg和sigma/I步长0.005；这是有限样本数值收敛建议，不保证大误差下真值一定在68%HDI内。

## Key Results

| ID | claim_kind | evidence_level | locator | 结论与边界 |
| --- | --- | --- | --- | --- |
| EGG-1 | code-reproduction | direct-computation | geometry/results.json; 用户p_ado_135Pr/physics/pado.py fast_pr及config.py | [2W157.6+W133.6]/[3W75.5]、P75.5；54点对旧系数与新振幅的R/P最大差5.78e-15/2.66e-15；代表角近似最大相对差19.24%，仅限所测点 |
| EGG-2 | model-comparison | quadrature-and-fits | asymmetric_errors/results.json, pdf_metrics.csv | 13组、六种初始实现独立积分偏差最大1.36e-12；现行模型每侧半概率但密度跳跃，连续split中心为mode、左质量eL/(eL+eR)，不是同一语义 |
| EGG-3 | numerical-fitting | controlled-multistart | asymmetric_errors/acceptance_aware_results.json, acceptance_aware_fits.csv | 宽窄比1.5的单初值候选最大分位残差13.33%，有符号多初值降至5e-8以下；747.3keV接受约束拟合最大残差1.557%，是近似，不是精确重建 |
| EGG-4 | model-property | analytic-limit-and-numerical-scan | asymmetric_errors/results.json skew_normal_feasibility_scan及README推导 | 精确16/50/84分位的skew-normal宽窄比极限约1.545890；747.3的1.625、813.2的2.4无法在该族精确匹配。大形状或不同起点不消除族限制 |
| EGG-5 | inference-sensitivity | fixed-response-comparison | asymmetric_errors/inference_summary.csv及acceptance_aware_inference_summary.csv | 固定旧747.3点角响应、只换P密度，角HDI分段mode最大差4.87deg；不是新加权135Pr反演，也不据接近原文delta择模型 |
| EGG-6 | numerical-convergence | frozen-design-grid-study | grid_resolution/results.json, grid_tradeoff.csv | 9种网格×9工况=81映射；0.1deg/.01通过6/9，0.1deg/.005通过9/9，参考.05deg/.001；前者部分段mode和低sigma端点超限 |
| EGG-7 | heldout-validation | fixed-input-holdout | grid_resolution/heldout.json及heldout_inputs.json | delta=-.5,+5三模式的6留出工况全通过，角HDI端点差<=.00147deg，宽度比端点差<=.000421，均触发P绝对误差下限0.1075 |
| EGG-8 | numerical-diagnostic | threshold-sweep | grid_resolution/threshold_audit.json | J警告阈值1e-14/1e-12/1e-10不改PDF或J；32/64/128epsilon只改变近精度玩具例分类。响应越界的1e-12容差未独立扫描 |

主研究的P误差取max(0.1075,0.8abs(P0))，R为10%相对误差。0.1075来自10条已核主层谱线的左右P误差平均值的跨线中位数，是声明的研究工作点，不是所有实验的固定精度。初始9例中floor未激活，6个留出例全部激活。P_ADO/P_DCO在delta=+5时P约-.000531，floor避免了纯80%规则产生约.000425的过小误差。P90deg、DCO125/90deg及无phi筛选模型在见结果前固定。

主研究9个工况的3个delta=-10例，在所有分辨率下都有两端边界警告，68%角HDI不含真值。这不是通过数值阈值调整可消除的“测试失败”，也不能因为离散收敛通过就说大混合真值恢复成功。留出6例的角与sigma/I的68%HDI均含真值，只属于这6例。

## Competing Interpretations and Limitations

- 当前左右尺度正态输入中心作为median，旧连续split把中心作为mode。相同中心和左右误差不是唯一PDF；实验误差原始似然或语义可决定适用模型。
- 光滑指数正态变换能匹配三个分位，但引入单侧边界和长尾；747.3例P上界.248是模型结果，不是独立实测约束。宽窄比5时[-1,1]外质量8.73%与当前模型2.28%不同。
- 接受约束多起点的形状范围[-14.5,14.5]是研究设置；既有接受限15和量化残差20%不是由本轮证明的最优阈值。13例11个近似接受不等于真实概率已校准。新解可贴在±14.5搜索边界，而原接受例程的边界诊断仍按±50，因此不能把原诊断非贴边标记解释成没有新搜索界依赖。
- 几何组原型只对有效权重合成响应，不计算实验效率或重新处理计数。全phi平均不是4pi；154Tb、190Tl按用户说明采用环模型，仍不声称知道逐对阵列接受度。
- 网格推荐仅针对所列输入、误差和范围；mode可能在边界，少量HDI支路对sigma步长敏感。0.01角区间通常很接近，选.005是为同时稳定段mode和取向分支。
- 计时受负载影响：最快通过候选本次约.553s/例、153MiB，参考约1.050s/例、495MiB；不含绘图、导出或进程启动，不能当所有平台性能。
- 这些研究不等于多组GUI、步长控件或最终误差模型已经接入。新实现仍须完整回归和独立发布。

## Extracted Pages

- [[pdm-three-mode-execution-contract-20261120]]：现行用户合同和执行边界。
- [[multipolepdm-20261120-synthetic-validation]]：旧误差/旧几何的合成验证，不能替代本次。
- [[multipolepdm-20261120-empirical-validation]]：六核来源与旧声明几何边界。
- [[lv-2022-evidence-against-wobbling-135pr]]：三个不对称P原件依赖；不是新独立实验。
