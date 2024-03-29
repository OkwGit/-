from PIL import Image
import os
import shutil
from datetime import datetime
art = """ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠤⠶⠶⠶⠶⠶⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠛⠃⢀⡠⠄⠀⢀⠀⠀⠀⠀⠀⠀⠤⡀⠀⠀⠀⠀⠀⠈⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠂⢂⣼⡇⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡃⠀⠀⠀⠀⢀⡾⡿⡀⠐⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢸⡄⠀⠐⡄⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⡜⢀⣞⢿⡇⢁⣾⣟⡀⠀⠀⠀⠀⠀⢀⠆⠀⣞⠀⣼⢻⠀⠀⡟⡄⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠋⠀⠀⠀⢠⡇⡾⡝⢸⠇⡼⠁⡇⠉⠁⠀⠀⠀⠀⣸⠀⢠⣯⢴⣏⠚⡇⠀⣿⢃⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀
⠲⣖⣚⠉⢀⣴⠀⠀⠀⢸⢰⠷⠁⠀⣀⣄⣘⠧⡠⠄⠀⣀⣀⢠⠇⣠⡏⣿⠿⠂⠁⣷⢀⡿⡏⠀⠀⠀⠀⠀⠀⠀⢠⠸⡇⠀⠀⠀⠀
⠀⠀⠉⠉⢹⡇⠀⠀⠀⢸⣾⢤⣴⡿⣿⢿⣿⣿⢦⡀⠀⠀⠀⠉⠘⠋⣹⠏⣀⣀⠀⠙⠸⠃⣿⠀⠀⠀⠀⠀⠀⠀⠈⢷⣧⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⡆⠀⠀⢸⢿⣿⠃⣸⢅⣠⣿⠛⡇⠀⠀⠀⠀⠀⠀⠀⢔⣿⣿⣟⡻⣶⡄⠀⢹⠀⠀⠀⠀⠀⠀⢸⡀⠀⠙⢦⣀⠀⠀
⠀⠀⠀⠀⢸⠀⡇⠀⠀⢸⡏⡏⠂⢸⡖⠘⠋⢧⡟⠀⠀⠀⠀⠀⠀⢀⣎⣀⣽⢿⠿⡌⢻⣦⣸⠀⠀⠀⡄⠀⠀⢸⡷⢦⣤⣤⣬⠽⠒
⠀⠀⠀⠀⠸⡇⣹⡀⠀⠘⣿⡇⠀⠀⠙⠲⠶⠊⠀⠀⠀⠀⠀⠀⠀⠈⡧⠖⠛⠫⣵⡇⢈⡿⣾⠀⠀⠀⡏⠀⠀⢸⣇⢣⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⡜⣧⠀⠀⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⣤⠤⠞⠀⠈⢀⡇⠀⠀⢰⠇⠀⠀⢸⡇⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣧⡀⠘⣿⣿⣦⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠈⠀⢄⡾⠀⢀⡴⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⣘⢿⠛⠛⠓⠢⣤⣀⣈⠑⠒⠒⠚⠀⠀⠀⠀⠀⣀⣠⣴⣾⠇⠀⣠⣾⣋⠔⣫⡾⠹⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠀⠀⣼⣿⣏⢻⣿⣟⠟⠛⠛⣻⣟⣻⣿⡿⣿⡿⠋⣀⣼⡿⣙⣦⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣏⣿⡇⠈⠑⠒⢹⣿⢧⣿⣯⣿⡿⠗⠋⠑⠞⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⣿⢷⣿⣯⣼⣶⢶⣦⣾⣿⣻⣞⣿⡟⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣟⣺⣿⢎⢿⣿⣽⣻⣾⢿⣽⣿⣷⡯⣳⠹⡜⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⣻⣴⣿⢾⠚⢻⣿⣞⣧⣼⡿⣞⣿⠧⢿⡵⣫⠝⣖⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣷⣚⣼⣏⡾⣂⣿⣿⣽⣻⣟⣿⣿⣿⣤⢬⢿⡵⣛⡜⢶⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⣠⠭⢿⢿⣰⣏⣿⣯⠿⣽⣿⢯⣿⣽⣧⣛⡞⣿⡵⡾⣏⣳⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡹⣅⢀⡿⠯⣟⣿⣿⣧⡭⣿⣿⡁⢈⡷⣻⣷⠟⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠷⣏⢾⣷⣮⣿⣿⣿⣷⣻⣽⣿⢮⣝⢶⣻⣟⠉⠓⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⣬⣿⡟⠛⠛⠛⠻⡽⡿⠿⢿⣚⢬⢳⣜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⢰⠀⡇⠀⠘⠛⢻⠯⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⢸⠂⡇⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⢀⣸⠃⢹⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡯⠭⡯⣹⠁⢸⣖⢶⡶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠉⠁⠀⠘⠦⠭⠵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""" 
def create_long_image(folder_path):
    # 获取所有未处理的PNG和JPG文件，忽略程序生成的长图
    valid_extensions = ['.png', '.jpg', '.jpeg']
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in valid_extensions and not f.startswith("长图_")]

    num_files = len(files)
    if num_files == 0:
        print("\033[35m马忽悠\033[37m发现你文件夹里\033[91m没有\033[37m找到合适的未处理图片格式...\033[0m")
        return

    print(f"\033[95m肖瑞希\033[92m发现了{num_files}张图片，开始处理...\033[0m")

    files.sort(key=os.path.getmtime)

    images = [Image.open(f) for f in files]
    max_width = max(im.width for im in images)

    # Rescale images first to get their new heights for accurate total_height calculation
    rescaled_images = [im.resize((max_width, int(im.height * max_width / im.width)), Image.Resampling.LANCZOS) for im in images]
    total_height = sum(im.height for im in rescaled_images) + (len(rescaled_images) - 1) * 10  # Add separator height

    # Create the long image
    long_image = Image.new('RGB', (max_width, total_height), 'white')
    y_offset = 0
    for im in rescaled_images:
        long_image.paste(im, (0, y_offset))
        y_offset += im.height + 10  # Add the height of the current image and the separator

    # Save the long image
    custom_name = "长图_" +input("\033[96m小气走\033[36m邀请你输入自定义输出文件名，按回车使用默认命名:\033[93m ").strip()
    if not custom_name:
        custom_name = "长图_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = os.path.join(folder_path, f"{custom_name}.png")
    long_image.save(output_path)

    # Move the original images to the "OG Archived" folder
    archive_folder_path = os.path.join(folder_path, "OG Archived")
    os.makedirs(archive_folder_path, exist_ok=True)
    for file in files:
        shutil.move(file, os.path.join(archive_folder_path, os.path.basename(file)))

    # print(f"\033[97m小白葱\033[92m提醒你长图保存完成 \033[37m文件路径：\033[96m {output_path}\033[0m")
    print("\033[95m" + art + "\033[0m")
    print(f"\033[97m小白葱\033[92m提醒你长图保存完成, \033[91m爽")
    print("\033[33m董慧明\033[93m通知你:所有原始图片已经被移动到\033[33m'OG Archived'\033[93m文件夹.\033[0m")
   


folder_path = os.getcwd()
create_long_image(folder_path)


