# 导入sys模块是python内置的
import sys
# 导入自定义模块所在的目录 路径为模块路径
sys.path.append(r"D:\Python\python0\python0")
# 导入模块
import JiFu
print('开始集福啦~~~')
# 五福字典 保存拥有的五福数据
fu={'爱国福':0,'富强福':0,'和谐福':0,'友善福':0,'敬业福':0}
# 判断是否集齐五福
while  JiFu.five_blessings(fu)==0:
    # 没有集齐五福提示用户
    input('\n按下<Enter>键获取五福')
    # 获取福卡
    Strfu=JiFu.Ji_Fu()[0]
    # 提示用户获取的的五福卡
    print('获取到：' +Strfu)
    # 在五福字典中 为获取到的福卡加1
    fu[Strfu] += 1
    # 打印拥有的福卡
    JiFu.fus(fu)
print('\n恭喜您集成五福！！！')
