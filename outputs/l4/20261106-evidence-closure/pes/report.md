---
status: partial
date: 2026-11-06
stop_reason: user-requested immediate closeout because of quota
knowledge_files_modified: []
code_files_modified: []
---

**收束状态：仅完成只读扫描，未传播修改。**

用户要求立即停止新增阅读／调查时，本任务尚未编辑知识页或代码。现冻结为 partial，不将扫描发现写成“已修复”或“证据闭环已完成”。本次唯一新增文件为本报告：

`outputs/l4/20261106-evidence-closure/pes/report.md`

**已向主代理列明的精确范围**

1. `knowledge/concepts/cranked-triaxial-shape-coexistence-pes.md`
2. `knowledge/concepts/triaxial-hexadecapole-deformation-and-wobbling-modification.md`
3. `knowledge/concepts/triaxial-superdeformed-pes-strutinsky-landscape.md`

三页均已读取。需澄清引用关系：扫描未发现这些页逐字引用 BM2-9/10/13 编号；它们正文使用了 Bohr–Mottelson 书名／章节归属，并保留与已撤回 source 条目对应的具体断言。因此本报告记录实际归属，不将它们描述为已有精确 claim-ID 链接的页面。没有进一步扩展待修改页。

**已确认的知识传播缺口**

既有 [BM-II source 更正](/workspace/wiki/knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md:56)是本轮依据；未重新读取 raw 原件。BM2-9 保留的是电四极／十六极矩与表面多极分量关系，撤回了所写惯量修正及 β₄ 符号普遍稳定／破坏 TW 的归属。BM2-10 保留平滑能量与壳结构贡献的区分及总能量条件，撤回固定高自旋阈值和固定降能。BM2-13 撤回未绑定核素、输入、输出和原书 locator 的极小位置及交叉频率断言。

| 扫描页面与原位置 | 仍保留的问题 | 后续最小传播动作；本次未执行 |
|---|---|---|
| [cranked PES](/workspace/wiki/knowledge/concepts/cranked-triaxial-shape-coexistence-pes.md:20)，原 lines 20–47、56–63、86–97 | 将固定频率的负转动项称为总能量，并直接连接到骤然一阶形状相变及高自旋模式。给出 β≈0.24/0.16、γ≈24°、惯量 55–60/30–35，以及核素命名命令旁的交叉频率 0.236/0.262/0.232；这些行未附来源定位或可追溯运行记录。泛称实验提供“直接实证”。 | 保留有条件的模型／Routhian 定义，明确固定频率与固定角动量的解释边界；撤回具体极小、交叉值及实验确认身份，不把命令存在当成结果验证。 |
| [hexadecapole](/workspace/wiki/knowledge/concepts/triaxial-hexadecapole-deformation-and-wobbling-modification.md:20)，原 lines 20–40、59–65、78–89 | 在书目总归属下给出惯量乘法修正和 κ₄≈1.85，并把 β₄>0／<0 分别写成稳定 TW／加速失稳。核素命名的频移数值被列作 benchmark validation，实验支持段未提供逐项证据。 | 保留有来源的表面多极展开；撤回 BM-II 对该惯量修正、系数和普适符号判据的支持。频移数值在有独立输入与 producer/replay 定位前不保留为已验证核素结果。 |
| [TSD PES](/workspace/wiki/knowledge/concepts/triaxial-superdeformed-pes-strutinsky-landscape.md:18)，原 lines 18–45、64–68、81–92 | 仍将固定 β₂/γ 范围、25–40ℏ 阈值、约 65ℏ²/MeV 惯量及 10–15 MeV 降能放在原书归属下。后文虽标明 model/fixture 非实验验证，仍列确定极小、势垒与 `STABLE_TRIAXIAL_SUPERDEFORMED_WELL_PRESENT`；页首的来源越界没有随之解除。 | 保留有来源的宏观／壳修正分解及其条件；撤回无明确计算链的固定降能、极小／势垒数值和稳定性裁决。不能只增加“模型”标签便视为完成验证。 |

以上为所读文本与已更正 source 的归属冲突，不等于已证明这些参数化在所有模型中均不成立。没有新算 PES、重建微观壳修正或扫描参数，也没有据 source 更正否定所有形状共存／TSD 研究。

**脚本风险：已报告主代理，代码未改**

只对以下三个知识页所点名脚本进行了有界文字检索，没有运行、导入或完整算法审计：

| 脚本 | 已看到的状态 |
|---|---|
| [cranked_triaxial_shape_coexistence_pes_engine.py](/workspace/wiki/system/scripts/analysis/cranked_triaxial_shape_coexistence_pes_engine.py:28) | 壳修正以局域 Gaussian 势谷参数化；顶部 lines 39–46 仍有形状交叉的物理解释和 BM 归属。正面边界也已存在：预设及结果标有 `synthetic_model_benchmark`，报告输出使用 “Model crossing detected”。不能把这个脚本概括成完全未区分 synthetic 与实验；顶部归属仍需负责代码的代理复核。 |
| [triaxial_hexadecapole_deformation_wobbling_modifier.py](/workspace/wiki/system/scripts/analysis/triaxial_hexadecapole_deformation_wobbling_modifier.py:11) | 顶部 BM 归属、lines 24–27 的惯量修正及 κ₄≈1.85、函数默认参数，以及 line 193 “strictly reproduces Bohr-Mottelson quadrupole rotor” 的措辞仍在。现有扫描不足以认证这些物理归属或数值。 |
| [triaxial_superdeformed_pes_strutinsky_engine.py](/workspace/wiki/system/scripts/analysis/triaxial_superdeformed_pes_strutinsky_engine.py:267) | 顶部有 BM 归属；输出仍包含 `STABLE_TRIAXIAL_SUPERDEFORMED_WELL_PRESENT`，line 280 的 CLI 提示为 “Load experimental preset”。这些标签可能继续把条件模型结果包装成实验或结构判决，需主代理分配代码修正；本任务没有改动。 |

**已有验证与未完成项**

已完成：三页全文读取、BM2-9/10/13 当前 source 条目对照、精确引用／关键词检索、三个点名脚本的相关文字定位。未完成：知识页更正、代码完整审查、计算重放、测试及修改后检查。不存在可宣称通过的数值验证。

若后续恢复，优先在上述三页内传播已存在的来源更正，保留可定位的模型定义，撤回未建立计算链的数字身份；脚本交给主代理协调。当前不自动继续。

本次未修改知识页、raw、代码、PLAN、index、handoff、其它 session 文件或既有报告；未使用 get-paper，未 commit。
