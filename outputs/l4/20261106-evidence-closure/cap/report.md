**CAP 更正传播已按用户要求停止；当前停在定位和静态阅读阶段，尚未实施修订。**

本轮没有修改两篇授权知识页、分析脚本、测试或原始资料，没有运行 CAP 求解、测试或拟合。没有本轮半成品代码需要撤销。仅新增本目录的 report.md 和 receipt.json 保存交接。

已完成的有限核查：

- 已读 `knowledge/concepts/coriolis-anti-pairing-and-moment-of-inertia-expansion.md` 与 `knowledge/research-notes/coriolis-antipairing-and-superdeformed-alignment-transitions.md`。
- 已读更正后的 `knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md`。其中 BM2-11 已将普适平方根配对隙函数、固定临界自旋和统一二级相变断言撤回；可用定位为 §4-3a、物理 PDF64／printed42、编号1及试探性上下文。该 source 将原文归为配对减弱及可能转变的作者解释，并记载当时 A约160、I约20 的可能关联。本轮只读该既有更正，尚未独立打开原书页面，不把此项登记为新完成的原件核查。
- 已读下面两份直接绑定脚本，发现它们仍保留与更正冲突的归属和机制表述。

精确文件范围与碰撞边界：

| 文件 | 本轮实际操作 | 修订状态 |
|---|---|---|
| `knowledge/concepts/coriolis-anti-pairing-and-moment-of-inertia-expansion.md` | 读取 | 未改 |
| `knowledge/research-notes/coriolis-antipairing-and-superdeformed-alignment-transitions.md` | 读取 | 未改 |
| `system/scripts/analysis/coriolis_anti_pairing_gap_quenching_moi_engine.py` | 读取 | 未改 |
| `system/scripts/day27_sd_vs_nd_pairing_cap_study.py` | 读取 | 未改 |
| `system/tests/test_coriolis_anti_pairing.py` | 引用检索定位到专用测试路径及导入 | 未读测试正文、未运行、未改 |
| `system/scripts/analysis/test_analysis_suite.py` | 引用定位：L200、L2116–2121 | 共享聚合测试，不修改 |
| `system/scripts/analysis/nuclear_analyzer.py` | 引用定位：L173、L3846起、L5874–5878 | 共享CLI入口，不修改 |

现有 BM-II 更正审计位于 `outputs/l4/20261106-odd-ba-manuscript-revision/bm2-source-attribution/`。本轮仅列出其文件名，未进一步读取其报告、图像或原件。该目录不属于本轮写入范围。

已经从所读代码确认、但尚未修复的问题：

1. CAP engine 的模块说明仍把人为平方根插值称为自洽 BCS/cranking 预测，并把归零称为二级量子相变。当前代码本身没有求解 gap/number 方程，也没有给出判定相变阶数所需的能量或热力学分析。
2. `calculate_cap_pairing_gap` 对非正初始 gap 一律返回零，并以 `max(1e-4, omega_crit_MeV)` 隐式替换临界尺度；负值、非有限输入及零初始 gap 的归一化语义尚未审定和测试。
3. `calculate_cap_moments_of_inertia` 给三个轴乘同一 gap-dependent 因子。模块关于中轴相对更快膨胀、由此产生新惯量不对称并稳定特定模式的断言，不由该实现建立。
4. `solve_spin_state_cap` 使用固定上界的二分循环，未显式验证输入自旋被根括号覆盖。它只是给定插值下的代数自洽映射，不是微观配对自洽。相关频率变量的数值采用 MeV，必须明确是 hbar*omega；页面和报告中的 omega、hbar*omega 与自旋单位目前混用。
5. `run_cap_analysis` 所谓临界自旋来自输入采样列表中首个 gap低于初值5%或归零的点。这是采样/阈值指标，不能被当成普适临界自旋或精确相变点。
6. Day27 的 `solve_cranked_pairing_bcs` 实际采用固定尺度0.65和 `sqrt(max(0.04,...))` 的 gap示意式；`G_pair` 不参与计算。两能带混合的能差由输入交叉频率和顺排参数规定，不由该 gap 求出。因此不能称其为“全微观、自洽BCS”或将其输出视为对跨质量区争议的排他解决。
7. Day27 输出列举了经验文献/核素标签，但所读脚本没有对应实验输入的读取、误差或精确 source locator。其内部阈值自检首先检验指定曲线的性质，不能认证实验机制。研究笔记正文中的确定性归属、精确核素数值和排他结论，不能仅靠末尾泛化免责声明得到修复。

实际已有验证：只完成上述文件阅读、引用路径定位及开始时的 Git 状态查询。没有执行专用测试、共享测试、CLI回归、数值重放、原书图像核查或修订后的schema检查；没有新的测试通过声明或科学修复完成声明。

未完成项：原书 PDF64／printed42 的本轮直接复核；专用测试正文与接口依赖核查；两页科学表述修订；脚本的条件模型标签、量纲和输入域修复；不掩盖科学错误的针对性验证及最终差异审计。它们均未完成，不自动续跑，不改成成功状态。

本轮未改 raw、其它 knowledge、PLAN、get-paper、index、handoff、共享稿件或他人文件，未提交。
