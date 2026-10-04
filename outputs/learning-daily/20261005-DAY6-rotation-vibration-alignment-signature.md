# 2026-10-05 Day 6 — 转动、振动、alignment 与 signature

## Run state

- 计划：Day 6，nuclear-structure-framework；运行标识 2026-10-05-day-06-01；study window 截止 2026-10-06 15:00（Asia/Shanghai）。
- 恢复：原 session 01a10816-f550-7003-bb53-8dfafc2c18a2 在用户要求停止后留下 interrupted 回执；本轮按用户指令恢复该 session。恢复命令：codex resume 01a10816-f550-7003-bb53-8dfafc2c18a2 -C /workspace/wiki -s danger-full-access -a never。
- run-01 事件日志显示停止前已读计划和近期记录、完成主动回忆、核读 Liu 1996 全文并检查 Fig. 15；没有日报或知识写回。该中断不计作 Day 6 完成。
- 本次按两槽候选池完成连续性与新颖性工作，并在两者都达到证据饱和后提前收尾；不延长为第三个问题。学习结论与验收见下文。

## Candidate pool and selection

| 候选 | 近期香港覆盖与预期信息增益 | 选择 |
|---|---|---|
| 连续性：131Ce Bands 1–7 的 signature/configuration coupling 能否与振动或其它集体模式区分？ | 当前开放问题要求 mixing ratio、偏振、寿命和伙伴带绝对强度；Day 3 已整理 mean-field 与模型适用边界，Day 4 已覆盖 pairing/crossing，Day 5 已覆盖形状观测量。Day 6 的转频重建可把能级证据接到可测的模式判据。 | 选。沿用现有 131Ce 项目与原始 thesis 数据，不新建重复项目。 |
| 新颖性：A≈130 奇奇 h11/2 带的 signature inversion 对 bandhead spin crosswalk 有多敏感？ | Liu 1996 汇集 La/Pr/Pm/Eu/Cs 多核素，展示奇数 ΔI 重标可改变 signature 顺序；Cs 的相互冲突参考为独立于 131Ce 的系统学边界。 | 选。只研究自旋锚点和系统学，不把不同核素拼成 131Ce 的直接证据。 |
| Band termination 判据 | Afanasjev 1999 提供固定组态、有限最大自旋和 collectivity 衰减的综述判据。所选 131Ce 带没有本轮可核的 termination 端点。 | 作为练习的边界参照，不另开第三个案例。 |

**来源前主动回忆：** 转动带是同一内禀结构上随角动量增加的能级序列，低自旋时常以 I(I+1) 作为理想参照；振动带对应形变自由度的量子振荡；alignment 是准粒子角动量沿转轴的投影，数值依赖转频和参考转子；signature 是转 π 的离散对称标签，signature inversion 表示两支能量偏好随自旋反转。我记得 131Ce Band 1 的两支 crossing 约为 0.329 和 0.367 MeV/ℏ，但不确定 Table 5.1 的误差，也不确定能否从现有来源得到逐点 i_x(ω) 或 termination 证据。后续核到的表值、定位和误差见下节。

## Sources and evidence

