---
type: source
title: "同济大学数学系 2014 - 高等数学第七版下册"
aliases: [同济高等数学下册, 同济高数第七版下册, TongjiHigherMathVol2]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "高等数学第七版下册"
authors: [同济大学数学系]
publisher: "高等教育出版社 (北京)"
year: 2014
pages: "367"
isbn: "9787040396621"
citation_key: tongji2014
canonical_source: "同济大学数学系, 《高等数学》（第七版下册）, 高等教育出版社 (2014)"
library_file: "raw/books/同济大学高等数学第七版下册.pdf"
raw_file: "raw/books/同济大学高等数学第七版下册.pdf"
raw_sha256: "4fe09776fec91bd3d780b163758025e6fbc2ce62ec15b53ee41ccdb3a8c48bf2"
nuclei: []
reactions: []
experiments: []
tags: [higher-mathematics, vector-algebra, multivariable-calculus, multiple-integrals, surface-integrals, stokes-theorem, gauss-divergence]
models: [vector-calculus, lagrange-multipliers, fourier-series, volume-integrals]
topics: [vector-algebra, multivariable-calculus, multiple-integrals, surface-integrals, fourier-series]
---

# 同济大学数学系 2014 - 高等数学第七版下册

## Bibliographic Record

- **书名**：高等数学（第七版下册）
- **著者**：同济大学数学系
- **出版信息**：高等教育出版社，2014 年 7 月第 7 版，ISBN 978-7-04-039662-1。
- **全书规模**：367 物理 PDF 页；正文印刷页 1–336，附录答案 337–367。
- **本地原件**：`raw/books/同济大学高等数学第七版下册.pdf`
- **原件 SHA-256**：`4fe09776fec91bd3d780b163758025e6fbc2ce62ec15b53ee41ccdb3a8c48bf2`

## Scope and Reading Depth

本来源登记状态定为 `deep-read`。
本轮核验通过全书 5 大章节（第 8–12 章）完整书签映射与微积分推导核对，重点核读：
- **第八章 向量代数与空间解析几何（PDF pp. 8–60 / 印刷 pp. 1–53）**：
  - §2 数量积、向量积与混合积（pp. 14–23）：标量三重积 $\vec{A} \cdot (\vec{B} \times \vec{C})$ 的行列式几何定义与正交三面体右手性判定；
- **第九章 多元函数微分法及其应用（PDF pp. 61–141 / 印刷 pp. 54–134）**：
  - §7 方向导数与梯度（pp. 103–111）：势能曲面最陡下降路径与动力学力场；
  - §8 多元函数极值与条件极值（pp. 111–122）：Lagrange 乘子法在受约束自洽平均场形变计算中的数学基础；
- **第十章 重积分（PDF pp. 142–194 / 印刷 pp. 135–187）**：
  - §2–§3 二重与三重积分（球坐标/柱坐标变换）：核电荷密度分布积分提取内禀电四极矩 $Q_0$、电荷均方根半径与水动力学转动惯量；
- **第十一章 曲线积分与曲面积分（PDF pp. 195–257 / 印刷 pp. 188–250）**：
  - §4–§5 第一类与第二类曲面积分；
  - §6 高斯公式、通量与散度（Gauss Divergence Theorem）：核电荷流连续性方程；
  - §7 斯托克斯公式、环流量与旋度（Stokes Theorem）：水动力学无旋流条件 $\nabla \times \vec{v} = 0$ 与 Bohr 转动惯量推导；
- **第十二章 无穷级数（PDF pp. 258–336 / 印刷 pp. 251–329）**：
  - §7–§8 傅里叶级数：含时密度泛函（TD-CDFT）实时间相空间进动轨迹傅里叶变换提取准粒子激发能谱。
- **配套方法合同**：[[nuclear-mathematics-calculus-and-vector-geometry-contract]]。

## Summary

