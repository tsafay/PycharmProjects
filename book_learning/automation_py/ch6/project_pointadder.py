#！ python3
# 将Wikipedia项目符号点添加到剪贴板上每一行文本的开头。
import pyperclip
text = pyperclip.paste()

# 分隔文本并添加序号
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = str(i) + '.' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)

