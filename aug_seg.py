import os
import cv2
import albumentations as A
import random

random.seed(1)
# 定义增强配置
aug = A.Compose([
    A.Rotate(limit=(-15, 15), interpolation=cv2.INTER_LINEAR, border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=None,
             always_apply=False, p=1)
])

# load dataset
image_dir = r'E:\deeplearning\data\prac\seg\data\images'
mask_dir = r'E:\deeplearning\data\prac\seg\data\label1_png'
aug_image_dir = r'E:\deeplearning\data\prac\seg\data\rotate\images_2'
aug_mask_dir = r'E:\deeplearning\data\prac\seg\data\rotate\labels_mask'

# 确保输出目录存在
os.makedirs(aug_image_dir, exist_ok=True)
os.makedirs(aug_mask_dir, exist_ok=True)

# 获取图像和掩模文件列表
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
mask_files = [f for f in os.listdir(mask_dir) if f.endswith('.jpg') or f.endswith('.png')]

assert len(image_files) == len(mask_files), "Number of images and masks don't match"

for image_file, mask_file in zip(image_files, mask_files):
    # 读取原始图像和掩模
    image_path = os.path.join(image_dir, image_file)
    mask_path = os.path.join(mask_dir, mask_file)
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)  # 读取彩色掩模

    # 为当前图像和掩模生成多个增强版本（共1个）
    for i in range(1):
        augmented = aug(image=image, mask=mask)
        image_aug = augmented["image"]
        mask_aug = augmented["mask"]

        # 为增强结果构建新的文件名
        output_image_name = f'{image_file[:-4]}.jpg'  # 假设原始图像为 .jpg 格式
        output_mask_name = f'{mask_file[:-4]}.png'  # 假设原始掩模为 .png 格式

        # 保存增强后的图像和掩模
        output_image_path = os.path.join(aug_image_dir, output_image_name)
        output_mask_path = os.path.join(aug_mask_dir, output_mask_name)
        cv2.imwrite(output_image_path, image_aug)
        cv2.imwrite(output_mask_path, mask_aug)
