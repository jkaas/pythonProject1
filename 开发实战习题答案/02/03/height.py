father = None
mother = None
print('请输入父亲的身高：')
father = input()          # 获取控制台输入的父亲身高
print('请输入母亲身高：')
mother = input()          # 获取控制台输入的母亲身高
# 通过计算公式打印儿子身高
print('预测儿子身高为：',(float(father) + float(mother))*0.54)
