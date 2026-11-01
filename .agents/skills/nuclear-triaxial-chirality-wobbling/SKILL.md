---
name: nuclear-triaxial-chirality-wobbling
description: 用于三轴形变、核手征性和摆动候选的来源核查、模型条件比较及实验谱学分析；保留混合比分支、相位约定和竞争解释，并从 Wiki 原始来源回链。
---

# 三轴核集体激发研究

服务于低能核结构问答、研究设计与实验分析。按仓库授权确定读写范围；这份 skill 是工作入口，不替代原书、知识页或原始实验。

## 先定位相关证据

从仓库根目录读取与问题相符的入口，再按 source locator 查原件：

- `knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md`：纯转子高自旋近似，§4-5e / printed pp. 190–192。
- `knowledge/sources/book-petrache-chirality-and-wobbling.md`：所持 CRC 2025 版本的章节地图、135Pr 的相反判断与实际阅读范围。
- `knowledge/concepts/wobbling-mixing-ratio-phase-and-transition-diagnostics.md`：有符号矩阵元、光子混合份额与双根边界。
- `knowledge/synthesis/book-corpus-coverage-ledger.md`：全馆藏范围与未完成章节；提取成功不记作读完。
- 具体核素应再读对应 experiment/source；同一数据集的综述和论文不是独立重复实验。

## 会改变研究判断的约定

1. 先列出轴编号、s/m/l 形状轴、惯量排序、γ 正负范围和相位约定。经典刚体惯量、流体惯量及微观转动响应不默认等同。
2. TW/LW 是指定粒子–转子模型中的角动量几何分类。频率趋势依赖自旋区间、惯量与耦合；不能由下降/上升趋势单独指定模式。
3. 纯转子谐近似须检查横向角动量涨落，不能只写 I≫1。近分离轨道或重取向点时回完整量子解；低自旋进动的命名分歧应和实验数值分歧分开。
4. 对候选手征双带，核对相同宇称、自旋序列、组态与电磁性质。近简并不是充分条件；手征恢复不等于产生正负宇称双带。
5. 未经独立观测约束，不用理论偏好删除 δ 分支。偏振的正负须结合约定、响应与混合模型，不能直接变成 E2/M1 或模式标签。
6. 不设置跨所有核的固定 δ、E2 份额、B(E2) 比值、能隙或显著性阈值。两准粒子磁矩增强、大 δ 的 M1 小分母、γ 软核耦合和 TiP 都可能改变简单图像。

## 书籍知识如何成为可复用能力

用户要求持续研学时，沿用 book-to-skill 的方法提炼：问题 → 推导/方法 → 假设 → 可观测量 → 反例 → 原书 locator → 验证。长期科学内容留在 `knowledge/`；此处只维护检索入口和会影响决策的工作约定，不复制全书或制造与 Wiki 重复的第二知识库。

产生代码时，区分解析换算、示意参数化和真实分析；用独立基准、零/极限条件及可证伪案例验证。测试通过不认证生产级、全文阅读完成或物理模式成立。`wobphase` 只做矩阵元换算/候选根展示，不能调用它确认摆动。

按问题加载 [patterns.md](patterns.md)、[cheatsheet.md](cheatsheet.md)、[glossary.md](glossary.md)。
