---
type: source
title: "鞠国兴 2019 - 朗道《力学》解读"
aliases: [鞠国兴朗道力学, 朗道力学解读, Ju2019LandauMechanics]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "朗道《力学》解读"
authors: [鞠国兴]
publisher: "高等教育出版社 (北京)"
year: 2019
pages: "400"
isbn: "9787040510522"
citation_key: ju2019
canonical_source: "鞠国兴, 《朗道〈力学〉解读》, 高等教育出版社 (2019)"
library_file: "raw/books/朗道《力学》解读 (鞠国兴) (Z-Library).pdf"
raw_file: "raw/books/朗道《力学》解读 (鞠国兴) (Z-Library).pdf"
raw_sha256: "4886cb7585f26f41828e75e43d542d787d9202d3e0af41ce645c88bbff4a0d30"
nuclei: []
reactions: []
experiments: []
tags: [classical-mechanics, rigid-body-dynamics, euler-angles, inertia-tensor, asymmetric-top, routhian, poisson-brackets]
models: [rigid-rotor, euler-equations, routhian-formalism, canonical-transformations]
topics: [rigid-body-motion, euler-equations, asymmetric-top, routhian, poisson-brackets]
---

# 鞠国兴 2019 - 朗道《力学》解读

## Bibliographic Record

- **书名**：朗道《力学》解读
- **著者**：鞠国兴（南京大学物理学院）
- **出版信息**：高等教育出版社，2019 年 3 月第 1 版，ISBN 978-7-04-051052-2。
- **全书规模**：400 物理 PDF 页；正文印刷页 1–394。
- **本地原件**：
- **原件 SHA-256**：

## Scope and Reading Depth

本来源登记状态定为 。
本轮核验通过全书 7 章完整书签映射与正文推导核对，重点核读：
- **第六章 刚体的运动（PDF pp. 237–302 / 印刷 pp. 222–287）**：
  - §32 惯量张量（pp. 224–237）：主轴坐标系与惯量主值 , I_2, I_3$；
  - §35 欧拉角（pp. 243–255）：三维内禀系与实验室系欧拉旋转 $；
  - §36 欧拉方程（pp. 255–258）：欧拉运动学与动力学非线性方程组；
  - §37 非对称陀螺（pp. 258–267）：能量与角动量守恒椭球交线、Jacobi 椭圆函数 $\text{sn}(\tau), \text{cn}(\tau), \text{dn}(\tau)$ 解析解、绕中轴转动失稳与相空间分离线（Separatrix）。
- **第七章 正则方程（PDF pp. 303–394 / 印刷 pp. 288–379）**：
  - §40 哈密顿方程（pp. 288–294）；
  - §41 罗斯函数（Routhian, pp. 294–296）：循环坐标混合 Legendre 变换与转动坐标系 Routhian $R = H$ - \vec{\omega} \cdot \vec{I}$；
  - §42 泊松括号（pp. 296–305）：经典对易李代数与可积性；
  - §45 正则变换（pp. 314–325）；
  - §49 浸渐不变量（Adiabatic Invariants, pp. 348–355）。
- **配套方法合同**：[[landau-mechanics-rigid-body-and-routhian-contract]]。

## Summary

本书是南京大学鞠国兴教授对朗道经典《力学》（理论物理学教程第一卷）的权威详尽解读与推导拓展。全书系统解构了刚体运动、非对称陀螺解析解与相空间分岔，以及分析力学中的罗斯函数（Routhian）与正则变换理论，为理解原子核三轴转子模型（Davydov-Filippov）、推转壳模型（CSM）与 3D-TAC 提供了第一性原理的经典力学理论根基。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JU-1 | 非对称陀螺主轴转动稳定性定理：三个主惯量满足  < I_2 < I_3$ 时，绕最小惯量轴（1 轴）和最大惯量轴（3 轴）的转动是力学稳定的；绕中间惯量轴（2 轴）的转动是力学不稳定的。 | model-result | direct | 第六章 §37, 印刷 pp. 258–267 / PDF pp. 273–282 | false |
| JU-2 | 自由非对称陀螺相空间相轨迹与分离线（Separatrix）：能量椭球与角动量球面交截，在临界能量 E I_2 = M^2$ 处相轨迹退化为穿过中间轴鞍点的双渐近分离线，将相空间严格区隔为环绕短轴与长轴的两大闭合进动域。 | model-result | direct | 第六章 §37, 印刷 pp. 258–261 / PDF pp. 273–276 | false |
| JU-3 | 非对称刚体定点转动解析解：进动角速度分量严格由 Jacobi 椭圆函数 $\text{sn}(\tau, k), \text{cn}(\tau, k), \text{dn}(\tau, k)$ 解析参数化，确立了有限振幅进动非简谐波动的精确闭式解。 | method/formalism | direct | 第六章 §37, 印刷 pp. 258–264 / PDF pp. 273–279, 式 (37.1)–(37.5) | false |
| JU-4 | 罗斯函数（Routhian）与转动参照系动力学：对循环坐标执行部分动量 Legendre 变换导出 Routhian  = \sum p_c \dot{q}_c - L$；在绕转动轴 $\vec{\omega}$ 匀速旋转的非惯性系中， = H - \vec{\omega} \cdot \vec{I}$，微观形式奠定了推转壳模型（CSM）有效哈密顿量的经典基础。 | method/formalism | direct | 第七章 §41, 印刷 pp. 294–296 / PDF pp. 309–311, 式 (041.3)–(041.5) | false |
| JU-5 | 经典泊松括号（Poisson Brackets）与正则积分：泊松括号李代数 $\{f, g\}$ 在狄拉克对应原理下映射为量子力学对易子 0/(i\hbar)$，给出非对称刚体三维自旋动力学半经典映射与代数对角化的相空间规范。 | method/formalism | direct | 第七章 §42, 印刷 pp. 296–305 / PDF pp. 311–320, 式 (042.5) | false |

## Competing Interpretations and Limitations

刚体经典力学假设质量分布绝对刚性无形变且无量子涨落；微观原子核具有量子多体自旋 /2$ 费米子内禀结构、配对超流性以及离心拉伸软度，经典非对称陀螺周期轨道不能替代带有微观准粒子排布的粒子-转子模型（PRM）量子对角化。

## Extracted Pages

- 第六章 §32 & §35：PDF pp. 239–254，258–269，惯量张量、欧拉角与刚体动力学。
- 第六章 §37：PDF pp. 273–282，非对称陀螺椭圆函数解与相空间分离线。
- 第七章 §41 & §42：PDF pp. 309–320，罗斯函数推导、旋转系哈密顿量与泊松括号。

## Sources

- `raw/books/朗道《力学》解读 (鞠国兴) (Z-Library).pdf`
- [[landau-mechanics-rigid-body-and-routhian-contract]]
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]
- [[cranked-triaxial-shape-coexistence-pes]]
