# 导入sys模块是python内置的
import sys
# 导入自定义模块所在的目录 路径为模块路径
sys.path.append(r"D:\Python\python0\python0")
# 导入税额模块
import Net
# 导入随机模块
import  random
# 上网用户
name='小明'
# 上网总时间
time=0;
print(name,'上网时间、行为统计：')
# 打印用户上网时间行为，返回上网时间
time += Net.net_play(1.5)
time += Net.Watch_videos( 2)
time += Net.Play_game( 3)
time += Net.Study(2)
# 根据上网时间超出8小时提示用户注意休息
Net.times(time)