| Wiki 来源与原文 locator | 证据层 | 本轮核实及边界 |
|---|---|---|
| [Davidson 1965](../../knowledge/sources/davidson-1965-rotations-vibrations-deformed-nuclei.md)：DV65-1，printed pp.105–146；DV65-2，printed pp.129–146。DOI [10.1103/RevModPhys.37.105](https://doi.org/10.1103/RevModPhys.37.105)。 | 集体模型综述 | 形变表面坐标量子化为振动 phonon，稳定形变产生转动带；odd-particle、Coriolis 和 decoupling 改变能带系统学。它是理论背景，不是 131Ce 的观测证据。 |
| [Stephens 1975](../../knowledge/sources/stephens-1975-coriolis-rotation-alignment.md)：ST75-1，PDF pp.43–44 Eq. (1)；ST75-2，Secs. II–III；ST75-3，Sec. IV。DOI [10.1103/RevModPhys.47.43](https://doi.org/10.1103/RevModPhys.47.43)。 | Coriolis 与 alignment 综述 | Coriolis coupling 可混合邻近 K 带并改变 alignment、signature 和 backbending；blocking、配对和形变共同影响 crossing。它没有唯一指定某个 crossing 的组态。 |
| [Alwaleedi 2013, 131Ce](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md)：AW13-14，PDF p.63 Table 4.1；AW13-5，Table 5.1；AW13-4，Table 5.3；AW13-9，Eqs. 5.6–5.7；AW13-11，Chapters 3–5 方法盘点；AW13-18，Eq. (2.25), Table 4.1。DOI [10.17638/00015073](https://doi.org/10.17638/00015073)，本地 PDF SHA-256 为 B50C22877418DE560F06002588BB46D34F5BA670C6880E30A89D1509C79AD8C1。 | 实验能级/跃迁；派生 crossing；作者组态解释 | 100Mo(36S,5nγ) 在 165 MeV、Gammasphere 数据建立 Bands 1–7。按原文 Eq. (2.25)，每条 ΔI=2 E2 跃迁用 Eγ/2 给出转频，定位于跃迁中点；Table 4.1 能量误差未列。Table 5.1 将 Band 1 的负宇称两个 signature crossing 列为 0.329±0.002 和 0.367±0.002 MeV/ℏ。作者称其由实验 Routhian 提取，不能由单个 Eγ/2 点直接等同；都不是直接形变或振动测量。 |
| [Liu et al. 1996](../../knowledge/sources/liu-1996-signature-inversion-a130.md)：LU96-1，Tables I–II；LU96-2，Fig. 15；LU96-3，PDF pp.729–730；LU96-4，Table II；本轮新增 LU96-5，PDF p.729 Sec. VI.C。DOI [10.1103/PhysRevC.54.719](https://doi.org/10.1103/PhysRevC.54.719)；本地原文 SHA-256 为 ca3e1c1bc834158112dee525fa4c42c3d44596975a506f3a2a1da023580a346f。 | 已发表能级的系统学重标；独立模型计算 | Table I 中 13 个已有 bandhead spin 指认有 11 个被修改，且这 11 个改变量都是奇数；Fig. 15 在作者新指认下显示讨论核素的低自旋 signature inversion。Table II 对 Cs 保留不相容方案。Liu 汇编旧实验而非新 acquisition；Tajima 的模型参数拟合过 124Cs、I0=7 的同一参考，不能当作该自旋锚点的独立验证。 |
| [Ma et al. 1990, 131Ba](../../knowledge/sources/ma-1990-131ba-competing-alignments.md)：MA90-2，PDF pp.725–728 Figs. 5–7/Table II；MA90-5，PDF p.725 Eq. (2)/Fig. 5。DOI [10.1103/PhysRevC.41.717](https://doi.org/10.1103/PhysRevC.41.717)；原文 SHA-256 为 a0dbdd4957d1d11af570b5daffc9c44609d9ef5ed570dc3ad32a67388dad90de。 | 不同核素的直接谱学与派生 alignment | 131Ba 的 crossing 与 Harris alignment 作方法对照。其 119Sn(12C,4n) 实验与 131Ce Gammasphere 谱不同，不能当成 131Ce 的独立验证。 |
| [Afanasjev et al. 1999](../../knowledge/sources/afanasjev-1999-termination-rotational-bands.md)：AF99-1，PDF pp.4–7、33–39；AF99-2，PDF pp.33–40、43–95。PII S0370-1573(99)00035-6。 | 终止转动综述 | termination 指固定组态的集体转动连续走向该组态有限的最大 aligned spin；须联合能量、alignment、转动惯量和 Q_t/B(E2) 变化，排除 crossing、混合及统计不足。未在本轮 131Ce 序列上判定 termination。 |

**网络与原文核验：** Crossref 返回 Liu 的作者、题名、期刊、卷期页码和 DOI，与本地 PDF 一致；出版商 APS abstract URL 返回 HTTP 403。Google Scholar 检索请求失败，未把检索结果用于证据。论文主文 PDF 在仓库内可读，Liu 页 719–730 已沿摘要、spin-systematics 方法、La/Pr/Pm/Eu 与 Cs 赋值、Tables I–II、Figs. 1–15、模型比较和结论通读；Fig. 15 图像已渲染目视核查。原文特别说明 124Cs 的 I0=7 与 130Cs 的 I0=9 不能同时成立，并给出 130Cs I0=11 的另一方案。

## Theory/analysis exercise

**概念判读。** 转动序列通常依赖共同的形变内禀结构，能量可近似随 I(I+1) 增长；振动序列来自 β/γ 等形变自由度的量子激发，需用多声子能量和跃迁强度模式检验。仅有规则能级、近简并或高自旋 crossing 都不足以把带命名为振动、wobbling 或 chirality。alignment 描述准粒子对总角动量的贡献；signature splitting/inversion 描述按 signature 分支整理后的相对能量变化，不是唯一机制的标签。

**从 131Ce Table 4.1 重建自旋—转频点。** 原文 Eq. (2.25) 对 ΔI=2 转移定义 ℏω=Eγ/2，频率位置取跃迁自旋中点。将 Table 4.1 的 Eγ 从 keV 换成 MeV，得到一支 Band 1 序列：

| 跃迁 | 中点自旋 | Eγ | ℏω=Eγ/2 |
|---|---:|---:|---:|
| 15/2→11/2 | 13/2 | 507.9 keV | 0.25395 MeV |
| 19/2→15/2 | 17/2 | 641.2 keV | 0.32060 MeV |
| 23/2→19/2 | 21/2 | 749.3 keV | 0.37465 MeV |
| 27/2→23/2 | 25/2 | 825.4 keV | 0.41270 MeV |
| 31/2→27/2 | 29/2 | 780.6 keV | 0.39030 MeV |
| 35/2→31/2 | 33/2 | 691.4 keV | 0.34570 MeV |

频率随跃迁中点自旋上升至 25/2 后下降；Table 4.1 未给这些 γ 能量的不确定度，故只报中心值。该走势提示能带偏离简单刚性转子系统学，但单个转移序列不定位 crossing 来源。Table 5.1 另从实验 Routhian 提取 Band 1 两个 signature 的 crossing：0.329±0.002 和 0.367±0.002 MeV/ℏ。它们不是由单个 Eγ/2 点直接算出；表中未给两 crossing 的协方差，故不计算差值误差。Table 5.1 的 Band 2 两 signature 都列 0.316±0.002 MeV/ℏ，但其负宇称标签与 Figure 4.1、Tables 4.5–4.6、§5.2.2 冲突，本轮隔离该 parity 单元，不据此得出结论。

**alignment 参考项复算。** Ma 1990 Eq. (2) 的参考转子为 I_ref=J0ω+J1ω³，J0=11.90 ℏ² MeV⁻¹，J1=21.1 ℏ⁴ MeV⁻³；用 x=ℏω（MeV）后，I_ref/ℏ 的数值表达式为 11.90x+21.1x³。将作者报告的 131Ba 两 signature crossing 代入，得：

| ℏω | I_ref/ℏ | 仅传播报告的 crossing-frequency 误差 |
|---:|---:|---:|
| 0.415±0.003 MeV | 6.447 ℏ | ±0.068 ℏ |
| 0.445±0.003 MeV | 7.155 ℏ | ±0.073 ℏ |

微分使用 d(I_ref/ℏ)/dx = 11.90+3×21.1x²；J0/J1 拟合协方差未在 source page 给出，表中误差只来自 crossing-frequency 项。I_ref 是参考转子角动量，不是总自旋，也不是独立测量的 alignment gain；完整 i_x 还需同一频率下的带自旋和一致的参考。

**band termination 判据。** 需要固定组态下可追踪的有限最大 aligned spin，并同时看到转动/能级斜率、alignment、moment of inertia 与 Q_t 或 B(E2) 的相容演化；低强度末端跃迁、能带突然中止或单个 backbend 都不能单独证明 termination。AF99 的例子属于综述系统学和模型解释，不将其外推为 131Ce 的已观测终止带。

## Counter-evidence and missing companion observables

- Liu 1996 的结论随 bandhead spin crosswalk 变化：多数有旧自旋指认的 La/Pr/Pm/Eu 带中，11/13 个 I0 被改动且全是奇 ΔI；odd ΔI 会交换偶/奇自旋对应的 signature 标记。作者采用平滑同位素系统学支持改标，但平滑趋势本身是 systematics prior，不是新的直接自旋测量。
- Cs 仍无唯一锚点：文中称 124Cs I0=7 与 130Cs I0=9 无法同时满足平滑曲线，并列出 130Cs I0=11 的另一重建。Tajima 对 124Cs 的计算吻合不能解决此问题，因为模型参数拟合于同一 I0=7 数据。
- 131Ce 的 crossing/alignment 约束作者的准粒子组态解释，却不能单独区分 Coriolis mixing、配对/形变演化与振动响应。Band 4 的 γ-vibrational 标签是作者解释；611.1-keV Band 4→Band 1 link 为 M1/E2 指认，但本 thesis 无逐跃迁测得的 δ、线偏振、寿命或 partner-resolved 绝对 B(E2)/B(M1)。
- 必要伴随量：可靠自旋/宇称与带身份、完整带间 links、混合比两个分支和偏振、匹配自旋区间的寿命与绝对 B(E2)/B(M1)，以及能支持形状判断的 quadrupole observable。测量后须用同一 transition matrix 区分 signature/configuration coupling 与集体振动；若讨论 wobbling/chirality，还需相应 out-of-band E2、伙伴身份和随自旋模式能量。
- 源独立性：Alwaleedi 是一套 100Mo(36S,5nγ) Gammasphere acquisition；Liu 是多篇旧谱学的汇编；Tajima 是独立模型路线但模型参数依赖 124Cs 的同一自旋假设；Ma 是 131Ba 的不同反应/实验，仅作 alignment 方法参照。

## Knowledge Impact and Learning Decision

**Decision: revises。** 对 A≈130 signature-inversion crosswalk 的知识边界作了窄幅修订：除 I0 重标和 Cs 参考未决外，加入“模型与其拟合锚点共享 124Cs I0=7，因此不能独立验证该锚点”的来源定位。对 131Ce 的排序维持：已有能级、crossing 和作者组态解释支持普通 signature/configuration coupling 为可行基线；尚无寿命/偏振/partner-resolved 绝对强度，不能把带标签升级为振动、wobbling 或 chirality 的实验结论。未改变任何页面的 human-reviewed 状态，也未清除 needs_review。

## Durable knowledge delta

- [Liu 1996 source page](../../knowledge/sources/liu-1996-signature-inversion-a130.md)：新增 LU96-5，记录 Tajima 的 Cs 参数拟合依赖和非独立 spin-anchor 边界。
- [Alwaleedi 2013 source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md)：新增 AW13-18，保存原文 Eγ/2 转频定义和 Table 4.1 的跃迁中点自旋—转频复算。
- [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：修订 signature-inversion crosswalk 行，把同一 124Cs spin assignment 的拟合依赖纳入 evidence boundary。
- 复算表、来源依赖关系和停止条件同时写在本日报；可复用的转频复算与模型独立性边界已分别落入上述 source 和 project knowledge 页。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/liu-1996-signature-inversion-a130.md",
      "summary": "Added the source-grounded caveat that Tajima's Cs inversion-spin agreement is calibrated on the same 124Cs I0=7 anchor and therefore is not an independent validation of that assignment.",
      "anchor": "LU96-5",
      "sources": [
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "PDF p.729"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
      "summary": "Persisted the thesis rotational-frequency convention and the Band 1 transition-midpoint frequency reconstruction with the missing gamma-energy uncertainty boundary.",
      "anchor": "AW13-18",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "Eq. (2.25)"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "Table 4.1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Revised the A≈130 signature-inversion crosswalk row with the model-to-spin-anchor dependence boundary.",
      "anchor": "A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-5"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 131Ce Band 1 的 0.329/0.367 MeV/ℏ crossing 在统一带身份、reference 和偏振/mixing 约定下是否仍保留？若测得的 interband links 具有稳定且增强的 E2 强度，并由寿命给出匹配的绝对 B(E2)，可提高集体振动/摆动解释；若 links 以 M1 为主并随 crossing/组态演化，则普通 signature/configuration 解释更合适。
2. 哪一项独立自旋/宇称测量能排除 Cs 中不相容的 124Cs/130Cs 参考？若独立测得的 I0 改变偶奇自旋交错，将重排 Liu 图 15 的 favored/unfavored 标记，signature-inversion 结论及其 γ 解释须重新计算。
3. 是否存在具备固定组态、可达最大自旋和连续 Q_t/B(E2) 数据的 A≈130 候选 termination 带？在这些观测闭合前，本轮只采用 AF99 判据，不作目标核判定。

## L0–L4 state

- L0：写前 Wiki boundary check exit 0；保留原始 Liu/Ma/Alwaleedi PDF，不覆盖 raw。
- L1：本地全文、source page locators、Crossref 元数据和 publisher URL 状态已核对；Google Scholar/APS 的访问失败作为路由记录，未以摘要片段补结论。
- L2：完成 131Ce ΔI=2 跃迁中点的 Eγ/2 转频重建和 131Ba Harris reference 数值复算；能量行未报不确定度，Harris 拟合参数 covariance 缺失，按边界保留。
- L3：继续使用既有 131Ce collective-mode project 和 A≈130 thesis matrix；本轮没有新建研究问题或声称完成新 L3 milestone。
- L4：未进入。没有 event-level counts、共同 response/covariance package 和分析代码，不能做代理拟合或把派生曲线升格为原始实验事实。

## Verification and continuation

- 边界检查：写前运行 python3 system/scripts/wiki_boundary_check.py --root .，exit 0，errors=0、warnings=0。
- farmer：wiki_farmer.py status 显示 resumed session 正在运行；once --dry-run exit 0，actions=[]，用户请求停止没有触发自动故障续接。
- Wiki lint：python3 system/scripts/wiki_lint.py --fail-on error，exit 0，errors=0、warnings=91、info=1309。
- git diff --check：当前工作树检查 exit 0；暂存后还会对精确文件集重跑。
- 标题、单一 knowledge-writeback 块、3 个 anchor、4 个原子 locator、run-06 continuation prompt 和 Day 7 prompt 均已核验存在；原 run-01 中断回执和事件日志保留。
- 首轮终态回执暂记 publish-pending，里程碑暂未递增。完成 Gitee 精确 refspec 发布后再将 receipt 置为 completed、counted 并把 next_day_index 推进到 7。
- Day 6 达到两槽证据饱和后停止。下一日提示：outputs/learning-daily/prompts/20261006-DAY7-collective-motion-oral-exam.md。
