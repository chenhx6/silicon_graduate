# -*- coding: utf-8 -*-
path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-9.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

old_sentence = r"Lange 等给出的发射约定中 $\delta_{\rm KS}=-\delta_{\rm RB}$，转换文献时还必须同步转换几何干涉系数并区分发射与吸收。"
new_sentence = r"Lange 等~\cite{lange-kumar-hamilton-1982-multipole-admixtures}给出的发射约定中 $\delta_{\rm KS}=-\delta_{\rm RB}$，转换文献时还必须同步转换几何干涉系数并区分发射与吸收。"

assert old_sentence in text, "old_sentence not found"
text = text.replace(old_sentence, new_sentence)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Added Lange citation to sec-5-9.tex")
