# Cranked QRPA Chiral-Octupole Vibrational Phonon Solver

本目录包含三轴八极形变核中推转准粒子随机相位近似（Cranked Quasiparticle Random-Phase Approximation, C-QRPA）与手征-八极微振声子谱计算工件及可复现脚本。

## 物理模型概要

1. **推转平均场与基底**:
   - 平均场内禀哈密顿量在静态三轴八极（$\beta_2, \gamma, \beta_3$）变形下建立，引入推转项 $-\vec{\omega}\cdot\vec{J}$。
   - 在此准粒子真空上建立推转 QRPA 振动激发方程：
     $$[ H_{\text{crank}}, O_\nu^\dagger ] = \hbar \Omega_\nu(\omega) O_\nu^\dagger$$
     其中声子算符展开为：
     $$O_\nu^\dagger = \sum_{\mu < \mu'} \left[ X_{\mu\mu'}^\nu \alpha_\mu^\dagger \alpha_{\mu'}^\dagger - Y_{\mu\mu'}^\nu \alpha_{\mu'} \alpha_\mu \right]$$
2. **两类对称性恢复微振声子及其杂化**:
   - **手征摆动声子 (Chiral wobbling phonon)**：出平面振动模式，恢复时间反演与方位反对称性，其本征能量随转动频率 $\omega$ 发生特征性软化：$\hbar\Omega_\chi(\omega) = \sqrt{\Omega_{\chi 0}^2 - c_\chi \omega^2}$；
   - **八极微振声子 (Octupole vibrational phonon)**：空间反演宇称恢复模式，由 $\Delta l = \Delta j = 3$ 轨道偶极/八极激发构成，其能量为 $\hbar\Omega_3(\omega) = \Omega_{30} + c_3 \omega^2$；
   - **相干杂化与避免交叉**:
     转动过程中 Coriolis 力引入宇称混合项 $V_{\text{mix}}(\omega) = \lambda_{\text{mix}} \omega$，诱导手征模式与八极模式在临界转动频率 $\omega_{\text{cross}} \approx 0.235\text{ MeV}/\hbar$ 处发生强相干杂化与模式排斥。
3. **电多极跃迁动力学演化**:
   - 提取态向 yrast 基准带的约化跃迁几率 $B(M1), B(E1), B(E2), B(E3)$；
   - 在共振交叉区展示出显著的电磁跃迁强度模式互换（interchange of transition strengths）与相干反常共存。

## 文件清单

- `cqrpa_chiral_octupole_solver.py`: 独立可执行 Python 求解器；
- `cqrpa_chiral_octupole_modes.csv`: 随推转角频率 $\omega$（0.02 至 0.48 MeV/$\hbar$）扫描的能级、声子振幅 $(X, Y)$ 及 $B(M1), B(E1), B(E2), B(E3)$ 跃迁几率数据表；
- `cqrpa_chiral_octupole_summary.json`: 完整的模型参数、临界物理特征及 $^{78}\text{Br}, ^{133}\text{Ce}, ^{135}\text{Nd}$ 实验基准对账元数据；
- `README.md`: 本说明文档。

## 运行与复现指令

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/qrpa-chiral-octupole/cqrpa_chiral_octupole_solver.py outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/qrpa-chiral-octupole
```

## 实验对账与证据边界

1. **$^{78}\text{Br}$ (Liu et al. 2016 PRL 116, 112501)**:
   - 实验在正宇称手征双重带（Bands 1-2）与负宇称双重带（Bands 3-4）之间观测到 8 条强 $E1$ 连接跃迁；
   - 测定 $B(E1)/B(E2) \sim 1.2\times 10^{-4}\text{--}4.5\times 10^{-4}\text{ fm}^{-2}$，比稳定八极核 $^{224}\text{Th}$ 小一个数量级，与微观 C-QRPA 八极声子软振动图像一致。
2. **$^{133}\text{Ce}$ (Ayangeakaa et al. 2013 PRL 110, 172504; Wakudyanaye 2022)**:
   - 具有典型的多手征双重带（M$\chi$D）和三轴超形变/常规形变共存，在低自旋手征声子能量 $\sim 0.4\text{ MeV}$；
   - 势能面沿 $\beta_{30}$ 表现为软振动势阱，受八极声子有限混合扰动。
3. **$^{135}\text{Nd}$ (Mukhopadhyay et al. 2007 PRL 99, 172501)**:
   - 手征微振动随自旋/推转频率增加向静态手征双阱过渡；
   - $\Delta E(I)$ 与 $B(M1)/B(E2)$ 演化支持出平面摆动声子模式在临界转动频率附近的剧烈软化。
