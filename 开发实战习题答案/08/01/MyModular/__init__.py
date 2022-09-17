# 导入随机模块
import  random
# 大乐透号码生成
def Great_lotto(times):
  # 创建返回的号码空列表
  Greatnumber = []
  # 根据随机注释 循环
  for i in range(0,times):
    #创建空列表
    numbers = []
    # 创建数字为1到35的红色球列表
    roselist = list(range(1, 36))
    # 在红球列表中选取5个元素，生成红色球.
    numberred=random.sample(roselist, 5)
    # 创建数字为1到12的蓝色球列表
    bulelist=list(range(1,13))
    # 在蓝色球列表中 选取2个蓝色球，生成蓝色球
    numberbulle=random.sample(bulelist, 2)
    # 按照大小号排序 红球
    numberred.sort()
    # 按照大小号 排序蓝球
    numberbulle.sort()
    # 蓝球红球 组成随机的号码 列表
    numbers=numberred+numberbulle
    # 循环随机的号码
    for n in range(len(numbers)):
        # 判断号码是否<10
        if numbers[n]<10:
            # 当号码小于10的时候在数字前添加0
            numbers[n]='0'+str(numbers[n])
    # 添加到返回的号码列表中
    Greatnumber.append(numbers)
  # 返回得到的数据
  return Greatnumber
