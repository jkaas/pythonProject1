# 导入sys模块是python内置的
import sys
# 导入自定义模块所在的目录 路径为模块路径
sys.path.append(r"D:\Python\python0\python0")
# 导入税额模块
import tax
# 提示用户输入工资
monthMoney=int(input("请输入月收入："))
# 通过税收计算模块计算税额 并打印
print("应纳个人所得税税额为%.2f" % tax.tax(monthMoney))