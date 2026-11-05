---
type: plan
graph-excluded: true
created: 2026-11-01
updated: 2026-11-01
status: provisional
review_status: unreviewed
topic: "133I quasi-continuum gamma-strength-function and low-energy-enhancement test"
knowledge_anchor: "knowledge/research-notes/133i-low-energy-gamma-strength-function-candidate-20261101.md"
---

# `133I` γSF/LEE 束流申请草案

## Physics case

`133I` 位于 A≈130、接近 `N=82` 的奇质量区。申请检验的大胆假设是：

> 在 `133I` 的准连续区，`Eγ≲2 MeV` 存在可重复的低能 γSF 增强，并且该增强
> 具有可由额外观测量约束的 dipole/M1 字符。

竞争解释包括 E1 或混合偶极辐射、剪刀式 M1 尾部、非统计 feeding、离散强线泄漏
以及低能阈值、summing、unfolding、NLD 或自旋分布造成的伪上弯。申请不预设
单一微观机制。

## Reaction and source lineage

公开 OCL 记录和 Book of Abstracts 已经给出 `130Te(α,pγ)133I`、SiRi–OSCAR
粒子–γ 装置和 γSF/NLD 提取路线，并明确实验已经进行
（[[indico-2026-133i-gamma-strength-record]] `OCL26-1`, `OCL26-2`）。目前仍没有
公开 γSF 数值、LEE/M1 结果、event-level producer、response 或 covariance。
因此第一优先级是取得现有 acquisition 的完整分析与响应包；只有现有数据缺少关键
低能响应或 dipole-character observable 时，才提出独立新运行。复用原 acquisition
不增加实验独立性。

束流能量、靶厚、束流强度、`133I` 产额和 channel competition 需要由反应模型和
小规模 commissioning 先给出。本文不填入未经计算的 rate、beam time 或 sensitivity。

## Minimum observable contract

1. 记录 event-level α/质子/γ 时间、能量、位置、触发和 live-time。
2. 在至少两个不重叠的初始激发能窗口提取 NLD 和 γSF。
3. 对 `Eγ<2 MeV` 保存阈值扫描、效率、summing、随机符合和离散强线污染模板。
4. 以 `3–4 MeV` γ 区及已知 E1/M1 参考跃迁作为响应和多极性控制。
5. 记录并验证两个窗口的 population contrast：用 SiRi 粒子能量/角度和反应运动学
   建立自旋分布 proxy，并用已知离散线或 Hauser–Feshbach/evaporation 扫描检验；
   不能把两个粒子门自动称作两个独立自旋族。
6. 增加 γ 角分布或 Compton 偏振；若既没有可验证的 population contrast，也没有
   独立 dipole-character observable，结果只能保留为 L3 γSF 观测，不能标成 M1。
7. 预留一个未参与主 fit 的 excitation window、control line 或独立 reaction
   path 作为 holdout。

## Detector and acquisition

首轮可采用与 SiRi–OSCAR 兼容的粒子–γ架构，外围加入可标定的高分辨 γ/偏振
子系统。若使用 `DRAGON-X`，应选择 high-resolution/polarization mode，而不是
同时启用 neutron 或 implantation 模块。必须保存：

- 低能 γ 的 detector-pair、阈值、summing 和 response matrix；
- 粒子 ΔE–E/TOF、门条件、随机窗口和污染 PID；
- run-by-run gain、效率、deadtime/livetime 与 shared calibration covariance；
- unfolding regularization、NLD/spin prior 和两个 excitation windows 的共同 nuisance；
- Compton `Q(Eγ,θ,ξ)` 或角分布 acceptance；不能用名义 clover 数代替。
- particle-gate → population-contrast mapping、其模型不确定度和与 γSF response
  的共享 covariance；若该映射不能验证，population contrast 只作为未闭合设计变量。

## Analysis and falsification

主分析使用 response-folded count/γSF likelihood，至少比较：

- `H_LEE,M1`: 低能增强并由 dipole/M1 响应支持；
- `H_LEE,dipole-unresolved`: 低能增强存在但 E1/M1 未分辨；
- `H_response`: 增强由阈值、离散 feeding、NLD/spin 或 unfolding 解释。

所有模型共同 profile 低能效率、summing、PID leakage、deadtime、NLD/spin、
population-contrast mapping 和窗口选择。若增强只在一个窗口存在，停止
Brink–Axel transfer 判断；若增强在响应折叠后消失，给出 sensitivity-limited null；
若增强保留但 population contrast 和偏振/角分布均不足，保留“γSF LEE candidate”
而不升级为 M1。

## Calibration and go/no-go

申请前必须获得：

- `Eγ<2 MeV` 的 source/in-beam efficiency 和 threshold scan；
- particle–γ random、beam-off/target-only 或等价背景控制；
- 已知 E1/M1 参考线的角分布或偏振 response；
- 两个粒子/激发窗口的 population-contrast closure，以及该映射的 nuisance/Covariance；
- 两个 excitation windows 的共同 response/Covariance 账本；
- 反应率、靶耐受、数据量和 deadtime 预算。

缺少低能 response、NLD/spin alternatives 或 holdout 时，停止在
`candidate-L4/readiness`，不生成 `133I` γSF、`B(M1)`、显著性或 Bayes factor。

## Deliverables

通过 feasibility gate 后，正式申请应补齐：

1. 反应模型和 beam-energy scan；
2. target-specific yield/rate range；
3. SiRi–OSCAR 与 γ/偏振几何；
4. calibration/response/Covariance manifest；
5. beam-time estimate；
6. blinded holdout 与 three-outcome belief-revision table。

当前状态：`provisional L3`, `unreviewed`, `not ready for final beam-time submission`.
