# T02：102Ru 有效 E1 的协变推导与可辨识性回执

**主要结果。** 固定轴向四极背景、仅保留单一最低阶 $[Q_2\otimes O_3]^1$、标准 $Y_{3K}$ 规范时，$C_0=3/\sqrt{35}$、$C_{\pm1}=\sqrt{6/35}$，所以 $b_{\pm1}/b_0=\sqrt{2/3}$，而 PRL 实际取 $b_0=b_{\pm1}$。加入协变 rank-4 背景，可明确构造共同系数；不能由最低阶不等式推断作者参数化不合法，也不能称作者采用该构造。

**物理层次。** 平动修正的裸长波 E1、电偶极和八极同 $K^\pi$ 的 QRPA 模混合、消去其他模式后投影出的 E1 有效算符是不同对象。Hamamoto 1989 pp.19–20 确实写出 Wigner $D^1$ 旋转及有效内禀算符，建立在该文的微扰与静态极化条件下；Hagemann 1993 p.2011 的 $b_\nu$ 包含 RPA 模能量与相对矩阵元。2026 文献对 $r^3Y_3$ 使用的电荷系数与旧文不同。以相同空间同时处理 QRPA 波函数和极化顶角是否重复计数，须由作者空间划分及匹配细节判断。

**SI 新增与缺口。** SI p.3 Eqs.(1)–(4) 明确列出 ISDD、ISJJ、IVSS、IVJJ、IVDD、IVOO 六项；PRL p.4 将前两项赝模推高，但没有公布赝模污染量。SI 未给 stretching 的具体实施、$\kappa^{sc}$ 的公式/数值、IS/IV 归一、空间截断或完整求解器配置；不能唯一恢复其 Hamiltonian 或代码。SI pp.1–3 逐态表增量重要，但没有公开逐态理论复振幅、相位、完整实验协方差或作者响应；对于 $b$ 和 $\kappa$，相关性、局部秩及全局多解都必须以一致响应和似然检验，不能宣称已严格退化或唯一。

**验证与可复现资料。**

- 详细来源 locator、条件推导、质心有效电荷、rank-4 构造、Fisher/相位与 $L\Sigma L^T$、拟议的同态 E1/E2/E3 观测，见 `knowledge/research-notes/continuation-t02-ru102-covariant-effective-e1-20261107.md`。
- `python3 outputs/l4/20261107-ru102-effective-e1/cg_audit.py`：通过六个 CG 系数符号和有理数平方断言；无真实核谱计算。仅依赖 Python 3 标准库。
- `python3 system/scripts/wiki_archive_gate.py check --root . -- raw/papers/gpt/query/20261107-continuation-G14/manifest.json raw/papers/gpt/query/20261107-continuation-G15/manifest.json`：两个 manifest，0 failures。
- `python3 -m py_compile outputs/l4/20261107-ru102-effective-e1/cg_audit.py`：通过。`git diff --check`：通过；未跟踪文件另作行尾、frontmatter、展示数学括号核查通过。
- 全库 lint 的实际统计及本任务条目见配套 receipt；这是共享工作树的整体结果，不将其他 worker 的问题归因于本任务。

**仍缺。** $\kappa^{sc}$ 及坐标定义、完整输入空间、理论复响应及其 $\kappa$ 扫描、实验事件/效率/BR 协方差；同态多探针绝对 E1、E2、E3 矩阵元及可观测的干涉相位。以比较软振动、组态混合和其他 E1 机制的前向模型进行未拟合观测检验；不能以单个 E1/E3 或通用阈值确认静态八极形变。G15 原文由其他 worker 获取，本任务没有下载新原件。

**运行身份。** 用户指定 Terra/xhigh；当前系统仅声明 Codex 基于 GPT-6，未向本 worker 暴露可核实的实际路由型号与 reasoning effort。不能把用户指定值当作已实测的运行元数据；配套 receipt 分别记录 requested 和 actual/unverified。

**G15 只读核查供父代理集成。** 本任务笔记末节列出 8 项具体修订，包含协变构造不等价、三轴与静态近似的条件、联合拟合不可直接推出共线、2.95 MeV 的假说级别及算符电荷差。另发现直接的数值错误：Hagemann 1993 p.2017 Eq.(8) 的 $\bar\kappa_0=-4.8\times10^{-5}$、$\bar\kappa_1=+1.58\times10^{-5}\,\mathrm{MeV\,fm^{-6}}$，G15 草案误写为 $10^{-3}$，均大 100 倍；已对照该页图像。未修改 G15 文件。
