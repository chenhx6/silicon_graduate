# Ch3实际校准量化前冻结

已完整文本/视觉读Ch3/PDF44–72/printed41–69，31图8表11式均核；有Ch4–6/F23/publiccode的强priming，非盲测。现在只核actualsource输入：Eq3.9 roundedcoeff[-2.7,.54,-.084]与Fig3.19 fullprintedfit[-2.703,.5367,-.08448]在1300/7333keV的ε(分数，不是百分数)；source低能实测+Geant高能归一1.80(.06)不是7333实测。声明β.077及θDS120/145/176的Dopplerenergy带入ε差别仅演示lab/rest角色，不推原job采用哪种或source偏差。

Eq3.6 literal把r=Bρq/(mc)放1/sqrt(1−r²)；与从p=Bρq得到sqrt(1+r²)的exactenergy比，在实际referenceBρ.95和源constants mkg=4*1.673e−27/mc2=3728/q2*1.6e−19/c2.99e8下给名义差。公共Brho_Ekin_conv被VAMOS调用，函数body尚未新读，下一定向开body核是否同printed式，不能预设public/native必错或修原expr。

Table3.5几何r24/48,z95的边缘角及smallangle与source12.8/24.5比较，只条件数学；Fig3.14 105与298/580、Table300/640、public119.8/23各版本保，不强配shift解释。Table3.7四象限FWHM转σ，σθ.35与∆φ22.5不可互称Gaussianstd。全部是校准合同，不新BR/τCI或重建event接受。
