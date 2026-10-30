# Day24 发布范围与路径审计 092

结论：**需要先修发布范围与若干现行科学转录/归属错误；研究可继续。** 这是 root 092 修正前的只读快照，不是课程收束或论文级科学通过证书。保持原 run/session、2026-10-27 15:00（Asia/Shanghai）硬截止；本审计未修改 canonical、raw、凭据、Git 或课程状态。

## 路径与安全 rehome

五个新根目录 worker 共 **13 文件**：080×3、081×3、083×2、088×3、089×2。此前中间消息估计14，已更正为实际13。根 `workers/` 不属于六目录合同；boundary exit0 只表示当前脚本覆盖项通过，不能覆盖脚本未检查的新增根目录。

`path-manifest-proposal.json` 给逐文件旧路径、精确新路径、字节数、SHA256及目标冲突状态。目标统一是：

`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/<原worker名>/<原文件名>`。

root 可按显式清单逐文件 rehome，先核旧 hash/目标无覆盖，再修活跃路径、相对链接与新 receipt hash，同时保旧→新及原 hash 记录。不递归删除；本 worker 不执行移动。080/081/083/089 的相对 `../../tmp`、`../../outputs` 链接不能在新深度原样沿用；JSON 自身 old 路径应区分历史快照与当前操作入口。

## 已重算的结构通过项

- 日报只有一个 `knowledge-writeback` block；45 items、45 unique knowledge paths；所有路径和 anchor 字符串存在。
- 771 个 source locator 引用全部在目标 source 中按原子边界找到；无缺失、无前缀冒匹配。这证明可导航，**不证明科学正确或独立**。
- 45 个目标中39个 source；36 unreviewed、3 human-reviewed。3页既有 human-reviewed 状态本身不是新增claim通过证书，未建议批量改旧 flags。
- 17个显式 `actual_body_file` 中15个存在且 SHA 与声明相符；2个指针失效但实源另名存在且 hash 匹配（见下）。这里只哈希 tmp，不读写 raw。

完整逐页状态、阅读范围记录、body hash 与 selflink 行在 `writeback-audit.json`。此检查不等于39篇全文重新阅读；root/fullread 资格只按实际读区说明。

## 发布前必须纠正或隔离

1. **原件指针**：Emediato 的 `actual_body_file` 应指向 `tmp/day24-emediato1997-ce133-rdds-072/publisher-direct-pdf.pdf`；Joss 应指 `tmp/day24-joss1998-133ce-triaxial-lifetime-078/publisher-pdf.pdf`。目前两个 `attachment-object-response.pdf` 不存在。文件102259/120604 bytes分别 hash 匹配，不是来源丢失。
2. **Hauschild1996 当前摘要/蓝本谱系**：source line45与蓝本line584的“独立”及“不重复票”仍会把1995/1996当独立事件；source line61已有正确同campaign说明。应把当前摘要明确改成同一116Cd+22Ne/31Ge数据的新增序列与重分析，仅相对Joss1998独立。保留087历史修正。
3. **HA96 布居**：HA96-D24-002 把3/5/6/7写成“.5–2%”；原文 printed614 明报每条约.5%。不能把band2的2%范围分配给另外四带。
4. **Joss 三处**：PDF2 TableI fresh visual确认999.3线的τSF=0.49±0.01ps，canonical `.49(.10)`错一位；PDF1实际人口次序132Ce:131Ce:133Ce=5:4:1，canonical当前语句顺序含混；PDF4分别警告 absoluteQt约10–15%阻停误差，不能说已包含于作者2.2±.1形式误差。JO98-D24-002还多一个`direct` cell，8列错位于7列表头下。
5. **母态错位**：蓝本line592把582.7/582out/out问题写到1809.1行；它属于1409.8。1809.1应保464.4及982.0 out/out候选、608.3 out/in和重叠门问题。现有其它表格已正确，不应让短crosswalk覆盖它们。
6. **080审计自身须修/隔离**：本worker也是080作者，现明确自纠。080把592.1/13/2−写成仅derived/unobserved，而现存adopted.ensdf line148给592.1(6)/13/2−和后续384.7/554.9 links。080 ledger line441误写Gizon1163.6→9/2，实际→13/2。报告只与现代608.3比，漏保旧1163.6→554.9/608.7 ↔ 现代1200.8→592.1/608.7的单边候选。报告line70“Emediato itself warns modern WK22…”是错误归因：这是本任务迁移推断，非1997作者的话。正确边界仍是无三母态τ、817.7 energy-only、582out/out缺，不扩wholeBand4。
7. **SI历史跳过**：081 report明确`--no-si`，manifest `si_requested:false`，发生在045自动SI规则后。不能把canonical“SI入口未识别”当已做发现检索或认定无SI；应保历史flag，执行有界官方SI发现或明确当前未请求/未核与scope。它阻止“完整资源已完成”认证，不自动否定有边界的主文科学。不要询问用户，也不假定SI存在。
8. **未完成durable写回**：081的Table1/136Nd逐线对照、083的具体逐band crossing/gain/候选832/847/934/1177 links与旧Qt>2.3 unpublishedRef12谱系，部分仍只在worker报告。root需挑有用行direct-primary核后补source ID/locator/writeback，或明确未采纳/临时；45paths/771tokens不能认证这些细节已写回。

以上每项的定位、条件和最小修法在 `findings.json`（PUB092-B01–B09）。它们是相应内容的发布门问题；不是要求停住全日等待，也不是说未知τ/producer/Cov必须先取得才能发布。

## 不阻塞但必须校准的表述

- 079/083 worker receipts支持其Ha96 fullbody/Figs1–9读取；本审计未证明 root 又独立全读。当前source“079完整读…表格”应去掉不存在的编号表，按实际读者区分全主线与root抽核。不从extraction/文件存在推rootfullread；也不反向断言已有记录的所有root全文读都是假的。
- 089的771/771结果属字符串/导航与metadata审计；其“scientific verified no-op/no defect”不能覆盖092找到的原件指针、母态、数值与归属问题。保历史报告，追加092限定即可。
- NNDC/Butler/Emediato/Joss/Ha95/Ha96尾部`Day24...link`指向自己，Singh也有一处selflink；冗余清理可随触及处理，单独不阻塞。
- 001 publication manifest 是旧checkpoint范围，不是本轮最终45页清单。原文/PDF/整页图继续不进发布manifest；原session/resume与版权/凭据/raw保护照旧。run.json旧partial[]和continuation1不要假造新runner历史，正式收束再按真实状态对账。
- 未知三母态τ、817.7 observedreference、582denominator、实际producer/response/Cov及1991正文access gap均为可发布的科学partial；不因此开Day26或授Day25信用。

## 输出

`path-manifest-proposal.json`：13文件安全rehome建议；`writeback-audit.json`：45目标/39source inventory；`report-writeback-coverage.json`：五worker的唯一知识边界；`findings.json`：blocking/nonblocking；`receipt.json`：本审计范围与hash。
