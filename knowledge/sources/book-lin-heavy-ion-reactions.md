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
| LIN-5 | 复合核初态自旋分布与出射道设计：分波截面 $\sigma_\ell = \frac{\pi}{k^2}(2\ell+1)T_\ell$ 构成三角形自旋分布；结合转动液滴模型（RLDM）裂变极限 $\ell_{\text{fiss}} \approx 70\ \hbar$ 与中子蒸发结合能-动能损失（每中子 $\sim 10.5\text{ MeV}$），给出 $A \sim 130$ 区手征与三轴态在束高自旋实验的推荐入射能量 $E_{\text{lab}}^{\text{opt}}(xn)$。 | model-result | direct | 第 6 章 §6.1, 印刷 pp. 136–138 / PDF pp. 146–148 | false |
| LIN-6 | 深部非弹性散射（DIC）动力学、能量耗散（TKEL）与 Wilczynski 能量-角度关联：在 $\ell_{\text{crit}} < \ell \le \ell_{\text{grazing}}$ 碰撞窗口内，双核摩擦力使质心动能完全松弛降至库仑接触势，粘滞极限（Sticking limit）将相对轨道角动量的 $28\% \sim 48\%$ 转移为碎片内禀自旋（可高达 $60\ \hbar$）；双核绕旋转轴盘旋越过 $0^\circ$ 形成负角偏转分支，在 $(\theta_{\text{obs}}, \text{TKEL})$ 平面构成鸟嘴形 Wilczynski 动力学特征脊线。 | model-result | direct | 第 5 章 §5.1–5.4, 印刷 pp. 110–133 / PDF pp. 120–143 | false |
| LIN-7 | 重离子核彩虹散射（Nuclear Rainbow Scattering）与 Airy 结构：在中高能弹性散射（$E_{\text{lab}} \ge 10-25\text{ MeV/u}$）中，强吸引核势使半经典偏转函数 $\Theta(l)$ 产生极小值（$d\Theta/dl = 0 \implies \Theta_R < 0$），将经典焦散奇异性转化为量子 Airy 衍射振荡；彩虹角 $\theta_R$ 与 Airy 极小位置直接反演核内部实光学势深度 $V_0$，彻底消除低能区 $V_0 R^2 \approx \text{const}$ 的离散势多重解歧义。 | model-result | direct | 第 3–4 章, 印刷 pp. 80–110 / PDF pp. 90–120 | false |

## Competing Interpretations and Limitations

- **单势垒穿透与耦合道效应差异**：简单的 Wong 单势垒公式忽略了弹核与靶核的内禀自由度耦合（转动带激发、低频四极/八极振动及核子转移道）。在近垒区，实验测量的势垒分布呈现复杂的精细峰结构，必须采用耦合道计算程序（如 CCFULL）进行多道耦合求和。
- **出射道物理截面预测边界**：宏观重离子势模型仅能给出熔合总截面 $\sigma_{\text{fus}}$；蒸发余核各 $xn, pxn, \alpha xn$ 出射道的具体截面与角动量布居，必须依赖统计蒸发去激程序（如 Hauser-Feshbach 或 PACE4），结合精确的实验测量分离能与电荷质量表，不能由示意高斯分布替代。

## Extracted Pages

- 印刷 pp. 18–36（PDF pp. 28–46）：重离子核势、接近势与唯象势参数化。
- 印刷 pp. 134–143（PDF pp. 144–153）：临界角动量、Wong 穿透公式与近垒耦合道效应。
- 印刷 pp. 177–179（PDF pp. 187–189）：熔合裂变势能演化与准裂变图像。
