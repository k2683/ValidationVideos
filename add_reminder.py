#!/usr/bin/env python3
import os
import re

directory = "/home/magicmon/ValidationVideos"

# 新的提醒文本（只包含一行提示，去掉“Attention:”前缀）
new_reminder_html = (
    '<div class="attention" style="margin-top:20px;font-size:16px;color:red;">'
    'Please make sure you fully play the video above before making your rating'
    '</div>\n'
)

# 用于匹配并删除旧的 <div class="attention"> … </div> 块
attention_pattern = re.compile(r'<div class="attention".*?</div>\s*', re.DOTALL)

for filename in os.listdir(directory):
    if not filename.endswith(".html") or filename == "index.html":
        continue

    fullpath = os.path.join(directory, filename)
    with open(fullpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 先移除已插入的旧提醒
    content = re.sub(attention_pattern, "", content)

    # 如果新的提醒尚未插入，则在 </body> 前面加入新的提醒
    if "Please make sure you fully play the video above before making your rating" not in content:
        content = content.replace("</body>", new_reminder_html + "</body>")

        with open(fullpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"No changes needed: {filename}")
