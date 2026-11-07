---
type: research-note
title: "E3轨道允许性与集体性的边界：精确角向控制"
aliases: [octupole orbital angular audit, E3单粒子选择规则]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, campaign-g05-rong-2023-96zr-mdc-cdft]
created_from: project
promotion_target:
tags: [octupole, angular-momentum, selection-rules, cross-region, l4]
---

# E3允许耦合是否已经意味着八极集体性

## Research Trigger

本轮使用的旧八极跨区综合，将πp1/2↔g9/2列为E3驱动轨道对，
并把Δl=Δj=3写成守恒定则及“单粒子矩阵元必达极值”。
这会改变对A≈100机制的判断，须先在确定的单粒子表示中核查。

## Grounded Evidence

[[book-suhonen-from-nucleons-to-nucleus]]本次实际核读
printed29–30、121–124、127–128（PDF44–45、136–139、142–143），
依据Eqs2.27–2.29、6.18、6.23及Table6.5。
[[campaign-g05-rong-2023-96zr-mdc-cdft]]的Fig4/PDF7讨论
πp3/2↔g9/2与νd5/2↔h11/2，是具体模型中的候选驱动，
不是πp1/2↔g9/2。原件与代码/输出哈希见运行provenance。

## Assumptions

球形单核子轨道，s=1/2，Condon–Shortley约定，归一化球谐算符Y3q；
将有效电荷和径向积分完全因子化，不假定各轨道实际径向重叠相等。
表中的角向B是
\(B_{\rm angular}=B(E3)/(e_{\rm eff}^2|R_{fi}^{(3)}|^2)\)，
无量纲；径向积分为零时只讨论形式上的角因子，不作除法测量。
没有输入真实核占据、配对、价空间相互作用或有效电荷。

## Provisional Reasoning

E3必要条件为异宇称及
\[
 |j_f-j_i|\le3\le j_f+j_i,\quad
 |l_f-l_i|\le3\le l_f+l_i,\quad
 l_f+l_i+3\ \text{为偶数}.
\]
对本表示，约化角向元的模方也可写成
\[
 |A_{fi}|^2=
 \frac{1+(-1)^{l_f+l_i+3}}2
 \frac{7(2j_f+1)(2j_i+1)}{4\pi}
 \begin{pmatrix}j_f&3&j_i\\-\frac12&0&\frac12\end{pmatrix}^{\!2}.
\]
这里只给模方，不据此认证所有CS/BR或ls/sl有符号相位转换。

| 初轨道→末轨道 | Δl / Δj | 精确B角因子 | 对当前问题的含义 |
|---|---|---|---|
| p1/2→g9/2 | 3 / 4 | 0 | 旧驱动指定违反j三角关系 |
| p3/2→g9/2 | 3 / 3 | 5/(6π) | 角向允许，但不证明真实占据或集体性 |
| d5/2→h11/2 | 3 / 3 | 25/(33π) | 同上 |
| f7/2→i13/2 | 3 / 3 | 1225/(1716π) | 同上 |
| g9/2→j15/2 | 3 / 3 | 98/(143π) | 同上 |
| p1/2→d5/2 | 1 / 2 | 3/(4π) | Δl=Δj=3不是必要条件 |
| d3/2→f5/2 | 1 / 1 | 3/(10π) | Δj=1也可允许 |
| s1/2→f7/2 | 3 / 3 | 1/π | 单一Δl/Δj标签不定义通用极值 |

以上是本任务精确模型结果，不是新的实测B(E3)。
表中规定了初末方向；反向约化元模方相同，B须改变初态简并分母。

## Falsification or Reverse Tests

脚本 `system/scripts/octupole_orbital_selection_audit.py` 用三条路线交叉核对：
逐磁量子数CG/Gaunt展开、轨道到j的6j重耦合、上述3j模方。
共10对轨道、42个初态磁投影均检查各自总强度各向同性；
另查反向约化模方、同宇称禁戒和j求和不足的负例。
Terra独立复跑发现输出路径的provenance错误，总控修正相对路径解析后重跑；
数值核查和产物生成成功分别记录，原失败不抹去。

标准重放需要SymPy1.14.0；本轮在仓库内被忽略的独立venv安装，
不修改系统Python。运行结果在
`outputs/l4/20261107-nuclear-structure-campaign/angular-selection/`，
其中 `angular-results.json`、`angular-pairs.csv`、`run-provenance.json`
保存精确表达式、检查和版本。输出不是原始实验数据。

## Competing Explanations

球形单粒子禁戒不排除经过其它轨道、变形组态或多体有效算符的响应。
相反，角向允许也不能保证宏观八极：能隙大、径向相消、占据或配对阻塞、
以及多体振幅相消都可能减弱它。哪些效应支配目标核需要实际模型输入。

## Transfer Conditions

可跨区迁移的是张量选择规则与完整矩阵元的因子化检查，
不是把某对轨道的角因子当成一整个质量区的B(E3)。
迁移时必须补上目标核径向、组态、相互作用和电磁算符。

## Failure Conditions

本控制不能推导真实核静态β3、形状势垒、寿命、全球首次或统一强度门槛。
未核径向或占据时停止在允许性判断，不将这一次纠错升级为新的核区禁戒。

## Open Questions

对N=56链，哪些多体相干项解释真实E3/E1而不是仅给允许性？
需要共同波函数的E2/E3/E1预测与绝对矩阵元，不能凭单粒子表决定。

## Human Review

无新增人工审核事件。P0: none identified in this scoped model。
P1：真实核应用、有效算符和相位必须另核；本轮只认证角向模方与选择规则。

## Promotion or Rejection History

2026-11-07：撤回旧专题的错误轨道对和通用增强/阈值断言，
控制与边界已并入[[octupole-collectivity-microscopic-matrix-elements-cross-regions]]。
不将数学规则的局部核验称为所有核素八极机制已解释。
