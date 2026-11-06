---
type: source
title: "135,137Ba 静态四极矩与 15/2− E2 分母：NNDC 定标依赖及可检验性"
aliases: [Ba135 Ba137 static E2 constraints, "Ba R_stat^(1) denominator readiness"]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-collection
reading_depth: skimmed
title_original: "Scoped ENSDF collection: 135,137Ba adopted and high-spin reaction records, with 136Ba core calibration"
authors: [B. Singh, A. A. Rodionov, Y. L. Khazov, E. Browne, J. K. Tuli, E. A. McCutchan]
year: 2026
year_basis: "Collection-audit year; underlying evaluation publications are 2007, 2008 and 2018."
canonical_source: "ENSDF:135056001+135056005@200803;137056001+137056005@200709;136056001+136056012@201810:static-E2-Rstat-collection-v1"
citation_key: NNDCBa135Ba137StaticE2Constraints2026
citation_key_origin: "Unique agent-local dataset-collection key; not a claimed match to an existing BibTeX export."
raw_file: "raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/manifest.json"
raw_sha256: "9fc2cdcbc7542179f215da46322282caf5b353b825b7c042ea268e2062635102"
raw_storage_status: archived-local
archive_required: true
data_version: "135Ba 200803; 137Ba 200709; 136Ba 201810. Actual retrieval timestamps are retained in the manifests."
nuclei: [135ba, 137ba, 136ba]
reactions: [130Te-9Be-4n, 128Te-9Be-2n, 136Xe-alpha-3n, Coulomb-excitation]
models: [interacting-boson-fermion-model]
observables: [spectroscopic-quadrupole-moment, magnetic-moment, reduced-E2-transition-probability, half-life, relative-gamma-intensity, internal-conversion-coefficient]
methods: [source-lineage-audit, level-scheme-reconstruction, angular-momentum-normalization]
tags: [a130, ensdf, quadrupole-moment, E2, calibration-dependence, incomplete-data]
---

# 135,137Ba 静态矩与可检验 E2 比值

## Bibliographic Record

本页是指定数据集集合的有界核查，`year: 2026` 表示集合核查年度，**不是评价论文或新实验的发表年**。核心评价为：

- B. Singh、A. A. Rodionov、Y. L. Khazov，*Nuclear Data Sheets* **109**, 517 (2008)：135Ba，记录版本 `200803`，截止 **2008-01-22**。
- E. Browne、J. K. Tuli，*Nuclear Data Sheets* **108**, 2173 (2007)：137Ba，记录版本 `200709`，截止 **2006-10-01**；后续 header 更新保留在原件。
- E. A. McCutchan，*Nuclear Data Sheets* **152**, 331 (2018)：136Ba，记录版本 `201810`，截止 **2018-04-01**。
- 定标声明与理论比较另回链 K. Nomura、T. Nikšić、D. Vretenar，*Phys. Rev. C* **96**, 014304 (2017)，本地 PDF 与 arXiv-v2 TeX；该论文没有报告新的矩测量。
- **指定新原文的后续修订：** A. Vogt et al.，*Phys. Rev. C* **95**, 024316，发表于 **2017-02-15**，DOI `10.1103/PhysRevC.95.024316`；详见 [[vogt-2017-135xe-137ba-isomers-high-spin]]。它提供旧 ENSDF 未采用的 tentative \(15/2^-\) 对应，必须纳入当前可用性判断。

以下 manifest 的条目给出原始 HTTP 响应、精确派生 ENSDF 文本、PDF、实际取得时间和逐文件 SHA-256。两个新增集合的 manifest `retrieved_at` 分别为 **2026-11-06T03:31:40.288392+00:00**（静态矩集合）和 **2026-11-06T03:56:06.940107+00:00**（\(R_{\rm stat}^{(1)}\) 分母集合），均为 **2026-11-06 UTC**；各 HTTP 请求的具体时间仍以条目记录为准，原始时间戳未改写。

