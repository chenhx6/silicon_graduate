---
type: research-note
title: "三多极偏振的相位、有限乘积与各向同性角分布反例"
aliases: [three multipole polarization response, isotropic AD nonzero polarization]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: daily-learning-Day17-L3-design
evidence_sources: [vaillancourt-taras-1974-three-multipole-formulas]
promotion_target: ""
tags: [polarization, multipole-mixing, phase-convention, response, identifiability]
---

# 三多极偏振的相位、有限乘积与各向同性角分布反例

## Research Trigger

[[vaillancourt-taras-1974-three-multipole-formulas]] VT74-D17-1–14原8页/56主式/九pair表/一图本session完整核读。Eq32给AD到线偏振的逐多极替代，Eq52又明确ADisotropic仍可能有偏振。这决定physicalP能否由已测AD直接替代，也影响单仪器Q=A/P的参考可信度。

本页只保存原式的条件推导与独立重放。旧Day16finiteStokes/CGzero/phase已有priming，不称本session盲测或复用旧检查数授卡；新源合同、新输入和新exact双路线artifact另存。

## Grounded Evidence

- 原Eq1–6固定time-reversal/CondonShortley、RB initialleft/finalright及T/G/BM算符关系；Eq16/38的δ是signed T_L/√(2L+1)相对lowestamplitude，而非裸RME比或无符号强度比（VT74-D17-2/3）。
- Eq7–9起点是cylindrical环境、diagonalM布居；Eq21在definiteparity、不测circular时只evenK。不能把“general”扩大到任意coherent3Dρ（VT74-D17-4）。
- Eq26含CG比，Eq39含1+δ1²+δ2²及三干涉项；Eq52警告isotropicAD仍可能linearP（VT74-D17-5–8）。
- Eq42–45是完整unobservedγtrace，Eq53定义p为J0/J90、Eq56将其与count ratio桥接；没有本篇35Cl/37Ar新fit（VT74-D17-1/10/12）。

## Assumptions

固定原sourcephase、real multipoleamplitudes、definiteparity、axisymmetric positive diagonalρ和pointγ方向。直接振幅采用Eq9的h^π T_L CG D，T_L=√(2L+1)δ_L；线场按Eq22。只比较归一I与planeStokesS，不认证原FORTRAN/generalStokes/实际arrayresponse。所有δ和布居例是明示设计，不是实验拟合或任意核素的测量。

## Provisional Reasoning

### phase与归一先于替代

原RB的初态在左，Eq5的BM/G转换含√[(2L+1)(2Ji+1)/(4π)]且αmag=−iαelec。若改RME顺序、去掉算符因子或用别家nativeδ，需完整phase桥，不能只翻输出符号。三个分量以最低项为1时，δ1/δ2有共同基准；若该基准幅度为0，坐标本身奇异，应换reference或直接幅度，不定义一个假有限δ。

原normalized线分布和AD的K0项都为1：令W(θ,Ω)=I(θ)+S(θ)cos2Ω，则W0+W90=2I、boundedP=S/I。原normalization并非将半因子遗漏；同一物理计数若改分布整体常数，P不变，但绝对效率/response归一必须配套。

### 先保存有限的R乘K

令source Eq15除CG外的公共因子为

