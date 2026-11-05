# 129Ba：原始证据、能量定标与未标定观测量检验

日期：2026-11-05。完整A≈130研究goal继续active。本批完成原件和计算的
可追溯检查点，**没有形成已经证明新颖、可投稿的物理结论**。
可复用知识在
[研究笔记](../../../knowledge/research-notes/ba129-model-input-and-holdout-contract.md)、
[模型合同](../../../knowledge/models/paired-single-j-positive-bcs-rotor.md)
及对应source页；本目录保存运行、审查与交接工件。

## 本批结论

能量最优参数不能自动提供可靠的电磁预测。指定单j正能BCS模型中，
放宽场强上限60→120 MeV只把最佳能量RMS从39.9955降至39.9252 keV，
却明显改变共同EM尺度和分支预测。预先冻结的一组尺度标定之后，
其余五组分支未能同时描述。独立核查又发现舍弃的Nambu耦合不够小，
因此失配尚不能被解释为对真实形状或整个PRM模型族的排除。

等谱/EM对偶已有1975明确先例；1998的同一(d,t)实验也早已用于波函数约束。
新取得的DAE68两页TPSM报告进一步关闭了“尚无微观129Ba模型比较”的候选空间。
值得继续研究的具体问题是：**受偶芯、占据和算符约束的同一波函数，能否同时
描述能谱、转移及所留出的电磁分支？** 方法名称或又一条能谱曲线不构成创新点。

## 原件进展

- Gizon1977：完整13页PDF；p.466 Table1已视觉核验。365.0/461.8两行的
  A4确为正，原误差大于2014评价；两个版本独立保存，不当作两次实验。
- Bucurescu1998：完整18页；偏振130Ba(d,t)129Ba实验、相对转移归一、
  映射转移算符及多轨道IBFM先例已核读。无逐点强度误差，不构造虚假显著性。
- Byrne1992：完整28页，核读相关实验方法/表格/讨论；Table1说明符合强度已
  作角关联校正。由分支和pure-K/等Q假设导出的δ/B比不作为独立验证。
- Meyer-ter-Vehn1975 Parts I/II：按已有哈希从临时原件恢复raw的缺失文件，
  没有覆盖已有证据；核读对偶、算符及舍弃耦合的原式。
- Rouoof DAE68：完整两页已读；PDF卷年2024，INSPIRE出版登记2025，两层日期
  都保留。两幅图展示能量比较，未列数值EM分支；γ=0.150的规范不擅自补写。
- Bucurescu1991：Crossref确认身份与卷页；APS页面403、Harvest401，仍只有
  元数据。Stuch2000及1978误差修订边界继续存在，不重复声称已取得正文。

两次归档集合：

```text
raw/papers/gpt/query/20261105-ba129-model-readiness/manifest.json
raw/papers/gpt/query/20261105-ba129-model-precedents/manifest.json
```

出版社PDF、XML、正文提取和裁图保留本地；本目录没有这些全文/页图的公开复制。

## 实际计算与反检验

能量输入为十态，扣除首11/2态能量后九个相对能量；态序号、Δ=1 MeV及
参数范围明列在四份energy-fit-contract中。RMS是描述性指标，不是实验χ²。
全部七次能量初值和各自对偶共14组预测保存于
[observable-predictions.json](observables-v1/observable-predictions.json)。

用153.8/518.6光子比固定共同非负尺度；其余五对按
`r=a+eta*b`检验。独立惯量最佳能量解预测604.7/701.3=9.17447，
发表中心比为0.60833；157/678预测0.00031，中心比0.06658。
604.7/701.3的纯E2项本身为0.974149，非负M1无法把它减至中心值。
未把中心失配换算成置信水平，也未用这些结果换带或重拟合参数。

[诊断图](figures/energy_vs_observables.png)同时显示三个未碰搜索边界的能量
极小点，以及最佳独立惯量解的对偶转移分布。灰框是RI各自±1报价误差的
矩形投影，**不是置信区间**；转移面板只有模型能量，未画成实验态匹配。
矢量图和绘图CSV由`make_diagnostic_figure.py`生成。

[对偶审查](symmetry-review/audit.md)核对1975/1998先例和固定转移通道：
等谱与B值保持，signed Q及相位一致的E2/M1相对符号反转；
加/移除强度交换。固定移除通道的不同碎裂可用于条件比较，但裸h11/2
算符不描述全部9/2拾取，也未独立定标真实130Ba的配对真空。

[观测量审查结果](observable-review/audit-results.json)重查84个光子比、
源数据/态映射、相空间幂次、140个Nambu态诊断、140个有符号对角矩阵元
和42组相位关系。I=11/2最佳点的舍弃耦合谱范数为1.095091 MeV。
这些范数是近似诊断；不是新的能级、修正后拟合或误差条。

## 重放入口

从仓库根目录运行，例如：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B \
  system/scripts/ba129_energy_calibration.py \
  --contract outputs/l4/20261105-ba129-model-readiness/energy-fit-contract-free-inertias-C120.json \
  --output-dir tmp/ba129-replay-energy

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B \
  system/scripts/ba129_observable_predictions.py \
  --fit outputs/l4/20261105-ba129-model-readiness/model-fit-C60/energy-calibration.json \
  --fit outputs/l4/20261105-ba129-model-readiness/model-fit-free-inertias/energy-calibration.json \
  --fit outputs/l4/20261105-ba129-model-readiness/model-fit-free-inertias-C120/energy-calibration.json \
  --contract outputs/l4/20261105-ba129-model-readiness/em-branch-test-contract.json \
  --output-dir tmp/ba129-replay-observables

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B \
  -m unittest discover -s system/tests -p 'test_paired_single_j_*.py' -v
```

源ENSDF及其哈希必须存在；这不是不带原始证据的独立下载包。
`probe/`、`replay-review/`和`lifetime/`内的早期脚本是原运行快照，
部分保留原tmp输出位置；当前主入口以上述system/scripts为准。

## 角分布草稿与验证

`raw/writing/gpt/ba129-rank4-identifiability/`仍为exploratory/not-ready。
这次将原表版本、50个系数协方差情景及6个正布居存在性算例闭合到验证器；
δ=-2时共同非负母态布居最小margin倍数为原表1.85768、评价3.39629。
草稿重新编译为5页并视觉检查；正文仍只讨论条件一致性，未扩成多主题物理论文。

48项新模型测试通过；角分布独立Wigner/光子计算、GLS与数值细化检查通过。
最终lint、archive、boundary、preflight及Git范围结果记录在本目录验证/
发布回执中；通过这些检查不等于科学目标完成。

## 下一步

1. 对舍弃耦合作有物理态追踪的受控比较；先核清完整模型与正能近似的关系，
   不将形式二阶量直接补进能谱后声称修复。
2. 用邻偶核及单粒子/占据信息约束C、惯量和真空，再检查能量近似等价参数域
   的转移/EM范围；固定数据分工，所有重标定都登记。
3. 核IBFM原输入和TPSM参数约定，比较真实先例与新信息增益；若没有超出既有
   研究的稳健单点结果，继续其它A≈130候选，不用代码或PDF产量代替文章成果。
