# Day23 checkpoint018：Day24无学分preview的135Nd真实export输入

原run2026-10-25-day-23-01/session01a172fd-cbfb-7a13-b715-cfa0c479e08e，deadline2026-10-26T15:00:00+08；run_date仍25、goalactive/Farmer2698。completed=[] partial=[23,24] next23，Day24恰好无学分预习、Day25不打开。本run正式信用只Day23；还有12h+，继续至原15:00后才收束，不因checkpoint结束。

018官方IAEAv0 fields=gammas/levels&nuclides=135nd实际均200，gammas168/levels94非空，各1全空尾record严格忽略，nonempty宽度错误仍拒。两CSV分别tmp/day23-originals/iaea-nd135-gammas-018.csv SHA153f5735282b2ce8cc7932f38d0a9aa14d604704fa82177123922c25c4af65b4、levels018 SHAaccf66c5f5fb5d5d6dbdaeaf57336b9f2141b57de819cc07d836050ca70aca93；raw未新增/覆盖、正式archive deferred。cutoff22Jan2008，Extraction2026-10-25，不是2026新实验/评价。guide实际RTPW=WeisskopfUnits，不能裸比MU07μN²/e²b²。sourceAPI字段外部身份新增MU07-D24P-001–003而非MU07新实验；ZH03-D24P-001保原图版本。

新script day24_preview_nd135_export_identity.py实际CSV14controls过：IDs/核素/全部端点energyJπjoins/重复unc_hl列12+15/clock/nearline身份。648 ID(59,52,2)31/2->29/2 vs649.2(60,52,1)33/2->29/2；590(66,60,1)35/2->33/2 vs591(66,59,2)35/2->31/2，不能能量近就合并！原ZH03 Fig2打印648/591等先保留，不据API判原paper错/强绑定2007图marker。

声明历史A/B sameI候选，API31/2…39/2 E_B−E_A=356.8/280.8/184.1/118.1/95.2keV仅中心算术，不是新split/CI/静态chirality阈值。4006.7与4008.1虽然只差1.4keV却分别B31/2/A33/2，不可当sameI伙伴。APIhalf_life是T1/2不是meanτ：例如Bidx59T1/2 1.012ps /ln2≈1.46；Aidx55 .52/ln2≈.7502。10candidate与MU07TableImeanτ中心最大差.0044ps，只同源/评价链中心相容、非独立复测或uncertaintyverification。relativeI100不是absolutebranch/completebudget。226 ID(59,56,0)mixing_ratio字符串+.14、uncmr空、adoptednotes/phase缺，不认证physicalδ；不恢复225.8 P正号/16.3h方案。δ/Q/g/τCI/beamtime没新造。

实际targeted回核Mu07PDF1setup/2methodTableI/3graphroles，freshvisual2/3、SHA9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425；ZH03原PDF4Fig2/ΔI文字freshvisual/SHA8dd7aaa0a2e369532dd673384bcc18c60abc330408f20243939b31df15d98542。未新全读4/10页。图marker/component/branch不闭合仍保；旧MU07-8/9/10/16的quantities全conditional，未借API提升认证。Nuclearchirality概念追加partnerresolved map分energy/B/geometry/g（此对无可绑定dualpartnerg，128Cs不迁入）。

fresh boundary/lint/diff/exportidentity0，true报告/28changed知识页writebackvalid，lint0error/220warning/182旧citation债务。Git指针main · Day23: bind preview observables to135Nd endpoints and clocks；actualH3/hash看task-publication-receipt018。

下一同一个Day24preview高信息route：原adoptednotes或作者publicarxivsource archive，以解决MU07图中outgoing/inband组件绑定。**inflight exec64415请poll同handle**，查询NuDat3 getdataset.jsp?nucleus=135ND&unc=nds 与OpenAlex DOI10.1103/PhysRevLett.99.172501 OA/arxivlocations，输出tmp/day23-originals/nd135-primary-input-discovery019.json。若publisher/dns失败保 typedaccessbound，不改凭据/无限重试；若NuDat200实际看notes/timeversion。若发现arxiv原source，publictar仅tmp，先list+rejectabsolute/.. /symlink/etc再safeextract，不runTeX或scripts；可能含原fig/EPS/data可检查精确marker/元数据，但不擅当原events。无新input保持notready，不按τbudget判paper错。普通archive/νAPI是原始证据旁证，非newacquisitionvote。

01759antiunitary/twolevel controls的数学/physicalg边界、Day23Pr/Au所有calibration/SH26支持、011operator及旧QtCI/225.8撤回保持。raw/PLAN/Bib/旧flags/Day21/22credit/继承untracked/114隔离producer保护；Day24不正式audit/credit、不Day25。只在原15:00后正式Day23audit/原runnerreceipt/nextprep/H3。