\[
F_K=(-1)^{1+J_i-J_f+L'-L-K}
\sqrt{(2J_i+1)(2L+1)(2L'+1)}\,
\mathcal W(J_iJ_iLL';KJ_f).
\]

这里𝒲是原Racah系数，不是发射角分布。则

\[
R_K=F_K\langle L1,L'{-1}|K0\rangle,
\qquad
R_K\mathcal K_K=-F_K\sqrt{\frac{(K-2)!}{(K+2)!}}
\langle L1,L'1|K2\rangle\quad(K\ge2).
\]

polarization还需原Eq32的(−1)^π′，π′属于**第二**多极。K<2没有q2项。不能先独立求无限/未定义𝒦，再以R=0删除整个项；R的零若来自CGq0，不必使有限polarized product为零。若零来自Racah/triangle，则应按完整乘积判断。

本sessionL≤6网格找出L3/L′5/K6及交换的CGq0=0、CGq2=−√22/11。在Ji3→Jf2，该R=0但R𝒦=√1155/1980。它出现在明示E3/M4/E5条件例，用来核通用recipe的实现边界，不是source中E1/M2/E3实际核data，更不是官方erratum或原publicproducer已修复。

### 各向同性I仍可强偏振

取Ji=3/2→Jf=1/2的M1/E2，ρ在M=±1/2各1/2，在±3/2为0，δ采用本source归一/相位。正定、对称布居但并非unorientedρ。最大evenrank仅2，独立原振幅和rank展开均给

\[
a_2=\frac{\delta^2-2\sqrt3\delta-1}{2(1+\delta^2)}.
\]

在δ=√3−2及√3+2，两根使a2=0，归一I(θ)=1，而

\[
P(\theta)=S(\theta)=\mp\frac{\sqrt3}{2}\sin^2\theta
\]

分别对应小负根、大正根，P90为−√3/2、+√3/2。两根的E2份额约.0669873/.9330127，不由相同AD挑一根。这里physicalP的非零来自不同multipole对I的抵消与对S的不同干涉；Eq52把未知B_K用aK除混合核替代时出现0/0，不能人为赋零。

它是源警告的正密度条件反例，不能推出任何实际isotropicAD都有此P，亦不把当前35Cl/37Ar或164Yb的Jπ/δ重赋。unorientedρ另有I1/S0控制，说明“isotropicI”不等“所有ρ必isotropic”。

### 双路线实际覆盖

`system/scripts/day17_vaillancourt1974_response.py`独立实现Eq14/15/26秩系数和Eq9/22直接helicity/Jones振幅，不导入旧Day16tensor/UC代码。声明三个case：M1/E2两分量、正布居E1/M2/E3，以及m0的E3/M4/E5 zeroCG。各在θ0/π6/π4/π3/π2 exactI/S交核；另全EMflip使I不变/S反、unoriented I1/S0和第三幅度0→两分量极限均过。allcases不是任意3D密度的证明，亦不认证实际几何核。合同/结果为本run `vaillancourt1974-response-contract.json` / `vaillancourt1974-response-result.json`。

### ratio不是boundedP

原Eq53 p=J0/J90，末段p′=(J0−J90)/(J0+J90)。Eq54全EM互换给p倒数，p′才反号；p>1合法。Eq55/56中N=N90/N0、R=σ90/σ0，有

\[
N=\frac{pR+1}{p+R},\quad
A=\frac{N-1}{N+1}=\frac{R-1}{R+1}\frac{p-1}{p+1}=QP.
\]

新symbolic桥精确通过。它独立确认历史文献中“偏振参数”可用强度比的明确例子，和[[ewan-1969-single-geli-polarimeter]] EW69-D17-11的精确可行ratio解释相容；但没有补上EW69的Ref9body或原作者意图，不能升级该归因。真实finitegeometry/a/背景及Q仍需matchingcalibration。

## Competing Explanations

isotropicAD也可来自unorientedρ、接受平滑或低统计；本页仅证明存在另一个已对称取向的幅度抵消机制。实际异常P还可能来自偏置/门/混线，不能用该例替代其核查。

## Transfer Conditions

同时分析AD/P需sameparent、phase、核布居与门。原MethodII要求particle detector沿symmetryaxis以共享tensor（VT74-D17-14）；“normallyunique”不等universality。Eq42–45的无干涉Uk需完整unobservedγtrace，finite门要显式接受operator/normalizer，totalICC/branch也不能未经匹配替γ权重。核finiteangleQk与仪器polarimeterQ分开。

## Failure Conditions

任意coherent3Dρ、complexphase、未说明RME桥、基准幅度为0、错误normalizer或finitegate取代完整trace均超出本页声明域。源ratio分母或I为零处须保定义域，不用无穷数当boundedP。

## Falsification or Reverse Tests

两根的I1/S非零已以两独立路线和五角exact交核；unoriented/EMflip/thirdzero控制已执行。若数据能独立测定布居/δ族或匹配P，可排本页条件族；仅aK=0不能排。actualcalibration/Σ未得时，不由本script给新实验置信度。

## Open Questions

原35Cl/37Ar是否有后续samegate三混合数据/response与phase清单；currentreference的finiteangle/feeding是否保相同tensor；哪些actualobs可排两根？本篇仅理论动机，没有新fit。当前不造数值δ实验或仪器Q。

## Human Review

Codex self-audit、provisional；新sourceclaim全部needs_review，旧flags保持，不新增human-reviewed。

## Knowledge Impact and Learning Decision

`supports`原任意多极recipe及p/计数/response字典；`limits`CG0删除偏振项、ADisotropic便P0、ratio>1便失败与多observable自动唯一的简写。没有新测量或collectivemode/strength裁决。

## Promotion or Rejection History

2026-10-20作为Day17原件新读/条件exactexercise固化；未晋升实际核素发现或认证历史代码。