| 证据集合 | raw manifest | manifest SHA-256 |
|---|---|---|
| 135/137Ba adopted，本文主 raw 集合 | `raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/manifest.json` | `9fc2cdcbc7542179f215da46322282caf5b353b825b7c042ea268e2062635102` |
| 两个起源高自旋反应对象及其 NNDC references | `raw/papers/gpt/query/20261106-ba-rstat-readiness/manifest.json` | `0efb86a77aaf424a0a384c4e9d3d0646c5337dc6741d97b7a5d1f2824089a8c9` |
| 既有 136Ba adopted/Coulomb 集合 | `raw/papers/gpt/query/20261106-ba-core-E2-calibration/manifest.json` | `ee30e3a0c13f8f5187f871b794269e085810b8f81e68c56c4e08c0363e6e192b` |
| 既有 Nomura2017 arXiv-v2 源码集合 | `raw/papers/gpt/query/20261105-nomura2017-input-audit/manifest.json` | `6983451319465b527cc02adbabd8f4561c71dfe395c291632b20868674ec9cb9` |
| Vogt2017 两份 accepted manuscripts、元数据及本地核查派生物 | `raw/papers/gpt/query/20261106-vogt2017-ba137-rstat/manifest.json` | `3e777f4bae5e9e2ca7b4a6bd773436d1282bdd64678b117250d512c886f5854f` |

Nomura 本地 PDF：`raw/papers/2017_Nomura et al_Shape-phase transitions in odd-mass γ -soft nuclei with mass A ≈ 130.pdf`，SHA-256 `481e6a9e0f6b01e9c5db5e2b06d9b350dba0638393c7da7f532c3040e9efaea9`。

定位符缩写如下；ENSDF/TeX 行号从 1 开始，保留 ENSDF 首行空行：

| 缩写 | 原件 |
|---|---|
| A135 | [135Ba adopted](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc135-adopted-text.ens)；配套 PDF 20 页 |
| A137 | [137Ba adopted](/workspace/wiki/raw/papers/gpt/query/20261106-ba-spin-moment-benchmark/nndc137-adopted-text.ens)；配套 PDF 11 页 |
| R135 | [135056005，130Te(9Be,4nγ)](/workspace/wiki/raw/papers/gpt/query/20261106-ba-rstat-readiness/nndc135-reaction-text.ens) |
| R137 | [137056005，136Xe(α,3nγ)](/workspace/wiki/raw/papers/gpt/query/20261106-ba-rstat-readiness/nndc137-reaction-text.ens) |
| A136/C136 | [136Ba adopted](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-adopted-text.ens) / [Coulomb](/workspace/wiki/raw/papers/gpt/query/20261106-ba-core-E2-calibration/nndc136-coulomb-text.ens) |
| N17 | [Nomura arXiv-v2 TeX](/workspace/wiki/raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex)，与上列 PDF 对读 |

## Scope and Reading Depth

**Covered scope:** 135/137Ba 最低 \(11/2^-\) 的静态矩与 isomer 衰变；136Ba \(2_1^+\) 定标矩的原样多解；135/137Ba 最低 \(15/2^-\rightarrow11/2^-_1\) 目标的能级、γ、半衰期、ICC 与绝对 E2 数据可用性；N17 E2 定义/定标段、Tables I/III/V/VI；固定模型的独立 \(Q_s\) 收缩与比值归一化。后续只增加指定 Vogt2017 的 Fig.6/7、Table II/III 及相关正文核查，修订 137Ba 的当前目标指认状态。

**Not covered:** 未通读这些评价的全部能级物理内容；未获取所有原始矩实验或 2006/1973 反应论文全文；未穷尽 135/137Ba 后续实验，更未展开整条同位素链新检索；没有重拟合 \(e_F,\chi_E\)，没有原作者运行卡或已认证的原文 EM 图重放。因此阅读状态为 `skimmed`，不把局部深入核验标为全文 deep-read。

## Summary

\(^{137}\)Ba \(11/2^-_1\) 的 adopted \(Q_s=+0.78(9)\) e b 与固定实现 \(+0.7729629\) e b 接近，但它正是 N17 明确用于调整中子有效电荷的目标态；这种一致只支持定标一致性。\(^{135}\)Ba 的固定值 \(+1.1769303\) e b 高于 N17 所列实验 \(+0.98(8)\) e b 和当前 archived adopted \(+0.96(8)\) e b，也不等于其印刷理论 \(+1.13\) e b。

136Ba 定标矩包含同一实验的干涉多解，不能只挑有利解。提出的 \(R_{\rm stat}^{(1)}\) 是以第一个 \(15/2^-\) 态为分母目标的旋转不变可观测组合，与整个 \(J+2\) 通道求和的比值不同。当前核查仍不能给出两个核的实验分母：135Ba 的 tentative 目标缺少母态寿命；**137Ba 已有 Vogt2017 的 2229.8-keV \((15/2^-)\) 候选及约 1568-keV 支路，但该态的独立寿命/绝对 E2 强度未给出**。此前“没有已指认 \(15/2\)”只描述两个旧 ENSDF 对象，不再作为当前文献结论。

## Key Results

