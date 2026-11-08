---
type: research-note
title: "A130配对研学：相同BCS记号背后的不同哈密顿量、自能与曲率"
aliases: [A130 BCS conventions and model Hamiltonians]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "冻结G67-v1、Terra T10原件核查及总控独立重放"
promotion_target: ""
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, hinohara-2015-nambu-goldstone-inertia-response]
tags: [A130, BCS, pairing, self-energy, gauge-rotation, model-comparison]
---

# 原书中的公式正确，不保证可以接到另一种相互作用后面

## Research Trigger

2.3初稿把正确的BCS占据公式、相位不相容的本征矩阵，以及另一模型的自能和临界强度拼在一起。
本页保存明确模型后的更正。冻结稿只用于定位错误，不是正确核物理的证据。

## Grounded Evidence

| 原件 | 精确范围 | 用途 |
|---|---|---|
| [[book-suhonen-from-nucleons-to-nucleus]] | 印刷399–404、408–411；PDF412–417、421–424；Eqs.(13.40)–(13.65),(13.103)–(13.124) | 变分、相位、原书两壳矩阵元及自能 |
| [[hinohara-2015-nambu-goldstone-inertia-response]] | APS PDF5 Eqs.(49)–(53)、8–9 Eqs.(66)–(67)与Fig.4图注 | 局域规范坐标、总能/束缚能记法和响应定义 |

T10定向读以上页。总控另核模型代数并执行16维pair占据空间控制，结果与T10一致。
本地Suhonen PDF在该处页序不连续：印刷408–411也在PDF396–399重复出现，
PDF402–403为印刷414–415，PDF404又回到印刷391。不能按全书固定偏移造locator。
Hinohara身份/原件以R2的APS主底本为准，不混预印本。

## Provisional Reasoning

### 1. 先固定能量的正负号

令正束缚能为 \(B_+>0\)、内部总能为 \(E=-B_+\)。
一种三点奇偶差分约定是

$$
\Delta_B^{(3)}(N)=\frac{(-1)^{N+1}}2
[B_+(N-1)-2B_+(N)+B_+(N+1)].
$$

以N−1和N为中心的两项平均给四点约定

$$
\Delta_B^{(4)}(N)=\frac{\Delta_B^{(3)}(N-1)+\Delta_B^{(3)}(N)}2
=\frac{(-1)^N}4[B_+(N-2)-3B_+(N-1)+3B_+(N)-B_+(N+1)].
$$

这是约定和任务代数，不冒引为Suhonen同名原式。取正交错项
\(B_+=B_{\rm sm}+p(-1)^N\)，两式均给+2p；
初稿三点因子用 \((-1)^N\)，会给−2p，和其四点式冲突。
若用E，符号应相应变换；平滑背景、壳结构和重排仍可污染指标，不保证所有核素正值。
经验奇偶差也不是某个哈密顿量的纯能隙参数。

### 2. 固定时间反演pair不等于已投影的J=0态

在球形单j壳层，以有序费米产生算符表示的归一化集体pair为

$$
|j^2;00\rangle=\frac1{\sqrt{2(2j+1)}}\sum_{m=-j}^j
(-1)^{j-m}c^\dagger_{jm}c^\dagger_{j,-m}|0\rangle
=\frac1{\sqrt{\Omega}}\sum_{m>0}(-1)^{j-m}
c^\dagger_{jm}c^\dagger_{j,-m}|0\rangle,\quad \Omega=\frac{2j+1}2.
$$

单个固定m的时间反演pair通常只是M=0，仍可含多个J。
不能混用有序直积、归一Slater态和已经反对称化耦合态的根号二。
变形轨道通常也没有好J；时间反演配对本身不是角动量投影。

### 3. 同一BCS相位必须贯穿真空、危险项和本征矢

取实数 \(u_k,v_k\)，每对规定 \(u_k^2+v_k^2=1\)，
\(|\Phi\rangle=\prod_{k>0}(u_k+v_kP_k^\dagger)|0\rangle\)，
\(P_k^\dagger=c_k^\dagger c_{\bar k}^\dagger\)。
对明确的pair-only哈密顿量

$$
H=\sum_{k>0}\epsilon_k(n_k+n_{\bar k})
-\sum_{k,l>0}G_{kl}P_k^\dagger P_l,\qquad H'=H-\lambda N,
$$

保留k=l项，Wick收缩给
\(\mu_k=G_{kk}v_k^2,\ \xi_k=\epsilon_k-\lambda-\mu_k\)，
\(\Delta_k=\sum_lG_{kl}u_lv_l\)。
初稿所用准粒子变换和真空相容，危险项系数为
\(2\xi_ku_kv_k-\Delta_k(u_k^2-v_k^2)\)。
与正 \(u_kv_k=\Delta_k/(2E_k)\) 相容的矩阵是

$$
\begin{pmatrix}\xi_k&+\Delta_k\\+\Delta_k&-\xi_k\end{pmatrix}
\binom{u_k}{v_k}=E_k\binom{u_k}{v_k},\qquad
E_k=\sqrt{\xi_k^2+\Delta_k^2}.
$$

若保留负非对角，须改用 \((u_k,-v_k)\) 等一致Nambu基底。
只改一处符号不能构成相位约定。自能也不能在后面某个分母中无声明消失。
逐对归一是所选规范，不由“归一因子乘积为1”单独推出。
\(H_{20}=0\)是驻点条件，极小还须检查受约束二阶变分和竞争分支。

