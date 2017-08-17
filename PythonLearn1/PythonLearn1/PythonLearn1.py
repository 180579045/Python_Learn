#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a Python basic konwledge learning
print('This is a base print!')

#list：一个容器，和vector类似
alist = [1,2]
alist.append(9)
alist.insert(1,'string')
print(alist)
a = 0
for iter in alist:
    a = a + 1
    print('第' +str(a)+ '个参数是：' +str(iter))


#tuple：初始化之后不可变
atuple = (1,'aaa',3,4)
print('atuple的第二个参数是：'+atuple[1])

#可变参数（参数接收的是一个tuple）
def functuple(name, age, *args):
    print('name:', name, 'age:', age, 'ohter:', args)
# 以下是可变参数的调用
functuple('A', 10, 'beijing', 'aass')


# 关键字参数（参数接收的是一个dict）
# 可以将参数设置为可变长度的，且可以传入字典中的关键字
def funckw(name, age, **kw):
    print('name:',name, 'age:', age, 'other:',kw)
    if ('city' in kw) :
        print(kw['city'])
# 以下是关键字参数的调用
other = {'city':'beijing','job':'chengxuyuan'}
# 参数会自动转变为字典的关键字
funckw('C', 20, city = 'shanghai', job = 'z')
funckw('D', 10, city = other['city'])

