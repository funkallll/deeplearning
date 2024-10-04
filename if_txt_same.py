def read_file_to_set(file_path):
    """读取文件内容，并将其存储在一个集合中"""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # 去除每行末尾的换行符，并将结果存储在一个集合中
    line_set = {line.strip() for line in lines}
    return line_set


def check_common_lines(file1_path, file2_path):
    """检查两个文件中是否有相同的行"""
    set1 = read_file_to_set(file1_path)
    set2 = read_file_to_set(file2_path)

    # 使用集合的交集操作来找出共同的行
    common_lines = set1.intersection(set2)

    # 如果common_lines不为空，则表示两个文件中有相同的行
    return bool(common_lines), common_lines


# 示例用法
file1_path = 'dataSet/Main/trainval.txt'
file2_path = 'dataSet/Main/train.txt'
has_common, common_lines = check_common_lines(file1_path, file2_path)

if has_common:
    print(f"两个文件中有相同的行：{len(common_lines)}")
    for line in common_lines:
        print(line)  # 这里会自动在每行末尾添加换行符
else:
    print("两个文件中没有相同的行。")