### 4. 三个两壳临界强度，各有自己的条件

两壳单粒子能为±ε/2，每壳Ω对轨道，平均粒子数2Ω。
在非零配对、镜像对称支上，各方案给：

| 相互作用/自能合同 | 化学势 | 临界强度 |
|---|---|---|
| 上述pair-only，保留 \(\mu_i=Gv_i^2\) | −G/2 | ε/(2Ω−1) |
| Suhonen §13.5.2，任意壳标签a,b,c,d的耦合J=0矩阵元均为−ΩG | −3G/4 | 2ε/(4Ω−1) |
| 明确忽略全部自能的常G近似 | 0 | ε/(2Ω) |

第二行是原书的模型结果，其自能为
\(\mu_1=G(v_1^2+v_2^2/2)\)、\(\mu_2=G(v_1^2/2+v_2^2)\)，
含额外跨壳贡献，不能拼到第一行的H后面。
第一行是本任务对所写H的独立推导，令 \(t=v_1^2-v_2^2\)：

$$
\langle H\rangle=-\Omega\epsilon t
-G\left[\Omega+\frac{(4\Omega^2-2\Omega)(1-t^2)}4\right],\quad
t_*=\frac{\epsilon}{G(2\Omega-1)}.
$$

在 \(0<t_*<1\) 支上，
\(E_{\rm qp}=\Omega G\)、
\(|\xi|=\Omega\epsilon/(2\Omega-1)\)、
\(\Delta=\Omega G\sqrt{1-t_*^2}\)。
该受限路径曲率为 \(G\Omega(2\Omega-1)>0\)，不证明全变分空间的全局极小。
塌缩区粒子数平台上的λ也不必唯一。

### 5. 粒子数、曲率和相角必须使用相同单位与路径

N和单粒子规范角θ均无量纲，角表示中共轭生成元是−i∂θ，
不是−iℏ∂θ；若用pair相角，二倍相位、周期和共轭数都要映射。
QRPA局域共轭坐标也不是有限体系全空间中的严格全局自伴相角。

固定N态中 \(\langle c_{\bar k}c_k\rangle=0\)，
而 \(\langle P_k^\dagger P_l\rangle\) 或两粒子转移矩阵元可非零。
因此配对关联不要求态内反常密度非零；投影后的好N试探态也不自动成为精确能量本征态。

与 \(H-\lambda N\) 一致的局部展开为

$$
E(N)=E_0+\lambda\delta N+\frac{(\delta N)^2}{2\mathcal J}+\cdots,\quad
B_+(N)=B_{+,0}-\lambda\delta N-\frac{(\delta N)^2}{2\mathcal J}+\cdots.
$$

在指定平滑自洽态族、固定其它粒子数及非奇异响应的条件下，
\(\mathcal J=\partial N/\partial\lambda=-S(N,0)\)，单位MeV⁻¹。
Hinohara APS Eq.(66)字面把B称binding energy且写正曲率，
Fig.4图注却用−Bexp并给负化学势；原文记法边界须保留，
不把正束缚能与其记号静默合并，也不猜作者程序的错误成因。

## Assumptions

实静态BCS、一对时间反演轨道只计一次；两壳控制固定上述相互作用、容量和自能。
这些不是实核配对参数的测量。不同模型的G不可仅按同名直接比较。

## Competing Explanations

奇偶质量差、低激发谱和转动响应同时受壳结构、配对、阻塞、残余作用和重排影响。
冻结独立准粒子的 \(E_k+E_l\ge2\Delta\) 只是共同正Δ下的下界；
离散谱、量子数和残余作用可改变最低允许组态，不能当所有实核激发的精确阈值。

## Transfer Conditions

跨核区迁移的是成对计数、算符和约定；具体配对空间、相互作用、自能和形状必须重建。
部分阻塞不证明所有配对消失，也不能凭此把实际惯量替换成刚体值。

## Failure Conditions

有限G处Δ→0不等于G→0；此控制的Δ在临界附近可按根号连续趋零。
有限体系不具热力学极限的相变，不等于任何参数路径都无能级交叉或非解析选支。
PBCS/VAP也不保证所有路径平滑，不由弱配对自动推出强烈配对振动。

## Falsification or Reverse Tests

[`a130_rewrite_bcs_model_audit.py`](../../system/scripts/a130_rewrite_bcs_model_audit.py)
在16维seniority-zero pair占据空间直接计算BCS积态期望，
核四个t点、受限路径驻点、矩阵相位残差和三/四点交错符号。
总控实际重放退出0，与T10输出一致；输入/producer/产物SHA在
`outputs/l4/20261108-A130-bcs-model-controls/run-provenance.json`。
这不是完整核谱或全局BCS最低能态的验证。

## Open Questions

真实旋转核的阻塞与动态配对须用共同相互作用、算符和响应输入比较；
本次系数对账不能替代它们，也不要求先解决这些前沿才修正基础正文。

## Human Review

T10独立原件/代数审计与总控重放，没有用户人工审核事件。

## Promotion or Rejection History

- 2026-11-08：以明确Hamiltonian修正拼接公式，保留原书正确结果和源内符号边界。
