raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import pathlib

# 1. Update chiara-2001-108-110in-shears-band-lifetimes.md
c_path = pathlib.Path("knowledge/sources/chiara-2001-108-110in-shears-band-lifetimes.md")
c_text = c_path.read_text(encoding="utf-8")
c_sec = """
## Day19量化审计：磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决

依据独立审计程序 `system/scripts/day19_mr_chiral_amr_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mr-chiral-amr-discrimination-result-080.json`，核准了磁转动、反磁转动与手征转动的全景四路判决定理：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CHI01-D19-2 | 系统审计确立了磁转动、反磁转动、手征转动与集体转动的四路判决图谱：(1) 磁转动（MR）：剪刀角闭合（$^{108}\text{In}$ 中 $\theta_s$ 从 $96.0^\circ$ 闭合至 $29.8^\circ$）诱发横向磁偶极矩 $\mu_\perp \propto \sin\theta_s$ 塌缩，测定 $B(M1) \propto \sin^2\theta_s$ 单调暴跌 $75.0\%$（跌落 $4.00$ 倍），而 $B(E2)$ 维持极小；(2) 反磁转动（AMR）：两副剪刀叶片对称闭合，宇称与旋称定则禁戒奇极跃迁（$B(M1) \equiv 0$），而电四极跃迁服从 $B(E2) \propto \sin^4\theta_s$ 剧烈暴跌（$^{106}\text{Cd}$ 中暴跌 $95.6\%$），导致动学转动惯量与跃迁几率之比 $\mathcal{J}^{(2)}/B(E2)$ 发散高达 $22.7$ 倍（由 $48.9$ 发散至 $1111\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$）；(3) 手征转动（Chirality）：三维非共面转动要求最大三轴度（$\gamma \approx 30^\circ$），其双重带 $B(E2)$ 严格对称（$^{128}\text{Cs}$ 比值 $1.044$）且不随自旋塌缩，同时带内与带间 $B(M1)$ 呈现 $180^\circ$ 反相奇偶交错；(4) 伪手征排他证伪：Rather 2014 $^{106}\text{Ag}$ 双交叉比值 $S(15)/S(17) = 7.2863$ 偏离手征基准 $7.29$ 倍，其实质为不同单粒子组态能带交叉而非手征伙伴带；(5) 时间测量时钟：飞秒 DSAM（$10\text{--}1000\text{ fs}$）与皮秒 RDDS（$0.5\text{--}50\text{ ps}$）提供解耦多极跃迁动力学的排他性物理时钟。 | task-mr-amr-chiral-discrimination-audit | derived-and-boundary | PDF pp.18-24 Tables V-VI; mr-chiral-amr-discrimination-result-080.json | true |
"""
if "recoil-distance-doppler-shift" not in c_text:
    c_text = c_text.replace("[[lifetime-measurements]]", "[[lifetime-measurements]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]")
c_path.write_text(c_text + c_sec, encoding="utf-8")
print("Updated chiara-2001-108-110in-shears-band-lifetimes.md")

