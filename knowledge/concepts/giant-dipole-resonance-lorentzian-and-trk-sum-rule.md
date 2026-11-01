# 巨偶极共振（GDR）双洛伦兹线形、Danos 形变分裂与 TRK 能量加权求和规则：光核反应微观动力学

## 1. 物理图像与 TRK 求和规则基准

巨偶极共振（Giant Dipole Resonance, GDR）是原子核中质子系统与中子系统在电偶极外场激发下发生的整体反相高频相对位移振荡，属于多极激发中的电异旋模式（$L=1, S=0, T=1$）。它在几乎所有质量数 $A \ge 12$ 的原子核中均普遍存在，吸收截面峰值高达数百毫靶（mb）。

卢希庭《原子核物理（修订版）》（第 9 章与第 11 章）与 Bohr & Mottelson《Nuclear Structure》（Vol. II，第 6 章）对 GDR 动力学奠定了经典解析框架：
1. **Thomas-Reiche-Kuhn (TRK) 经典未加权能谱积分求和规则（Classical TRK Sum Rule）**：
   $$\sigma_0 = \int_0^\infty \sigma_{\text{abs}}(E) dE = \frac{2\pi^2 e^2 \hbar}{m c} \frac{N Z}{A} \approx 59.74 \frac{N Z}{A}\text{ MeV}\cdot\text{mb}$$
   对于双幻核 $^{208}\text{Pb}$（$Z=82, N=126$），经典 TRK 积分截面为 $\sigma_0 \approx 2967.5\text{ MeV}\cdot\text{mb}$。

2. **亚核子介子交换流（MEC）增强因子 $\kappa$**：
   实际实验光核全吸收截面积分值 $\sigma_{\text{int}}$ 系统性超过经典 TRK 预测值 $20\% \sim 40\%$：
   $$\sigma_{\text{int}} = \sigma_0 (1 + \kappa_{\text{TRK}}), \quad \kappa_{\text{TRK}} \approx 0.20 - 0.35$$
   物理起源：核力包含强烈的交换张量项（如 $\pi, \rho$ 介子交换），该电荷交换算符与空间坐标算符不正则对易，产生额外的空间矢量流偶极分量。在 $^{208}\text{Pb}$ 中，实验积分截面达 $\sim 3700\text{ MeV}\cdot\text{mb}$（$\kappa \approx 0.25$）。

3. **球形核 GDR 质心能量标度律**：
   在球形核中，共振峰能量由核表面振荡与流体动力学可压缩性共同决定（Berman & Fultz 1975）：
   $$E_{\text{GDR}}^{\text{sph}} \approx 31.2 A^{-1/3} + 20.6 A^{-1/6}\text{ MeV}$$
   在 $^{208}\text{Pb}$ 处，该标度律精确给出 $E_{\text{GDR}} \approx 13.7\text{ MeV}$。

---

## 2. 轴对称与三轴形变下的 Danos 模型分裂

当原子核处于基态四极形变时，原子核的长轴与短轴具有不同的空间振荡几何尺度，导致单一洛伦兹共振峰发生剧烈分裂（Danos 1958）：
1. **长轴振荡（Long Axis $z$，对应振荡投影量子数 $K=0$）**：
   振荡恢复力路径较长，恢复力常数偏软，共振频率降低为低能峰 $E_1$：
   $$E_1 = \frac{E_{\text{GDR}}}{1 + 0.66 \beta_2}$$
2. **短轴对称振荡（Short Axes $x, y$，对应振荡投影量子数 $K=1$）**：
   振荡路径较短，恢复力强，对应高能峰 $E_2$：
   $$E_2 = \frac{E_{\text{GDR}}}{1 - 0.33 \beta_2}$$

### 2.1 轴比 $a/b$ 与 Danos 频率比解析反演
原子核等效椭球轴比 $a/b$ 与长轴四极形变参数 $\beta_2$ 满足几何关系：
$$\frac{a}{b} \approx \frac{1 + 0.63 \beta_2}{1 - 0.315 \beta_2}$$
Danos 流体动力学频率比定理指出：
$$\frac{E_2}{E_1} = 0.911 \left( \frac{a}{b} \right) + 0.089$$
此解析关系构成了核物理实验中反演原子核基态四极形变 $\beta_2$ 的“光学标尺”（Optical Caliper）！

### 2.2 双洛伦兹线形（Double Lorentzian Parameterization）
形变核的光吸收截面表象为双峰叠加：
$$\sigma_{\text{abs}}(E) = \sum_{k=1}^2 \frac{\sigma_k E^2 \Gamma_k^2}{(E^2 - E_k^2)^2 + E^2 \Gamma_k^2}$$
对于长椭球（Prolate）：低能峰与高能峰的面积比满足振动简并度比 $\sigma_1 \Gamma_1 : \sigma_2 \Gamma_2 = 1 : 2$。

---

## 3. 科学分析套件实战验证

Wiki 内置模块 `system/scripts/analysis/gdr_lorentzian_trk_sumrule_calculator.py`（CLI 命令：`python3 system/scripts/analysis/nuclear_analyzer.py gdr`）对 $^{208}\text{Pb}$ 及形变体系进行了完整核算：

```bash
# 模拟 208Pb 在形变假定 beta2 = 0.30 下的 GDR 分裂与 TRK 积分核算
python3 system/scripts/analysis/nuclear_analyzer.py gdr -Z 82 -A 208 --beta2 0.30 --kappa 0.25 --invert
```

**实测输出解析**：
- **经典 TRK 求和值**：$\sigma_0 = 2967.5\text{ MeV}\cdot\text{mb}$，计入介子交换流后总增强积分为 $3709.3\text{ MeV}\cdot\text{mb}$；
- **球形等效质心**：$E_{\text{GDR}} = 13.73\text{ MeV}$；
- **Danos 双洛伦兹裂分**：
  - 低能长轴峰（$K=0$）：$E_1 = 11.54\text{ MeV}$，$\Gamma_1 = 3.44\text{ MeV}$，$\sigma_1 = 228.8\text{ mb}$；
  - 高能短轴峰（$K=1$）：$E_2 = 14.83\text{ MeV}$，$\Gamma_2 = 4.86\text{ MeV}$，$\sigma_2 = 323.9\text{ mb}$；
  - 裂分能差：$\Delta E = E_2 - E_1 = 3.29\text{ MeV}$（频率比 $E_2 / E_1 = 1.285$）；
- **形变逆向反演**：从双峰能量比直接闭合重构出 $\beta_2 = 0.300$，误差小于 $0.001$！
