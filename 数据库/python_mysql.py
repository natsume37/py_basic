# coding : utf-8
# 夏目&青一
# @name:python_mysql
# @time: 2023/2/1  15:43

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123',
                     )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
while True:
    msg = input('请输入sql命令>>>')
    if msg == 'q':
        break
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(msg)

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        print(data)
    except:
        print('命令错误，请重新输入！')
        continue
# 关闭数据库连接
db.close()