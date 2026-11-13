#!/usr/bin/env python3
"""Band-label networks for section4.5, not level schemes on an energy scale.

78Br uses Liu2016 Fig. 1/textPDF2–4;74As2022 uses Xiao2022Fig. 1/PDF3.
The2019 negative-parity labels are intentionally not mapped to2022Band3.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family":"DejaVu Sans","svg.hashsalt":"a130-br-as-network-v4"})
    fig,axes=plt.subplots(1,2,figsize=(11,7.2),layout="constrained")
    def box(ax,x,y,text,fill):
        ax.add_patch(FancyBboxPatch((x,y),4.1,2.5,boxstyle="round,pad=.05",
                     fc=fill,ec="#4c6072",lw=1.2))
        ax.text(x+2.05,y+1.25,text,ha="center",va="center",fontsize=9,linespacing=1.6)
    def edge(ax,a,b,label,xy):
        ax.plot([a[0],b[0]],[a[1],b[1]],color="#45687d",lw=1.5)
        ax.text(*xy,label,ha="center",va="center",fontsize=9,
                bbox={"fc":"white","ec":"none","pad":2})
    for ax in axes:ax.set(xlim=(0,10),ylim=(0,13));ax.axis("off")
    a,b=axes
    a.set_title(r"(a) $^{78}$Br: Liu et al. (2016) labels",fontsize=11,weight="bold",pad=12)
    box(a,.3,9.1,"Band 1: positive parity\n"+r"Assigned $\pi g_{9/2}\otimes\nu g_{9/2}$"+"\nFig. 1 extends to "+r"$(20^+)$", "#e7effa")
    box(a,5.6,9.1,"Band 2: positive parity\nChiral-partner candidate\n"+r"$9^+$ to $13^+$", "#e7effa")
    box(a,.3,3.8,"Band 3: negative parity\n"+r"Assigned $\pi f_{5/2}(p_{3/2})\otimes\nu g_{9/2}$"+"\nFig. 1 extends to "+r"$(19^-)$", "#fbece7")
    box(a,5.6,3.8,"Band 4: negative parity\n"+r"Lowest $6^-$; top $(14^-)$"+"\n404.3-keV link from "+r"$7^-$", "#fbece7")
    edge(a,(4.4,10.35),(5.6,10.35),"Links",(5,10.8))
    edge(a,(4.4,5.05),(5.6,5.05),"Links",(5,5.5))
    edge(a,(2.35,9.1),(2.35,6.3),"8 reported\n"+r"$E1$ links",(2.35,7.7))
    a.text(7.5,7.7,"Other cross-parity links\nnot reported here",ha="center",va="center",fontsize=8.8)
    a.text(5,1.95,"Partner assignments are interpretations.\nA missing line is not a measured zero rate.",ha="center",va="center",fontsize=9)
    b.set_title(r"(b) $^{74}$As: Xiao et al. (2022) labels",fontsize=11,weight="bold",pad=12)
    box(b,.3,9.1,"Band 1: positive parity\n"+r"$6^+$ to $(16^+)$"+"\nChiral-doublet candidate", "#e7effa")
    box(b,5.6,9.1,"Band 2: positive parity\n"+r"$7^+$ to $(14^+)$"+"\nChiral-doublet candidate", "#e7effa")
    box(b,.3,3.8,"Band 3: negative parity\nFig. 1 includes low "+r"$5^-,6^-$"+"\nExtends to "+r"$14^-$", "#fbece7")
    box(b,5.6,3.8,"2019 thesis labels\nNegative Bands 3/4\nNo unique 2022 label mapping", "#f0f0f0")
    edge(b,(4.4,10.35),(5.6,10.35),"Links",(5,10.8))
    edge(b,(2.35,9.1),(2.35,6.3),"3 reported "+r"$E1$ links"+"\n372.4,919.4,1293.4keV",(2.35,7.7))
    b.text(7.5,7.7,"Thesis and journal\nshare experimental lineage",ha="center",va="center",fontsize=8.8)
    b.text(5,1.95,"The historical thesis box has no connecting edge:\nit does not identify a journal partner band.",ha="center",va="center",fontsize=8.8)
    fig.suptitle("Reported links, assigned configurations and version boundaries",fontsize=12,weight="bold")
    for ax in axes:ax.text(5,.35,"Schematic positions; parentheses retain tentative spin assignments.",ha="center",va="center",fontsize=8)
    out=Path(__file__).resolve().parents[2]/"raw/writing/gpt/A130/these_2023_template/these_template/Img";out.mkdir(parents=True,exist_ok=True)
    fig.savefig(out/"br-as-network-topology.pdf",bbox_inches="tight",metadata={"CreationDate":None,"ModDate":None})
    fig.savefig(out/"br-as-network-topology.svg",bbox_inches="tight",metadata={"Date":None})
    plt.close(fig);print("br-as-network-topology: PDF and SVG exported")


if __name__=="__main__":main()
