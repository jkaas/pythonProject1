import os     # 文件或目录模块
import time   # 导入时间模块


def nsfile(s):
    '''''The number of new expected documents'''
    # 判断文件夹是否存在，如果不存在则创建
    b = os.path.exists("E:\\testFile\\")
    if b:
        print("该目录存在！")
    else:
        os.mkdir("E:\\testFile\\")
        # 生成文件
    for i in range(1, s + 1):
        # 获取当前系统时间
        localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # 以当前系统时间作为文件名称
        filename = "E:\\testFile\\" + localTime + ".txt"
        # a:以追加模式打开（必要时可以创建）append;b:表示二进制
        f = open(filename, 'ab')
        # 文件内写入的信息
        testnote = '文件测试'
        # 写入文件信息
        f.write(testnote.encode('utf-8'))
        f.close()
        # 输出第几个文件和对应的文件名称
        print("file" + " " + str(i) + ":" + str(localTime) + ".txt")
        time.sleep(1)     # 休眠一秒
    print('生成文件成功！')


if __name__ == '__main__':
    s = int(input("请输入需要生成的文件数："))    # 获取输入的文件个数
    nsfile(s)