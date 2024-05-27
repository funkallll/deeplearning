import albumentations as A
import cv2
import os
import numpy as np

"""
该脚本主要实现了利用albumentations工具包对yolo标注数据进行增强
给定一个存放图像和标注文件的主目录，在主目录下自动生成增强的图像和标注文件
"""


# def add_min_value_to_rgb(image, min_value=50):
#     # 确保输入图像是NumPy数组
#     assert isinstance(image, np.ndarray)
#     # 检查图像是否有三个通道（RGB）
#     assert image.shape[-1] == 3
#
#     # 将RGB值低于min_value的像素值加上min_value
#     image[image < min_value] = min_value
#
#     # 注意：由于我们直接修改了输入图像，所以不需要返回任何值
#     # 如果你想保持原始图像不变并返回新的图像，你需要先复制图像
#     # return np.copy(image)

def get_enhance_save(old_images_files, old_labels_files, label_list, enhance_images_files, enhance_labels_files):
    # 这里设置指定的数据增强方法
    transform = A.Compose([
        # A.RandomCrop(width=450, height=450), # 随机裁剪图像到指定的宽度和高度（450x450像素）。如果裁剪操作导致边界框的面积小于指定的阈值或可见性低于指定的阈值，那么该操作可能会被跳过。
        # A.HorizontalFlip(p=1), # 以100%的概率水平翻转图像。p=1 表示该操作总是会执行
        # A.VerticalFlip(p=1), # 以100%的概率垂直翻转图像
        # A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=1),  # 随机调整图像的亮度和对比度
        # A.Rotate(limit=(-15, 15), interpolation=cv2.INTER_LINEAR, border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=None, always_apply=False, p=1)
        # A.RGBShift(r_shift_limit=50, g_shift_limit=50, b_shift_limit=50, always_apply=False, p=1)
        # A.Blur(blur_limit=11, always_apply=False, p=1)
        # A.MotionBlur(blur_limit=11, always_apply=False, p=1)
        # A.GaussNoise(var_limit=5000, mean=0, always_apply=False, p=1)
        # A.RandomScale(scale_limit=0.8, interpolation=cv2.INTER_LINEAR, always_apply=False, p=1)
        # A.InvertImg(always_apply=False, p=1)
        # A.ISONoise(color_shift=(0.01, 0.05), intensity=(0.1, 0.5), always_apply=False, p=1)
        # A.Solarize(threshold=200, always_apply=False, p=1)

        # A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=1),  # 随机调整图像的亮度和对比度
        A.Rotate(limit=(-15, 15), interpolation=cv2.INTER_LINEAR, border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=None, always_apply=False, p=1)
        # A.RGBShift(r_shift_limit=50, g_shift_limit=50, b_shift_limit=50, always_apply=False, p=1)
        # A.GaussNoise(var_limit=5000, mean=0, always_apply=False, p=1)
        # A.InvertImg(always_apply=False, p=1)
    ], bbox_params=A.BboxParams(format='yolo', min_area=1024, min_visibility=0.2, label_fields=['class_labels']))
    # format='yolo': 指定边界框的格式为 YOLO
    # min_area=1024: 最小边界框面积阈值。如果裁剪后边界框的面积小于这个值，那么裁剪操作可能会被跳过。
    # min_visibility=0.2: 最小边界框可见性阈值。这通常用于确定边界框在裁剪或翻转后是否仍然可见。

    # 这里指定修改后image和label的文件名
    # mid_name = "_VerticalFlip"
    mid_name = ""

    label_files_name = os.listdir(old_labels_files)

    for name in label_files_name:

        label_files = os.path.join(old_labels_files, name)

        yolo_b_boxes = open(label_files).read().splitlines()

        bboxes = []

        class_labels = []

        # 对一个txt文件的每一行标注数据进行处理
        for b_box in yolo_b_boxes:
            b_box = b_box.split(" ")
            m_box = b_box[1:5]

            m_box = list(map(float, m_box))

            m_class = b_box[0]

            bboxes.append(m_box)
            class_labels.append(label_list[int(float(m_class))])

        # 读取对应的图像
        image_path = os.path.join(old_images_files, name.replace(".txt", ".png"))
        if os.path.exists(image_path) is False:
            image_path = os.path.join(old_images_files, name.replace(".txt", ".png"))

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 调用上面定义的图像增强方法进行数据增强
        transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
        transformed_image = transformed['image']
        transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
        transformed_b_boxes = transformed['bboxes']
        transformed_class_labels = transformed['class_labels']

        # 先判断目标文件夹路径是否存在
        if os.path.exists(enhance_images_files) is False:
            os.mkdir(enhance_images_files)
        a, b = os.path.splitext(name)
        new_name = a + mid_name + b
        cv2.imwrite(os.path.join(enhance_images_files, new_name.replace(".txt", ".png")), transformed_image)

        if os.path.exists(enhance_labels_files) is False:
            os.mkdir(enhance_labels_files)

        new_txt_file = open(os.path.join(enhance_labels_files, new_name), "w")

        new_bboxes = []

        for box, label in zip(transformed_b_boxes, transformed_class_labels):

            new_class_num = label_list.index(label)
            box = list(box)
            for i in range(len(box)):
                box[i] = str(('%.20f' % box[i]))
            box.insert(0, str(new_class_num))
            new_bboxes.append(box)

        for new_box in new_bboxes:

            for ele in new_box:
                if ele is not new_box[-1]:
                    new_txt_file.write(ele + " ")
                else:
                    new_txt_file.write(ele)

            new_txt_file.write('\n')

        new_txt_file.close()


def main():
    root = r"F:\x\20240426\all_data"

    old_images_files = os.path.join(root, "Rotate_png_data/png")
    old_labels_files = os.path.join(root, "Rotate_png_data/labels")

    enhance_images_files = os.path.join(root, "Rotate_png_data/png_r")
    enhance_labels_files = os.path.join(root, "Rotate_png_data/png_labels")

    # 这里设置数据集的类别
    # label_list = ["plate"]
    label_list = ["plate"]

    # 实现对传入的数据文件进行遍历读取，并进行数据增强
    get_enhance_save(old_images_files, old_labels_files, label_list, enhance_images_files, enhance_labels_files)


if __name__ == '__main__':
    main()
