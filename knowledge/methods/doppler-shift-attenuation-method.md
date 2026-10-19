---
type: method
title: Doppler-shift attenuation method
aliases: [DSAM, Doppler-shifted attenuation method, Doppler-broadened line-shape analysis]
created: 2026-08-11
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
method_type: nuclear-lifetime-doppler-attenuation
tags: [lifetime, doppler-shift, stopping-power, side-feeding, lineshape]
---

# Doppler-Shift Attenuation Method

## Purpose

DSAM uses the attenuation of recoil Doppler shifts during slowing in target/backing material to constrain short excited-state lifetimes. Depending on the analysis, the measured observable is an angle-dependent centroid shift or the full Doppler-broadened γ-ray line shape. Forward and backward detector angles provide complementary velocity sensitivity.

## Inputs and Assumptions

- reaction kinematics, recoil velocity histories and detector geometry;
- stopping powers and material thickness/profile;
- transition placement, contaminant peaks and detector response;
- direct and side-feeding intensities, lifetimes or effective quadrupole moments;
- branching/mixing information for conversion from lifetime to `B(E2)` or `Q_t`.

## Analysis Chain

Singh 2016 uses LINESHAPE Monte Carlo histories at `0.002-ps` time steps and fits forward/backward gated spectra simultaneously. Ziegler and shell-corrected Northcliffe–Schilling stopping powers are treated as alternative prescriptions; central values are averaged and the larger uncertainty retained.

## What It Can Establish

- source-specific mean lifetimes or limits in the line-shape sensitivity window;
- side-feeding-sensitive `Q_t` after a rotational conversion;
- angle/stopping-prescription consistency and contaminant diagnostics.

## What It Cannot Establish Alone

- intrinsic γ softness/rigidity, microscopic configuration or nuclear chirality;
- a unique lifetime if side feeding, stopping or contaminant structure is underconstrained;
- partner-band electromagnetic equality from a single measured sequence;
- direct intrinsic `Q0` without rotational-geometry assumptions.

## Known Limitations

Thick targets broaden the production-depth/velocity distribution. Stopping powers, side-feeding cascades and long feeding times can dominate the systematic budget. A line that is fully shifted or shows no significant angle-dependent shape yields only a limit or complementary RDDS bracket.

[[wang-2023-experimental-studies-nuclear-chirality-china]] adds a review-level statistical caution: the common practice of varying one nuisance parameter at a time and adding lifetime shifts in quadrature does not represent correlations, asymmetric intervals or physical limits. 该二级入口的历史边界保留；现在原读的[[sun-2023-bayesian-dsam-31s]] SUN23-6–11核了actual2022v2 primary的priors、Gaussianlikelihood、GP/MCMC与quantile/6390限制。完整SI/实际input仍未得，不能把review赞词当完整precision认证。

[[bark-2024-investigations-nuclear-chirality-ithembalabs]] describes the AFRODITE use of forward/backward line shapes and COMPA/GAMMA/SHAPE Monte Carlo histories that include slowing, feeding and statistical/collective cascades. Its `106Ag` example is secondary to the original Lieder 2014 experiment and should not substitute for that source's fit/systematic details.

[[jensen-2001-165tm-h9-2-configuration]] provides a classic Nordball DSAM example: four angle-specific γγ matrices, Au/Pb backings, Monte Carlo recoil histories, Bateman side-feeding cascades and a fitted effective `Qs` are used to obtain `Qt` for `165Tm` bands. The reported `Qt` comparison is therefore tied to the stated stopping, feeding and rotational-model assumptions.

## 质心位移与恒定Qt提取：Riley2001

[[riley-2001-global-lifetime-a135]] RI01-1–5给出centroid-shift DSAM的直接例子，不只使用完整lineshape。其`F(τ)=[Eγ(θ)−E0]/[E0 β′cosθ]`中β′是mid-target recoil velocity；实际producer/数值未给，不能用束流能量代填。173 MeV 35Cl+105Pd、Au backing、97HPGe和Microball是采集条件。底部stopped门的前角31.7°/37.4°、后角142.6°/148.3°，moving double gates与90°谱、最高spin门是不同选择。

FITFTAU以带内恒定Qt拟合F曲线；默认`Qt(sf)=Qt(band)`，不等于τ相等。高spin上方门针对下方态侧馈，五个b注pair的Qt增加约8.3–12.1%；135Sm c注另用`τsf≈1.2τband`时序假设，不属于相同gate比较。不要把band-average Qt当每条transition独立测得τ（RI01-3/4/7/8）。

正文称阻停加侧馈可给absolute Qt附加15–20%系统误差，相对accuracy约5–10%；Table I caption称stopping-only 10–15%。作用范围及概率解释未统一，缺Σ时不将它们独立quadrature，也不把摘要“free from common systematics”当剩余误差为零。共同条件有助相对比较，不能直接推出所有点完全相关或各核素独立（RI01-5/9）。

### 原始重拟合的输入边界

进入真实L4需要逐ring/gate谱与centroid/calibration、事件交集和共同Σ、反应点/β′定义、靶厚与slowing histories、门污染/效率和feeding模型、E2/branch/geometry及FITFTAU版本/输入。现有表只能支持已发表参数的角色审计与条件敏感性；不能生成Pr136新τ、补原始CI或取代Laird2002最终版本。

