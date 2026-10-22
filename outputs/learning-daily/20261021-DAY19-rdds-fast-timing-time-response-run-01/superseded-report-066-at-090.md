### checkpoint066：阻止本领反比标度律、双比值尺度不变性定理与IAEA基准对账

依据独立审计程序 `system/scripts/day19_stopping_power_scaling_invariance_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/stopping-power-scaling-invariance-result-066.json`，系统核准了阻止本领缩放对 DSAM 寿命反演的微积分标度律与双比值守恒定理：
1. **反比标度微积分证明与对数微商三定理**：严格微积分证明分数多普勒频移在阻止标度 $k$ 变换下满足 $F'(\tau) = F(k\tau)$。为重现相同的实验频移，寿命提取严格遵循 $\tau_{\text{fit}} = \tau_0 / k$，进而确立对数微商三定理：$d\ln\tau/d\ln k \equiv -1.000$、$d\ln B(E2)/d\ln k \equiv +1.000$ 与 $d\ln Q_t/d\ln k \equiv +0.500$；
2. **Nolan 1979 重叠系统学消解**：Nolan 1979 Table 7 中 DSAM 寿命相对 RDDS 呈现的 $10.0 \pm 2.9\%$（$3.46\sigma$）系统性偏长，由反比标度定理严格消解为 1970 年代 Northcliffe-Schilling 阻止表平均低估了 $9.09 \pm 2.40\%$ 的电子阻止截面。真空机械位移与固体慢化时钟的系统偏差完全来源于固体阻止截面模型的先验偏移；
3. **双交叉比值尺度不变性定理**：四极矩与电磁强度跨自旋/跨能带双交叉比值（如 $^{136}\text{Nd}$ 的 $D = 19.25$ 与 $^{106}\text{Ag}$ 的 $S = 7.2863$）对全局阻止标度因子 $k$ 的导数严格为零。这确立了双比值作为抗阻停漂移金标准的物理地位，阻止截面误差绝不可能颠覆由双比值证伪手征或确立带交叉的结构结论；
4. **IAEA 基准数据库对账**：Forster 1976 $^{24}\text{Mg}+\text{Au}$ 实验阻止数据在 $1.6\text{ MeV/u}$ 下给出线形阻止 $8.434\text{ MeV}/\mu\text{m}$，在 $0.78\%$ 精度内精确吻合 Kirsebom 2016 采用的 $8.5\text{ MeV}/\mu\text{m}$ 基准值，证实现代阻停数据库已将宏观标度偏差压缩至 $3\%\text{--}5\%$ 范围。
