import hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-2.tex'
with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Photoelectric K-shell condition
old_pe = r'光子与锗原子的束缚内壳层电子（主要为 $K$ 壳层，结合能约 $11.1\,\text{keV}$）发生完全非弹性碰撞'
new_pe = r'光子与锗原子的束缚内壳层电子（在能量高于锗 $K$ 吸收边 $11.1\,\text{keV}$ 的给定能区下主要由 $K$ 壳层贡献）发生完全非弹性碰撞'
assert old_pe in text, "Could not find old_pe"
text = text.replace(old_pe, new_pe)

# 2. Pair fluctuation vs logarithm
old_fano = r'对数涨落方差为无量纲数 $\sigma_N^2 = F N = F E_\gamma / \epsilon$'
new_fano = r'电子—空穴对数目的方差为无量纲数 $\sigma_N^2 = F N = F E_\gamma / \epsilon$'
assert old_fano in text, "Could not find old_fano"
text = text.replace(old_fano, new_fano)

# 3. BGO veto false veto description
old_bgo = r'从靶室散射的低能粒子、核反应中微子伴生快中子或级联发射的另一个不相关光子若误入 BGO'
new_bgo = r'从靶室散射的低能粒子、重离子核反应产生的快中子或散射本底、以及其它不相关级联光子若误入 BGO'
assert old_bgo in text, "Could not find old_bgo"
text = text.replace(old_bgo, new_bgo)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(text)

staging_path = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G99/sec-5-2.tex'
with open(staging_path, 'w', encoding='utf-8') as f:
    f.write(text)

sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
print(f'Done! Patched sec-5-2.tex successfully. New SHA-256: {sha}')
