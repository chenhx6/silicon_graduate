# Suhonen Ch 18: 准粒子无规相位近似 (QRPA) 与微观集体振动

### 核心物理定位
超越 Tamm-Dancoff 近似（TDA），在准粒子真空中包容基态两准粒子零点涨落（$Y$ 振幅）。

### 关键解析公式
1. **超矩阵子块显式形式**：
   $$A(ab, cd; J) = (E_a + E_b) \delta_{ab, cd} + \langle ab; J | V_{\text{res}} | cd; J \rangle (u_a u_b u_c u_d + v_a v_b v_c v_d)$$
   $$B(ab, cd; J) = -\langle ab; J | V_{\text{res}} | cd; J \rangle (u_a u_b v_c v_d + v_a v_b u_c u_d)$$
2. **第一激发态 $2_1^+$ 跃迁概率相干增强**：
   $$\langle 2_1^+ || \mathcal{M}(E2) || \text{QRPA}\rangle = \sum_{a \le b} (u_a v_b + v_a u_b) \langle a || \mathcal{M}(E2) || b \rangle [X_{ab} + Y_{ab}]$$
   因 $X_{ab}$ 与 $Y_{ab}$ 在最低集体态呈同相相加，导致 $B(E2)$ 获得数十倍 Weisskopf 单位的巨额集体相干增强。
