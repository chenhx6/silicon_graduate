#!/usr/bin/env python3
"""Conceptual joint-prediction map for section3.8; no new experimental data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({"font.family":"DejaVu Sans","svg.hashsalt":"a130-joint-predictions-v3"})
    fig,ax=plt.subplots(figsize=(9.2,7.4),layout="constrained")
    ax.set(xlim=(0,10),ylim=(0,10));ax.axis("off")
    def block(y,h,color):
        ax.add_patch(FancyBboxPatch((.15,y),9.7,h,boxstyle="round,pad=.02",
                     facecolor=color,edgecolor="#45536b",linewidth=1.2))
    def text(y,s,size=10,weight="normal"):
        ax.text(5,y,s,ha="center",va="center",fontsize=size,weight=weight,linespacing=1.6)
    text(9.65,"Joint predictions and complementary measurements",12,"bold")
    block(6.95,2.15,"#e9edfa")
    text(8.7,"I. Explicit model, fitted inputs and independent predictions",10.5,"bold")
    text(8.12,"Orientation and shape coordinates; quasiparticle space; conserved quantum numbers",9.5)
    text(7.64,"Potential, inertia, pairing and effective operators, with stated assumptions",9.5)
    text(7.18,"Intrinsic trajectories and basis components remain model representations.",9.3)
    ax.annotate("",xy=(5,6.5),xytext=(5,6.92),arrowprops={"arrowstyle":"->","lw":1.4})
    block(3.95,2.5,"#e7f3f0")
    text(6.04,"II. Correlated observables and data held out from fitting",10.5,"bold")
    labels=["Energy sequence\nCrossings and\nstaggering","Lifetimes and rates\nBranching, ICC\nand shared errors","Angular response\nMixed amplitudes\nand phase conventions","Spin dependence\nAlignment and\nconfiguration change"]
    for x,s in zip([1.4,3.8,6.2,8.6],labels):
        ax.text(x,4.98,s,ha="center",va="center",fontsize=9.2,linespacing=1.55,
                bbox={"boxstyle":"round,pad=.4","fc":"#ffffff","ec":"#5b8e84"})
    text(4.18,"Joint response and covariance are needed; derived quantities are not independent experiments.",9.0)
    ax.annotate("",xy=(5,3.5),xytext=(5,3.92),arrowprops={"arrowstyle":"->","lw":1.4})
    block(.3,3.15,"#faf0e9")
    text(3.1,"III. Concrete transitions test specified model implementations",10.5,"bold")
    text(2.46,r"$^{98}$Mo: weak $E3$ candidates at 1833.3 and 1585.8 keV"+"\nLifetime plus complete same-mother branches tests enhancement versus a weak denominator.",9.4)
    text(1.68,r"$^{102}$Ru: separate $E1$ and $M1$ responses"+"\nNRF branching and two-phonon decay strengths constrain different interpretations.",9.4)
    text(.89,r"$^{135}$Pr: the 747.3-keV $17/2^-\to15/2^-$ link"+"\nCompare absolute electromagnetic predictions, root branches and model-input uncertainty.",9.4)
    text(.02,"Conceptual map; arrows do not encode causal proof, measured rates or statistical significance.",8.6)
    out=Path(__file__).resolve().parents[2]/"raw/writing/gpt/A130/these_2023_template/these_template/Img"
    out.mkdir(parents=True,exist_ok=True)
    fig.savefig(out/"joint-predictions-workflow.pdf",bbox_inches="tight",metadata={"CreationDate":None,"ModDate":None})
    fig.savefig(out/"joint-predictions-workflow.svg",bbox_inches="tight",metadata={"Date":None})
    plt.close(fig)
    print("joint-predictions-workflow: PDF and SVG exported")


if __name__=="__main__":main()
