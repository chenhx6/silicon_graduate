---
type: source
title: 'Rodríguez & Martínez-Pinedo 2010: 基于能量密度泛函与生成坐标法研究无中微子双贝塔衰变核矩阵元 (PRL 105, 252503)'
aliases: [Rodriguez 2010 PRL 0nubb EDF, 'Phys. Rev. Lett. 105, 252503', 10.1103/PhysRevLett.105.252503, 'arXiv:1008.5260']
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: Energy density functional study of nuclear matrix elements for neutrinoless ββ decay
authors: [Tomás R. Rodríguez, Gabriel Martínez-Pinedo]
journal: Physical Review Letters
year: 2010
volume: 105
pages: '252503'
doi: 10.1103/PhysRevLett.105.252503
arxiv: 1008.5260v2
language: en
canonical_source: https://doi.org/10.1103/PhysRevLett.105.252503
zotero_item_key: ''
citation_key: ''
zotero_uri: ''
library_file: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G35/rodriguez-2010-prl105-252503-0nubb.pdf
raw_sha256: b8d5322216450965e6cabd29b695e7fb7fe7b09333b993bc45aa659efab78014
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: [48ca, 76ge, 82se, 96zr, 100mo, 116cd, 124sn, 128te, 130te, 136xe, 150nd, 150sm]
reactions: []
experiments: []
models: [energy-density-functional, gogny-d1s, gcm, particle-number-projection, angular-momentum-projection]
observables: [0nu-nme, half-life, gt-strength, q-value, deformation-beta, pairing-energy]
methods: [gcm-pnamp, closure-approximation, hill-wheeler-griffin-equation, ucom-src]
tags: [0nu-beta-beta, nuclear-matrix-elements, energy-density-functional, gogny-d1s, deformation-mismatch, pairing-correlations, closure-approximation, fulltext-read]
---

# Rodríguez & Martínez-Pinedo 2010：基于能量密度泛函与生成坐标法研究无中微子双贝塔衰变核矩阵元

## Bibliographic Record

Tomás R. Rodríguez and Gabriel Martínez-Pinedo, *Energy density functional study of nuclear matrix elements for neutrinoless $\beta\beta$ decay*, Physical Review Letters **105**, 252503 (2010). DOI: `10.1103/PhysRevLett.105.252503`。arXiv 预印本版本为 `arXiv:1008.5260v2 [nucl-th]`（提交日期为 2010 年 11 月 26 日；下载的预印本首页注记 "(Dated: November 10, 2018)" 与版本/发表年份不同；其产生原因未查明，不据此另立2018年研究）。本地归档 PDF 位于 `raw/papers/gpt/query/20261108-foundations-G35/rodriguez-2010-prl105-252503-0nubb.pdf`，大小 462,144 字节，SHA-256 值为 `b8d5322216450965e6cabd29b695e7fb7fe7b09333b993bc45aa659efab78014`。

## Scope and Reading Depth

- Completed reading_depth: deep-read（全文共 5 页深度精读，涵盖公式 Eqs. 1–4、表 I 完整数据、图 1–3 能谱、集体波函数与形变空间分布）。
- Covered scope:
  1. 轻马约拉纳中微子交换机制下的无中微子双贝塔衰变半衰期与核矩阵元（NME）形式（Eqs. 1–2）；
  2. 闭合近似（closure approximation）的假定与两体跃迁算符分解（Fermi、Gamow-Teller、Tensor）；
  3. 轴矢量常数与相空间因子的文献约定说明（$g_V=1.0, g_A=1.25$）；
  4. 基于 Gogny D1S 泛函的大模型空间（11 个球形谐振子主壳，无冻结惰性核芯）约束 HFB 计算；
  5. 变分后粒子数投影（PNP: $P^N, P^Z$）与角动量投影（AMP: $P^{I=0}$）以恢复对称性；
  6. 沿轴对称四极形变 $\beta$ 坐标的生成坐标法（GCM）组态混合，求解 Hill-Wheeler-Griffin (HWG) 方程获取初末态物理集体波函数；
  7. 跃迁核在内禀形变平面 $(\beta_i, \beta_f)$ 上的分布特征及与配对能 $-E_{pp}$ 的空间相关性；
  8. $^{150}\text{Nd} \to {}^{150}\text{Sm}$ 形变重叠对该模型矩阵元的影响，以及 $^{48}\text{Ca}$ 双闭壳低配对能对应的小矩阵元；
  9. 表 I 所列 11 个主要衰变母核的理论与实验 $Q$ 值偏差、单电荷交换反应总 Gamow-Teller 强度 $S_\pm$ 校验、核矩阵元 $M^{0\nu}$ 与预测半衰期。
