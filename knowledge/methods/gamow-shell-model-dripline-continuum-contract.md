---
type: method
title: "Gamow Shell Model：滴线连续谱、共振和开放量子系统合同"
aliases: [GSM dripline contract, Berggren shell model, continuum-coupled shell model]
method_type: "open-quantum-system-shell-model"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 5, article pp.139-160 / physical PDF pp.150-171 selected sections"
confidence: "high for reviewed formalism and oxygen/fluorine examples; conditional for specific numerical predictions"
tags: [gamow-shell-model, berggren-basis, dripline, halo, continuum, oxygen, fluorine, calcium]
sources: [book-nuclear-shell-model-70-years]
---

# Gamow Shell Model：滴线连续谱、共振和开放量子系统合同

## Purpose

把传统离散壳模型扩展到滴线附近的开放量子系统，连接：

```text
Berggren 基底 -> 束缚态/共振态/散射连续谱
              -> 复能本征值 E - iΓ/2
              -> 分离能、宽度、晕核和滴线
```

## Inputs and Assumptions

- 核芯 + 价核子模型仍需要明确惰性核芯和价空间；
- 单粒子基底使用 Berggren completeness，把束缚态、离散共振和复动量积分路径
  上的散射态放在同一完备关系中；
- 复能本征值写成
  \[
  E=E_R-\frac{i}{2}\Gamma,
  \]
  其中 \(\Gamma\) 是共振宽度；
- 非厄米复对称哈密顿量的本征矢和矩阵元需要采用相应的双正交/复内积约定；
- 长程动能和 Coulomb 项不能简单用短程 HO 重叠处理，文章采用外部复标度等技术；
- 连续谱截断、积分路径、有效相互作用和核芯选择都会影响数值结果。

## What It Can Establish

### Continuum-coupled formalism

文章的 GSM 形式允许同一模型同时描述：

- 稳定束缚态；
- 窄或宽的单粒子/多体共振；
- 散射连续谱；
- 由 \(E_R\) 和 \(\Gamma\) 共同决定的近滴线结构。

这比只含离散壳模型基底的计算更适合处理 \(S_n\) 很小、共振宽度可见、
两中子发射和晕核关联的体系。

### Oxygen and fluorine examples

文章用中子丰富氧、氟同位素作为连续谱实验室：

- \(^{24}\mathrm O\) 作为接近双幻数的束缚体系；
- \(^{25}\mathrm O\)、\(^{26}\mathrm O\) 的不稳定/共振性质；
- 氟链可比氧链延伸到更多中子，体现 oxygen anomaly；
- GSM 计算可同时比较能级、\(S_n\)、共振位置和宽度；
- 只使用 Woods–Saxon 单粒子能量时，缺少三体力可能导致 \(^{24}\mathrm O\) 之后过度束缚；
- 用实验单粒子能量或自洽 GHF Berggren 基底会改变滴线预测。

这些实例说明：滴线判定不能只看一个平均场轨道是否“越过零点”，而要把多体
结合能、连续谱耦合、共振宽度和三体力一起检查。

### Halo and reaction interface

开放量子系统壳模型可以为晕核和滴线反应提供结构输入，包括：

- 弱束缚轨道的长程尾部；
- 核子去除/敲除反应的谱因子和动量分布；
- 低能共振和非束缚态的宽度；
- 两中子发射、反应截面和连续谱耦合。

实验分析时，能级峰的位置和宽度必须与探测器分辨率、阈值、反应线形和本底模型
分开记录。

### Calcium and proton-emission cases

文章还讨论了中子丰富 Ca 链的 \(S_{2n}\) 和双中子滴线、\(^{57}\mathrm{Ca}\)
的束缚边界，以及 \(^{16}\mathrm{Ne}\)、\(^{18}\mathrm{Mg}\) 的一质子/二质子
发射宽度。模型显示当一质子通道打开时总宽度会快速改变，而二质子宽度可在
特定输入下约为 \(10\)–\(15\) keV。

这些例子表明，开放通道不仅影响束缚/不束缚判定，也直接决定可观测共振线宽。
一质子和二质子衰变必须在反应或衰变响应中分开建模，不能把总宽度直接当成
单一通道宽度。

## What It Cannot Establish Alone

- 复能本征值不是直接实验峰位，必须经过反应响应和分辨率卷积比较；
- Gamow 基底的共振宽度不能单独等同于实验半衰宽度，通道和观测算符也很重要；
- GSM 与传统壳模型的差异不能单独归因于连续谱，三体力、单粒子输入和模型空间
  也可能产生同样变化；
- \(S_n\) 或 \(S_{2n}\) 的一个趋势不能单独确认晕核；
- 滴线附近的质量、反应和共振数据必须保留实验上限、未束缚判定和模型协方差。

## Evidence and Locators

- article pp.139–143 / physical PDF pp.150–154：Berggren 基底、复能和有效哈密顿量；
- article pp.144–147 / physical PDF pp.155–158：氧/氟滴线、\(^{24-26}\mathrm O\)
  能级、分离能和三体力边界；
- article pp.147–160 / physical PDF pp.158–171：GHF 基底、Ca/Ne/Si、halo、
  一/二质子衰变和方法比较。

本轮完成文章前半部和氧/氟核心示例的有界核读，文章后续核素与完整公式仍需继续。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[drip-line-physics-and-frib-science]]
- [[halo-nuclei-borromean-systems-and-breakup-dynamics]]
- [[heavy-ion-abrasion-ablation-fragmentation]]
