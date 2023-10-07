import os
import cv2

# 输入和输出文件夹路径
input_folder = 'photos'
output_folder = 'grays'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图像
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 读取图像
        img = cv2.imread(os.path.join(input_folder, filename))

        # 将图像转换为灰度图像
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 使用阈值将灰度图像转换为二值图像
        _, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

        # 保存二值图像到输出文件夹
        cv2.imwrite(os.path.join(output_folder, filename), binary_img)