- Not covered:
  1. 奇奇中间核逐态色散能谱（闭合近似消除了中间核分立能级求和，本框架无法直接计算两中微子模式 $2\nu\beta\beta$）；
  2. 三轴非轴对称形变自由度 $\gamma$、八极空间反射不对称度及时间反演破缺分量；
  3. 质子-中子同位旋标量配对（$T=0$ isoscalar pairing）的显式动力学处理。

## Summary

Rodríguez & Martínez-Pinedo (PRL 2010) 基于自洽微观能量密度泛函（Gogny D1S）与对称性恢复生成坐标法（GCM+PNAMP），在 11 个主振子壳大基矢空间中计算了 11 个主要双贝塔候选核的核矩阵元。在轻马约拉纳中微子交换与闭合近似下，半衰期写为 $[T_{1/2}^{0\nu}]^{-1} = G_{01} |M^{0\nu}|^2 (\langle m_{\beta\beta} \rangle / m_e)^2$，矩阵元分解为 $M^{0\nu} = -(g_V/g_A)^2 M_{\text{F}}^{0\nu} + M_{\text{GT}}^{0\nu} - M_{\text{T}}^{0\nu}$，取 $g_V=1.0, g_A=1.25$，作者指出张量项 $M_{\text{T}}^{0\nu}$ 依文献评估较小而予以略去。计算表明：轴对称两体跃迁核在形变相空间 $(\beta_i, \beta_f)$ 上呈对角聚集，离开对角线强度衰减；在 $^{150}\text{Nd} \to {}^{150}\text{Sm}$ 算例中，母核长椭球（$\beta \approx +0.40$）与子核长椭分布（$\beta \approx +0.25$）的集体波函数峰值错位使得两态重叠受到削弱，得到较小的矩阵元 $M^{0\nu} = 1.71$；跃迁核分布与超流配对能 $-E_{pp}$ 具有正向空间关联，双闭壳核 $^{48}\text{Ca}$ 因配对能最低呈现出较小矩阵元 $M^{0\nu} = 2.37$；形变相近的开壳核矩阵元较为平稳地分布在 4.2–5.7 之间。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| R10-1 | 在轻马约拉纳中微子交换机制与闭合近似下，衰变半衰期为 $[T_{1/2}^{0\nu}(0^+ \to 0^+)]^{-1} = G_{01} \vert M^{0\nu}\vert ^2 (\langle m_{\beta\beta} \rangle / m_e)^2$；核矩阵元分解为 $M^{0\nu} = -(g_V/g_A)^2 M_{\text{F}}^{0\nu} + M_{\text{GT}}^{0\nu} - M_{\text{T}}^{0\nu}$，取 $g_V=1.0, g_A=1.25$；作者依据文献 [5, 8] 指出张量项较小而在本工作中略去。 | model-result | direct | p. 1, col. 2, Eqs. (1)-(2) | false |
| R10-2 | 轴对称 GCM+PNAMP 投影两体跃迁核在形变相空间 $(\beta_i, \beta_f)$ 上主要聚集在对角线 $\beta_i \approx \beta_f$ 附近，球形构型 $(\beta=0)$ 处取得全局极大值，非对角元随初末态形变差增大而衰减。 | model-result | direct | p. 2, col. 2; p. 3, Fig. 2a | false |
| R10-3 | 0νββ 跃迁核在形变相空间上的分布与该模型计算的超流配对能量 $-E_{pp}$ 展现出直接的空间正关联，强配对基底构型提供较大的跃迁核强度。 | model-result | direct | p. 3, col. 1-2, Fig. 2b | false |
| R10-4 | 在 $^{150}\text{Nd} \to {}^{150}\text{Sm}$ 计算中，母核长椭形变 $(\beta \approx +0.40)$ 与子核长椭形变 $(\beta \approx +0.25)$ 产生波函数峰值分离，相空间重叠减弱，计算得到 $M^{0\nu} = 1.71$（$M_{\text{GT}} = 1.28$, $-(g_V/g_A)^2 M_F = 0.43$）。 | model-result | direct | p. 3, col. 1; Fig. 1 inset | false |
| R10-5 | 在 $^{48}\text{Ca} \to {}^{48}\text{Ti}$ 计算中，因 $^{48}\text{Ca}$ 为双闭壳（$Z=20, N=28$），其超流配对能 $-E_{pp}$ 为全表最低，计算得到较小的 $M^{0\nu} = 2.37$。 | model-result | direct | p. 3, col. 2; Table I | false |
| R10-6 | 该模型计算的开壳核 $^{76}\text{Ge} (4.60), {}^{82}\text{Se} (4.22), {}^{96}\text{Zr} (5.65), {}^{100}\text{Mo} (5.08), {}^{116}\text{Cd} (4.72), {}^{124}\text{Sn} (4.81)$ 的矩阵元分布在 4.2–5.7 之间，高于当时未扩壳的壳模型（ISM）结果（约 2.3–2.8）。 | model-result | direct | p. 3, col. 2; Table I, Fig. 3 | false |
| R10-7 | 作者用电荷交换GT总强度作模型校验，并采用(0.74)²；存在相近值也存在偏差，例如96Mo的S+理论2.56、采用实验0.29(8)。不能称全表均在误差内吻合，也不能据此自动确定0ν算符的缩放。 | model-versus-adopted-experiment | direct-original | PDF4 Table I及校验段 | false |

