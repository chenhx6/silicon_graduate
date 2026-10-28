---
type: research-note
title: "同核多重磁转动带共存：Pb、141Eu与139Sm的组态分支、交叉和混合"
aliases: [multi-band shears coexistence, Pb 141Eu 139Sm multiple MR bands]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, agarwal-2007-137pr-magnetic-rotation-bandcrossing, podsvirova-2004-141eu-dipole-lifetimes]
created_from: Day26 independent multi-band MR coexistence audit
promotion_target: magnetic-rotation
tags: [magnetic-rotation, shears, multi-band, band-crossing, configuration-mixing, 198Pb, 199Pb, 139Sm, 141Eu]
external_source_records: [brandolini-1996-139sm-plb388-468, podsvirova-2004-141eu-epja, marcinkowska-2003-141eu-acta]
---

# 同核多重磁转动带共存：Pb、141Eu与139Sm的组态分支、交叉和混合

## Research Trigger

多条同核 $\Delta I=1$ M1带并不是同一剪刀轨迹的复制；它们可以对应不同质子粒子/空穴组态、不同中子空穴排布、不同有效叶片长度与不同 $V_2$。本笔记把“多带共存”“带间混合”“同一带内配置交叉”分开，并标出139Sm与141Eu证据强度的差异。

## Grounded Evidence

| 区域/核 | 直接来源事实 | 证据定位与边界 |
|---|---|---|
| $^{198}$Pb | Clark 2000说明198Pb已发现5条M1带，其中198Pb(1)/(3)有寿命曲线；Clark Fig.5列出不同配置标签并比较B(M1)随跃迁能量变化 | [[clark-2000-shears-mechanism]] pp.5,11–12,17；综述图示，不是本轮重新提取逐带原始表 |
| $^{199}$Pb | Hübel 2005给Band2配置 $\nu(i_{13/2}^{-2}f_{5/2})\otimes\pi(h_{9/2}i_{13/2})$（ABE11），带头质子叶片11、中子叶片29/2，约35/2；旧配置终止后再破一对i13/2中子，形成新带并重新张开 | [[hubel-2005-magnetic-rotation-review]] pp.49–51；配置交叉与重开是综述转引的模型/实验综合 |
| $^{141}$Eu | Podsvirova 2004原件测量DB1、DB2两条偶极带，各含三个DSAM寿命；TAC分别假设 $\pi h_{11/2}\otimes\nu h_{11/2}^{-2}$ 与 $\pi h_{11/2}\otimes\nu h_{11/2}^{-4}$ | [[podsvirova-2004-141eu-dipole-lifetimes]] pp.2–5, Table1/Figs1–4；两带是原件事实，组态是模型假设 |
| $^{141}$Eu交叉解释 | 原件以逆向初始排列、在 $I_{\rm tr}=18.7\hbar$ 处增强核芯集体性的SPAC方案较好描述背弯；作者试过带混合方案，但其描述较差 | [[podsvirova-2004-141eu-dipole-lifetimes]] pp.4–5；不能把一般两态混合模型宣称为本核已测机制 |
| $^{141}$Eu统计 | DB2的 $B(M1)$ 中心值依次为 $0.77,1.32,0.50\ \mu_N^2$，区间宽且重叠；Table1为非线性Monte Carlo众数/68%区间，单独众数相除不必等于强度比众数 | [[podsvirova-2004-141eu-dipole-lifetimes]] pp.2,4；不从非单调中心值单独断言剪刀重开 |
| $^{139}$Sm | Brandolini等1996用DSAM测量3325-keV、25/2−带头的负宇称规则偶极带；337、409、473-keV线寿命为0.60(21)、0.40(14)、0.25(8) ps，提取B(M1)、B(E2)与TAC相容 | 外部登记页、DOI 10.1016/S0370-2693(96)01202-6；本轮未获得全文原件，不能扩展为139Sm多条独立剪刀带共存证据 |
| 综述范围 | Hübel Fig.10给Pb区多带数量：198Pb为5(3)、199Pb为5(3)；Clark汇编191–202Pb和198–203Bi大量M1带 | [[hubel-2005-magnetic-rotation-review]] p.13；括号为连接低能级带数，不能当独立构型数 |

139Sm目前仅有单条寿命带的摘要级记录，保留为控制案例；141Eu已取得两条偶极带的六页原件。此前“3条带”的概括没有在本原件得到确认，已撤回；p.4的三个初始排列分支属于模型可能性。139Sm没有全文，不能写成已完成逐态原件核验，更不能扩写为多带共存。

