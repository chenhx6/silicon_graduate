# 真实源谱响应重放可行性前置回忆

本route延续实际NSCL7quad source/background归一问题，Day16/partial17，原19日15:00上海截止不变。当前只有measuredprocessedROOT，无现成MCtemplate；actualfit窗口1800–3000，README1540文字不同，simpleprimaryγ表最高1408.022而radioactivedecay有cascade/event。不能仅凭a差把高区叫sourcefree。

高信息下一步是先核公开geant4.11 branch与安装SDK11.4.2、几何/源/能分辨/sorting输入是否足够做**有版本限定的**source能谱response重放。不是Morse/L26exactproducer，不用它测δ/Q；新的code/leveldata/beaminput若与2012原物理实验不match，保留差别。

先锁真实branchsha、README/Makefile/build依赖并读代码，后编译；不执行带清理rm的原Makefile、不在root/raw写数据、不改全局env/credentials/SDK，不引新daemon。可生成repo tmp自己的CMake wrapper与工作目录。所有第三方/source/geometry/MCdata/binary都只tmp/hash。SDK已实际存在，UCGretina/grutinizer binary不存在。

若能跑，先小量smoke+energy/multiplicity/conservation/geometry/source-countsanity，再决定1e6级γ/decay MC与统计门；新input/seed必须先冻。两模式event分母不同，MCfinite统计/新Geant4核数据不等价2012exacttemplate。缺actualsortingdependency也要如实notready；最高价值仍可实际gamma spectrum/sourcefreewindow/共享Cov分析，不能捏造MC或追目标调geometry。

只研究source calibration/Compton计数response，不研究能级寿命/强度/Day18。
