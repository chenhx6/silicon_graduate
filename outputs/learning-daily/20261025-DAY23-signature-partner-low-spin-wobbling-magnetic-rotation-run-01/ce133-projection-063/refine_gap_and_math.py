from pathlib import Path
import json,re,hashlib,datetime,ast
O=Path(__file__).resolve().parent;p=O/'derivation.md';s=p.read_text()
pairs=[
(r'(31/4)',r'$31/4$'),(r'(j=11/2)',r'$j=11/2$'),(r'(m=\pm9/2)',r'$m=\pm9/2$'),
(r'(Pj_xP=Pj_yP=0)',r'$Pj_xP=Pj_yP=0$'),
(r'(Pj_x^2P=Pj_y^2P=(31/4)\mathbf1_2)',r'$Pj_x^2P=Pj_y^2P=(31/4)\mathbf1_2$'),
(r'(\Gamma(M1)=g_RR+\sum(g_ll+g_ss))',r'$\Gamma(M1)=g_RR+\sum(g_ll+g_ss)$'),
(r'(|18\rangle\)',r'$|18\rangle$'),(r'(9/2^-[514]\)',r'$9/2^-[514]$'),
(r'\(\Omega\)',r'$\Omega$'),(r'(m=9/2\)',r'$m=9/2$'),
(r'(j_y\)',r'$j_y$'),(r'(j_x,j_y\)',r'$j_x,j_y$'),
(r'(j_{x,\rm eff}=Pj_xP=0\)',r'$j_{x,\rm eff}=Pj_xP=0$'),
(r'(1=P+Q\)',r'$1=P+Q$'),(r'(j_k\)',r'$j_k$'),
(r'( (Qj_kP)^\dagger(Qj_kP)\)',r'$(Qj_kP)^\dagger(Qj_kP)$'),
(r'(P\mathbf j^2P=143/4\)',r'$P\mathbf j^2P=143/4$'),
(r'((|+9/2\rangle,|-9/2\rangle)\)',r'$(|+9/2\rangle,|-9/2\rangle)$'),
(r'(T|+9/2\rangle=-|-9/2\rangle\)',r'$T|+9/2\rangle=-|-9/2\rangle$'),
(r'(T|-9/2\rangle=|+9/2\rangle\)',r'$T|-9/2\rangle=|+9/2\rangle$'),
(r'(|+9/2\rangle\)',r'$|+9/2\rangle$'),
(r'(a_0\mathbf1+\mathbf a\cdot\boldsymbol\sigma\)',r'$a_0\mathbf1+\mathbf a\cdot\boldsymbol\sigma$'),
(r'(|j,m=+9/2\rangle\)',r'$|j,m=+9/2\rangle$'),
(r'(\langle\mathbf j\rangle=(0,0,9/2)\)',r'$\langle\mathbf j\rangle=(0,0,9/2)$'),
(r'(m=j=11/2\)',r'$m=j=11/2$'),
(r'(\Delta j_x\Delta j_y=j/2=|\langle j_z\rangle|/2\)',r'$\Delta j_x\Delta j_y=j/2=|\langle j_z\rangle|/2$'),
(r'(j\to\infty\)',r'$j\to\infty$'),(r'(1/\sqrt{j}\)',r'$1/\sqrt{j}$'),
(r'(m=\pm1/2\)',r'$m=\pm1/2$'),(r'(Pj_xP\)',r'$Pj_xP$'),
(r'(X_k\)',r'$X_k$'),(r'(A_x=1/3,A_y=2/5,A_z=1/2\)',r'$A_x=1/3,A_y=2/5,A_z=1/2$'),
(r'(mathbf j_{\rm cl}=(0,0,+9/2)\)',r'$\mathbf j_{\rm cl}=(0,0,+9/2)$'),
(r'(|\mathbf j_{\rm cl}|=j=11/2\)',r'$|\mathbf j_{\rm cl}|=j=11/2$'),
(r'(\{\pm9/2\}\)',r'$\{\pm9/2\}$'),(r'(\{\pm7/2\}\)',r'$\{\pm7/2\}$'),
(r'(\lambda_k^{\rm full}\le\lambda_k^{20}\le\lambda_k^{10}\)',r'$\lambda_k^{\rm full}\le\lambda_k^{20}\le\lambda_k^{10}$'),
]
for a,b in sorted(pairs,key=lambda x:-len(x[0])):
    s=s.replace(a,b)
old='但不能对各空间先减各自ground energy后仍套相同不等式。最简同H反例：(H=\\operatorname{diag}(0,1,100)\\)，限制到后两个basis态后绝对本征值为1、100，满足变分上界；完整第一excitation gap为1，受限空间第一gap却为99。两条gap的变化不由简单variational排序控制。'
new=r'''但不能对各空间先减各自ground energy后仍套相同不等式。下面每一行分别保持同一个H，限制空间均由后两个basis态张成，并且两项有序绝对本征值都满足Rayleigh–Ritz上界：

|同H对角元|完整空间第一gap|受限绝对本征值|受限空间第一gap|变化|
|---|---:|---|---:|---|
|$(0,1,100)$|1|$(1,100)$|99|增大|
|$(0,99,100)$|99|$(99,100)$|1|减小|

两例分别用精确有理数比较有序绝对上界、检查gap变化方向，再独立用NumPy对同H的实际子空间压缩求本征值验证。它们共同说明：各ordinal绝对本征值的上界不能推出各自减去ground energy后的excitation gap单调增大或单调减小。这里没有比较两种不同H之间的变分序关系；每个反例都单独使用其自身固定H。'''
assert old in s or new in s
s=s.replace(old,new).replace('当前63项检查全部通过','当前68项检查全部通过')
assert r'\(' not in s and r'\)' not in s
# Convert a nested parenthesis expression left literal after long replacement into valid math syntax.
s=s.replace('$Pj_x^2P=Pj_y^2P=$31/4$\\mathbf1_2$','$Pj_x^2P=Pj_y^2P=(31/4)\\mathbf1_2$')
p.write_text(s)
# Enforce paired inline delimiters per non-display paragraph and identify bare LaTeX.
inline_lines=[]
for number,line in enumerate(s.splitlines(),1):
    if '$$' not in line and line.count('$')%2:
        inline_lines.append(number)
assert not inline_lines,inline_lines
outside=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
outside=re.sub(r'\$[^$\n]*\$','',outside)
bare=re.findall(r'\\[A-Za-z]+',outside)
assert not bare,bare
r=json.loads((O/'results.json').read_text())
assert len(r['checks'])==68 and r['all_pass']
g=r['external_H_control']['different_reference_excitation_counterexamples']
assert [(x['full_first_gap'],x['restricted_first_gap']) for x in g]==[('1','99'),('99','1')]
for q in O.glob('*.py'):ast.parse(q.read_text())
v=json.loads((O/'verification.json').read_text())
v.update(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_checks_pass=True,check_count=68,
         RR_gap_counterexamples=g,markdown_inline_delimiters_paired=True,no_bare_latex_outside_math=True)
v['changed_paths']=[str(x.relative_to(O)) for x in sorted(O.iterdir()) if x.is_file()]
v['files']=[{'path':str(x.relative_to(O)),'sha256':hashlib.sha256(x.read_bytes()).hexdigest(),'bytes':x.stat().st_size}
            for x in sorted(O.iterdir()) if x.is_file() and x.name!='verification.json']
(O/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
print(json.dumps({'checks':68,'all_pass':True,'gap_examples':g,'math_delimiters':'paired; no bare LaTeX'},ensure_ascii=False,indent=2))
