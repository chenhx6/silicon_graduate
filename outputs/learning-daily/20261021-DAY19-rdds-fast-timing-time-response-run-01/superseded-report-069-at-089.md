### checkpoint069：逆运动学Degrader-RDDS空间尺度拉伸、多普勒桥失真与亚皮秒测量下限定理

依据独立审计程序 `system/scripts/day19_degrader_rdds_kinematic_expansion_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/degrader-rdds-kinematic-expansion-result-069.json`，系统核准了逆运动学降能层 RDDS 空间拉伸机制：
1. **逆运动学速度提升与空间尺度拉伸**：速度提升（$\beta = 5.1\%$ 对比常规 $1.6\%$）实现 $3.1875\times$ 空间尺度放大，使 $\tau = 0.72\text{ ps}$ 态衰减长度由 $3.45\ \mu\text{m}$ 扩展至 $11.01\ \mu\text{m}$，脱离接触零点 $d_0 \approx 1.5\ \mu\text{m}$ 强干扰区；
2. **零点漂移误差稀释律**：接触零点误差敏感度反比稀释，将 $0.5\ \mu\text{m}$ 接触零点漂移误差从常规运动学的 $14.48\%$ 压缩至 $4.54\%$（稀释 $3.19$ 倍）；
3. **降能层穿行时间与箔内衰变**：薄降能层穿行时间 $\Delta t_{\text{foil}} = 0.1627\text{ ps} < 0.20\text{ ps}$，测定箔内衰变份额随寿命由 $5\text{ ps}$（$3.2\%$）递增至 $0.20\text{ ps}$（$55.7\%$）；
4. **多普勒桥失真消解规程**：丢失连续多普勒桥导致二元归一化曲线虚假变陡（寿命低估 $-7.5\%\text{--}-16.9\%$）；单分量微分公式消除多普勒桥失真，将机械时钟下限拓展至 $\sim 0.5\text{ ps}$。
