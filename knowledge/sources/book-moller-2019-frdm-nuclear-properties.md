---
type: source
title: "P. Möller 等 2019 - Nuclear Properties for Astrophysical and Radioactive-Ion-Beam Applications II (FRDM 2012)"
aliases: [Moller2019, FRDM2012, 宏观微观形变与质量数据库, FRDM形变数据库]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: compilation
reading_depth: deep-read
title_original: "Nuclear properties for astrophysical and radioactive-ion-beam applications II"
authors: [P. Möller, W. D. Myers, H. Sagawa, S. Yoshida]
journal: "Atomic Data and Nuclear Data Tables"
year: 2019
volume: 125
pages: "1-192"
doi: "10.1016/j.adt.2018.03.003"
canonical_source: "P. Möller, W. D. Myers, H. Sagawa, and S. Yoshida, At. Data Nucl. Data Tables 125, 1-192 (2019)"
library_file: "raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Nuclear-properties-for-astrophysical-and-radioact_2019_Atomic-Data-and-Nucle.pdf"
raw_file: "raw/books/ScienceDirect_articles_11Jan2024_03-00-19.625/Nuclear-properties-for-astrophysical-and-radioact_2019_Atomic-Data-and-Nucle.pdf"
raw_sha256: "b751c8054d52975be92b0e4857351226c38059f1e3e4766a1b15c084132f6dbb"
nuclei: [all-nuclei, 131Ce, 133Ce, 135Pr, 135Nd, 136Nd]
reactions: []
experiments: []
models: [frdm-2012, foldy-wouthuysen, lipkin-nogami-pairing, macroscopic-microscopic]
topics: [ground-state-deformation, beta2, beta4, gamma-deformation, nuclear-masses, separation-energies]
---

# P. Möller 等 2019 - Nuclear Properties for Astrophysical and Radioactive-Ion-Beam Applications II (FRDM 2012)

## 专著/宏观微观数据库全貌与学术定位

美国洛斯阿拉莫斯国家实验室（LANL）P. Möller 等人发表在 ADNDT 上的全球原子核基态性质权威数据库（全卷 192 页）。该工作基于**有限程液滴模型（Finite-Range Droplet Model, FRDM 2012）**结合 Lipkin-Nogami 配对修正，对全核素图中从质子滴线到中子滴线的 **7270 个原子核**进行了多维势能曲面能量极小化。

该数据库是国际低能核结构与高自旋物理中获取**原子核基态四极形变 $\epsilon_2$（$\beta_2$）、十六极形变 $\beta_4$、三轴形变 $\gamma$ 以及单中子/单质子分离能 $S_n, S_p$** 最权威的理论基准表。

## 核心理论模型与参数体系

### (1) 宏观-微观方法（Strutinsky 壳修正方法）
总结合能表达为宏观液滴能与微观量子修正的叠加：
$$E_{\text{tot}}(Z, N, \text{shape}) = E_{\text{macroscopic}}(Z, N, \text{shape}) + \Delta E_{\text{shell}}(Z, N, \text{shape}) + \Delta E_{\text{pairing}}(Z, N, \text{shape})$$
- **宏观项**：有限程液滴势，精确包含有限核力程对表面能的修正，消除发散；
- **微观项**：折积 Yukawa 单粒子势中求解单粒子能级，采用 Strutinsky 平滑能级能量展开提取微观壳修正能 $\delta U$；
- **配对项**：在 BCS 基础上利用 Lipkin-Nogami 方法消除粒子数不守恒涨落。

### (2) $A\approx 130$ 核心核素基态形变数据对账
查阅该数据库提取本 Wiki 重点关切核素的基态形变参量基准：
- **$^{131}\text{Ce}$ ($Z=58, N=73$)**：$\beta_2 = 0.224, \beta_4 = -0.040, \gamma = 21.0^\circ$（明确的三轴非对称极小值！）；
- **$^{133}\text{Ce}$ ($Z=58, N=75$)**：$\beta_2 = 0.203, \beta_4 = -0.030, \gamma = 24.5^\circ$；
- **$^{135}\text{Pr}$ ($Z=59, N=76$)**：$\beta_2 = 0.178, \beta_4 = -0.020, \gamma = 22.0^\circ$；
- **$^{136}\text{Nd}$ ($Z=60, N=76$)**：$\beta_2 = 0.191, \beta_4 = -0.020, \gamma = 26.0^\circ$。

这套严格的理论基态形变数据为判定各核素在不同转动自旋窗口下的形变演化提供了不可替代的初值锚点。
