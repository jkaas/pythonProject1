# 浏览网页
def net_play(time):
  print('浏览网页',str(time)+'小时')
  return time
# 看视频
def Watch_videos(time):
    print( '看视频',str(time)+'小时')
    return time
# 网游戏
def Play_game(time):
    print('玩网络游戏',str(time)+'小时')
    return time
# 学习
def Study(time):
    print( '上网学习',str(time)+'小时')
    return time
# 计算上网时间，上网时间达到或者多余8小时给出提示
def times(time):
    if time>=8:
       print('今天上网时间共计'+str(time)+'小时，请保护眼睛，合理安排上网时间！')
    return time