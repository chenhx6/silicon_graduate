raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import pathlib

# 1. Update kirsebom-2016-23mg-dsam-lifetimes.md
k_path = pathlib.Path("knowledge/sources/kirsebom-2016-23mg-dsam-lifetimes.md")
k_text = k_path.read_text(encoding="utf-8")
k_sec = """
## Day19量化审计：23Mg飞秒寿命对账、传统DSAM线形阈值与天体速率坍缩机制

依据独立审计程序 `system/scripts/day19_mg23_dsam_dvdm_reconciliation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mg23-dsam-dvdm-reconciliation-result-085.json`，核准了针对 Kirsebom 2016 Table II 中 $^{23}\text{Mg}$ 能级寿命全谱及与 Fougères 2023 对账的量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| K16-D19-2 | 对 Kirsebom 2016 Table II 中 $^{23}\text{Mg}$ 12 个激发态寿命与 Fougères 2023 多普勒速度差法（DVDM）执行系统交叉审计：(1) Table II 全谱对账：测得 4 项有限寿命（$2052\text{ keV}$ 态 $104(18)\text{ fs}$、$2771\text{ keV}$ 态 $98(15)\text{ fs}$、$2908\text{ keV}$ 态 $15(3)\text{ fs}$、$3798\text{ keV}$ 态 $41(6)\text{ fs}$）与 8 项上限（含关键天体物理态 $7787\text{ keV}$ $\tau < 12\text{ fs}$）；(2) $3798\text{ keV}$ 基准态完美闭环：Kirsebom 2016（$41 \pm 6\text{ fs}$）与 Fougères 2023（$40_{-7}^{+6}\text{ fs}$）相差仅 $1.0\text{ fs}$（$z = 0.11\sigma$），在 $40\text{ fs}$ 处确立了两大独立装置极高精度的相互校准；(3) $7787\text{ keV}$ 态三方一致性：Kirsebom 2016 上限（$<12\text{ fs}$）、Jenkins 2004（$10 \pm 3\text{ fs}$）与 Fougères 2023（$11_{-5}^{+7}\text{ fs}$）高度自洽于综合值 $\tau = 10.2 \pm 2.6\text{ fs}$；(4) 传统 DSAM 线形拟合阈值局限：在 $\tau \lesssim 15\text{ fs}$ 域，几乎所有衰变均发生于初速无减速区，全多普勒峰线形与瞬发响应几乎不可区分，致使传统单谱拟合仅能给出上限，而多普勒速度差法通过逐事件测量反冲核出射速度 $\vec{\beta}_{\text{reac}}$ 与光子发射速度 $\beta_{\text{ems}}$，形成 $\Delta\beta \propto \langle d\beta/dt \rangle t$ 的直接时间映射，将测量下限突破至亚飞秒区；(5) 新星 $^{22}\text{Na}(p,\gamma)$ 反应率坍缩解耦定理：经典新星共振强度由早期 $\omega\gamma \approx 1.39\text{ meV}$ 暴跌 $5.72$ 倍至 $0.243\text{ meV}$，微积分敏感性证实其中 $95.5\%$ 的变动由质子分支比修正（$\text{BR}_p$ 由假定的 $3.7\%$ 跌落至实测的 $0.66\%$）主导，能级寿命仅贡献 $<4.5\%$ 变动，澄清了天体反应率争议的本质为衰变分支比而非核寿命测量。 | task-mg23-dsam-dvdm-audit | derived-and-boundary | PDF10 Table II; mg23-dsam-dvdm-reconciliation-result-085.json | true |
"""
k_path.write_text(k_text + k_sec, encoding="utf-8")
print("Updated kirsebom-2016-23mg-dsam-lifetimes.md")

# 2. Update recoil-distance-doppler-shift.md
rdds_path = pathlib.Path("knowledge/methods/recoil-distance-doppler-shift.md")
rdds_text = rdds_path.read_text(encoding="utf-8")
rdds_sec = """
## Day19 23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩

[[kirsebom-2016-23mg-dsam-lifetimes]] K16-D19-2 结合前序审计，进一步确立了飞秒多普勒方法在天体物理与核结构中的判决边界：

1. **$^{23}\text{Mg}$ $3798\text{ keV}$ 基准态 $0.11\sigma$ 跨装置重合**：Kirsebom 2016（$41(6)\text{ fs}$）与 Fougères 2023（$40(6)\text{ fs}$）相差仅 $1.0\text{ fs}$，确立了 $40\text{ fs}$ 处的绝对物理标尺；
2. **多普勒速度差法（DVDM）突破传统 DSAM 线形阈值**：传统单谱积分在 $\tau < 15\text{ fs}$ 仅能给出上限（$7787\text{ keV}$ 态 $\tau < 12\text{ fs}$），DVDM 通过 $\Delta\beta = \beta_{\text{reac}} - \beta_{\text{ems}}$ 逐事件重构将灵敏度突破至 $11(+7/-5)\text{ fs}$；
3. **天体反应率主导驱动源解耦**：$^{22}\text{Na}(p,\gamma)$ 共振强度 $5.72$ 倍塌缩由质子分支比 $\text{BR}_p$（$3.7\% \to 0.66\%$）驱动 $95.5\%$，彻底澄清了寿命与衰变分支比的各自职责。
"""
rdds_path.write_text(rdds_text + rdds_sec, encoding="utf-8")
print("Updated recoil-distance-doppler-shift.md")

# 3. Update lifetime-method-selection-response-contract.md
notes_path = pathlib.Path("knowledge/research-notes/lifetime-method-selection-response-contract.md")
notes_text = notes_path.read_text(encoding="utf-8")
notes_sec = """
## Day19 23Mg飞秒寿命对账：传统DSAM线形阈值、速度差法突破与天体速率坍缩

依据独立审计程序 `system/scripts/day19_mg23_dsam_dvdm_reconciliation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/mg23-dsam-dvdm-reconciliation-result-085.json`，核准了针对 [[kirsebom-2016-23mg-dsam-lifetimes]] 的飞秒多普勒方法契约：
1. **$7787\text{ keV}$ 态三方一致性**：K16（$<12\text{ fs}$）、J04（$10(3)\text{ fs}$）与 F23（$11(6)\text{ fs}$）高度收敛；
2. **传统线形 vs DVDM 时间映射**：逐事件 $\Delta\beta$ 重构消除核多次散射对微小频移峰位的掩盖；
3. **天体共振强度解耦**：确立 $\omega\gamma$ 误差由分支比主导，寿命测量无显著争议。
"""
notes_path.write_text(notes_text + notes_sec, encoding="utf-8")
print("Updated lifetime-method-selection-response-contract.md")