表中 `direct` 指直接读取指定评价字段、原论文表格或核验指定数学关系，**不表示重新分析了原始事件数据**。

| ID | 陈述 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| BA-MOM-1 | N17 以各芯 \(B(E2;2_1^+\to0_1^+)\) 调整 \(e_B\)，以 136Ba \(2_1^+\) 矩调整 \(\chi_E=+0.35\)，以 137Ba \(11/2^-_1\) 矩调整中子 \(e_F=0.125\) e b；该段未给出后两态的数值矩。 | author-interpretation | direct | single | high | N17 PDF p.4 Eqs.(7)–(8) 后；TeX 549–582 | false |
| BA-MOM-2 | A137 的 661.659-keV \(11/2^-\) 态为 \(Q_s=+0.78(9)\) e b，\(\mu=-0.992(26)\mu_N\)；另保留与 adopted 值冲突的旧 \(Q\approx-0.05\) 结果。 | experimental-fact | direct | multiple-dependent | high | A137 60–69；PDF p.1；1983Mu12/1989Ra17、旧值 1976Fu06 | false |
| BA-MOM-3 | N17 Table VI 为 135Ba \(11/2^-_1\) 引用实验 \(Q_s=+0.98(8)\) e b；A135 268.218-keV 同态的评价值为 \(+0.96(8)\) e b。 | experimental-fact | direct | multiple-dependent | high | N17 PDF p.9 Table VI；TeX 986–993；A135 107–115、PDF p.1 | false |
| BA-MOM-3T | N17 Table VI 给出的作者模型结果为 135Ba \(11/2^-_1\) 的 \(Q_s=+1.13\) e b。 | model-result | direct | single | high | N17 PDF p.9 Table VI；TeX 993 | false |
| BA-MOM-4 | 136Ba \(2_1^+\) 的 constructive/destructive 矩依次为 −0.19(6)/+0.07(7)、+0.01(5)/+0.25(5)、−0.19(17)/+0.02(18) e b。 | experimental-fact | direct | multiple-dependent | high | A136 51–61、PDF p.1；C136 46–58 | false |
| BA-MOM-5 | 固定参数的独立重构给出 \(Q_s(135)=+1.1769303\)、\(Q_s(137)=+0.7729629\)、\(Q_s(136,2_1^+)=-0.3032375\) e b；这不是原作者计算值或新的实验值。 | model-result | direct | single | high | static-v1 benchmark-results.json；本文下述方法与代码/输入哈希；N17 参数 Tables I/III/V | false |
| BA-RSTAT-1 | A135 最低候选为 \(950.5(3)\)-keV \((15/2^-)\)，682.3-keV `Q` γ 接 268.218-keV \(11/2^-\)。RI=100，无母态 T 字段和 ICC；R135 给出 DCO=1.18(3)，仍没有绝对 E2 强度。 | experimental-fact | direct | multiple-dependent | high | A135 51–54、202–206；R135 21–33、53–57 | true |
| BA-RSTAT-2 | **历史范围：** A137/R137 未列出已指认的 \(15/2\) 态；2047.4-keV 未定自旋态的 \(T_{1/2}<10\) ns 界不足以确定目标。此结论只适用于所查 2007 ENSDF 对象，已由下面的 V17 指认信息扩展。 | our-inference | direct | multiple-dependent | high | A137 147–150；R137 7、25–26；两对象全部 L 记录的有界扫描 | true |
| BA-RSTAT-3 | **2007 ENSDF 旧标注：** 0.59(10) μs、120.2-keV E2、\(\alpha=1.004(17)\)、\(B(E2)=0.45(8)\) W.u. 对应 \((17/2^-)\to(13/2^-)\)。原记录保留为历史版本，不覆盖 V17 的新解释。 | experimental-fact | direct | single | high | A137 192–200；R137 31–33 | false |
| BA-RSTAT-V17A | Vogt2017 在 2229.8、2349.9 keV 分别给出 \((15/2^-)\)、\((19/2^-)\) tentative 指认，依据同中子素系统学；不能继续声称当前没有 \(15/2^-\) 候选。 | author-interpretation | direct | single | high | Vogt2017 Fig.6、Table II；accepted PDF pp.8–9，稿件 pp.7–8 | true |
| BA-RSTAT-V17B | Vogt2017 的 \(T_{1/2}=589(20)\) ns 属于 2349.9-keV 上游态；报告的 \(B(E2;(19/2^-)\to(15/2^-))=0.46(3)\) W.u. 是不同于所需分母的跃迁。 | experimental-fact | direct | multiple-dependent | high | Vogt2017 Fig.7/Sec.III B、Table III；accepted PDF pp.9、14 | false |
| BA-RSTAT-4 | 对 \(J=11/2\)，\(S_{\rm stat}=91Q_s^2/(176\pi)\)，\(B_\uparrow=(16/12)B_\downarrow\)。纳入 V17 后两个实验 \(R_{\rm stat}^{(1)}\) 仍未确定；137Ba 的缺口是 2229.8-keV 态的绝对 E2 分母，不是完全没有候选指认。 | our-inference | direct | multiple-dependent | high | 下述归一化推导；历史 rstat-readiness.json；新增 vogt2017-readiness.json 与原文 Table II/III | false |

