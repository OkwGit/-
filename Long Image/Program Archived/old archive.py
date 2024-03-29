from PIL import Image, ImageDraw
import os

def create_long_image(folder_path):
    # 获取所有PNG和JPG文件
    valid_extensions = ['.png', '.jpg', '.jpeg']
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in valid_extensions]
    num_files = len(files)
    if num_files == 0:
        print("\033[91m你文件夹里没有找到合适的图片格式...\033[0m")
        return

    print(f"\033[92m发现了{num_files}张图片，开始处理...\033[0m")

    files.sort(key=os.path.getmtime)

    images = [Image.open(f) for f in files]
    max_width = max(im.width for im in images)
    images = [im.resize((max_width, int(im.height * max_width / im.width))) for im in images]

    # 确保在总高度中包含了所有图片的高度和分隔线的高度
    separator_height = 10  # 分隔线的高度
    total_height = sum(im.height for im in images) + separator_height * (len(images) - 1)

    long_image = Image.new('RGB', (max_width, total_height), 'white')
    draw = ImageDraw.Draw(long_image)
    separator_color = (200, 255, 200)  # 淡绿色分隔线

    y_offset = 0
    for im in images:
        long_image.paste(im, (0, y_offset))
        y_offset += im.height
        if y_offset < total_height:  # 确保最后一张图片下方不绘制分隔线
            draw.line((0, y_offset, max_width, y_offset), fill=separator_color, width=separator_height)
            y_offset += separator_height

    output_path = os.path.join(folder_path, 'long_image.png')
    long_image.save(output_path)

    file_size = os.path.getsize(output_path)
    print(f"\033[96m长图保存完成，文件路径：{output_path}, 文件大小：{file_size / 1024:.2f} KB ({file_size / (1024 * 1024):.2f} MB)\033[0m")

folder_path = os.getcwd()
create_long_image(folder_path)