## Competing Interpretations and Limitations

1. **大尺度壳模型（ISM）的组态相消解释**：ISM 计算（如 Caurier 2008, Menéndez 2009）给出的 $M^{0\nu}$ 普遍在 2.0–2.8 左右，约为本工作的约 $50\%$。壳模型讨论指出，GCM 仅考虑了纯准粒子真空的四极投影态，缺少破对的高 Seniority（$s=4, 6$）多准粒子组态；在壳模型中，这些高 Seniority 组态由于多极相消干涉会压低矩阵元。反之，EDF 作者认为 ISM 限制在单个价壳层内，缺乏高动量虚中微子交换所能激发的跨主壳相干贡献。
2. **QRPA 的同位旋破缺与质中相互作用敏感性**：QRPA 依赖质子-中子相互作用常数 $g_{pp}$ 的唯象调节，该参数通常拟合于 $2\nu\beta\beta$ 数据；而 GCM 自洽使用 Gogny 泛函，无需引入 $g_{pp}$。
3. **本工作自身模型局限**：
   - 限于轴对称形变空间，未包含三轴自由度 $\gamma$；
   - 未显式包含配对自由度涨落坐标（仅限制在沿 $\beta$ 的自洽 HFB 极小处）；
   - 依赖闭合近似，两体算符未包含更高阶手征流修正。

## Extracted Pages

- Nuclei: $^{48}\text{Ca}, {}^{76}\text{Ge}, {}^{82}\text{Se}, {}^{96}\text{Zr}, {}^{100}\text{Mo}, {}^{116}\text{Cd}, {}^{124}\text{Sn}, {}^{150}\text{Nd}, {}^{150}\text{Sm}$.
- Concepts: 无中微子双贝塔衰变核矩阵元, 闭合近似, 投影生成坐标法 (GCM+PNAMP), 形变相空间重叠, 超流配对关联.
- Methods: Gogny D1S 能量泛函, 粒子数与角动量投影, Hill-Wheeler-Griffin 方程.
