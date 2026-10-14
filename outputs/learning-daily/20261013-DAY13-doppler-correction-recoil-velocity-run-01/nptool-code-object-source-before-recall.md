# Day13：NPTool public kinematics object 来源前记录

2026-10-14T10:24:01.484711+08:00

已读ZA23/AS21的particle-assistedentry和NPTool引用；publicrepository/代码尚未打开。

- 要核two-bodyreconstruction输入beam/target/light/重核mass、kineticenergy、angle与vertex/loss assumptions，以及返回的是哪一stage的velocity/Ex。
- 预测Lorentz4vector invariantmass可能给Ex和heavyrecoil，但不预设具体function/API或angle单位。测得proton输入和外部beam/mass/materialprior的条件依赖应分开。
- 查currentpublic源码对象是methodentry，不证明2017/2020experiment使用相同commit或productionconfig；必须pinupstreamcommit/文件hash和line locator，不能以latest代paper版本。
- 只读相关Physics/source/doc/license文件，在tmp保存公开副本，不build/execute第三方source、不改raw/PLAN/credentials、不为Wiki恢复Githubremote。
- 如果sourcecurrent只有Ex而无heavyvelocity接口，也只记实际范围；sourcecause/actualL4fit仍需experimentpacket。
- 对照本任务已做exacttwo-body/entrypoint的四向量和branch/Σ要求；避免重跑原toy或猜API语义。
