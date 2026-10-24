---
type: source
title: "NNDC当前LOGFT：质量Q、绝对分支与EC/β+输入合同"
title_original: "LogFT Help and LogFTDataServlet"
aliases: [NNDC LOGFT current interface, LOGFT输入合同]
created: 2026-10-24
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
source_type: public-calculator-interface
reading_depth: read
authors: [NNDC]
year: 2026
canonical_source: https://www.nndc.bnl.gov/logft/help.html
citation_key: ""
raw_file: raw/software-reference/day21-20261024/nndc-logft-help.html
raw_sha256: cc466141f516a8c126818294e751c81afe64b572104b4851a413689ca9e4d7ec
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [100Sn, 100In]
methods: [beta-decay, logft, electron-capture]
tags: [software-interface, input-identity, absolute-branch, day21]
---

# LOGFT：先匹配输入含义，再比较输出

## Bibliographic Record

实际访问NNDC的[Help](https://www.nndc.bnl.gov/logft/help.html)、[计算页](https://www.nndc.bnl.gov/logft/)和页面链接的`js/logft-index.js`。Help自述使用RadiationReport项目的LogftCalculator，程序由Jun Chen提供；本次未取得服务器代码commit或历史可执行版本。2026是访问年份，不是软件首发年份。

Help原始HTML与UI脚本暂存`tmp/day21-checkpoint102/`；frontmatter的raw_file为未写入的归档槽，hash对应实际暂存Help。当前网页及请求/响应身份见本run的`logft-current-interface-099.json`、`logft-contract-result-102.json`和四个`logft-current-*-102.json`。未修改raw或Bib。

## Scope and Reading Depth

完整读取短Help正文及相关前端输入、输出和请求逻辑；只核当前公开接口，不声称读完服务器实现。四项声明中央输入的条件计算均实际返回HTTP200、success=true，原始响应文本与SHA256已保存。未输入测量误差，未产生实验CI；未回放2010/2016的原LOGFT作业。

## Summary

当前接口的Q值是母子核基态能差，另输入初/末态能量。EC/β+模式的强度是每100次母核衰变进入指定子态的绝对概率，输出再分EC和β+。这与正电子最大动能、相对γ强度是不同对象。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LOGFT26-1 | Help把Q定义为母子核基态能差，并要求另输入母/子态激发能；EC/β+模式的transition intensity为每100次母核衰变进入指定子态的绝对强度。 | method-input-definition | direct-interface | Help Q-value and transition intensity paragraphs | true |
| LOGFT26-2 | Help要求NDS末位数字误差格式；UI以JSON字段parent_q_value、daughter_energy_value、transition_intensity_value等请求LogFTDataServlet，返回logft与EC/β+数值。当前代码版本不由网页名称确定。 | interface-and-version-boundary | direct-interface | logft-index.js getFormData | true |
| LOGFT26-3 | 声明单通道控制A=100、Zparent=50、Ei=Ex=0、强度100%，以构造Q=Ekin+2me输入：Ekin=3.29MeV/T=1.16s得logft=2.62、EC13.3/β+86.7；3.74MeV/T=1.17s得2.86、EC9.49/β+90.5。Q和100%强度是控制假设，非新质量/分支测量。 | declared-calculator-result | direct-response-with-task-assumptions | response endpoint374 values | true |
| LOGFT26-4 | 将3.74MeV控制的Q与子态能量同时加1000keV，返回的values对象完全相同；保持总T与端点、将绝对分支从100%改50%，logft从2.86变3.16，EC/β+分别4.74/45.3。输出已舍入，不反演未舍入f或新误差。 | input-contract-control | direct-response-with-task-assumptions | response endpoint374_branch50 values | true |
| LOGFT26-5 | 当前控制的logft中央数与两学位论文打印值相同，只支持定义/中央量级对账；不认证原端点拟合、母核分支、模型quenching或历史程序版本。新增软件计算也不是独立核实验。 | comparison-and-independence-boundary | explicit-task-inference | response endpoint329 values | true |

## Analytical Reconstruction

用`Q−Ex+Ei=Ekin,max+2me`构造固定端点的控制。这里的Ex=0是计算参考选择，不能写入100In实测能级表。保持能差不变的共同平移应不改可用相空间；保持总半衰期而将分支减半，部分半衰期加倍，因此logft增加log10(2)≈.301。实际服务器输出3.16−2.86=.30符合其打印精度。

脚本`system/scripts/day21_checkpoint102_logft_contract.py --fetch`只在缺少已保存响应时查询；默认模式离线核验请求、原始响应hash和四项控制。未对响应原文件进行数值改写。两个端点的EC份额不同，因此仅β+积分不能自动代替EC/β+总相空间。

## Competing Interpretations and Limitations

与[[hinke-2010-100sn-decay-spectroscopy]] HK10-D21-R99-2和[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]] LB16-D21-R99-3的logft在两位小数相同，不等于原job被复现。服务端数值精度、程序版本、历史选项和原输入误差未得；原谱形、共同响应与母核分支也未从网页控制中恢复。

旧078的168/304与105.5%认证仍撤回。当前控制不能给旧误差模型补CI，不能因为数值匹配就消除不同实验之间的潜在系统差异。

## Knowledge Impact and Learning Decision

`supports`：当前公开接口可实际执行声明单通道计算；`revises`：从仅知道输入合同推进到真实程序响应与归一控制；`limits`：历史版本、实验输入和淬灭裁决仍未闭合。原source review/flags不改变，新claim均needs_review=true。

## Related Knowledge and Project Relations

- methodological-bridge：[[experimental-claim-boundaries]]，区分接口、模型计算与原实验反演。
- limits：[[100sn-gamow-teller-independent-evidence]]，中央数值对账不作新增独立实验。
- not-direct-evidence：[[hinke-2010-100sn-decay-spectroscopy]]、[[lubos-2016-100sn-neighboring-nuclei-decay-spectroscopy]]，当前接口不能替代两篇论文的实验记录。

## Human Review Triage

P0: none identified；合成Q/100%分支明确隔离为控制，未写成测量。P1：历史版本/EC约定、原母核分支及jointCov仍缺；精确f或原误差重算前需这些输入。citation key未取得，不改Bib。

## Extracted Pages

只建当前接口source并关联现有方法/项目；不新增核素、能级、实验或模式页面。
