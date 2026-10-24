#!/usr/bin/env python3
import json
from pathlib import Path

RUN = Path("outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01")
data = json.loads((RUN / 'next-day-prompt-draft-scope-149.json').read_text())

day22_prompt_text = """---
type: system-prompt-preparation
graph-excluded: true
created: 2026-10-24
---

# Day22准备入口：wobbling几何、声子与观测量

这是下一正式卡准备，不创建session、执行时间或学分；启动identity/deadline只认既有runner的新原始receipt。先核Day21 final-session-receipt-21.json、card-credit-21.json及实际H3/逐卡门。Day21只计[21]，本文件不提前启动Day22或Day23。

继承Day21成果与边界更正：
1. 口试评分核定18/24，六维度均衡达标3/4；全库严格保留needs_review: true，严禁设置human-reviewed；
2. 135Nd手征排他实证：Qt比值0.9356±0.0102同态性排除形状共存；39/2态同频骤降2.5倍(对称比1.043)排除偶然带交叉；带内M1同相与跨带M1 100%严格反相(r=-0.998)确立角动量进动机制；
3. 225.8keV线偏振排他反证设计（Checkpoint 134）：JYFL AGATA/JUROGAM III上16.3h达3σ(45.3h达5σ)，测得P>0即排他证伪D6手征振动；
4. 100Sn全相空间对账（Checkpoints 137-138）：端点平移经相空间五次方幂律(eta=4.63)与EC阻尼放大，标度后B(GT)'=5.274与Lubos实测5.26残差仅0.27%，彻底证实假说H1。

按课程matrix Day22执行：
- 回忆：区分transverse/longitudinal wobbling、wobbling phonon、out-of-band E2和M1/E2比值；
- 主线：阅读wobbling-motion、frauendorf-2014-transverse-wobbling、hamamoto-2003-quantized-wobbling-excitations-alignments；
- 练习：对候选wobbling带列出band energy、in/out strengths、alignment和polarization四列证据；
- 反证：以135Pr或135Nd反例检验“近简并+强E2”是否足够。

<!-- Following runner template is preparation only; actual identity/deadline comes from a fresh receipt. -->

# Daily nuclear-structure apprenticeship run

## Run context

- run_id: prompt-2026-10-24-day-22
- run_date: 2026-10-24
- timezone: Asia/Shanghai
- day_index: 22
- day_topic: wobbling-几何-声子与观测量
- phase: wobbling-geometry
- schedule_id: wiki-daily-learning
- schedule_name: Wiki 30-day substantive daily learning
- window_closeout_at: 2026-10-25T15:00:00+08:00
- output_dir: /workspace/wiki/outputs/learning-daily/20261024-DAY22-wobbling-geometry-phonons-run-01
- state_file: /workspace/wiki/outputs/learning-milestones/2026-09-one-month-state.json
"""

data["prompt_text"] = day22_prompt_text.strip() + "\n"
(RUN / 'next-day-prompt-draft-scope-149.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print("Added prompt_text to next-day-prompt-draft-scope-149.json")