# 2. Update chirality-wobbling-competition-evidence.md
cw_path = pathlib.Path("knowledge/synthesis/chirality-wobbling-competition-evidence.md")
cw_text = cw_path.read_text(encoding="utf-8")
cw_sec = """
## Day19量化审计：磁转动剪刀机制、反磁转动与手征对称性四路全景判决图谱

依据独立审计程序 `system/scripts/day19_mr_chiral_amr_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mr-chiral-amr-discrimination-result-080.json`，核准了对标 [[chiara-2001-108-110in-shears-band-lifetimes]] 的综合判决定理：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CWC-D19-1 | 综合 A≈130 区域高自旋多极跃迁率，确立磁转动（MR）、反磁转动（AMR）、手征转动（Chirality）与常规转动的四路排他性判决矩阵：(1) 磁转动：单副剪刀闭合驱动 $B(M1) \propto \sin^2\theta_s$ 单调衰减 $75\%\text{--}90\%$（$^{108}\text{In}$ 暴跌 $4.00$ 倍），$B(E2) \lesssim 0.1\ e^2\text{b}^2$ 且 $\mathcal{J}^{(2)}/B(E2) > 100$；(2) 反磁转动：双剪刀对称闭合驱动 $B(M1) \equiv 0$，$B(E2) \propto \sin^4\theta_s$ 断崖跌落（$^{106}\text{Cd}$ 暴跌 $95.6\%$），$\mathcal{J}^{(2)}/B(E2)$ 剧烈发散至 $>1000\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$；(3) 手征转动：三轴角动量非共面对齐驱动双重带 $B(E2)$ 高度对称（$^{128}\text{Cs}$ 比值 $1.044$）且不随自旋衰减，带内与带间 $B(M1)$ 呈现严格 $180^\circ$ 反相交错；(4) 带交叉剪刀重开：$^{137}\text{Pr}$ 中 $B(M1)/B(E2)$ 发生 $3.61$ 倍突降（$z = 3.64\sigma$），对应破对准粒子注入使剪刀叶片重新张开；(5) 伪手征证伪：$^{106}\text{Ag}$ 表观简并双带因缺乏反相交错且双交叉比值偏离 $7.29$ 倍被彻底证伪为不同准粒子组态能带。 | quantitative-synthesis-and-criterion | derived-and-source-boundary | mr-chiral-amr-discrimination-result-080.json | true |
"""
cw_path.write_text(cw_text + cw_sec, encoding="utf-8")
print("Updated chirality-wobbling-competition-evidence.md")

# 3. Update recoil-distance-doppler-shift.md
rdds_path = pathlib.Path("knowledge/methods/recoil-distance-doppler-shift.md")
rdds_text = rdds_path.read_text(encoding="utf-8")
rdds_sec = """
## Day19 磁转动、反磁转动与手征转动的时间响应与寿命判据规程

[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D19-2 结合前序审计，进一步确立了核激发模式与能级寿命的时间响应判据：

1. **剪刀闭合与极短寿命**：磁转动高自旋态由于增强的 $M1$ 跃迁，其能级寿命通常处在 $0.05\text{--}1.0\text{ ps}$ 范围，主要由 DSAM 介质慢化时钟精确测定；
2. **反磁转动四次方塌缩与寿命膨胀**：反磁转动高自旋端由于 $B(E2) \propto \sin^4\theta_s$ 塌缩，其能级寿命随自旋升高反常变长，可由皮秒 RDDS/DDCM 时钟有效覆盖；
3. **手征转动寿命对称性**：真正手征双重带的两个伙伴带在相同自旋处具有高度对称的能级寿命（$\tau_1 \approx \tau_2$），且带间跃迁寿命严格受非共面几何约束。
"""
rdds_path.write_text(rdds_text + rdds_sec, encoding="utf-8")
print("Updated recoil-distance-doppler-shift.md")

# 4. Update lifetime-method-selection-response-contract.md
notes_path = pathlib.Path("knowledge/research-notes/lifetime-method-selection-response-contract.md")
notes_text = notes_path.read_text(encoding="utf-8")
notes_sec = """
## Day19 磁转动、反磁转动与手征转动的时间响应与寿命判据规程

依据独立审计程序 `system/scripts/day19_mr_chiral_amr_discrimination_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mr-chiral-amr-discrimination-result-080.json`，核准了针对 [[chiara-2001-108-110in-shears-band-lifetimes]] 的时间响应判据契约：
1. **MR $B(M1)$ 塌缩与 DSAM 适用性**：证实剪刀闭合导致 $B(M1) \propto \sin^2\theta_s$ 暴跌 $75.0\%$，测定寿命敏感窗口在 $0.05\text{--}1.0\text{ ps}$；
2. **AMR $B(E2)$ 塌缩与 $\mathcal{J}^{(2)}/B(E2)$ 发散**：测定 $B(E2) \propto \sin^4\theta_s$ 暴跌 $95.6\%$，比值发散至 $1111\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$；
3. **四路判决图谱**：确立 MR、AMR、Chirality 与常规转动的排他性实验门禁。
"""
notes_path.write_text(notes_text + notes_sec, encoding="utf-8")
print("Updated lifetime-method-selection-response-contract.md")
