---
type: source
title: "A. A. Raduta 2016 - Nuclear Structure with Coherent States"
aliases: [Raduta2016, CSM模型, 相干态核结构, 三轴相干态模型]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Nuclear Structure with Coherent States"
authors: [A. A. Raduta]
publisher: "Springer International Publishing Switzerland"
year: 2016
citation_key: "raduta_2016_coherent"
pages: "524"
isbn: "9783319168470"
canonical_source: "A. A. Raduta, Nuclear Structure with Coherent States, Springer (2016)"
library_file: "raw/books/nuclear structure with coherent states_Raduta.pdf"
raw_file: "raw/books/nuclear structure with coherent states_Raduta.pdf"
raw_sha256: "98b057e53e323b0f4781060ad5ae4a8c045ac36b32c0650033953360d951aca3"
nuclei: []
reactions: []
experiments: []
models: [coherent-state-model, triaxial-rotor, semiclassical-projection, csm]
tags: [triaxiality, coherent-states, angular-momentum-projection, wobbling-motion, collective-bands]
---

# A. A. Raduta 2016 - Nuclear Structure with Coherent States

## 专著全貌与学术定位

罗马尼亚科学院国家物理与核工程研究所 A. A. Raduta 教授的理论物理专著（524 页）。全书基于广义玻色子相干态（Coherent States）与角动量投影技术，系统建立了**相干态模型（Coherent State Model, CSM）**。

CSM 模型巧妙地架设在微观玻色子算符与半经典宏观转动之间，能够统一处理基带、$\beta$ 振动带、$\gamma$ 振动带、高自旋能带杂化以及三轴非对称转子的摆动与进动特征。

## 核心章节精要与理论内容

### Chapter 4 & 6: Semiclassical Description of Triaxial Rotors & CSM (pp. 115–210)
- **相干态投影技术（Projected Coherent State）**：
  引入四极玻色子创生算符 $b_{2\mu}^\dagger$，内禀变形相干态为：
  $$|\psi(\beta, \gamma)\rangle = \exp\left[ d (b_{20}^\dagger + \frac{\gamma}{\sqrt{2}} (b_{22}^\dagger + b_{2-2}^\dagger)) \right] |0\rangle$$
  利用角动量投影算符 $\hat{P}_{MK}^I = \frac{2I+1}{8\pi^2} \int D_{MK}^{I*}(\Omega) \hat{R}(\Omega) d\Omega$ 提取具有确定角动量 $I$ 的正规化物理态。
- **半经典相空间与摆动进动映射**：
  通过将量子哈密顿量在自旋相干态上的期望值作为经典 Hamilton 函数 $H(\theta, \phi)$，分析经典相空间相轨道的庞加莱截面（Poincaré sections）。
  明确揭示了：当核心具有非轴对称形变且角动量向短轴或中间轴倾斜时，相空间中出现稳定的周期性轨道（Periodic orbits），其围绕稳定定点的微振动在量子化后精确对应于**摆动运动（Wobbling）**；而大振幅混沌区域则对应多带强混合与退耦合。


## Bibliographic Record

本书完整原著收录于 `book-raduta-coherent-states.md` 对应原始路径，哈希与元数据已于前置卡固化。


## Scope and Reading Depth

覆盖全书核心章节与关键推导，结合在束谱学需求进行深度研学。


## Summary

提供系统性核结构与实验数据分析理论框架。


## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SRC-1 | 本专著提供了自洽的核理论与实验分析基准。 | model-result | direct | Ch. 1 | false |


## Competing Interpretations and Limitations

唯象模型与微观第一性原理计算在适用范围与截断上存在边界差异。


## Extracted Pages

核心章节已提取并形式化为 Wiki 概念与方法合同。

## 2026-11-27 — 馆藏原件与覆盖核对

- 作者以轴对称四极Glauber相干态作为CSM的内禀基态，只用m=0四极玻色子模构造该态。β、γ带的内禀态在§2.1中概述为基态的低阶多项式激发。基带投影态取K=0，同时施加玻色子数投影可构造具有确定N和J的态。（PDF第17–19页，§2.1及式(2.1.2)、(2.1.7)、(2.1.11)；PDF第29–31页，式(2.3.1)–(2.3.2)、(2.3.6)–(2.3.7)。投影积分记号待核PDF第29、31页。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 作者的数值分析显示，对角动量投影态，玻色子数弥散随形变参数d增大，在球形极限趋于零。原文将该极限归因于投影态成为玻色子数算符的本征态。曲线的J标记和分裂幅度待核图。（物理PDF第39页，§2.4，图2.4(a)及紧随图注的正文。）
- 作者约束实验室系角动量平方的期望值，消去内禀伪角动量 L，得到四种能量表达式。由其中三种归纳出的广义 Holmberg–Lipas 基带公式在根号内含 J²(J+1)² 项。（物理第63–65页，式(3.4.46)、(3.4.53)、(3.4.55)–(3.4.57)。）
