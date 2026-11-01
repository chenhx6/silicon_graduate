---
type: source
title: "林承键 2017 - 重离子核反应"
aliases: [林承键重离子核反应, Lin 2017 Heavy Ion Reactions, 重离子核反应专著]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "重离子核反应"
authors: [林承键]
publisher: "科学出版社"
year: 2017
pages: "223"
isbn: "9787030537232"
canonical_source: "林承键, 《重离子核反应》, 科学出版社 (2017)"
raw_storage_status: archived-local
archive_required: true
library_file: "raw/books/重离子核反应 (林承键) (Z-Library).pdf"
raw_file: "raw/books/重离子核反应 (林承键) (Z-Library).pdf"
raw_sha256: "792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e"
nuclei: []
reactions: [heavy-ion-fusion, elastic-scattering, deep-inelastic, transfer-reactions, fusion-evaporation]
experiments: []
models: [optical-model, proximity-potential, bass-model, compound-nucleus-decay]
tags: [books, heavy-ion-reactions, fusion-cross-section, critical-angular-momentum, reaction-kinematics]
---

# 林承键 2017 - 重离子核反应

## Bibliographic Record

- **书名**：重离子核反应
- **著**：林承键（中国原子能科学研究院）
- **出版信息**：科学出版社（北京东黄城根北街 16 号），2017 年 8 月第 1 版，第 1 次印刷。
- **书号与定版**：ISBN 978-7-03-053723-2，中国版本图书馆 CIP 数据核字 (2017) 第 162973 号。
- **全书规模**：223 物理 PDF 页；正文印刷页 1–212（目录页至正文印刷页第 1 页有约 10 页前置偏移）。
- **本地原件**：`raw/books/重离子核反应 (林承键) (Z-Library).pdf`
- **原件 SHA-256**：`792bfe7f7807623b7e1439b32eddb7320ab3ec6bf6be7e3894b436c1c9f65b2e`

## Scope and Reading Depth

本来源登记状态定为 `skimmed`，明确界定本轮核查范围为重离子相互作用势、熔合势垒模型与裂变竞争：
- **已核查章节**：
  - 目录（PDF pp. 9–10）；
  - 第 2 章 重离子相互作用势（印刷 pp. 18–36 / PDF pp. 28–46）：库仑势、核势参数化、接近势与有效相互作用势垒；
  - 第 6 章 熔合反应（印刷 pp. 134–143 / PDF pp. 144–153）：锐截止模型、临界角动量 $\ell_{\text{crit}}$、Hill-Wheeler 公式、Wong 单势垒穿透公式、近垒异常增强与形变耦合道效应；
  - 第 7 章 裂变反应（印刷 pp. 177–179 / PDF pp. 187–189）：熔合-裂变动力学途径、快裂变与准裂变物理图像。
- **未核查内容**：第 1 章概述、第 3 章弹性散射、第 4 章准弹性散射与第 5 章深部非弹性散射的全文微观推导。

## Summary

本书是中国原子能科学研究院林承键研究员编著的重离子反应专业专著，系统阐述了重离子碰撞中的相互作用势、散射动力学、多核子转移、深部非弹性碰撞、熔合与裂变机制。在实验核物理中，重离子熔合蒸发反应是产生中高质量区核素并布居高自旋态（如三轴形变手征带与摆动带）的核心工具。书中给出了势垒穿透、临界角动量截断与近垒耦合道效应的系统性理论描述。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LIN-1 | 经典锐截止模型（Sharp Cutoff Model）：熔合截面 $\sigma_{\text{fus}} = \frac{\pi}{k^2} \sum_{l=0}^{\ell_{\text{crit}}} (2l+1) = \frac{\pi R_B^2}{E_{\text{c.m.}}} (E_{\text{c.m.}} - V_B)$，在远高于势垒能区受临界角动量 $\ell_{\text{crit}}$ 限制转为线性下落。 | model-result | direct | 第 6 章 §6.1, 印刷 pp. 134–136 / PDF pp. 144–146, 式 (6.1)–(6.8) | false |
| LIN-2 | Wong 单抛物线势垒穿透公式：$\sigma_{\text{fus}} = \frac{\hbar\omega_B R_B^2}{2E_{\text{c.m.}}} \ln[1 + \exp(\frac{2\pi(E_{\text{c.m.}}-V_B)}{\hbar\omega_B})]$；当能量远高于势垒时渐近还原为经典公式，但在深垒下因偏离反转抛物线而产生局限性。 | model-result | direct | 第 6 章 §6.1, 印刷 pp. 137–138 / PDF pp. 147–148, 式 (6.13)–(6.15) | false |
| LIN-3 | 近垒与垒下熔合截面增强：静态四极/八极形变取向平均以及表面集体振动（低激发态声子）诱发多势垒分布，使近垒截面比单势垒穿透理论提高数个数量级。 | model-result | direct | 第 6 章 §6.2, 印刷 pp. 138–143 / PDF pp. 148–153, 式 (6.17)–(6.20) | false |
| LIN-4 | 熔合-裂变演化与准裂变（Quasi-fission）：在重体系中，接触双核系统因受到强库仑排斥力在越过鞍点前即可沿质量不对称自由度重新分离，构成重元素合成中完全熔合截面塌缩的主要机制。 | model-result | direct | 第 7 章 §7.1, 印刷 pp. 177–179 / PDF pp. 187–189, 图 7.1–7.2 | false |

## Competing Interpretations and Limitations

- **单势垒穿透与耦合道效应差异**：简单的 Wong 单势垒公式忽略了弹核与靶核的内禀自由度耦合（转动带激发、低频四极/八极振动及核子转移道）。在近垒区，实验测量的势垒分布呈现复杂的精细峰结构，必须采用耦合道计算程序（如 CCFULL）进行多道耦合求和。
- **出射道物理截面预测边界**：宏观重离子势模型仅能给出熔合总截面 $\sigma_{\text{fus}}$；蒸发余核各 $xn, pxn, \alpha xn$ 出射道的具体截面与角动量布居，必须依赖统计蒸发去激程序（如 Hauser-Feshbach 或 PACE4），结合精确的实验测量分离能与电荷质量表，不能由示意高斯分布替代。

## Extracted Pages

- 印刷 pp. 18–36（PDF pp. 28–46）：重离子核势、接近势与唯象势参数化。
- 印刷 pp. 134–143（PDF pp. 144–153）：临界角动量、Wong 穿透公式与近垒耦合道效应。
- 印刷 pp. 177–179（PDF pp. 187–189）：熔合裂变势能演化与准裂变图像。
