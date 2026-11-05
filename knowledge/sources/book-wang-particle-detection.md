---
type: source
title: "汪晓莲等 2009 - 粒子探测技术"
aliases: [汪晓莲粒子探测技术, Wang 2009 Particle Detection, 粒子探测技术]
created: 2026-11-02
updated: 2026-11-02
status: active
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "粒子探测技术"
authors: [汪晓莲, 李澄, 邵明, 陈宏芳]
publisher: "中国科学技术大学出版社"
year: 2009
citation_key: "wang_2009_particle-detectors-gaseous-detectors"
pages: "444"
isbn: "978-7-312-02299-9"
canonical_source: "汪晓莲, 李澄, 邵明, 陈宏芳 编, 《粒子探测技术》, 中国科学技术大学出版社 (2009)"
raw_file: "raw/books/粒子探测技术 (汪晓莲  李澄  绍明  陈宏芳) (Z-Library).pdf"
raw_sha256: "250b51039f35e6a22e1311d645637d741b0f859af9d328f62c450ae9422c3cb4"
archive_required: true
nuclei: []
reactions: []
experiments: []
models: [gas-discharge-deadtime, semiconductor-radiation-damage]
tags: [particle-detectors, gaseous-detectors, semiconductor-detectors, radiation-damage]
topics: [gaseous-detectors, gm-counter, semiconductor-detectors, radiation-damage]
---

# 汪晓莲等 2009 - 粒子探测技术

## Bibliographic Record

- 题名：粒子探测技术（中国科学技术大学精品教材、“十一五”国家重点图书）
- 编者：汪晓莲、李澄、邵明、陈宏芳（前言载：陈宏芳负责组织，邵明编写第 1～3 章，李澄编写第 4 章，汪晓莲编写第 5～8 章；CIP 将陈宏芳列为检索点）
- 出版社：中国科学技术大学出版社（合肥市金寨路 96 号）
- 版次：2009 年 6 月第 1 版，第 1 次印刷
- ISBN：978-7-312-02299-9
- 定价：45.00 元
- 本地原件路径：`raw/books/粒子探测技术 (汪晓莲  李澄  绍明  陈宏芳) (Z-Library).pdf`
- 本地原件 SHA-256：`250b51039f35e6a22e1311d645637d741b0f859af9d328f62c450ae9422c3cb4`
- 原件全长：444 页（PDF 文件 1-based 页数）

## Scope and Reading Depth

本来源登记状态为 `skimmed`，仅覆盖为死时间与电荷收集核查而定向阅读的选定页面，不宣称完成全书逐章 deep-read，也不从目录推断全书作者观点：

1. **封面与版权页**（PDF pp.1–4、8）：书名、作者分工、ISBN、版次与出版年份。
2. **第 4 章气体探测器选页**（PDF pp.140–145 = 印刷 pp.126–131，重点 PDF p.143 = 印刷 p.129、图 4.2.18）：G-M 计数管的死时间与复原时间概念，正离子鞘向阴极移动引起电场恢复的微观过程。
3. **第 5 章半导体探测器选页**（PDF p.236 = 印刷 p.222，§5.4.8）：半导体辐射损伤的一般机制、缺陷俘获中心对载流子寿命的影响。

未阅读内容包括第 1～3 章基础物理机制与统计误差、第 4 章其它气体室细节、第 5 章位置灵敏探测器及第 6～8 章闪烁、切伦科夫与系统回路，后续使用时须另行查验正文。

## Summary

本书是中国科学技术大学粒子与核物理课程教材，涵盖微观粒子与辐射和物质相互作用、气体探测器、半导体探测器、闪烁探测器、切伦科夫/穿越辐射以及探测系统的组成与输出回路。在涉及计数器时间特性的章节中，定性阐述了放电电荷运动对探测器死时间和复原时间的物理约束，以及半导体探测器受辐照后产生缺陷能级、缩短载流子寿命的一般物理图像。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WANG-1 | MWPC 与漂移室共形映射电位分布：阳极丝阵列电位严格表达为 $V(x, y) = V_0 - \frac{q}{4\pi\varepsilon_0}[\frac{2\pi L}{s} - \ln(4(\sin^2\frac{\pi x}{s} + \sinh^2\frac{\pi y}{s}))]$，揭示近丝强场区（$r \ll s$）反比发散与远丝漂移区（$y \ge s/2$）均匀电场的双重拓扑架构。 | model-result | direct | 第 3 章 §3.3, 印刷 pp. 75–88 / PDF pp. 89–102 | false |
| WANG-2 | 第一 Townsend 电离系数与气体雪崩放大：$\alpha(E) = A P \exp(-B P / E)$，沿径向场强积分确定正比工作区雪崩倍增倍数 $M \approx \exp[\int_{r_0}^{r_c} \alpha dr] \sim 10^4 - 10^6$，给出阳极丝表面场强 $E(r_0) \sim 10^5\text{ V/cm}$ 下的工作高压选择准则。 | model-result | direct | 第 3 章 §3.1–3.3, 印刷 pp. 62–75 / PDF pp. 76–89 | false |
| WANG-3 | 漂移室饱和漂移速度与扩散空间分辨极限：在饱和场区电子漂移速度恒定为 $v_d \approx 50\ \mu\text{m/ns}$，推导由热扩散决定的横向/纵向位置分辨极限 $\sigma_x = \sqrt{2 D x / v_d} \propto \sqrt{x}$。 | model-result | direct | 第 3 章 §3.4, 印刷 pp. 88–95 / PDF pp. 102–109 | false |
| WANG-4 | G-M 计数管死时间与复原时间：放电后正离子鞘包围阳极丝使周围电场降低；只有当正离子鞘向阴极移动、阳极电场恢复到足以再次引起雪崩增殖的时间称为失效时间（死时间 $t_d$）。死时间之后至脉冲高度恢复到正常幅度的时间称为复原时间 $t_r$。 | model-result | direct | 第 4 章 §4.2, 印刷 p. 129 / PDF p. 143, 图 4.2.18 | false |
| WANG-5 | 半导体辐射损伤机制：快中子辐照在晶格中造成 Frenkel 缺陷并形成深能级俘获中心，增加漏电流并导致严重的空穴载流子俘获，恶化探测器能量分辨率。 | model-result | direct | 第 5 章 §5.4, 印刷 p. 222 / PDF p. 236, §5.4.8 | false |

## Competing Interpretations and Limitations

- **无作者专属死时间公式**：本书已读章节未提出任何独立于通用辐射测量物理的作者专有死时间公式，更未与吴治华教材展开学术争论；旧概念页所称“汪晓莲麻痹型微观物理 vs 吴治华非麻痹型”系由目录推断的虚构冲突，已被撤回。
- **不可外推到定量的抗中子性能比较**：§5.4.8 的辐射损伤是通用物理阐述，不包含 N 型同轴与 P 型同轴 HPGe 抗快中子损伤比值的定量测量数据。

## Extracted Pages

- PDF p.2 / 印刷封底：ISBN `978-7-312-02299-9`，定价 45.00 元。
- PDF p.4 / 印刷版权页：中国版本图书馆 CIP 数据核字 (2008) 第 168083 号，2009 年 6 月第 1 版。
- PDF p.8 / 印刷前言 p.2：陈宏芳负责组织，邵明编写第 1～3 章，李澄编写第 4 章，汪晓莲编写第 5～8 章。
- PDF p.143 / 印刷 p.129、图 4.2.18：G-M 计数器输出脉冲幅度随时间变化、失效时间与复原时间定义。
- PDF p.236 / 印刷 p.222、§5.4.8：半导体探测器辐照效应与载流子俘获。
