# Unit 039 — $^{225}$Ra/$^{225}$Ac 跨来源一致性收敛审计

## 检查范围

只读核对两份已归档 ENSDF source、016/028/030/033/036 JSON/Markdown、相关 research-note 与原 raw 哈希。未修改现有文件。

## 通过项

- 两份 raw SHA-256 与 source 页、030/033/036 工件一致：Ra `93ce30628f3f24d08bc1e69c47d2c96e739748868fd03407ddbede9e4732e31e`；Ac `fb3d87428e000397881227c3dc96973c1765310a7811062cc8c297259872a817`。
- E1 评价值在各工件一致：Ra 0.00081(20) W.u.，Ac 0.00171(15) W.u.。
- $A=225,r_0=1.2$ fm 的 $1$ W.u.($E1$) $=2.384497\ e^2\mathrm{fm}^2$；W.u. 到绝对 $B$、$B$ 到约化矩阵元的 $(2J_i+1)$ 因子和数值均一致。
- 正逆方向简并因子一致：Ra $B_\mathrm{rev}/B_\mathrm{fwd}=2$，Ac 为 1。
- CG² 和条件 $D_0$ 一致：Ra $C^2=1/3$、$|D_0|=0.155792\pm0.019234\ e\mathrm{fm}$；Ac $C^2=0.6$、$|D_0|=0.168719\pm0.007400\ e\mathrm{fm}$。
- 036 的窗口计数与 030 level 输入一致：Ra 3/8/15，Ac 6/9/11（50/100/200 keV）。

## 发现的一项措辞不一致

`knowledge/research-notes/parity-doublet-e1-unit-boundary.md` 将 Ra E1 字段的来源概括为“$^{225}$Ra β− decay 链中的转换电子来源”。归档 Ra ENSDF 的 L31.56 注释实际写的是该能级寿命来自 $(\alpha)(ce)(t)$ in $^{229}$Th $\alpha$ decay (1985Is03)；Ac 的 40.09-keV E1 注释才明确写 `from L-subshell ratios in ^225Ra β− decay`。数值 `BE1W=0.00081 20` 字段本身未受影响，但 provenance 句子应在后续修订时按 raw 注释拆开。该单元不修改原文件。

## 物理边界

所有 $D_0$ 都是给定 $K$、CG 和半径约定后的条件转子反演，符号未知，不能写成实测内禀偶极矩。最近能级与能量窗结果是评价 level list 的候选计数，A–D 带标签不等于实验带连接；没有原实验 γ 连接、寿命、E1/E2/E3 和微观组态信息，不能选定物理宇称双重带。016 中其他目标核的 null 字段与本单元 Ra/Ac 评价数值不冲突。

完整机器可读检查与状态见 `parity-doublet-cross-source-consistency-039.json`。本单元未抓取网络、未运行全库 lint、未暂存、提交或推送。
