# Mixed-partner Cov推导前预测（冻结）

- frozen_at: 2026-10-16T22:49:37.917559+08:00
- priming：已读SG19原件Sec3.2、全部主线及既有shared-event方法；不是盲测。
- 预期：同一批physical events被多次配对，partner数增加会减小配对随机性，但不能把固定事件样本的所有方差变成1/pair entries。分母与prompt共享events还给cross Cov，忽略它不保证保守或激进。
- 拟固定的chosen模型：每个独立physical event有二元(X,Y)，p(X=1)=.35、p(Y=1)=.60、Cov(X,Y)=.02；H(X,Y)=1[X=Y]定义一个coarse pair bin。固定N；prompt取同event，mixed每个X从其它N−1个events无放回选K个Y partners。不是实际GRIFFIN angular kernel/时间窗/efficiency。
- 要验证：全配对mixed是U统计量；Var随K出现非零event-level floor；需同时推Var(prompt)、Var(mixed)、Cov与比值的delta传播。若投影恰好退化，floor可能消失，必须给出反例条件而非绝对化。
- 不回写本文件；来源/计算后纠正另存knowledge/report。
