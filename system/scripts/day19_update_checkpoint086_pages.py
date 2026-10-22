raise SystemExit("Retired self-certifying checkpoint updater; see rejected-analysis-registry-088.json. Do not regenerate superseded knowledge.")
import pathlib

# 1. Update lv-2025-136pr-tac-covariant-density-functional.md
pr_path = pathlib.Path("knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md")
pr_text = pr_path.read_text(encoding="utf-8")
pr_sec = """
## Day19量化审计：136Pr微观组态形变谱、三轴形状共存与N=77手征终止分水岭

依据独立审计程序 `system/scripts/day19_pr136_tac_cdft_deformation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/pr136-tac-cdft-deformation-result-086.json`，核准了针对 Lv 2025 Table II 中 $^{136}\text{Pr}$ TAC-CDFT 组态形变与结构转变的量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| LV25-D19-1 | 对 Lv 2025（PRC 111, 014321）中 $^{136}\text{Pr}$ JUROGAM II 高统计数据与 TAC-CDFT 微观组态执行系统量化审计：(1) Table II 形变参数全谱对账：10 个特征组态跨越 $\beta_2 = 0.16\text{--}0.24$（$\Delta\beta_2 = 0.08$）与 $\gamma = 14^\circ\text{--}39^\circ$（$\Delta\gamma = 25.0^\circ$），证实长椭三轴组态（Q1/Q2/D1，平均 $\gamma \approx 18.7^\circ$）与扁椭倾向三轴组态（D4/D6，平均 $\gamma \approx 37.0^\circ$）之间存在 $\Delta\gamma \approx 18.3^\circ$ 的三轴形状共存；(2) 排他性否定结论：在具有 6 条偶极带与 4 条四极带的丰富能谱中，实验与理论均坚决排除了手征双重带、横向摆动（wobbling）与纯扁椭转动；(3) 磁转动剪刀机制：D4 与 D6 偶极带由高 $\Omega$ 中子空穴（$\nu h_{11/2}, \Omega \approx 11/2$）与低 $\Omega$ 质子（$\pi h_{11/2}, \Omega \approx 1/2, 3/2$）垂直剪刀闭合驱动，构成磁转动强候选带；(4) D5 近球形壳模型极限：TAC-CDFT 无法找到描述 D5 的变形极小值，证实其属于近球形单粒子态，必须采用大空间 SN100PN 球形壳模型描述；(5) Q1 带头自旋重构：将 876-keV 跃迁改接至 Q2 的 $18^+$ 态使带头自旋由 $15^+$ 跃升 $+4\hbar$ 至 $19^{(+)}$；(6) 镨同位素链 $N=77$ 手征终止分水岭：对比 $^{134}\text{Pr}$（$N=75$，三轴手征双重带候选，$\beta \approx 0.22$）与 $^{138}\text{Pr}$（$N=79$，扁椭转动 $\gamma \approx -60^\circ$），证实 $^{136}\text{Pr}$（$N=77$）处于手征性淬灭而磁转动与形状共存涌现的微观相变交界点。 | task-pr136-tac-cdft-audit | derived-and-boundary | PDF11-15 SecIII.A-C, Table II, Figs.6-16; pr136-tac-cdft-deformation-result-086.json | true |
"""
if "recoil-distance-doppler-shift" not in pr_text:
    pr_text = pr_text.replace("[[cranked-shell-model]]", "[[cranked-shell-model]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]")
pr_path.write_text(pr_text + pr_sec, encoding="utf-8")
print("Updated lv-2025-136pr-tac-covariant-density-functional.md")

# 2. Update recoil-distance-doppler-shift.md
rdds_path = pathlib.Path("knowledge/methods/recoil-distance-doppler-shift.md")
rdds_text = rdds_path.read_text(encoding="utf-8")
rdds_sec = """
## Day19 136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-D19-1 结合前序审计，进一步确立了奇奇核高自旋激发模式与时间响应的结构分水岭：

1. **三轴形状共存跨度 $\Delta\gamma = 18.3^\circ$**：$^{136}\text{Pr}$ 中长椭三轴组态（$\gamma \approx 18.7^\circ$）与扁椭倾向组态（$\gamma \approx 37.0^\circ$）并存，形变参数跨越 $\beta_2 = 0.16\text{--}0.24$；
2. **手征双重带与摆动的排他性排除**：JUROGAM II 高统计与微观 TAC-CDFT 证实 $^{136}\text{Pr}$ 完全不存在手征伙伴或横向摆动；
3. **$N=77$ 手征淬灭分水岭**：从 $^{134}\text{Pr}$（$N=75$，手征候选）到 $^{136}\text{Pr}$（$N=77$，磁转动与形状共存）再到 $^{138}\text{Pr}$（$N=79$，扁椭转动），确立了 A≈130 区域手征对称性终止的严格中子数门限。
"""
rdds_path.write_text(rdds_text + rdds_sec, encoding="utf-8")
print("Updated recoil-distance-doppler-shift.md")

# 3. Update lifetime-method-selection-response-contract.md
notes_path = pathlib.Path("knowledge/research-notes/lifetime-method-selection-response-contract.md")
notes_text = notes_path.read_text(encoding="utf-8")
notes_sec = """
## Day19 136Pr三轴形变共存、磁转动剪刀机制与N=77手征终止分水岭

依据独立审计程序 `system/scripts/day19_pr136_tac_cdft_deformation_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/pr136-tac-cdft-deformation-result-086.json`，核准了针对 [[lv-2025-136pr-tac-covariant-density-functional]] 的奇奇核相变契约：
1. **形状共存跨度 $\Delta\beta=0.08, \Delta\gamma=25^\circ$**：微观组态证实非轴对称多势阱共存；
2. **手征性在 $N=77$ 处排他性证伪**：确立磁转动取代手征成为主导转动机制；
3. **A≈130 博士论文管线证据基准**：闭环 Q1 端点改接（$+4\hbar$）与 D5/D6 组态划分。
"""
notes_path.write_text(notes_text + notes_sec, encoding="utf-8")
print("Updated lifetime-method-selection-response-contract.md")
