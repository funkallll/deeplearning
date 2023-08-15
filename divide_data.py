# 将数据集随机划分为训练集和验证集,测试集
import os
import random
import shutil

from tqdm import tqdm

image_path = r'F:\pycharmpractice\yolov8-test\data\images\\'  # 源图片文件夹路径
label_path = r'F:\pycharmpractice\yolov8-test\data\labels\\'  # 标签文件夹路径

train_images = r'F:\pycharmpractice\yolov8-test\data\train_random\images'  # 划分后训练集图片的保存路径
train_labels = r'F:\pycharmpractice\yolov8-test\data\train_random\labels'
val_images = r'F:\pycharmpractice\yolov8-test\data\val_random\images'
val_labels = r'F:\pycharmpractice\yolov8-test\data\val_random\labels'
test_images = r'F:\pycharmpractice\yolov8-test\data\test_random\images'
test_labels = r'F:\pycharmpractice\yolov8-test\data\test_random\labels'

if not os.path.exists(train_images):
    os.makedirs(train_images)
if not os.path.exists(train_labels):
    os.makedirs(train_labels)
if not os.path.exists(val_images):
    os.makedirs(val_images)
if not os.path.exists(val_labels):
    os.makedirs(val_labels)
if not os.path.exists(test_images):
    os.makedirs(test_images)
if not os.path.exists(test_labels):
    os.makedirs(test_labels)
train_rate = 0.8  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
val_rate = 0.1
test_rate = 0.1
# 求训练集
pathDir = os.listdir(image_path)  # 取图片的原始路径
print('数据集总共有图片:', len(pathDir))
print(
    '划分比例如下：训练集:{},验证集:{},测试集:{}'.format(int(len(pathDir) * train_rate), int(len(pathDir) * val_rate),
                                                        int(len(pathDir) * test_rate)))
picknumber = int(len(pathDir) * train_rate)  # 按照rate比例从文件夹中取一定数量图片
train_sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
print('训练集的大小为：', len(train_sample))

# 复制为训练集
for name in tqdm(train_sample):
    shutil.copy(image_path + name, train_images + "\\" + name)
    name = name.replace('.jpg', '.txt')  # 修改文件后缀将 name = xxxx.jpg 改为 name = xxxx.txt
    shutil.copy(label_path + name, train_labels + "\\" + name)



# 求出原数据集不含训练集
all_images = os.listdir(image_path)
remaining_image = []
for file in all_images:
    if file not in train_sample:
        remaining_image.append(file)
# 求验证集
picknumber2 = int(len(remaining_image) * val_rate / (val_rate + test_rate))  # 按照rate比例从文件夹中取一定数量图片
val_sample = random.sample(remaining_image, picknumber2)  # 随机选取picknumber数量的样本图片
print('验证集的大小为：', len(val_sample))
# 复制为验证集
for file in tqdm(val_sample):
    shutil.copy(image_path + file, val_images + "\\" + file)
    file = file.replace('.jpg', '.txt')
    shutil.copy(label_path + file, val_labels + "\\" + file)

test_sample = []
for file in remaining_image:
    if file not in val_sample:
        test_sample.append(file)
print('测试集的大小为：', len(test_sample))
# 复制为测试集
for file in tqdm(test_sample):
    shutil.copy(image_path + file, test_images + "\\" + file)
    file = file.replace('.jpg', '.txt')
    shutil.copy(label_path + file, test_labels + "\\" + file)
