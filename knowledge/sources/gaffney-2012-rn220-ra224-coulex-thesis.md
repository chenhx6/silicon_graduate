---
type: source
title: "Gaffney 2012 - Octupole collectivity in 220Rn and 224Ra"
title_original: "Octupole collectivity in 220Rn and 224Ra"
aliases: ["CERN-THESIS-2012-309"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: read
authors: ["Liam Paul Gaffney"]
year: 2012
institution: "University of Liverpool"
doi: "10.17638/00009255"
canonical_source: "University of Liverpool doctoral thesis, September 2012, CERN-THESIS-2012-309"
raw_file: raw/theses/gpt/query/20261119-international-nuclear-structure/W857501821.pdf
raw_sha256: f9d14ff7eb104849960010c3d6da890d1a894e7f018f2b784447b4ae188deb8d
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/theses/gpt/query/20261119-international-nuclear-structure/manifest-acquisition-batch1.json
nuclei: ["220Rn", "224Ra"]
tags: ["Coulomb-excitation", "octupole", "GOSIA", "thesis"]
---

# Gaffney 2012：²²⁰Rn、²²⁴Ra 的八极集体性

## Bibliographic Record

Liam Paul Gaffney，利物浦大学博士论文，2012 年 9 月，CERN `CERN-THESIS-2012-309`。原件 122 页，正文印刷页为 PDF 页减 10。关联期刊为 [[gaffney-2013-pear-shaped-rn-ra]]，两者使用同一批库仑激发数据。

## Scope and Reading Depth

已核 120/122 页科研、附录与书目。PDF 2 为致谢，PDF 102 为附录分隔页。与期刊原件对照输入规模、矩阵元和误差表达。

## Summary

REX–ISOLDE 的 ²²⁰Rn、²²⁴Ra 放射性束分别打在 Ni、Cd、Sn 靶，MINIBALL 测粒子符合 γ 产额。各靶按角度分成两组并进入 GOSIA。较重靶和较大的质心散射角提高多步激发强度，直接激发负宇称态的 E3 信息仍与其它路径和效率参数共同依赖。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| GAF12-RUN | 学位表 5.1 对每个核素列六个靶–角区组合。Rn 对 ⁶⁰Ni、¹¹⁴Cd、¹²⁰Sn 用 620.40 MeV；Ra 对 ¹¹²Cd、¹²⁰Sn 用 633.92 MeV，对 ⁶⁰Ni 用 631.68 MeV。Cd 的已知矩阵元用于产额交叉检查。附录 B 列效率校正的 γ 产额。 | geometry-and-yield-selection | direct-original-pages | 学位 PDF 50–69、71、105–111，表 5.1、B.1–B.2；Nature PDF 3 |
| GAF12-E3 | 学位表 5.5–5.6 给下行 \(B(E3;3^-\to0^+)=33(4)\) W.u.（Rn）、42(3) W.u.（Ra），期刊表 1 相同。学位摘要把 \(3^-\) 印成 \(3^+\)，Rn 的中心值写为 32。两版 Ra \(\lvert\langle0^+\Vert E3\Vert3^-\rangle\rvert\) 同为 940 \(e\,\mathrm{fm}^3\)，误差在学位表为 40、期刊表为 30。 | versioned-reduced-matrix-elements | direct-original-and-arithmetic | 学位 PDF 3、85、88；Nature PDF 3，表 1 |
| GAF12-Q3 | 学位表 5.5 与期刊表 2 给 Rn 的 \(Q_3(3^-\to0^+)=2180(130)\ e\,\mathrm{fm}^3\)，学位表 6.1 印 \(2180(30)\)。转子换算 \(Q_3=\sqrt{16\pi/7}\lvert\langle0^+\Vert E3\Vert3^-\rangle\rvert\)，由 \(810(50)\ e\,\mathrm{fm}^3\) 得约 2171(134)，支持沿用结果表的误差。 | versioned-intrinsic-moment-and-propagation-check | direct-original-and-arithmetic | 学位 PDF 14、85、92，式 1.7、表 5.5、6.1；Nature PDF 4，表 2 |
| GAF12-FIT | GOSIA 同时拟合多个矩阵元与每组产额归一。误差先逐项固定其它参量取截面，再沿最大相关路径扫描，取 68.3% 的积分区间。对角 E2 灵敏度不足，建模时与跃迁 E2 耦合，另比较符号或置零的影响。束能、靶厚、E1/E3 相位和不灵敏 E4 也作系统比较。 | estimator-and-conditional-uncertainty | direct-original-pages | 学位 PDF 70–84，表 5.2–5.4、图 5.1–5.3 |
| GAF12-TAU | ²²⁰Rn 移除附加谱学输入后仍得到与既知 \(2^+\) 寿命相容的值。²²⁴Ra 的 84.4 keV 线受特征 X 射线影响，最终保留 \(2^+\) 寿命约束。\(4^+\) 寿命可供不使用该点的相容性检查。 | cross-check-and-lit-input-dependency | direct-original-pages | 学位 PDF 74、76–77、87；Nature PDF 3–4 |

## Competing Interpretations and Limitations

- 不同靶和散射角改变直接激发与多步激发的权重。拟合台账需保留转子耦合、符号、归一和附加数据。同源期刊给较大的自由参数数目，按版本引用拟合。学位 PDF 74–78；Nature PDF 3。
- ²²⁴Ra 的多条 E3 约束、宇称能级位移和相对角动量对准共同支持较持久的八极关联。²²⁰Rn 仅有两个有效的 \(Q_3\) 点，低能谱的振动解释仍重要。期刊明确指出矩阵元本身无法区分投影的静态形状与四极形状上的八极振动。学位 PDF 85–101；Nature PDF 4–5。
- 期刊表 1 的上限为 \(3\sigma\)，结果表误差与模型换算分开。这里核对了附录中的角区、各谱线产额与部分转子换算。重新估计协方差需要拟合输入卡与原始数据。

## Extracted Pages

- 学位 PDF 1、3–31：身份、导航、反射不对称指标及库仑激发和 GOSIA 推导。
- 学位 PDF 32–69：设施、效率、运动学和角度条件、分支数据与谱学。
- 学位 PDF 70–101：归一、矩阵元、误差、跨核比较和解释。
- 学位 PDF 103–122：运动学近似、逐组产额及书目。
- 关联 Nature 原件 PDF 1–6，重点 PDF 3–4 表 1–2。原件路径见 [[gaffney-2013-pear-shaped-rn-ra]]。