**静态矩及依赖。** N17 引用的 135Ba 实验矩 +0.98(8) 与 A135 评价矩 +0.96(8) 分别保留，不平均、不当成两个独立测量；作者模型 +1.13 单独归为 `model-result`。135/137Ba 的矩评价共享 1983Mu12、1989Ra17 等来源键，未获得联合协方差。136Ba 的三组矩来自 1986BaZJ/1986Ro15、1984Be20、1972Ke16；同一研究的两种干涉解不是独立观测，这些研究还贡献芯 \(B(E2)\) 定标。N17 Table VI 同时给出 135Ba \(\mu_{\rm th}=-1.161\)、\(\mu_{\rm expt}=-1.001(15)\mu_N\)；其矩表头印成 \(\mu_N^2\)，本页按静态磁矩物理量标注 \(\mu_N\)，没有将其解释为 \(B(M1)\)。

**半衰期与算符范围。** A135 107–122、PDF pp.1/6 的 28.7(2) h、\(B(M4)=2.50(7)\) W.u.，以及 A137 60–76、PDF pp.1/4 的 2.552(1) min、\(B(M4)=2.719(9)\) W.u.，均属于 \(11/2^-\to3/2^+\) isomer 衰变。它们不是 \(15/2^-\) 母态寿命，也不能给单负宇称 E2 空间的目标分母定标。

**135Ba 目标拓扑。** R135 中未加括号的 \(15/2^-\) 不覆盖 adopted 的 tentative 标注。2006Ch51 是 Che 等，*Eur. Phys. J. A* **30**, 347 (2006)；RI/DCO 还依赖 2007ChZZ 私人通信。1987Dr13 的较早 γ 能量为 682.7 keV，另列保留。能量关系 \(950.5-682.3\simeq268.218\) keV 支持该连接，但 RI=100 不是绝对衰变概率。`Q` 表示四极阶数；若 tentative 同宇称指认成立，它与 E2 相容。缺失的 ICC 不能置零。

**137Ba 防止错配。** R137 源于 1973Ke07/1973Ke22 的 \((\alpha,3n\gamma)\) 工作。未定自旋的 2047-keV 能级不能仅因有到 \(11/2^-\) 的 γ 就指认为模型 \(15/2^-_1\)；其时间界也不是精确寿命。A137 106–111 的 \(7/2^-\to11/2^-\) E2 属于另一自旋通道，同样不能替代所需 \(J+2\) 分母。

**Vogt2017 后的当前范围。** Fig.6/Table II 给出的目标候选为 \(2229.8\;(15/2^-)\to661.7\;11/2^-\)，Table II 的 γ 值是 1568.2±0.5 keV，Fig.6 标 1568.1 keV；两者分别保留。Table II 没有填写该行 \(I_\gamma\)，也没有给出该母态的独立寿命。用下游 1568-keV γ 加门测出的 589(20) ns 属于上游 \(2349.9\;(19/2^-)\) isomer，不能借给 2229.8-keV 态。其 120.1-keV \((19/2^-)\to(15/2^-)\) E2 的 0.46(3) W.u. 可作为**另列的** EM 检验，已由作者校正内转换；不是 \(R_{\rm stat}^{(1)}\) 分母。初态 11/2 的三阶闭合链要求两个中间自旋都在 \(7/2,\ldots,15/2\)，因此 19/2 也不直接进入该三阶矩。该文的 135Xe 9.0(9)-ns 数据不能误接到 135Ba。

