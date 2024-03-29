from PIL import Image
import os
import shutil
from datetime import datetime

def create_long_image(folder_path):
    # 获取所有未处理的PNG和JPG文件
    valid_extensions = ['.png', '.jpg', '.jpeg']
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in valid_extensions]
    num_files = len(files)
    if num_files == 0:
        print("\033[91m你文件夹里没有找到合适的未处理图片格式...\033[0m")
        return

    print(f"\033[92m发现了{num_files}张图片，开始处理...\033[0m")

    files.sort(key=os.path.getmtime)

    images = [Image.open(f) for f in files]
    max_width = max(im.width for im in images)
    total_height = sum(im.height for im in images) + (len(images) - 1) * 10  # Assuming a fixed separator height of 10

    # Rescale images to have the same width
    images = [im.resize((max_width, int(im.height * max_width / im.width)), Image.Resampling.LANCZOS) for im in images]

    # Create the long image
    long_image = Image.new('RGB', (max_width, total_height), 'white')
    y_offset = 0
    for im in images:
        long_image.paste(im, (0, y_offset))
        y_offset += im.height + 10  # Move to the next position and add separator height

    # Save the long image
    custom_name = input("请输入自定义输出文件名，按回车使用默认命名: ").strip()
    if not custom_name:
        custom_name = "长图_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(folder_path, f"{custom_name}.png")
    long_image.save(output_path)

    # Move the original images to the "OG Archived" folder
    archive_folder_path = os.path.join(folder_path, "OG Archived")
    os.makedirs(archive_folder_path, exist_ok=True)
    for file in files:
        shutil.move(file, os.path.join(archive_folder_path, os.path.basename(file)))

    print(f"\033[96m长图保存完成，文件路径：{output_path}\033[0m")
    print("\033[92m所有原始图片已经被移动到'OG Archived'文件夹.\033[0m")

folder_path = os.getcwd()
create_long_image(folder_path)
