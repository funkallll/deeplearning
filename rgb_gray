import os
import cv2
import numpy as np

def convert2gray(filename):                                     # 将彩色图转灰度图的函数
    img = cv2.imread(file_path+'/'+filename, 1)                 # 1是以彩色图方式去读
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(out_path + '/GRAY' + filename, gray_img)        # 保存在新文件夹下，且图名中加GRAY

file_path = "F:/pycharmpractice/my/datazip/ORCA-Uboat_data/WaterSegmentation/training/training/640_320_undistorted_gt"               # 输入文件夹
#os.mkdir("F:/pycharmpractice/my/datazip/ORCA-Uboat_data/WaterSegmentation/training/training/640_320_undistorted_gt_gray")            # 建立新的目录
out_path ="F:/pycharmpractice/my/datazip/ORCA-Uboat_data/WaterSegmentation/training/training/640_320_undistorted_gt_gray"            # 设置为新目录为输出文件夹

for filename in os.listdir(file_path):                          # 遍历输入路径，得到图片名
    print(filename)
    convert2gray(filename)

