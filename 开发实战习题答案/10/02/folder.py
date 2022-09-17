import os  # 文件或目录模块

path = 'E:\\testFile\\'  # 外层路径


def folder(s):
    for i in range(1, s + 1):
        # 设置文件夹名称
        folder_name = path + str(i)
        # 检测文件夹是否存在
        if isExists(folder_name):
            print("该目录存在！")
        else:
            # 不存在进行创建
            os.makedirs(folder_name)
            if isExists(folder_name):
                print('文件夹', i, '创建成功！')

# 检测文件夹是否存在
def isExists(folder_name):
    b = os.path.exists(folder_name)
    return b


if __name__ == '__main__':
    s = int(input("请输入需要生成的文件夹个数："))  # 获取输入的文件夹个数
    folder(s)
