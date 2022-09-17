# 根据月收入计算税额
def tax(monthMoney):
    # 扣除标准
    # 最低工资额 3500往下不扣税
    ds = 3500
    # 三险一金上线
    threeInsurancesUp = 7662
    # 养老保险
    yangLao = monthMoney * 0.08
    # 医疗保险
    yiLiao = monthMoney * 0.02
    # 失业保险
    shiYe = monthMoney * 0.005
    # 住房公积金
    homeMoney = monthMoney * 0.12
    # 计算应扣除 的 三险一金
    threeInsurances = yangLao + yiLiao + shiYe + homeMoney
    # 判断是否超出三险一金 上线
    if threeInsurances > threeInsurancesUp:
        # 超出等于默认值
        threeInsurances = threeInsurancesUp
    # 应纳税所得额= 扣除三险一金  - 扣除最低月收入 的收入部分
    payable = monthMoney - threeInsurances - ds
    # 初始化应交税
    single = 0
    # 根据收入判断 不同级别收入 扣除不同的税
    if payable < 1500:
        single = payable * 0.03 - 0
    elif payable >= 1500 and payable < 4500:
        single = payable * 0.1 - 105
    elif payable >= 4500 and payable < 9000:
        single = payable * 0.2 - 555
    elif payable >= 9000 and payable < 35000:
        single = payable * 0.25 - 1005
    elif payable >= 35000 and payable < 55000:
        single = payable * 0.3 - 2002
    elif payable >= 55000 and payable < 80000:
        single = payable * 0.35 - 5505
    elif payable >= 80000:
        single = payable * 0.45 - 13505
    # 如果 计算的single等于负数 返回0 证明收入不满3500
    if single < 0:
        single = 0
    # 返回应交的个税
    return single