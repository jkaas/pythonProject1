import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "mrsoft",charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 执行SQL语句，筛选数据
cursor.execute("select name,price from books order by id ")
# 获取查询结果:
result = cursor.fetchall()

for book in result :
    print("图书：《{name}》, 价格：￥{price}元".format(name=book[0], price=book[1]))
# 关闭数据库连接
db.close()