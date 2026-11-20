---
type: source
title: "Lettmann 2018 - Spectroscopy of neutron-rich germanium and krypton isotopes"
title_original: "Spectroscopy of neutron-rich germanium and krypton isotopes - A quest of triaxiality"
aliases: []
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Marc Lettmann"]
year: 2018
institution: Technische Universität Darmstadt
doi: 10.26083/tuprints-00007382
canonical_source: "Marc Lettmann, approved TU Darmstadt doctoral dissertation, 2018"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/Dissertation_Lettmann_27_4_2018.pdf
raw_sha256: 2c635ba63e1e71f5c81bac6bc952af5de6828c49973952ec347c1cb0d5aa5dad
raw_storage_status: archived-local
archive_required: true
nuclei: ["84Ge", "86Ge", "88Ge", "94Kr", "96Kr"]
tags: [triaxiality, gamma-band, knockout, inelastic-scattering, thesis]
---

# Lettmann 2018：富中子锗与氪的低位谱学

## Bibliographic Record

Marc Lettmann，Technische Universität Darmstadt 博士论文。PDF 1–2
记载 2018 年 2 月 1 日提交、4 月 16 日答辩。PDF 180 列同作者
Ge 实验论文 *Phys. Rev. C* **96**, 011301(R) (2017)，DOI `10.1103/PhysRevC.96.011301`。

## Scope and Reading Depth

原件 189 页。科研内容、附录及书证共核 188 页。PDF 187 为个人履历，
留在本地原件。图像补核正文、附录的无文字层页面。分隔页按版面核查。
正文印刷页为 PDF 页减 10。未收到 Gemini 主读回执，原论文的版本逐项比对仍待补。

## Summary

