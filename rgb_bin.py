import os
import cv2

# 输入和输出文件夹路径
input_folder = 'F:/pycharmpractice/my/datazip/ORCA-Uboat_data/WaterSegmentation/training/training/640_320_undistorted_gt'
output_folder = 'F:/pycharmpractice/my/datazip/ORCA-Uboat_data/WaterSegmentation/training/training/640_320_undistorted_gt_bin'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 如果文件是图片文件，则将其转换为二值图并保存到输出文件夹中
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        img = cv2.imread(input_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        cv2.imwrite(output_path, binary)
