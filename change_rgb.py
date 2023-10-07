from PIL import Image
import os

# 输入和输出文件夹路径
input_folder = 'seconds'
output_folder = 'thirds'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图像
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取图像
        img = Image.open(os.path.join(input_folder, filename))

        # 将图像转换为RGB色彩空间（如果它不是RGB）
        if img.mode != 'RGB':
            img = img.convert('RGB')

            # 遍历图像中的每个像素
        for y in range(img.height):
            for x in range(img.width):
                # 获取当前像素的RGB值
                r, g, b = img.getpixel((x, y))

                # 如果RGB值等于(236, 236, 236)，则将其设置为(255, 255, 255)
                # 如果RGB值不等于(236, 236, 236)，则保持不变
                # if r == 236 and g == 236 and b == 236:
                # if r == g == b and 233 <= r <= 255:
                if r == g == b and r == 255:
                    img.putpixel((x, y), (247, 199, 199))  # 更改后的RGB值

                    # 将处理后的图像保存到输出文件夹
        img.save(os.path.join(output_folder, filename))
