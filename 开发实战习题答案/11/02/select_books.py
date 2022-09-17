import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "mrsoft",charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 执行SQL语句，筛选数据
cursor.execute("select name,price,publish_time from books where price < 70 and publish_time >= '2017-01-01' ")
# 获取查询结果:
result = cursor.fetchall()
# print(result)

for book in result :
    print("图书：《{name}》, 价格：￥{price}元，出版日期：{publish_time}".format(name=book[0], price=book[1],publish_time=book[2]))
# 关闭数据库连接
db.close()