## Provisional Reasoning

### 1. 不同组态如何产生不同带头和剪刀轨迹

为每个构型 $a$ 定义有效叶片 $j_{p,a},j_{n,a}$，无芯近似带头为

$$I_{0,a}^{\rm cl}\simeq\sqrt{j_{p,a}^2+j_{n,a}^2},$$

有限-$j$量子版本用 $I(I+1)$替代平方。若同一核中破开/填充不同高-$j$粒子或空穴对，$j_{p,a}$、$j_{n,a}$和带头自旋就改变。其角度轨迹为

$$\cos\theta_a(I)=\frac{I^2-j_{p,a}^2-j_{n,a}^2}{2j_{p,a}j_{n,a}},$$

但这是无芯近似；含核芯时严格使用矢量 $\mathbf I=\mathbf J_{\rm shears}+\mathbf R_{\rm core}$；只有二者共线才可写标量 $I=I_{\rm shears}+R_{\rm core}$。SPAC允许非共线核芯耦合，每个构型的 $R_{\rm core}$和惯量也不同。

若用有效粒子–空穴势

$$V_a(\theta)=V_{0,a}+V_{2,a}P_2(\cos\theta),$$

则不同$V_{2,a}$改变相同角度下的能量曲率和跃迁能量步长。在核芯与剪刀合矢量共线的额外假设下，条件能量是

$$E_a(I,\theta)=\frac{[I-J_{s,a}(\theta)]^2}{2\mathcal J_{c,a}}+V_a(\theta)+E_{\rm qp,a},$$

其中 $J_{s,a}=|\mathbf j_{p,a}+\mathbf j_{n,a}|$。$E_{\rm qp,a}$、配对和形变决定哪个构型在给定$I$最低，不能只从$V_2$比较。

### 2. 同核多带：交叉、混合和跃迁

对同宇称、同自旋的两个构型$a,b$，最小混合矩阵为

$$H_I=\begin{pmatrix}E_a(I)&W_I\\W_I^*&E_b(I)\end{pmatrix},
\qquad E_{\pm}=\frac{E_a+E_b}{2}\pm\sqrt{\frac{(E_a-E_b)^2}{4}+|W_I|^2}.$$

裸交叉条件为 $E_a(I_c)=E_b(I_c)$；若 $W_I\ne0$，实验能级出现最小间隔 $2|W_I|$，混合角满足

$$\tan2\alpha_I=\frac{2W_I}{E_a(I)-E_b(I)}.$$

因此“带间能量接近”只能说明可能存在混合；要量化$W_I$，需要同自旋能级的两侧能量和足够明确的带身份。不同配置若有不同宇称、signature或选择定则，则可以近似真正交叉，不必出现明显排斥。

跃迁矩阵元不是简单地把两条纯带强度相加：

$$M_{fi}=\sum_{x,y=\{a,b\}}C_{f,x}^*(I_f)C_{i,y}(I_i)M_{fi}^{xy}.$$

带间crossover/链接强度可由混合系数与跨配置核共同产生；一个弱链接不能自动等于零混合，一个强链接也可能来自算符本身的跨配置矩阵元。必须把M1、E2、偏振、内转换和相位约定放在同一响应模型中。

### 3. Pb区：多带是配置扇出，不是单一连续轨道

Pb区高-$j$质子配置常以11或8等有效对齐自旋标记，中子由i13/2空穴A、B、C、D及自然宇称E/F排布形成不同叶片。Clark Fig.5对198Pb(1)/(3)以及邻近Pb带给出不同配置标签，Hübel的199Pb例子则显示旧ABE11带终止后新增i13/2中子对，产生新带头和重开。由此可见：

1. 不同中子空穴数改变 $j_n$，所以改变 $I_0$、$\theta(I)$和终止自旋；
2. 不同质子激发改变 $j_p$及有效$g$差，因而改变B(M1)尺度；
3. 每条带可有自己的$V_2$和核心贡献，不能用一条全核通用势拟合所有带；
4. 198/199Pb的寿命数据支持多带中B(M1)随各自剪刀闭合下降，但交叉后新配置会再次增大，不构成所有带的单调定理。

### 4. 141Eu与139Sm：A≈140的多带与单带控制

