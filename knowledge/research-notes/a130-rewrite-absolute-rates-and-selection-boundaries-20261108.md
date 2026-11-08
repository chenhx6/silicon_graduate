---
type: research-note
title: "A130重写研学：选择定则允许性、退激率归一与磁单位"
aliases: [A130 absolute rates and selection boundaries]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G65样节原件回读、独立算例复算与总控修订"
promotion_target: ""
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, lange-kumar-hamilton-1982-multipole-admixtures, campaign-g07-gorgen-2004-163lu-quadrupole-moments]
tags: [A130, doctoral-thesis, electromagnetic-rates, internal-conversion, selection-rules, covariance]
---

# 最低允许多极、观测分支与总退激流是三个不同问题

## Research Trigger

5.9初稿的教学支路把4⁺→2⁺设为M1+E2，违反角动量三角条件。
修成4⁺→3⁺后，仍须避免把“允许”写成“必有”，或把M1禁戒写成纯E2定理。
本页保存可复用推理与实际原件，不以writer回执自评作证据。

## Grounded Evidence

- [[book-suhonen-from-nucleons-to-nucleus]]：总控本轮回PDF133–136/印刷118–121，
  Eqs.(6.1)–(6.18)，含率、B、算符、单位与最低多极的限定。
- [[lange-kumar-hamilton-1982-multipole-admixtures]]：PDF3–4/印刷121–122，
  Eqs.(2.1)–(2.6)及后续角分布约定，混合比平方定义、相位和光子波数。
- [[campaign-g07-gorgen-2004-163lu-quadrupole-moments]]：PDF2–3/Tables I–II；
  总控本轮重新核该范围，15个带内寿命与5条带间强度的采用输入分别记录。

## Provisional Reasoning

### 允许性不等于分量的存在或纯度

辐射多极有L≥1，并满足|Iᵢ−I𝒻|≤L≤Iᵢ+I𝒻及相应宇称条件。
4⁺→2⁺禁止L=1，允许E2，也允许更高的M3、E4等；纯E2须额外声明忽略高多极。
4⁺→3⁺允许M1和E2，并不强迫二者矩阵元都非零。
同理，ΔI=0、同宇称也不自动保证M1+E2均允许，须检查上界与0→0辐射禁戒。
Suhonen印刷121明确其分类只列最低多极，并用2⁺→2⁺说明还可含E2、M3、E4。

### 光子分支的定义必须带归一对象

令总退激率λₜ=1/τ，通道k的光子率为λγ,k，电子率为αₖλγ,k，
则总分支bₖ=(1+αₖ)λγ,k/λₜ，光子对全部退激的分支bγ,k=λγ,k/λₜ。
即使总分支闭合，Σbγ一般也不等于1。
效率/接受度修正后的相对光子强度aₖ仅给λγ,k的相对比例。
已知通道闭合且无另外的非光子通道时，

$$
\lambda_{\gamma,k}=\frac{a_k}{\tau\sum_j a_j(1+\alpha_j)}.
$$

实δ的混合支路有fE2=δ²/(1+δ²)、
αmix=[αM1+δ²αE2]/(1+δ²)。
若有未计入的正退激流，强行只对已知a归一会高估其率；
E0无相应单光子支路，不能假装给其一个普通αE0乘上光子率解决漏项。
实核还须考虑内对产生等实际开放通道，本教学控制只取低能IC与光子。

### 率常数和磁单位必须一起重建

Suhonen Eq.(6.14)印出的圆数给
CE2=5.498×10²²/(150×197.33⁵)=1.2250333078×10⁹，
E以MeV、B以e²fm⁴计时λγ=CE2 E⁵ B，单位s⁻¹。
这是教材圆数重建，尾数不代表新的物理精度；不能一面换成另一套常数，
一面保留旧算例的全部尾数。
该书采用SI核磁子μN=eℏ/(2mₚ)，磁算符含μN/c，
其B(M1)以(μN/c)²计；Eq.(6.14)给CM1=1.7583758801×10¹³。
书中脚注说明高斯磁子定义含c，不能把SI单位的c凭空删掉而不映射。

声明τ=5ps、a=(100,25)、δ₁=1.5、Eγ=(0.8,0.5)MeV，
α₁(M1,E2)=(0.003,0.0015)、α₂(E2)=0.005，
忽略高多极且无其它通道时，复算得BE2=(275.2371,1042.1919)e²fm⁴、
BM1₁=0.00545432教材磁单位，E2比约0.26409。
这些是虚拟教学输入，不是核素数据；显示数字可圆整，不附实测误差。

### 163Lu的数据链并非全由同一谱直接测得

Görgen Table I列TSD1八个、TSD2七个寿命。
PDF3说明TSD2竞争带出修正采用Jensen2002薄靶分支；
Table II带间E2/M1拆分采用先前角关联和偏振给出的平均
δ=−3.10⁺⁰·³⁶₋₀·⁴⁴，作者把不显著变化至I=51/2的值用于更高自旋。
PDF2说明寿命误差包含拟合协方差及角度组合分散，未含阻止本领选择系统误差。
Qt还使用假定纯i13/2顺排的K权重，不能当与构型无关的几何直接测量。
作者的两带Qt相近和约4%差异解释限定在其摆动图像及倾角估计中；
不能从“作者称其必要”推广成所有摆动模型的普遍数值认证门。

## Assumptions

教学算例是两支路、给定δ/IC、单指数平均寿命。
真实分析须另核feeding、峰/效率、gate、漏支、电子过程与联合不确定度。

## Competing Explanations

B只约束约化矩阵元模平方；相同Qt可与多个具体结构模型相容。
同母态比值精确消去共同τ，但不自动消去效率、δ或峰拟合误差。
不同母态的阻止本领系统误差是否部分抵消，取决于各自速度/时间窗口的灵敏度。

## Transfer Conditions

按核/态、跃迁方向、算符和磁单位映射后，率代数可跨区复用。
相位变更同时作用于相应辐射/几何系数，不能只翻δ符号保其余定义不变。

## Failure Conditions

由M1禁戒推出严格纯E2、重复乘ℏ/ln2、把半衰期当平均寿命、
混用教材/其它常数或统计后验与似然剖面，均可产生看似精确的错误。

## Falsification or Reverse Tests

[`a130_rewrite_branch_rate_audit.py`](../../system/scripts/a130_rewrite_branch_rate_audit.py)
重建上述教学输入，检查三角条件、高多极仍允许、概率闭合、率重建和共同寿命消去。
实际运行及producer/原件/产物哈希保存在对应L4目录；
检查不构成真实寿命拟合或整节科学认可。

## Open Questions

实际新核素的绝对强度还需本核的完整分支、响应与Cov；
不能由本教学算例或163Lu的采用输入补齐。

## Human Review

总控原件/算术核查，无新增用户人工审核事件。

## Promotion or Rejection History

- 2026-11-08：保存5.9修订中发现的选择规则、归一、率常数与来源依赖边界。
