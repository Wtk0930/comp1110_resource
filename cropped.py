from PIL import Image
import os

# 输入文件夹和输出文件夹
input_folder = './r_online'
output_folder = './output_folder'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图片文件
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# 初始化最大裁剪宽度、最大裁剪高度和最小裁剪坐标
max_crop_width = 0
max_crop_height = 0
min_crop_left = float('inf')
min_crop_top = float('inf')
max_crop_left = 0
max_crop_top = 0
max_crop_right = 0
max_crop_bottom = 0

# 循环处理每张图片
for image_file in image_files:
    # 构建输入文件路径和输出文件路径
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    # 打开图像文件
    img = Image.open(input_path)

    # 获取图像内容的边界框
    bbox = img.getbbox()

    # 计算裁剪区域的宽度和高度
    crop_width = bbox[2] - bbox[0]
    crop_height = bbox[3] - bbox[1]

    # 更新最大裁剪宽度、最大裁剪高度和最小裁剪坐标
    max_crop_width = max(max_crop_width, crop_width)
    max_crop_height = max(max_crop_height, crop_height)

    min_crop_left = min(min_crop_left, bbox[0])
    min_crop_top = min(min_crop_top, bbox[1])

    max_crop_right = max(max_crop_right, bbox[2])
    max_crop_bottom = max(max_crop_bottom, bbox[3])

max_crop_width = max_crop_right - min_crop_left
max_crop_height = max_crop_bottom - min_crop_top

# 循环处理每张图片并裁剪至最大裁剪宽度、最大裁剪高度和最小裁剪坐标
for image_file in image_files:
    # 构建输入文件路径和输出文件路径
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)

    # 打开图像文件
    img = Image.open(input_path)

    # 计算裁剪区域的右下坐标
    crop_right = min_crop_left + max_crop_width
    crop_bottom = min_crop_top + max_crop_height

    # 裁剪图像至最大裁剪宽度、最大裁剪高度和最小裁剪坐标
    cropped_img = img.crop((min_crop_left, min_crop_top, crop_right, crop_bottom))

    # 保存裁剪后的图像
    cropped_img.save(output_path)

print("批量裁剪完成。")