141Eu原件中的DB1与DB2提供两带比较：其TAC方案分别增加一对中子 $h_{11/2}$ 空穴，并采用不同四极形变。作者同时用逆向剪刀初始排列与自旋依赖核芯集体性解释背弯；原件明确指出所试带混合方案效果较差。因此配置分支、集体性改变和微观混合应作为不同层次的解释比较；两条偶极带的存在不决定两态混合模型正确。早先基于外部摘要的“三条偶极级联”与质子交叉频率记录没有在本六页原件中得到对应，撤出本笔记的定量证据链。

139Sm的DSAM寿命是绝对强度方法的控制例：三个线的寿命随能量变化，所得B(M1)、B(E2)与TAC在允许三轴平衡形状的前提下相容。由于本轮未取得139Sm全文和完整表，不能从摘要恢复逐态混合或带间交叉，也不能把其单带直接当141Eu多带的数值模板。

## Assumptions

组态标签、叶片长度和$V_2$被视为每条带的有效参数；混合矩阵只示范同$I^\pi$构型交叉。$B(M1)$和$B(E2)$需由绝对寿命、分支、内转换和混合比获得，不能用相对强度替代。

## Competing Explanations

多条偶极带可来自不同准粒子组态、signature partner、普通形变转动、形状共存或同一带的配置交叉。大B(M1)/B(E2)支持MR候选，但不排除三轴核心或混合；能级排斥需要同$I^\pi$身份和间隔证据。

## Transfer Conditions

跨Pb和A≈140比较时必须统一自旋、宇称、叶片定义、核心惯量、$V_2$、有效g因子和寿命处理。综述图、摘要和同实验不同论文不能重复计为独立数据。

## Failure Conditions

把198/199Pb多带数直接当多组态精确计数；把141Eu模型的三个初始排列分支当成三条实测寿命带；把139Sm一条DSAM带写成多带共存；把带间链接强度直接换算成混合矩阵元，均超出原件。

## Falsification or Reverse Tests

对每条带分别拟合$E(I)$、$B(M1)$和$B(E2)$，再用同一探测响应联合拟合近交叉区的两带能级和链接强度。若一个$V_2$与固定叶片无法同时描述带头、能量曲率和M1/E2趋势，应引入构型依赖或混合，而非调整一个全局参数。

## Open Questions

198Pb每条已知带的完整构型、带头和混合矩阵仍需回到Refs.36/37原件；199Pb不同带链接与W_I尚未逐态提取；141Eu 2004 Table1和Fig1已归档，但没有完整协方差/联合似然及所试带混合参数，不应自行反演确定的W；139Sm全文及配置符号仍缺少本地归档。

## Human Review

Codex定向来源/外部登记检索和模型推导，页面保持 `review_status: unreviewed`，未获得人工逐项审核。

## Promotion or Rejection History

2026-10-29：建立多带剪刀共存边界。`supports` [[clark-2000-shears-mechanism]]、[[hubel-2005-magnetic-rotation-review]] 的Pb多带与配置交叉；补入139Sm外部记录并保留全文缺口；随后取得141Eu六页原件，修正为两条各含三个寿命的实测偶极带；`limits`把摘要、综述和多带标签升级成逐带混合/绝对强度认证。


## 本轮原件补齐与合成模型工件

已获取并读取 [[podsvirova-2004-141eu-dipole-lifetimes]] 六页原件，PDF签名、页数与SHA-256见来源页。其DB1的31/2−态 $B(E2)=0.041^{+0.023}_{-0.009}$、DB2的43/2−态 $0.064^{+0.041}_{-0.020}$ e²b²；原表E2列的 $10^{-2}$ 单位必须显式处理。DB2在37/2−处的大比值 $299^{+178}_{-54}$ 不附绝对寿命，不能解释成绝对M1强度已骤升。

可运行工件 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/multi-band-shears/multi-band-shears-mixing-model.py` 用两组**人为选择**的叶片、V2和 $W=0.040$ MeV演示避免交叉：裸交叉 $I_c=24.5$ 处能隙为0.080 MeV。它输出能谱、混合组分、开角以及M1/E2矩阵元，不是Pb、Eu或Sm拟合，也不从原件反演W或V2。

模型将初态与末态分别对角化，再执行 $M_{fi}=U_f^\dagger M^{(0)}U_i$。假设裸核为实数对角且同号，跨组态核置零；改变裸核相对符号或加入跨组态核，会改变带间强度及干涉。对完备的两维初末态空间，所有支路强度之和保持，因为Frobenius范数在酉变换下不变；实验若遗漏带、支路或态，这个完整性条件就不成立。
