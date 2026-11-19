---
type: source
title: "Ljungvall 2020 - Nuclear shapes, collectivity and gamma-ray spectroscopy HDR"
aliases: ["Joa Ljungvall HDR", "tel-03862484", "Nuclear shapes and collectivity investigated using lifetime measurements and gamma-ray spectroscopy"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: habilitation
reading_depth: read
title_original: "Nuclear shapes and collectivity investigated using lifetime measurements and gamma-ray spectroscopy"
authors: ["Joa Ljungvall"]
year: 2020
institution: "Universite Paris-Saclay"
canonical_source: "HAL tel-03862484v1, HDR dated February 28, 2020 and deposited November 21, 2022"
url: "https://hal.science/tel-03862484v1"
raw_file: "raw/theses/gpt/query/20261119-international-nuclear-structure/HDR.pdf"
raw_sha256: "82cb9e44f52530a02e9200ce9828618ce385592261d8d403e0ab3fb0be91d587"
raw_storage_status: archived-local
archive_required: true
tags: ["shape-coexistence", "collectivity", "RDDS", "AGATA", "PSA", "HDR"]
---

# Ljungvall 2020：核形状、集体性与 γ 谱学

## Bibliographic Record

Joa Ljungvall，*Nuclear shapes and collectivity investigated using lifetime
measurements and γ-ray spectroscopy*，Université Paris-Saclay HDR。
PDF 2 的文档日期为 2020-02-28。PDF 1 的 HAL 封页记录 2022-11-21
存档，版本 `tel-03862484v1`。这两个日期分别标记文档和存档。
附印论文的 DOI 各自标识该论文。它们与 HDR 的 HAL 标识分开管理。

## Scope and Reading Depth

正文及书目 PDF 1–120 由 Gemini 分段处理，Codex 核对选定原页。首次
书目返回漏读 PDF 81–105，保存的提交文本含这些页，服务侧是否截断
未证实。两个小批仅补这 25 页。书目页的处理范围是条目与来源依赖，
外引文献全文另有各自的阅读记录。PDF 121–310 按附印论文、提案、
书目与实验结果分别处理。覆盖合计 310 页，重点原页由 Codex 核验，
未重做原论文的寿命拟合、代码模拟或完整数据分析。
外层印刷页从 PDF 3 起等于 PDF 页减 2，附印期刊页保留各自的编号。

## Summary

HDR 从能谱、电磁矩阵元和寿命推断核形状与集体性的条件出发，连接
HPGe 分段、脉冲形状分析（PSA）、γ 径迹追踪及 RDDS 的测量链。
以轻 Se 为例，更新寿命改变了库仑激发截面容许的四极矩范围。以富中子
Fe 为例，下行强度的增长支持集体性演化，轨道占据及 intruder 组态
仍来自模型。仪器性能取自文档所述配置与时点。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| LH-1 | 寿命与分支约束跃迁强度。重取向对角矩阵元及多条跃迁约束的四极不变量提供额外形状信息。 | methodology | direct-original-pages | PDF 10–13, Ch. 1 |
| LH-2 | RDDS 的距离零点、反冲速度分布、侧馈、峰形和门条件必须进入分析。灵敏区内用距离依赖检查未观测馈入。 | methodology | direct-original-pages | PDF 56–69, Ch. 6 |
| LH-3 | 70Se \(2_1^+\) 新寿命 3.2(2) ps，\(B(E2;2_1^+\to0_1^+)=342(19)\ e^2\mathrm{fm}^4\)。与旧库仑激发截面合用时偏好正 \(Q_s\)，其数值仍欠精确约束。 | measurement-and-inference | direct-original-pages | PDF 124–125, Table I, Fig. 2 |
| LH-4 | 2010 年 62、64Fe \(2_1^+\to0_1^+\) 下行强度为 \(214(26)\) 和 \(470^{+210}_{-110}\ e^2\mathrm{fm}^4\)。衰变曲线与等馈入时间假设相容。 | analysis-with-assumption | direct-original-pages | PDF 130, Fig. 3 and discussion |
| LH-5 | OUPS 的 76Kr 调试给 \(4_1^+\) 寿命 4.3(6) ps，箔片张紧、距离标定及可用探测器数限制了有效数据。 | instrument-commissioning | direct-original-pages | PDF 136–137, Tables 1–2, Fig. 10 |
| LH-6 | 170Os 的下行强度比 \(B_{4/2}=0.38(11)\)。文中 SCCM 给出 \(4_1^+\to2_1^+\) 强度 0.81 \(e^2\mathrm b^2\)，实验为 \(0.21^{+0.07}_{-0.04}\ e^2\mathrm b^2\)。 | measurement-and-model-comparison | direct-original-pages | PDF 199–201, Table I |
| LH-7 | GANIL 附印版的峰总比和效率同时受单点事件选择影响。98Zr 的位置宽度估计与模拟及速度输入相关。 | instrument-response | direct-original-pages | PDF 211, 213–214 |
| LH-8 | E614 模拟与实测的信噪条件不同。记录中未从 255 keV 线取得计划的 136Sm 结构约束。 | unsuccessful-measurement | direct-original-pages | PDF 295–298 |

## Verified Evidence Chains

### 轻 Se 的形状约束

DOI `10.1103/PhysRevLett.100.102502`，PRL 100, 102502 (2008)，
期刊版附印在 PDF 123–126，PDF 122 为 HDR 节题。作者在直接馈入线的
在飞分量上设门，从随距离改变的两类峰强度用 DDCM 提取寿命。阻停膜中
减速期间的发射用模拟线形处理，文中给出平均阻停时间 1.45(18) ps。
这些条件随实验几何而变，尤其应检查门纯度和未分辨分量。

Table I 给 70Se 的 \(2_1^+,4_1^+,6_1^+\) 寿命依次为
3.2(2)、1.4(1)、1.9(3) ps，72Se 为 4.2(3)、3.3(2)、1.7(1) ps。
对应下行强度分别为 342(19)、370(24)、530(96) 和
405(25)、882(50)、1220(76)，单位 \(e^2\mathrm{fm}^4\)。
70Se \(2_1^+\) 旧寿命 1.5(3) ps。以新强度带与先前库仑激发的重取向约束
相交，Fig. 2 偏好正 \(Q_s\)。Table I 的光谱四极矩列是计算值。
Gogny D1S HFB 加 GCM 的强度整体偏大，虽支持相近的定性趋势，
仍需截面精度更高或额外对角、非对角矩阵元来判别形状混合。
[[mukherjee-2022-shape-coexistence-octupole-72se]] 是另一篇谱学研究。

### 富中子 Fe 的寿命与集体性

DOI `10.1103/PhysRevC.81.061301`，PRC 81, 061301(R) (2010)，
期刊版附印 PDF 128–131。EXOGAM 与 VAMOS 的距离扫描使用按核素
实测的平均速度转换飞行时间。60Fe 的 \(2_1^+\) 寿命 11.4(12) ps
与文献 11.6(22) ps 对照。62、64Fe 的 \(2_1^+\) 寿命分别为 7.4(9)
和 7.4(26) ps。相近的寿命可导出不同下行强度，需要同时考虑
跃迁能及辐射速率关系。作者用不同距离上是否有系统漂移检查等馈入
时间假设。壳模型的 \(g_{9/2},d_{5/2}\) 占据是计算解释，
寿命测量直接约束其对集体强度的预测。

### OUPS 的距离零点

DOI `10.1016/j.nima.2012.03.041`，NIM A 679, 61–66 (2012)，
期刊版附印 PDF 133–138。电容反馈维持相对间距，电接触和光学接触
的差异影响零点。Table 1 的六个有效距离为 11.24(8) 至 44.59(4) μm。
位移台的 40 nm 定位精度不能替代在束绝对距离的不确定度。
76Kr 三环拟合分别给 4.1(15)、4.9(11)、3.6(8) ps。同时拟合为
4.3(6) ps。该结果验证了所试配置的在束反馈和寿命测量能力。

### 附印作品与实验依赖

表中页码指 HDR 容器。题页中的文献身份与内容页分别核对，附印作品
沿用自身书目信息。同一篇的期刊版、预印本和此处附印均指向同一实验谱系。

| HDR PDF | 附印作品及身份 | 可复用结论与边界 |
| --- | --- | --- |
| 122–126 | 轻 Se，PRL 100, 102502 (2008) | 寿命与库仑重取向截面的联合约束见本页。两类输入分别来源于寿命实验与先前库仑激发。 |
| 127–131 | 富中子 Fe，PRC 81, 061301(R) (2010) | \(2_1^+\) 下行强度，采用 EXOGAM/VAMOS 的速度和距离条件。 |
| 132–138 | OUPS，NIM A 679, 61–66 (2012) | 76Kr 调试与距离零点，不外推到所有后续箔片配置。 |
| 139–150 | 252No 高 \(K\)，PRC 86, 044318 (2012) | PDF 141–142 的反冲与衰变关联给异能态半衰期 109(3) ms。半衰期与 γ 支路共同服务于组态讨论。 |
| 151–163 | MUSETT，DOI `10.1016/j.nima.2014.02.016` | PDF 160–162 区分可关联的反冲衰变与焦平面连续本底。谱仪抑制和模拟本底预期均随运行条件引用。 |
| 164–169 | 24Mg \(g\) 因子，PRL 114, 062501 (2015) | PDF 167–168 报告 \(g=0.538\pm0.011_{\mathrm{stat}}\pm0.007_{\mathrm{syst}}\)。寿命、几何和超精细场进入误差链。 |
| 170–181 | Fe、Co、Mn 寿命，PRC 95, 024312 (2017) | GANIL 的 OUPS/VAMOS++/AGATA 测量包含 Fe 的 \(4_1^+\) 态，区别于 2010 年 Fe \(2_1^+\) 数据。64Fe \(4_1^+\) 在文中侧馈处理下给 \(\tau<1.8\) ps 与下行 \(B(E2)>420\ e^2\mathrm{fm}^4\)，保留限值。见 PDF 173–178。 |
| 182–194 | 分段 HPGe 实验参考脉冲，DOI `10.1140/epja/i2018-12636-9` | PDF 191–193 描述以实验参考脉冲做定位的直接法。单分段事件在高能下仍可能有多次相互作用，适用性随事件类别改变。 |
| 195–203 | 170Os，PRC 100, 034302 (2019) | PDF 199–201 的低 \(B_{4/2}\) 与本文 SCCM 计算不符。模型势能面及推转检查给出各自的限制，异常原因仍开放。 |
| 204–217 | AGATA at GANIL，NIM A 955, 163297 (2020) | PDF 205–217 的期刊版与 [[ljungvall-2020-agata-ganil-performance]] 的 33 页预印本同一作品，见版本核查。 |
| 218–231 | AGATAGeFEM 脉冲计算，HDR 所附稿 | PDF 219 起为带 EPJ 模板的稿件。载流子运动、晶体方向和权重场的变化影响基组，参数灵敏度依赖定义。保留稿本身份。 |
| 232–239 | Extended Geant4 simulations，HDR 所附稿 | PDF 233 起讨论探测器及带时间结构的事件模拟。设定的束流和选择门用于评估模拟性能，不能引用成实际测得结构量。 |

### AGATA 期刊版与预印本

出版页 PDF 205 标明 NIM A 955 (2020) 163297 及相同 DOI
`10.1016/j.nima.2019.163297`。PDF 211 的 \(^{60}\)Co 条件下峰总比从
36.4(4)% 到剔除单点事件后的 52.4(6)%，伴随 17% 全能峰效率损失。
PDF 213 的 5.1 mm 是六探测器加权的有效位置 FWHM。PDF 214
的未关联事件比较支持先合并相互作用点再做 tracking 的归一化方法。
这些结果与已有预印本笔记的相应记录一致。旧 `raw_file` 现已核实
有 33 页实际字节，哈希与旧记录相符。两版分别保留页定位，未查尽
全部版本差别。期刊版本身也保留正文与结论的差异：PDF 208 写中心
触点校正前平均 FWHM 为 2.93 keV，PDF 215 写 3.08 keV，两处
校正后均为 2.57 keV。引用时应给明所据段落。

### 计划与失败诊断

- PDF 240–256 的 OASIS 为提案。PDF 257–268 的出版清单用于辨认作品，
  作者列出的条目各自需要全文检查。
- PDF 269–276 为 136Sm 的库仑激发提案，PDF 277–289 为测试，
  PDF 290–298 才是 E614 及事后诊断。模拟在假定参数和 8 ns 符合窗
  下支持可见性，原文同时指出实测装置对 255 keV 的时序性能可能较差。
  次级束组成和本底也是诊断变量，现有证据未唯一确定损失原因。
- PDF 299–307 的不完全熔合 RDDS 设计与 PDF 308–310 的运行记录
  配套。靶材、粒子鉴别和可用距离点制约寿命提取。作者提出测量出射粒子
  的运动学并区分质子与 α，作为后续改进，原件未给出验证后的寿命。

## Competing Interpretations and Limitations

- 形状推断依赖实验约束的组合。同一旋转模型导出的多个计算值不构成
  独立的形状证据。单个 \(B(E2)\) 给矩阵元平方，符号须由其它观测约束。
- 直接馈入在飞门的优势依赖可辨认的级联分量、几何和统计。只有单谱、
  未观测长寿命馈入和有限的减速膜渡越时间时，原文讨论的寿命偏差仍可能存在。
  本批未重跑谱拟合或作者计算。
- AGATA 的模拟与实测差异依赖阈值、材料、PSA 基组、追踪选择和事件类别。
  文献中给出的峰总比或分辨率须随配置引用。HDR 叙事、附印论文以及同一
  作品的预印本分别保留版本和实验依赖。

## Extracted Pages

- PDF 1–2：HAL 标识、文档日期、作者、机构。
- PDF 10–13、52–55、56–69：形状可观测量、性能快照及寿命分析条件。
- PDF 123–126：轻 Se 期刊版，直接门、寿命表及对角矩阵元约束。
- PDF 128–131：富中子 Fe 的 \(2_1^+\) 寿命及壳模型解释。
- PDF 133–138：OUPS 设计和在束调试，位移重复性、零点与寿命比较。
- PDF 139–239：九篇期刊附印及稿本的位置、独立身份和物理范围见上表。
- PDF 240–310：资助申请、著作目录、136Sm 及不完全熔合的提案和运行结果。