论文分析 SEASTAR 2015 的移除反应及质子非弹性散射数据。Ge 低位能级的放置
结合探测器响应、符合谱和邻核系统学。$^{86}$Ge 的三轴解释取决于一条暂定自旋
的馈入线。Ge/Kr 的八极候选来自另一组反应选择。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| LET-1 | $^{86}$Ge 在约 520 keV 有重叠峰。510 与 534 keV 两分量的能量和在误差内与 1064 keV 直达支路相容。Fig. 6.6 的 527 keV 基带跃迁采用较早 β 衰变结果。表列半衰期通过线形扫描估计并传播到线能量误差，受扫描和背景条件限制。 | line-placement-and-adopted-input | direct-original-pages | PDF 83–84, 101–104, Table 6.3, Fig. 6.6 |
| LET-2 | 371 keV 线在 1064 keV 门及约 520 keV 双线门下可见，在 1360 keV 比较门下未见。作者在拟合谱和符合谱中分别报告约 $4\sigma$ 和 $>2\sigma$ 的峰证据。根据衰变路径偏好 $(3^+)\to(2_2^+)$，$0^+$ 是讨论过的竞争归属。 | line-evidence-and-tentative-spin | direct-original-pages | PDF 102–104, Figs. 6.4–6.6 |
| LET-3 | Fig. 6.6 的拟议 $2_2^+,3^+,4_2^+$ 能量为 1051、1422、1912 keV。按 Eq. (7.1) 及 $E(2_1^+)=527$ keV，中心值 $(1912-2\times1422+1051)/527=0.226$，与 Table 7.1 的 $S(4)=0.23(6)$ 一致。正 $S(4)$ 与低 $2_2^+$ 带头合读，Davydov 模型给 $\gamma=30(1)^\circ$。 | model-conditioned-spectrum-test | direct-original-pages-and-arithmetic-check | PDF 104, 123–125, Table 7.1 |
| LET-4 | 对 $^{88}$Ge，Table 6.4 报三条线约 462、551、760 keV。作者以 551 keV 门和系统学提出支路。Table 7.1 未列实测 $S(4)$，壳模型与 SCCM 的相应值分别为 −0.01 和 0.22。 | measurement-and-model-contrast | direct-original-pages | PDF 104–106, 123–124 |
| LET-5 | Kr 的 $(p,p')$ 排除级联馈入后得到态布居截面。作者用能量和及反应偏好推测 $3^-$ 衰变。变形长度换算另用 ECIS-97 的光学势。用 $^{94}$Kr 归一后推得 Ge 的 $B(E2)$，属于间接、条件性估计。 | tentative-state-and-optical-model-dependence | direct-original-pages | PDF 116–120, 126–132, Tables 7.2–7.4 |
| LET-6 | BigRIPS 和 ZeroDegree 的粒子鉴别用飞行时间、磁刚度与能损结合，在焦点位置和角度上校正 $A/Q$。MINOS 漂移速度按机时段标定并用于反应顶点重建。不能重建顶点的 $(p,p')$ 数据采用靶中点近似，峰形与移除反应不同。 | calibration-and-response | direct-original-pages | PDF 59–79, Figs. 5.6–5.11、5.17–5.18 |
| LET-7 | 线形模拟包含光峰和 Compton 连续谱。论文的 $^{84}$Ge 例中，能区自符合投影拟合为 1063(32) 个计数，较高能跃迁的模拟 Compton 贡献为 1020(32)。两数由同一组实验与响应模型得到，自符合可由部分能量沉积产生。 | detector-response-and-coincidence-artifact | direct-original-pages | PDF 79–83, Figs. 5.19、5.21–5.22 |
| LET-8 | 作者先用零寿命线形及背景拟合，再固定其余峰和背景，只对当前线扫描半衰期模板并重拟能量、幅度，以 $\Delta\chi^2=1$ 估计线形寿命区间。对 371 keV 的显著性，面积–误差经验曲线在零面积处给 64(8) 个计数的不确定度。报告的显著性继承这些拟合条件。 | conditional-likelihood-and-empirical-significance | direct-original-pages | PDF 83–84、92–93, Figs. 5.23、5.27 |
| LET-9 | 基础及模型章分别定义 $\beta\cos\gamma$、$\beta\sin\gamma/\sqrt2$ 的四极形状分量、刚性三轴基准和 SCCM 的投影组态混合。后文用刚性转子与 SCCM 势能面对照同一组能级，适用假设不同。 | theoretical-comparison-scope | direct-original-pages | PDF 29–35, Eqs. (3.7)–(3.8), Fig. 3.3 |
| LET-10 | 附录 A.5 对按反应选出的线分别给条件 $\chi^2$ 图。$^{86}$Ge 的 371 keV 候选所用曲线最低点在零寿命附近，510 keV 分支在非零处。附录 C 用测得的截面区间在模型曲线上反演变形长度。 | appendix-confirmation-and-boundary | direct-original-pages | PDF 142 Fig. A.11, 157–159 Figs. C.1–C.4 |

## Competing Interpretations and Limitations

- 一条峰的统计证据与其母态自旋分别保留。拟议的 $3^+$ 一旦改变，按该带
  构建的 $S(4)$ 及形状比较就需重做。刚性转子的 $\gamma$ 是模型坐标，
  能级能量本身未给出形状涨落或四极矩阵元。
- PDF 128 明确指出所用光学势的检验范围及数据能量有落差。量 $\delta_{p,p'}$
  的单位为 fm，表示变形长度。它与在束 γ 的无量纲混合比 $\delta$ 不同。
- 学位论文与其 2017 PRC 的 Ge 结果保留潜在共用数据。Lizarazo Sabogal 学位
  论文也含 SEASTAR 2015 的在束对照，应按核素和事例样本查重。同一装置或
  campaign 无法单独确定同一实验结果。
- 第 4 章把 MINOS 相对 DALI2 中心的上游偏置印为 16.5 cm，线形模拟
  段写的是 16.5 mm，另有分析偏移值。复用几何时应区分这些字段并回查模拟
  名义中心和实际实现（PDF 54、78–79）。
- PDF 92、96 的截面公式中，DALI2 光峰效率已经进入模拟线形，DALI2
  触发效率仍单列。MINOS 顶点选择及 ZeroDegree 透射校正按反应类型处理。
- PDF 151–152 的 Figs. B.3–B.4 图注将反应简写为 $(p,pn)$，与同页
  $^{86,87}$As 到 $^{84}$Ge 的节题和质量数/电荷数不符。按节题分别保留
  $(p,2pn)$、$(p,2p2n)$。附录的多重性变体共用事例，未作独立测量计数。

## Extracted Pages

- PDF 1–10、189：题名、学位、摘要、卷首及声明。
- PDF 11–38：研究动机、反应基础、集体模型和组态混合。
- PDF 39–96：SEASTAR 装置、校准、Doppler 校正、峰形、符合与截面方法。
- PDF 97–132：Ge 移除反应、Ge/Kr 非弹性散射、结构比较及总结。
- PDF 133–160：校准、条件寿命曲线、多重性选择、光学势反演及分隔页。
- PDF 161–186、188：书目、图表目录、成果表、致谢及分隔页。
