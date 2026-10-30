# 027 阶段性记录：完整 136Nd 谱学身份已核，正文未取得

**状态：staged / stopped at two-route limit，body0；不是 whole-source-unit complete。** 新检索和下载路线已停止。当前只确认文章身份和一条机构提供的明确 PDF 链接，尚不能回答它是否补足 D5/D5-C 的 BR、δ、绝对 B，或是否仅提供更完整的 γ 纲图。

## 已核准的目标身份

**B. F. Lv et al., “Evolution from γ-soft to stable triaxiality in 136Nd as a prerequisite of chirality,” Physical Review C98,044304(2018)**，DOI **10.1103/PhysRevC.98.044304**，Crossref publication date **2018-10-05**。

Fresh Crossref exact DOI（HTTP200 JSON，20711bytes，SHA256 **6aa5cb19d38d22d0a8afe02d23e8b11914ca6373f36c3be531bd7ac5da3be486**）核准完整题名、作者与刊文信息。该题名不同于 PE18 *Evidence of Chiral Bands in Even-Even Nuclei*，不能把本篇当旧“假SI”或其同一六页 reprint。

Scoped Wiki 查到 LV19 Ref38 和 LV25-20 对 PRC98,044304 的引用，没有找到该确切题名的独立 source；raw 文件名检索也未发现该篇原件。另定向检查 tmp/day23-originals、tmp/day23-theses 的文件名未命中。这不是对所有未命名文件的穷尽扫描。

官方 arXiv exact DOI API 返回0条。OpenAlex exact DOI 指出 APS、JYX、Warsaw、HAL 等记录，其中 JYX 提供当前明确文件链接；OA标签只作路径线索，不是已下载正文的证据。

## 两条正文获取路线与现场结果

| 路线 | 实际请求 | 结果 |
|---|---|---|
|1. 官方出版社 PDF|`https://journals.aps.org/prc/pdf/10.1103/PhysRevC.98.044304`|HTTP **403**, text/html，5498bytes，非PDF；SHA256 **137b037a564f35b9662fe5ec5092997967248014da89e333ebebaebfdc7aab72**|
|2a. 有明确机构线索的 JYX record|`https://jyx.jyu.fi/handle/123456789/60029`，跳至 `https://jyx.jyu.fi/jyx/Record/jyx_123456789_60029`|HTTP **200**, text/html，53035bytes；SHA256 **de194086186928c2956ca87e47602f9bf48ac452cbabd151f793818df5cd0a7a**。记录名称与DOI相合，文件标为 **Publisher's PDF**|
|2b. 沿该 record 的实际文件链接|`https://jyx.jyu.fi/bitstreams/3d0af0a2-40db-464b-a3d5-1cf666530c82/download`|curl exit **52**, **Empty reply from server**，HTTP **000**；未收到可验证正文，没有PDF文件/SHA/页数|

2a/2b 是同一 JYX 获取路线的 landing→实际文件链，并非另加第三条泛搜。到此两条路线限额用完；没有重试 Tonev、旧SI、APS相同失败请求或其它新端点。

JYX record 所列永久标识是 `https://urn.fi/URN:NBN:fi:jyu-201810224470`；它的书目和 abstract 提到 JUROGAM II+RITU+GREAT、level-scheme extension 及配置分析。**这些是机构 metadata/abstract，不是已读正文。** 不据摘要填 transition table、精确实验选门或 EM 结论。

## 实际读取范围与未决项

- **正文0页、0图、0表、0式**。无PDF signature验证，无版本正文比较；JYX“Publisher's PDF”目前仅为record标签。
- D5/D5-C 是否有新增 component-resolved BR、signed δ 或 absolute B：**unknown from body**。
- 39个探测器如何分角组、实际 active detector数、事件选择和count定义：**unknown from body**。
- 与PE18/LV19是否共享同采集：现有其它源提供谱系线索，本次不能由相似事件数/仪器表述认证；尤其**same selected events / same gate / same producer**均未建立。
- PE18 Ref34当时待出版的完整谱学是否在逐参考/图表层确实对应本篇：题名、时间和LV19Ref38给出强候选线索，**还未取得本篇正文完成引用/内容crosswalk**。
- 不能把2018新长文发表自动计为另一独立采集，也不能把metadata中的“full scheme”误写成已闭合所有实验δ/τ/absolute B。

## 给 root 的阶段性交接

目前能写回的最多是**exact bibliography + access gap**，没有新增实验或模型科学claim。两条已查路线及JYX实际链接已固定在回执；只有访问状态或明确新原件发生改变时才有理由重开，不用继续当前端点循环。

现有 PE18-D25P-001–003 的“假SI撤回、D5真实ratio支持、其它partner缺EM”的记录继续保持。当前body0既不能补强为已得完整D5branch/δ，也不能削弱成“长文不存在/没有方法输入”。相同5.1×10^10事件数只能提示全campaign范围，不能证明同一selected histogram或response producer；这一方法边界不依赖本次未取得的正文。

`receipt.json` 汇总metadata、两条路线、现场错误和body0读取范围；各原始响应只在 `tmp/day24-nd136-fullscheme-027/`。所有输出只在本worker前缀。canonical/raw/PLAN/Bib/Git、session、课程状态与学分不变；编号027是worker/checkpoint，**不是课程Day27**。仍sameDay24run＋恰好Day25无学分preview，Day26未开。


## 单次明确授权的 transport retry 补记

2026-10-26T14:49:33Z，对已由机构 record 给出的**同一个 exact bitstream URL**作了一次 `curl --http1.1` 重试；连接上限8秒、总上限45秒，无自动 retry、无新URL或索引查询。结果仍为 **curl52 / Empty reply from server / HTTP000**，没有响应体、content type、有效PDF签名或bodySHA。

原 `body-route2.json` 和原阶段 `receipt.json` 保留；新增 `body-http11-single-retry.json` 记录此次失败，`receipt-after-http11-retry.json` 汇总最终状态。**正文仍0页/0图/0表/0式，whole-source-unit未完成。** 此 exact endpoint现停止。方法/transition表/39角组/activecounts/D5 EM与same-selected-producer问题全部保持unknown，不以transport失败推断论文内容或机构授权。
