# AMR 四叶片临界频率同位素定标工件

本目录保存 2026-10-29 对反磁转动剪刀临界频率、体积/同位旋标度和壳效应调制的可复现计算。入口脚本是 `amr_scaling_laws.py`，只使用 Python 3 标准库。

运行：

```bash
python3 amr_scaling_laws.py
```

脚本输出：

- `amr_isotope_systematics.csv`：26 个候选核素的模型输入、(V_{\pi\nu})、​\(\hbar\omega_c\)、闭合自旋和实验字段。实验字段只有在本地证据账本给出带头/终止/最高 \(E_\gamma\) 时才填入。
- `amr_scaling_laws_results.json`：同一结果的 JSON、公式、常数、证据状态和相图统计。
- `amr_scaling_phase_map.csv`：\(80\leq A\leq220\)、\(40\leq N\leq120\) 的平滑质量数/中子数扫描。
- `amr_scaling_phase_map.svg`：固定 \(N=60\)、\(j_\pi=4.5\hbar\) 的壳调制临界频率示意曲线。

模型使用

\[
\hbar\omega_c=\frac{3V_{\pi\nu}}{2j_\pi},\qquad
V_{\pi\nu}=V_0A^{-1/3}\left[1-\kappa\left(\frac{N-Z}{A}\right)^2\right].
\]

\(V_0\) 由 Roy 2011 采用的 \(^{110}\mathrm{Cd}\) 有效 \(V_{\pi\nu}=1.2\) MeV 校准。壳因子是独立的现象学代理，在 \(N=56\text{--}66\) 的 \(h_{11/2}\) 填充窗口内取正弦型增强；它不是实验拟合，也不能代替 PNC-CSM、HFB 或 EDF 自洽计算。

`observed_omega_proxy_MeV` 定义为已记录最高 \(E_\gamma\) 的一半，只作能量尺度代理。它不等于实验直接报告的旋转频率；缺少可定位最高跃迁的核素保留为空值。\(^{104}\mathrm{Pd}\) 的带头和终止自旋有来源定位，但本轮没有从图表逐线重建最高 \(E_\gamma\)，故相应字段为空。

来源边界：Roy 2011 的 \(^{106,108,110}\mathrm{Cd}\) 和 Rather 2014 的 \(^{104}\mathrm{Pd}\) 是直接 AMR 记录；Chiara 2001 的 \(^{108,110}\mathrm{In}\) 是剪刀带寿命来源，但本工件没有把未逐表核验的带头/终止数值补入。\(^{142\text{--}146}\mathrm{Gd}\)、Ru 控制行是跨质量区模型探针，不是已确证 AMR。
