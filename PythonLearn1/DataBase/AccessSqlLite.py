import sqlite3


# SQLite是Python3默认内置的模块
# 使用connect，会默认连接对应目录下的数据库，若没有文件则会自动创建
conn = sqlite3.connect('Test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 使用cursor.execute之后通过rowcount返回影响的行数
print('生效行数:' + cursor.rowcount)

cursor.close()
conn.commit()
conn.close()
