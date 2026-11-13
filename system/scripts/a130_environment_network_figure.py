#!/usr/bin/env python3
"""Conceptual network for A130 section4.8; no measured level scheme or rate data.

Sources and physical conditions are recorded in section-4-8.json and the
corresponding knowledge note. Labels7-/1- identify only the176Lu example;
positions, arrows and box sizes carry no numerical energy or rate information.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def box(ax, xy, width, height, text, color, size=9):
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.02",
                 facecolor=color, edgecolor="#3b4b5a", linewidth=1.1))
    ax.text(xy[0]+width/2, xy[1]+height/2, text, ha="center", va="center",
            fontsize=size, linespacing=1.6)


def arrow(ax, start, end, label="", offset=(0,0)):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color="#435565", lw=1.3))
    if label:
        ax.text((start[0]+end[0])/2+offset[0], (start[1]+end[1])/2+offset[1],
                label, ha="center", va="center", fontsize=9)


def main():
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10,
                         "svg.hashsalt":"a130-environment-network-v3"})
    fig=plt.figure(figsize=(10.4,8.8), layout="constrained")
    grid=fig.add_gridspec(2,2,height_ratios=[1.15,1.0])
    a=fig.add_subplot(grid[0,0]); b=fig.add_subplot(grid[0,1]); c=fig.add_subplot(grid[1,:])
    for ax in [a,b,c]: ax.set(xlim=(0,10),ylim=(0,10)); ax.axis("off")
    a.set_title("(a) Thermal exchange and loss", weight="bold", pad=12)
    box(a,(3.1,7.0),3.8,1.4,"Intermediate nuclear states\nThermal upward / downward rates", "#e8f3e6",8.8)
    box(a,(0.3,3.1),4.0,1.9,"Ground-band cluster $g$\n"+r"$^{176}$Lu example: $7^-$ ground state", "#e9f0fa",9)
    box(a,(5.7,3.1),4.0,1.9,"Isomer-band cluster $m$\n"+r"$^{176m}$Lu example: $1^-$ isomer", "#faeeea",9)
    arrow(a,(2.2,5.0),(3.5,7.0)); arrow(a,(6.5,7.0),(7.8,5.0))
    arrow(a,(4.3,4.4),(5.7,4.4),r"$a$",(0,.4))
    arrow(a,(5.7,3.7),(4.3,3.7),r"$b$",(0,-.4))
    arrow(a,(2.3,3.1),(2.3,1.8)); arrow(a,(7.7,3.1),(7.7,1.8))
    a.text(2.3,1.35,r"Loss $D_g$",ha="center");a.text(7.7,1.35,r"Loss $D_m$",ha="center")
    a.text(5,.15,"Equal loss cancels in the normalized fraction.\nFinite exchange time still limits equilibration.",ha="center",va="bottom",fontsize=9)
    b.set_title("(b) Distinct atomic-electron channels", weight="bold", pad=12)
    entries=[
        (7.3,"IC: bound electron emitted\n"+r"$E_e \simeq \Delta E_{\rm nuc}-E_b$"+"; occupied shell required", "#fff0e3"),
        (5.0,"NEEC: free electron captured\n"+r"$E_e+E_b\simeq\Delta E_{\rm nuc}$"+"; vacant shell required", "#e8f1fb"),
        (2.7,"NEET: bound electron changes orbital\nElectronic and nuclear transitions couple", "#e6f5ef"),
        (.4,"NEIES: free electron remains free\nInelastic scattering; nuclear excitation threshold", "#f2ebfa")]
    for y,text,color in entries:box(b,(.15,y),9.7,1.8,text,color,9)
    c.set_title("(c) Formation, survival and experimental acceptance", weight="bold", pad=12)
    box(c,(.15,6.5),2.8,2.0,"1. Capture\nBarrier transmission\n"+r"$\sigma_{\rm cap}(E,J_0)$", "#e6f3f1",9.5)
    box(c,(3.6,6.5),2.8,2.0,"2. Compound nucleus\nCompetition with quasifission\n"+r"$P_{\rm CN}(E,J_0)$", "#fff1e6",9.5)
    box(c,(7.05,6.5),2.8,2.0,"3. Evaporation and cooling\nNeutron / fission competition\n"+r"$W_{\rm sur}(E^*,J_0)$", "#eeecfb",9.5)
    arrow(c,(2.95,7.5),(3.6,7.5)); arrow(c,(6.4,7.5),(7.05,7.5))
    c.text(5,5.4,r"$\sigma_{\rm ER}(E)\simeq\sum_{J_0}\sigma_{\rm cap}(E,J_0)P_{\rm CN}(E,J_0)W_{\rm sur}(E^*,J_0)$",
           ha="center",va="center",fontsize=11)
    box(c,(.6,2.55),8.8,1.6,"Surviving entry-state ensemble $F$  "+r"$\longrightarrow$"+"  cascade feeding  "+r"$\bar b_{\rm feed}$"+"\nFinal isomer yield also depends on angular momentum and parity.","#f2f5f6",9.6)
    arrow(c,(5,4.85),(5,4.15))
    c.text(5,1.35,"Fixed flight time and a finite observation window give a conditional decay acceptance.\nCold-state hindrance, hot-nucleus survival and detected yield are different quantities.",
           ha="center",va="center",fontsize=9.4)
    c.text(5,.2,"Schematic only: box positions and arrows do not encode energies, rates or measured branching fractions.",
           ha="center",va="center",fontsize=8.8,color="#45555f")
    out=Path(__file__).resolve().parents[2]/"raw/writing/gpt/A130/these_2023_template/these_template/Img"
    out.mkdir(parents=True,exist_ok=True)
    fig.savefig(out/"environment-network-pathways.pdf",bbox_inches="tight",metadata={"CreationDate":None,"ModDate":None})
    fig.savefig(out/"environment-network-pathways.svg",bbox_inches="tight",metadata={"Date":None})
    plt.close(fig)
    print("environment-network-pathways: PDF and SVG exported")


if __name__=="__main__":main()
