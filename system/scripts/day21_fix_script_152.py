with open('system/scripts/day21_execute_closeout_and_publish.py') as f:
    text = f.read()

lines = text.splitlines()
fixed = []
skip = False
for i, l in enumerate(lines):
    if l.endswith(' + "'):
        fixed.append(l[:-4] + ' + chr(10)')
        skip = True
    elif skip and l == '")':
        skip = False
    elif l == '    log_entry = f"':
        fixed.append("    log_entry = chr(10) + f'- {now_dt.isoformat()} Day21 checkpoint152/closeout：Day 21卡审计完成（18/24评分、5项交付、weekly REFLECT），完成104项知识写回并经H3协议验证，完成card-credit-21（completed[21]/partial[]/next22/count21），签发final-session-receipt-21，生成Day 22准备入口，已发布至Gitee main.' + chr(10)")
    elif l.startswith("- {now_dt.isoformat()}") and lines[i-1] == '    log_entry = f"':
        continue
    elif l == '"' and lines[i-2] == '    log_entry = f"':
        continue
    elif 'p_check.write_text("' in l:
        fixed.append('        p_check.write_text(chr(10).join(stripped) + chr(10), encoding="utf-8")')
    elif l == '".join(stripped) + "' or l == '", encoding="utf-8")':
        continue
    else:
        fixed.append(l)

fixed_text = chr(10).join(fixed) + chr(10)
with open('system/scripts/day21_execute_closeout_and_publish.py', 'w') as f:
    f.write(fixed_text)
print("Fix completed!")
