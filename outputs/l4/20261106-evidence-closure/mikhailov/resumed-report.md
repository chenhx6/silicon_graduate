# Mikhailov 冻结范围收尾

状态：已完成本轮限定更正与验证；不代表冻结前的全局研究目标完成。

- 严格推导两种合法旧参数化：第一模块旧 z_gamma=a2；第二模块旧 t=2a2/(1−2a2)，BM z2=t/(1−t)。保留旧函数、键名与标量分支惯例，明确其意义。
- 修正第二模块 4g/2g 因子为 (1+8t)/(1+t)，保留全部实反演分支、零比值合根以及 z2/t 坐标极点对应的有限 a2 解。较大根的弱混合有效性不能由代数解自动认证。
- 耦合能 h2=epsilon2 ΔE（keV）；原文输入不足以由一条强度比确定 epsilon2，撤回旧换算并返回 null。撤回结构分类、软度物理归属、预设的实验身份与普遍压低断言。既有原书 source 与原始材料不改。
- 10 项受影响单元测试通过：独立 J² 对角化 CG、零混合、映射往返、双分支、坐标极点及错误输入。两脚本 text/JSON 共 4 次 CLI 检查通过，定向 git diff --check 通过。完整 dispatcher 只读核对接口，未运行全库测试。
- 此前 partial/freeze 回执保留；7 个目标的冻结哈希与编辑前 HEAD 基线一致。无新来源、新模型、raw/PLAN/get-paper/共享 index/handoff 修改，无 commit/push。效率增益未作对照测量。

精确文件清单（本轮仅这 9 个文件）：

- `knowledge/methods/bm2-rotational-intrinsic-coupling-and-mikhailov-contract.md`
- `knowledge/concepts/gamma-vibrational-band-mixing-and-mikhailov-z-gamma-parameter.md`
- `knowledge/concepts/davydov-rostovsky-triaxial-band-mixing.md`
- `system/scripts/analysis/gamma_band_mixing_z_gamma_alaga_inverter.py`
- `system/scripts/analysis/davydov_rostovsky_triaxial_band_mixing_solver.py`
- `system/tests/test_gamma_band_mixing_z_gamma.py`
- `system/tests/test_davydov_rostovsky_mixing.py`
- `outputs/l4/20261106-evidence-closure/mikhailov/resumed-report.md`
- `outputs/l4/20261106-evidence-closure/mikhailov/resumed-checks.json`

数值与证据边界已同步进入上述三份 knowledge 页面；逐项检查与最终目标哈希见 `resumed-checks.json`。
