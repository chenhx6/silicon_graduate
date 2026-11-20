---
type: source
title: "multipolePDM 六核文献观测量与声明模型比较"
aliases: [PDM六核案例验证]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
title_original: "multipolePDM six-nuclide declared-model literature comparison"
year: 2026
canonical_source: "Original published observations and local declared-model calculations"
raw_file: "raw/code/PDM/analysis/cases/empirical_manifest.json"
raw_sha256: "972904432be493c920a86a11619c443511282d4466de34eb2198ef730cc2c7e9"
raw_storage_status: archived-local
archive_required: true
tags: [pdm, pdco, polarization, dco, validation]
---

# 六核文献观测量与声明模型比较

## Bibliographic Record

这是本任务生成的可复跑计算证据，不是新增实验。原件与逐文件哈希见上述清单。原文观测值、自旋/几何解释、计算结果分开保存。外部原件的专题目录为 `raw/papers/gpt/query/20261120-pdm-response-validation/`；部分相同哈希原件复用已有馆藏，不重复下载。软件公开不包含出版社PDF或原始私人工作簿。

## Scope and Reading Depth

已核对原文相关方法、图、表和误差；并非这些论文全部物理结论的审核。公开数据在 `raw/code/PDM/analysis/cases/results/` 及 `followup/results/`。核素与能量标识不依赖Excel行号。原工作簿SHA256仍为 `4f6b2877ca0eeb39506e9d32457ca9c8b829afd657d3ef9de0151b41e593d125`。

## Summary

三模式共用一个参考初态与PDM核心；文献覆盖达到六核三种奇偶类别，但PDCO只有一个核，所有比较保留几何、测量定义和响应域边界。

## Key Results

| locator | 原文直接证据 | 本任务采用与边界 | claim_kind | evidence_level |
| --- | --- | --- | --- | --- |
| Biswas2026, DOI10.1016/j.physletb.2026.140929, Table1及补充SecII Eqs1-3 | 80Se最终P、ADO、DCO；原混合比用P+DCO、sigma/j=.35 | 6条P_ADO用另一观测比、扫描宽度；783.5中位-1.579接近文献-1.57，1455.3不重叠不能直接否定原DCO提取 | reported; model-comparison | original-full-text; local-computation |
| Lv2022, DOI10.1016/j.physletb.2021.136840, Table1及补充 | 135Pr P与环组角分布比、747.3非对称P误差 | 3条点角代表模型；不冒充环组完整加权 | reported; model-comparison | original-full-text; local-computation |
| Pal2026, DOI10.1016/j.physletb.2026.140454, Figs1/3/4, Table1 | 185Au518.1 delta=-3.4(6)，292.3才是-.03(3)；518和门323+409+548；554.9门264E1在上游 | 518和门在纯伸展E2且公共方向权重下由548门代表；554.9参考自旋17/2。各6种几何解释全部保留；与文献吻合不用于选择未知顺序 | reported; model-comparison | original-full-text; local-computation |
| 154Tb, DOI10.1016/j.nuclphysa.2025.123019, Eq1, Figs1-2, Table1 | 244.6和229.7的P/DCO、125/90顺序及符合阶梯 | 各3个方位场景；实际各表项方向门未逐条命名，采用有依据的下游E2代理而非声称精确重放 | reported; model-comparison | original-full-text; local-computation |
| Starosta1999, DOI10.1016/S0168-9002(98)01220-0, Secs4/6/7, Tables2-4 | 164Yb490 P_C=.50(8), P_D=.54(8), R=.96(2)，C/D方向门；14->14混合与16->14纯E2两假设 | 完整方位强度平均的理想环，不是4pi；两DCO顺序均保留。极角端目标分子C组混合delta中位-.3405；647E1控制支持该顺序但不构成原文明确分子标签 | reported; model-comparison | original-full-text; local-computation |
| Pal2025, DOI10.1140/epja/s10050-025-01678-3, Table1, Fig7(b), Fig8 | 190Tl272.1最终P图点及误差帽、R=.59(3)、上游662.4E2、目标157/门90作分子 | P图读-.35056 +.04045/-.03933，两像素约.0045，中心偏移敏感性独立记录；首场景delta中位.0710。单线P代理和未知相对方位是模型假设；Q低能外推局限不自行重校 | reported; model-comparison | original-full-text; local-computation |
| Hamilton Ch12 pp552-553, Eqs12.218-219 | 同阶纯伸展链满足U_k A_next=A_previous | 延伸到完整后选矩阵的等价门效应需旋转协变与相同几何权重，不是把U_k=1 | reported; model-comparison | original-full-text; local-computation |

## Coverage

六核为偶偶80Se/164Yb、奇A135Pr/185Au、奇奇154Tb/190Tl。P_ADO实测比较2核，P_DCO3核，PDCO仅1核。初始批次15个场景加11敏感性运行；补充32条记录中21条混合反演、11条纯前向，并有5条代表混合的网格加密。合计15条不同混合候选谱线；164Yb490的自旋替代假设不能计为两条线，几何或读图替代也不是独立实验。另有164Yb647和190Tl943.3纯线；所有数字以JSON为准。74Br排除；SHU74别名未确定。

## Competing Interpretations and Limitations

- 全部为点响应或声明的理想环模型，没有一次实验阵列的完整效率/接受度重放。未补造未知几何、实验误差或门线。
- 原文delta仅作事后参考，正负混合、低/中/高E2成分的选择不构成真值；有共同输入的文献提取不是独立实验核验。
- 164Yb490纯E2理想R=1与.96(2)相差2误差；647E1在反向DCO顺序严重不相容。190Tl943.3纯E1需2.17-2.35倍联合误差盒接触观测。全部保留，不为让测试通过而改观测。
- 某些185Au场景不在响应域附近，即使归一化PDF存在也不能把窄区间当好拟合。积分范围、单线P代理、相位未明确命名和几何解释均可能影响比较，不预先归咎实验或理论。
- 初始及补充代表网格加密通过不意味着积分域边界充分；完整区间与边缘警告保留。没有加入chi-square模块。

## Extracted Pages

- [[pdm-three-mode-execution-contract-20261120]]：共同参考态、模式及发布范围。
- [[multipolepdm-20261120-synthetic-validation]]：独立9j/振幅比较、内部自洽及重复观测；不与实测混计。
- [[starosta-1999-pdco-experimental-test]]、[[droste-1996-pdco-formalism]]、[[book-hamilton-electromagnetic-interaction]]：原始理论来源。
- 秘书手册 `raw/writing/pado/20261029_review_v1/PDM/main.tex` 给公式、实现、图文结果和未解决问题。
