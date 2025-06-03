#!/usr/bin/env python3
import os
import re

directory = "/home/magicmon/ValidationVideos"

# 定义新的说明文本块：两行原有提示 + 一行忽略声音和性别差异的提示
new_block = (
    '  <div class="reminder" style="margin-top:20px;font-size:16px;color:red;">\n'
    '    Please make sure you are currently answering the questionnaire section for this comparison.\n'
    '  </div>\n'
    '  <div class="attention" style="margin-top:20px;font-size:16px;color:red;">\n'
    '    Please make sure you fully play the video above before making your rating\n'
    '  </div>\n'
    '  <div style="margin-top:20px;font-size:16px;color:red;">\n'
    '    Please ignore any differences in audio and the gender of the persons depicted.\n'
    '  </div>\n'
)

# 用于匹配并删除旧的 <div class="reminder"> … </div> 块
reminder_pattern = re.compile(r'<div class="reminder".*?</div>\s*', re.DOTALL)
# 用于匹配并删除旧的 <div class="attention"> … </div> 块
attention_pattern = re.compile(r'<div class="attention".*?</div>\s*', re.DOTALL)

for filename in os.listdir(directory):
    if not filename.endswith(".html") or filename == "index.html":
        continue

    fullpath = os.path.join(directory, filename)
    with open(fullpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 如果已经插入过新的“忽略声音和性别差异”的提示，就跳过
    if "Please ignore any differences in audio and the gender of the persons" in content:
        print(f"No changes needed: {filename}")
        continue

    # 移除旧的 reminder 和 attention 块
    content = re.sub(reminder_pattern, "", content)
    content = re.sub(attention_pattern, "", content)

    # 在第一个 <video> 标签之前插入新的说明块
    content, count = re.subn(
        r'(<video\b[^>]*>)',
        new_block + r'\1',
        content,
        count=1
    )

    # 只有在确实找到了 <video> 并插入时才写回文件
    if count > 0:
        with open(fullpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filename}")
    else:
        print(f"Skipped (no <video> tag found): {filename}")
