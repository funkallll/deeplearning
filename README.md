# deeplearning
temp.py  统计标签文件夹中的数据种类及个数  
xml_txt.py  将xml标签格式转换为txt标签格式  
divide_data.py 随机划分数据集  
rgb_gray.py 将RGB彩色图像批量转换为灰度图并保存在文件夹中  
rgb_bin.py 将RGB彩色图像批量转换为二值图并保存在文件夹中  
check_data.py 查看数据集标注的质量，即将标签绘在原图片上，再保存到另一个文件夹中  
change_rgb.py 批量更改图片的RGB值，并保存在另一个文件夹中  
summary.py 查看网络结构  
seg_json2txt.py 将labelme的标签转换为txt格式（语义分割）  
mask2txt.py 批量读取语义分割标签（png格式）转换为txt格式并保存  
seg_txt_show.py 批量将txt语义分割标签显示在原图片上并保存  
aug_seg.py 对语义分割数据做随机旋转数据增强，包含图片及mask标签  
aug.py 使用albumentations库对目标检测进行数据增强  
if_txt_same.py 检测两个txt的每行是否有相同的行  
