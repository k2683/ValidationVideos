#!/usr/bin/env python3
import os

# 如果需要用绝对路径也可以，下面假设脚本和 HTML 文件都在同一个目录
directory = "/home/magicmon/ValidationVideos"

# 要插入的 HTML 片段
reminder_html = (
    '<div class="attention" style="margin-top:20px;font-size:16px;color:red;">'
    'Attention: Please make sure you fully play the video above before making your rating; '
    'otherwise, replay the video before answering.'
    '</div>\n'
)

for filename in os.listdir(directory):
    # 只处理 .html 文件，且跳过 index.html
    if not filename.endswith(".html") or filename == "index.html":
        continue

    fullpath = os.path.join(directory, filename)
    with open(fullpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 如果已经插入过就跳过
    if "Attention: Please make sure you fully play" in content:
        continue

    # 在 </body> 前插入 reminder_html
    new_content = content.replace("</body>", reminder_html + "</body>")

    with open(fullpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated: {filename}")
