import os
import sys

VIDEO_FOLDER_NAME = "videos"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\n[DEBUG] 脚本所在目录：{script_dir}")

    all_items = os.listdir(script_dir)
    print(f"[DEBUG] 目录内容（{script_dir}）:")
    for item in all_items:
        print(f"  - {item}")
    print("")

    video_dir = os.path.join(script_dir, VIDEO_FOLDER_NAME)
    print(f"[DEBUG] 预期的视频目录：{video_dir}")

    if not os.path.isdir(video_dir):
        print(f"\n[ERROR] 未找到名为 '{VIDEO_FOLDER_NAME}' 的文件夹。")
        print("        请确认 videos 文件夹与 generateVideos.py 位于同一级目录下。")
        sys.exit(1)
    else:
        print("[DEBUG] 成功找到 videos 文件夹。")

    video_items = os.listdir(video_dir)
    print(f"[DEBUG] videos 文件夹内容（{video_dir}）:")
    for item in video_items:
        print(f"  - {item}")
    print("")

    video_files = [f for f in video_items if f.lower().endswith(".mp4")]
    if not video_files:
        print(f"[ERROR] 在 '{video_dir}' 目录中未发现任何 .mp4 文件，请确认视频文件后缀名是否正确。")
        sys.exit(1)
    else:
        print("[DEBUG] 检测到以下 .mp4 视频文件：")
        for vf in video_files:
            print(f"  - {vf}")
        print("")

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Video: {title}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f8f8f8;
      text-align: center;
      padding: 40px;
    }}
    h1 {{
      font-size: 24px;
      margin-bottom: 20px;
    }}
    video {{
      width: 90%;
      max-width: 1280px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}
    p {{
      margin-top: 10px;
      font-size: 18px;
      font-weight: bold;
    }}
    .reminder {{
      margin-top: 30px;
      font-size: 16px;
      color: #555;
    }}
  </style>
</head>
<body>
  <h1>Comparison: {comparison}</h1>
  <video controls>
    <source src="{video_path}" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p>Video: {filename}</p>
  <div class="reminder">
    Please make sure you are currently answering the questionnaire section for this comparison.
  </div>
</body>
</html>
"""

    for video_filename in video_files:
        base_name = os.path.splitext(video_filename)[0]  # 去掉 .mp4 后缀，比如 "AB"
        comparison = base_name.replace("_", " × ").replace("-", " × ")
        video_path = f"{VIDEO_FOLDER_NAME}/{video_filename}"

        # 用实际内容填充 HTML 模板
        html_content = html_template.format(
            title=base_name,
            comparison=comparison,
            video_path=video_path,
            filename=video_filename
        )

        # 输出 HTML 文件，直接写到脚本所在目录
        output_filename = f"{base_name}.html"
        output_path = os.path.join(script_dir, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[生成成功] {output_path}")


if __name__ == "__main__":
    main()
