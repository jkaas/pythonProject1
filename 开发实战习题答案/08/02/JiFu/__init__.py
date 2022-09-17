# 导入随机模块
import  random
# 获取福卡方法
def Ji_Fu():
    # 所有福卡列表
    fus=['爱国福','富强福','和谐福','友善福','敬业福']
    # 获取列表中的一项组成新的列表
    fu=random.sample(fus, 1)
    # 返回获取到的福卡
    return fu
# 打印当前拥有的所有福卡 方法
def fus(fu):
    print('当前拥有的福：')
    # 循环福卡字典
    for i, j in fu.items():
        # 打印福卡
        print(i,': ',j,'\t',end='')
# 判断五福是否集齐方法 集齐返回1
def five_blessings(fu):
    # 拥于判断是否集齐的标识 1代表集齐
    type=1
    # 循环 福卡字典 判断副卡是否集齐
    for i, j in fu.items():
        # 当有副卡是0张的时候不能合成五福
        if j==0:
          #不能集成五福的时候返回0
          type=0
    # 返回 判断是否集齐标识
    return type;
