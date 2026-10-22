## Active handoff — Day19 checkpoint096，实验设计证伪反例与最小清单排错机制

Same run/session/goal active；原2026-10-22 15:00上海研究截止不变。096基于Nolan、Régis与Suzuki构建三类伪高精度证伪反例：(1)快速定时未补偿PRD走时差（14 ps）致tau假偏23sigma，由清单第7项（PRF/PRD全能峰走时校准）排除；(2)RDDS未扣除慢feeding拖尾（0.35/25 ps）致tau假偏109sigma，由清单第5项（feeder重合门/DDCM）排除；(3)DSAM电子阻止偏高+25%致寿命偏低-20%、Qt虚高+11.8%，由清单第4项（IAEA实验停止数据库对账）排除。给出tau=5.0 ps在五类技术下的逐项可行性判决。

程序day19_experiment_design_falsification096.py共18项数学与决策控制通过；两篇canonical页面写回。writeback valid/unmapped空、lint0error/249warning、boundary/preflight/protectedhash/diffcheck通过。receipt096存证。旧088–090撤回仍有效，019–078待逐claim审核；无全部闭环。completed[]、partial[19,20]、next19/count18；未收束/授分/发布，不开Day21。

整卡4/4核心交付物已完成实际scope核验。距离15:00硬截止仍有约4.5小时充裕时段，保持active状态继续推进系统自检与跨主题交叉核查，按时间门规则不提前收束。