## 同束靶的通道速度与可见带顶归一

[[petrache-1998-highly-deformed-lifetimes-131ce-nd]] PE98-16/17把粒子tag和v0输入放到实际证据链：GASP+ISIS的α veto/选择分开134Nd与131Ce近简并峰；Nd β0=.0202(2)，Ce α3n发射动量由MC修正为.0192(2)。共用束靶/backing不代表可以共用未经通道修正的速度，tag效率/污染仍需实际response。

保持同Ce平均发射速度却误借Nd β，按F定义归一会乘.950495（约−4.9505%）；这是条件敏感性，不是证明原作者用错值或给出τ/Q0偏差。原文带顶可见F<1还受thin-target已知而当前厚靶未见的更高跃迁和慢侧馈影响，不能无条件以观测最高点强制F=1校速度。其β值来自明确计算/MC并以高线shift交叉检查，不是由Ftop必须等1得到。

该文高门统计不够，最终对带内所有组合双门的sidefeeding effective intensity作选择修正，并用二维χ²拟合Q0/Qsf；缺实际grid/Σ不能复现误差或把单一/两段Q0的接受程度定量化。Band3表格alternative rows及Qsf文字范围歧义保留（PE98-5/6/11/18）。

## Sources

- [[riley-2001-global-lifetime-a135]] RI01-1–9/14：centroid shift、恒定Qt、门选/feeding、systematics与L4边界。

[[wadsworth-1977-61ni-levels]] is a historical `61Ni` DSAM example: centroid shifts at several beam energies are converted to attenuation factors/lifetimes with explicit stopping/feeding caveats.

- [[singh-2016-lifetime-131ce-133pr]]: explicit LINESHAPE/stopping/side-feeding audit for `131Ce`.
- [[li-2004-lifetimes-131ce]]: earlier `131Ce` DSAM lineage.
- [[petrache-1998-highly-deformed-lifetimes-131ce-nd]]: shared-systematics HD-band DSAM comparison.
- [[wang-2023-experimental-studies-nuclear-chirality-china]]: secondary review of DSAM uncertainty practice and pointer to correlated Bayesian/MCMC treatment.
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]: AFRODITE/COMPA-GAMMA-SHAPE overview and secondary `106Ag` line-shape counterexample.
- [[jensen-2001-165tm-h9-2-configuration]]: Nordball DSAM, `165Tm` `Qt`, side-feeding and stopping-systematics example.

## Related Methods

[[recoil-distance-doppler-shift]], [[doppler-correction]], [[transition-quadrupole-moment]].

## Evolution Log

- 2026-08-11: created from the Singh 2016 corpus on-touch audit with stopping and side-feeding boundaries explicit.
- 2026-08-11: added Wang 2023's correlated-uncertainty warning while retaining the un-ingested status of the cited Bayesian DSAM method.
- 2026-08-11: added Bark 2024's AFRODITE simulation-chain overview and original-source boundary.

- 2026-10-15：方法定义扩展为包含centroid shift；新增Riley2001的恒定Qt、门与误差预算，不改旧source/review状态。

[[lifetime-strength-audit-165tm-136nd]]按J01-6/7/8与MU08-15/16分开三步/五步feeding、5fs/2fs与两种stopping预算；fulltailbelowgate只控制一类selectionbias，不消sidefeeding。新11行/9行换算为条件审计，不是原谱重拟。

本次原件链：[[jensen-2001-165tm-h9-2-configuration]] J01-6–10与[[mukhopadhyay-2008-136nd-transition-rates]] MU08-15–17；实际逐角谱/response/Σ仍需匹配原producer。

## Bayesian DSAM的primary合同：31S

[[sun-2023-bayesian-dsam-31s]] SUN23-6–10：positivelifetimeprior、Eγ/bkg/sppriors和PCA/GP+Gaussianbinlikelihood是实际分析选择，restrictivenuisancepriors会强烈影响后验。τ–sp的负相关是原两long-lived态的报告，不裸迁给其它能区/体系。若emulatorΣ随参数变，完整Gaussian的normalizer也相关；原Eq3approx与actualtailoredcode需分开，未凭print判实验失败。

SUN23-11的6390态无finiteconstraint；20fs及Γ>33meV是条件应用链，不能当TableI第五项90%upperlimit。SUN23-12/13显示由总τ得到的B(M1)另含USDB E2partialrate扣除；它不是独立测得纯M1或δ。当前[[lifetime-strength-audit-165tm-136nd]]增加该链作方法对照，不修改两原实验数值或宣称L4原谱已重拟。

[[madai-2015-distribution-sampling-likelihood]] MDA15-2–8原样组件对variableΣ/normalizer、默认flag与ordinary/gradient-output两API作条件反例；fixedΣ是必要反证。它不认证[[sun-2023-bayesian-dsam-31s]] actualtailoredcode或原CI失效；需papercommit/config/实际response与数据。

SUN23-17–22的publisherSI已原读：见[[sun-2023-bayesian-dsam-31s]]。它补target/DAQ/逐态αgates与posterior图，不给actualGP/config/draws；Fig13不是额外90%limit表，图轴也不自动给priorhardcut。1/2+态的A2需先核其物理对象/帧，不能直接叫已测alignment。