**归一化与可观测定义。** 采用标准 Wigner–Eckart 约定，
\[
Q_s=\sqrt{16\pi/5}\,
\frac{C(JJ,20|JJ)}{\sqrt{2J+1}}R_{JJ},
\qquad C(11/2,11/2;2,0|11/2,11/2)^2=\frac{55}{91}.
\]
故
\[
S_{\rm stat}=\frac{|R_{JJ}|^2}{12}=\frac{91}{176\pi}Q_s^2,\qquad
R_{\rm stat}^{(1)}=\frac{273}{704\pi}\frac{Q_s^2}
{B(E2;15/2^-_1\rightarrow11/2^-_1)} .
\]
这里反向关系是 \(B(E2;11/2\to15/2)=(16/12)B(E2;15/2\to11/2)\)，不是其倒数；\(Q_s\) 以 e b、\(B(E2)\) 以 \(e^2b^2\) 计。比值含 \(Q_s^2\)，因此静态矩符号仍须单独保留。

若由衰变率求分母，在完整衰变支路已知的条件下需要
\[
B_\downarrow(E2)=
\frac{\ln2}{T_{1/2}(\text{emitting parent})\,C_{E2}E_\gamma^5}
\frac{I_{\gamma,t}f_{E2,t}}
{\sum_k I_{\gamma,k}(1+\alpha_k)} .
\]
\(f_{E2}=1\) 需要纯 E2 的依据；不能用相对峰面积、下方 isomer 寿命、芯的 \(B(E2)\) 或模型分母替代缺失实验输入。模型候选 \(R_{\rm stat}^{(1)}(135)=2.2722073553\)、\(R_{\rm stat}^{(1)}(137)=1.3565277480\) 暂无本次来源集内可构造的对应实验值。

**固定模型的物理范围。** static-v1 保持 \(e_F=0.125\) e b、\(\chi_E=+0.35\)，仅按既有冻结强度确定正 \(e_B\)。137Ba 的同态玻色子/费米子贡献为 +0.6947536/+0.0782093 e b；135Ba 为 +1.1255734/+0.0513569 e b。135 的玻色子项恰可四舍五入到 N17 的 +1.13，不能据此断言作者漏掉费米子项。136 的 −0.3032375 与 −0.19 中心值不同，但不同来源误差及干涉分支使其不能被简化为唯一的“定标失败”；作者的具体数值目标和运行卡仍未知。

## Competing Interpretations and Limitations

- 137Ba 静态矩是已声明的有效电荷定标目标。未来若有独立测定的 \(15/2^-\) 绝对 E2 分母，可以增加 EM 信息，但整个比值的静态分子仍与定标相关。
- 135Ba 固定实现高于论文/评价实验中心值，也不精确重放 N17 印刷理论；不把源参数圆整、版本差异、未公开运行卡等可能解释写成已确定原因。不重拟合 \(e_F\) 或 \(\chi_E\) 消除差异。
- 半衰期、由其导出的 \(B(M4)\)、同源相对强度，以及同一次库仑激发的干涉解不能逐行当成独立证据。quoted margins 保留原义，不假定高斯误差、模型误差或统计显著性。
- 135 tentative 自旋/宇称及缺失寿命、137 在 V17 中仍为 tentative 的目标对应及缺失绝对 E2 分母，是当前有界核查的实际边界。旧 ENSDF 无 \(15/2\) 标注保留为历史事实，不据此否定新原文已有的候选，也不宣称全世界不存在相关测量。
- 这些 snapshot 不是经认证的 N17 作者实际使用数据库版本。源能谱子集的一致性不能代替 EM 验证；完整模型空间的标量矩及限制态投影比值均可能具有旋转不变性，但都不自动给出物理内禀形状。没有原文 EM/不变量图重放或“修正已发表图”的结论。

## Extracted Pages

- 本次只新建本 source 页；不修改 index、handoff 或其它知识页。
- 相关既有 source：[[nomura-2017-odd-mass-gamma-soft-shape-transitions]]。
- 后续指定原文 source：[[vogt-2017-135xe-137ba-isomers-high-spin]]；其 bibliography 使用 `Vogt2017PRC95_024316`，新数据单独写入 Vogt2017 sidecar。
- 可复算实现及固定输入：[static-v1 report](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/report.md)、[benchmark-results.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/benchmark-results.json)、[source-constraints.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/source-constraints.json)。这些是模型/提取审计产物，实验事实以上述 raw locator 为依据。
- 原有 ENSDF 有界扩展作为历史审计保留：[rstat-readiness.md](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/rstat-readiness.md)、[rstat-readiness.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/rstat-readiness.json)、[check_rstat_availability.py](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/check_rstat_availability.py)。原 static-v1 及这些历史输出均不改写；当前 primary-paper 可用性以 [vogt2017-readiness.json](/workspace/wiki/outputs/l4/20261105-ba129-controlled-pairing/spin-invariant-moment-benchmark/vogt2017-readiness.json)补充。
