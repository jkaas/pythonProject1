# 导入sys模块是python内置的
import sys
# 导入自定义模块所在的目录 路径为模块路径
sys.path.append(r"D:\Python\python0\python0")
# 导入模块
import MyModular
# Greatnumber=[]
print('大乐透号码生成器')
# 提示用户输入要随机大乐透的数量 并获取输入的内容
time=input('请输入要生成的大乐透号码注数：')
# 根据注数获取 大乐透号码
Greatnumber=MyModular.Great_lotto(int(time))
# 循环打印每个号码
for i in range(0,int(time)):
    # 打印的时候 根据格式 显示号码
    print('{} {} {} {} {}       {} {}'.format(Greatnumber[i][0],Greatnumber[i][1],Greatnumber[i][2],Greatnumber[i][3],Greatnumber[i][4],Greatnumber[i][5],Greatnumber[i][6]))