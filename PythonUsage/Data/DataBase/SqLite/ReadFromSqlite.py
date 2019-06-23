import sqlite3


conn = sqlite3.connect('Test.db')
cursor = conn.cursor()
cursor.execute('select * from user')

# 通过fetchall返回结果，结果是一个list类型，每个元素都是一个tuple
ret = cursor.fetchall()

print(ret)
print(ret[0])

cursor.close()
conn.close()