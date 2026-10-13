# Day13：卷积线型的来源前回忆

时间：2026-10-14 00:48 Asia/Shanghai。已有Doppler练习后的primed recall；下面先写判断，再核验直接宽度记录与数学kernel，非新一日口试。

1. Gaussian独立误差可加variance；Lorentz自然线宽的variance不存在，不能将其Γ当σ或直接平方和FWHM。Lorentz卷积Gaussian是Voigt。
2. Total母态decay rate控制level width；理想稳定末态transition以该Γ为natural FWHM，有有限宽末态时理想gap spectrum可包含两者。真实干涉/共振/时间选择可能超出孤立Markov线近似。
3. 相同FWHM并不保证相同gate接受率或tails，局部Gaussian fit会遗漏tail强度；分母和背景窗口定义必须一起记录。
4. TUNL15.11-MeV态天然43.6eV比Crespi119keV观测FWHM小，卷积不能支持天然宽度主导；但其它broad resonances不能套用这个尺度判断。
5. 反证：构造ΓLorentz与FWHMGaussian同量级的已归一Voigt，核验真实half-height width与平方和的差；再检验不同finite gate内fraction，明确这是synthetic方法例题。

待核验：source Γ的frame/单位、Voigt normalized form、Γ/2与σ的约定、积分与zero-kernel极限；不以多核素宽度表冒充独立响应calibration。
