print('--------------跳一跳-------------\n')
print('欢迎回来，请开始游戏……')
print("请输入（中心、音乐块、微信支付块）：")
score = 0;
while (True):
    strIn = input("请输入：")
    if (strIn == "中心"):
        score += 2
        print("您的分数为：" + str(score))
    elif (strIn == "音乐块"):
        score += 30
        print("您的分数为：" + str(score))
    elif (strIn == "微信支付块"):
        score += 10
        print("您的分数为：" + str(score))