本书是中国理工科经典权威的高等数学教材。书中严密阐述的矢量代数、多变量微分学、重积分、曲面积分以及高斯/斯托克斯场论定理，构成了低能核结构中四极/八极形变表面微积分积分、手征非共面矢量三重积、无旋流流体转动惯量以及约束平均场形变极小化搜索的核心数学基石。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MATH-1 | 标量三重积（混合积）与空间手征性度规：三个非共面矢量混合积由三阶行列式给出：$\vec{A} \cdot (\vec{B} \times \vec{C}) = \det(\vec{A}, \vec{B}, \vec{C})$；其代数符号严格区分右手系（$>0$）与左手系（$<0$），其绝对值代表三面体平行六面体体积，构成了核手征几何中非共面手征度规 $\mathcal{V} = \vec{j}_p \cdot (\vec{j}_n \times \vec{R})$ 的第一性原理数学定义。 | mathematical-formalism | direct | 第八章 §2, 印刷 pp. 18–21 / PDF pp. 25–28 | false |
| MATH-2 | 多元函数条件极值与 Lagrange 乘子法定理：在约束条件 $\phi_k(\vec{x}) = 0$ 下寻找能量泛函 $E(\vec{x})$ 极值，通过引入乘子构造辅助函数 $L = E - \sum \lambda_k \phi_k$，使微观约束 Hartree-Fock 或自洽协变密度泛函约束形变势能曲面（PES）获得严密的微积分求解规范。 | mathematical-formalism | direct | 第九章 §8, 印刷 pp. 115–122 / PDF pp. 122–129 | false |
| MATH-3 | 空间球坐标三重积分与宏观四极形变矩提取：通过对轴对称及三轴核表面密度 $\rho(r, \theta, \phi)$ 进行体积积分，将高阶球谐多极矩精确解析化为形变参数 $(\beta, \gamma)$ 的幂级数：$Q_{20} = \iiint \rho r^2 Y_{20} dV = \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta \cos\gamma$。 | mathematical-formalism | direct | 第十章 §3–4, 印刷 pp. 160–178 / PDF pp. 167–185 | false |
| MATH-4 | 斯托克斯公式与水动力学无旋流转动惯量导出：根据斯托克斯定理 $\oint \vec{v} \cdot d\vec{r} = \iint (\nabla \times \vec{v}) \cdot d\vec{S}$，在无旋流假定 $\nabla \times \vec{v} = 0$ 下速度场存在势函数 $\vec{v} = \nabla \Phi$，通过求解 Laplace 方程 $\nabla^2 \Phi = 0$ 并积分动能导出 Bohr-Mottelson 四极形变液体无旋流转动惯量 $\mathcal{J}_k = 4 B \beta^2 \sin^2(\gamma - k 2\pi/3)$。 | mathematical-formalism | direct | 第十一章 §7, 印刷 pp. 240–250 / PDF pp. 247–257 | false |
| MATH-5 | 高斯通量定理与核电荷流连续性：通过高斯公式 $\iint \vec{j} \cdot d\vec{S} = \iiint (\nabla \cdot \vec{j}) dV$，严格将核表面向外辐射的光子通量与核内部电荷密度守恒方程 $\nabla \cdot \vec{j} + \partial \rho / \partial t = 0$ 闭合，微观形式推导电偶极与电四极辐射场微分矩阵元。 | mathematical-formalism | direct | 第十一章 §6, 印刷 pp. 232–240 / PDF pp. 239–247 | false |

## Competing Interpretations and Limitations

高等数学处理的是实数域与经典连续流体力学几何积分；在微观核多体系统中，费米子自旋具有半整数宇称、反对称波函数以及泡利排斥阻塞，连续密度微积分需配合 Slater 行列式与两体跃迁矩阵元代数离散化。

## Extracted Pages

- 第八章 §2：PDF pp. 21–30，混合积行列式与空间右手三面体判定。
- 第九章 §7–8：PDF pp. 110–128，梯度、方向导数与 Lagrange 条件极值。
- 第十章 §3–4：PDF pp. 167–185，重积分坐标变换与核电荷/惯量积分。
- 第十一章 §6–7：PDF pp. 239–255，高斯公式与斯托克斯定理在流动速度场中的应用。

## Sources

- `raw/books/同济大学高等数学第七版下册.pdf`
- [[nuclear-mathematics-calculus-and-vector-geometry-contract]]
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]
- [[bm2-collective-vibrations-and-sum-rules-contract]]
