note_path = 'knowledge/research-notes/a130-rewrite-detector-photon-response-audit-20261114.md'
with open(note_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any occurrence of 对数涨落
text = text.replace('载流子产生对数方差', '电子—空穴对数目方差')
text = text.replace('对数涨落与能量方差量纲转换', '载流子数目方差与能量方差量纲转换')
text = text.replace('由对数涨落转换到观测能量尺度', '由电子—空穴对数目的方差转换到观测能量尺度')

with open(note_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated knowledge note successfully.')
