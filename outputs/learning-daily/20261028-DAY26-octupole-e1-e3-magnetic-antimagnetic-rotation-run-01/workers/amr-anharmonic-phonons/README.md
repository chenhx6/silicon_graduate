# AMR 非简谐四叶片声子与零点涨落

运行：

```bash
python3 amr_anharmonic_phonons.py
```

程序在谐振子基底中数值对角化

`H=p_theta^2/(2M_theta)+C_AMR*x^2/2+kappa_3*x^3/6+kappa_4*x^4/24`，

其中 `x=theta-theta_0`，`hbar=1`，角度用弧度。它输出 `theta_0=0--20°`
的扫描、端点参数敏感性、JSON 参数记录和 SVG 图。

在谐近似下 `omega=sqrt(C_AMR/M_theta)`、
`E_ZPE=hbar*omega/2`、`sigma_theta^2=hbar/(2M_theta omega)`。若端点
电四极几何振幅近似为 `T(E2)=q_eff theta^2`，则基态的均方强度代理为
`B_res=q_eff^2 <theta^4> = 3 q_eff^2 sigma_theta^4`；有限 `sigma_theta`
因此使该强度代理不为零。这个量是零点涨落的诊断平台，不能替代特定
一声子跃迁的约化矩阵元（后者受宇称选择定则约束），也不能直接宣称
`q_eff` 是实验测量的内禀四极矩。

标称参数 `M=10 hbar^2/MeV, C=0.50 MeV/rad^2, kappa_3=0.02,
kappa_4=0.40 MeV/rad^4, q_eff=0.35 eb` 给出端点平台约 `0.018 e2b2`；
端点扫描显示 `0.01--0.03 e2b2` 只在相应惯量、曲率和有效电荷窗口内出现。
