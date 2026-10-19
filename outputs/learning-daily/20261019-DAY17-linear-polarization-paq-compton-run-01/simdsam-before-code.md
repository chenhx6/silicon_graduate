# SimDSAM代码前回忆

已本session原读Kirsebom13pages/21fig/2table/4eq：旧MC是ROOT/C++，Geant4负责epsilon_gamma，不是全transport；alpha先出Au再Gaussian测量，actualE/DE/total排序仍待代码角色；植入层Eq4、点8°/beamspot13°、source95%limit/±sigmaShift/Forster同源已暴露。GitHEAD仅metadata21809a67ea9f3b0514cc57908659463f29b1e1ab，未读publiccode。

待查：版本/commit历史是否与paper匹配，mass/4momentum/GammaProperTime、alpha measuredenergy变量与Si是否显式、输出counts/ROOT/config/Σ是否真公开。PDFt=integralgamma ds/v与properclock需实际代码核，不凭公式猜实验错；新代码HEAD不预填paperexactproducer或移给Sun。保原输入/失败，不安装全局依赖、不执行未知build/install或大批history。
