#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################
# Python的常用库函数、常用容器的使用
#################################

import os
from functools import reduce

# This is a Python basic knowledge learning
print('This is a base print!,Start to learn python basic grammar!')

# ---------------Python的一些基础容器和字典------------------

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# list：一个容器，和C++ STL中的vector类似
# 可以向里边加入任何元素，且不必担心vector那样必须是同一个数据类型
#
#     没有盖子↓↓↓↓↓  可随时任意的添加元素
#
#       |    [1,3,5,7,9]     |
#       |   3.14159          |
#       |        guoliang    |
#       |    func(x,y,z)     |
#       |  1    3     5      |
#        ---------------------

alist = [1, 2]
alist.append(9)
alist.insert(1, 'string')
alist.insert(2, [11, 13, 17])
print('alist is')
print(alist)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# tuple：另外一个容器，初始化之后不可变
#
#     有盖子↓↓↓↓↓  初始化之后是不可变的
#
#       ----------------------
#       |    [1,3,5,7,9]     |
#       |   3.14159          |
#       |        guoliang    |
#       |    func(x,y,z)     |
#       |  1    3     5      |
#       ----------------------

atuple = (1, 'aaa', 3, 4)
print('atuple的第二个参数是：'+atuple[1])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

a = 0
# --------------------------------------------------使用迭代器
for iter in alist:
    a = a + 1
    print('第' + str(a) + '个参数是：' + str(iter))

# ----------------------------------------------------------


# ----------------Python函数的参数--------------------------

# 可变参数，即一个星号代表参数只是一维的（参数接收的是一个tuple）
def functuple(name, age, *args):
    print('name:', name, 'age:', age, 'ohter:', args)
# 以下是可变参数的调用
functuple('A', 10, 'beijing', 'aass')


# 关键字参数（参数接收的是一个dict）
# 可以将参数设置为可变长度的，且可以传入字典中的关键字
# 两个星号代表参数是一个二维的
def funckeyword(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    if ('city' in kw) :
        print(kw['city'])


# 以下是关键字参数的调用
other = {'city':'beijing','job':'chengxuyuan'}
# 参数会自动转变为字典的关键字
funckeyword('C', 20, city = 'shanghai', job = 'z')
funckeyword('D', 10, job = other['job'])

# ----------------------------------------------------------


# ---------------------递归调用-----------------------------
# python支持递归调用
# 这是一个尾递归的用法，遗憾的是Python不支持……
# 尾递归就是在最后return的时候，只是单纯的调用一个函数就叫尾递归
# 尾递归可以节省栈空间
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

RecursionRet = fact(20)
print(str(RecursionRet))
# ----------------------------------------------------------


# ----------------切片（Slice）的使用----------------------
BeSlicedList = ['A', 'B', 'C', 'D', 'E']
# 打印2到4位置的内容
print('使用切片：' + str(BeSlicedList[2 : 4]))
# ----------------------------------------------------------


# ----------------迭代表达式，列表生成式--------------------

CreateAList = []
for i in range(1,10):
    CreateAList.append('List' + str(i))

print('先初始化一个列表：' + str(CreateAList))

# ---列表生成式
lowerList = [s.lower() for s in CreateAList]
print('直接使用列表生成式，将列表转为小写：' + str(lowerList))



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ---列表生成器（Generator）
# 列表生成器与列表生成式不同，使用圆括号（）或关键字yield
# 使用列表生成器（Generator）保存的是生成列表的算法
# 所以列表生成器生成出来的列表是不能直接打印出全量集的（因为它是无限的）
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
SquareList = (x * x for x in range(1,20))
PrintSquareList = []

for n in SquareList:
    PrintSquareList.append(n)

print('列表生成器：' + str(PrintSquareList))
# ----------------------------------------------------------


# -------打印一个斐波那契数列(列表生成式Generator版本)------
def GeneratorFbi(max):
    a, b = 0, 1
    n = 0
    while(n < max):
        yield b
        tempc = a + b
        a = b
        b = tempc
        n = n + 1
    return 'done'


GereratorFbiList = GeneratorFbi(10)


GeneratorFbiListRet = []
for n in GereratorFbiList:
    GeneratorFbiListRet.append(n)

print('斐波那契数列，使用列表生成式的结果：' +str(GeneratorFbiListRet))

# ----------------------------------------------------------


# -----------打印一个斐波那契数列(递归版本)-----------------
def Fbi(n):
    res = 0
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    elif n >= 2:
        res = Fbi(n - 1) + Fbi(n - 2)
    return res


def PrintFbi(n):
    for i in range(0,n):
        a = Fbi(i)
        print(a)

# PrintFbi(10)
# ----------------------------------------------------------

# -----------打印一个斐波那契数列(迭代版本)-------------------
FbiList = [0, 1]
def FbiIterator(n):
    if n == 1:
        FbiList.pop()    # 移除掉最后一个数字
    else:
        for x in range(2, n):
            FbiList.append(FbiList[x-1] + FbiList[x-2])

FbiIterator(12)
print('迭代法打印的斐波那契数列：'+str(FbiList))
# ----------------------------------------------------------


# ----------------------回调函数----------------------------
Callbackabs = abs
def callbackfunc(arg1, f1):
    arg1 = f1(arg1)
    print('callbackfunc print:'+str(arg1))

callbackfunc(-10, Callbackabs)
# ----------------------------------------------------------


# ----------------------map函数-----------------------------
# map函数接收两个参数，一个是函数，另一个是一个容器
# map函数的入参函数只接受一个参数，所以map函数作用在容器的每一个元素
# map是将容器中的每一个元素都所用在入参的第一个函数当中
AMapList = [1, 2, 3, 4, 5, 6]


def mapfunc(x):
    return x * x


mapres = map(mapfunc, AMapList)
mapresShow = list(mapres)
# 最终打印：[1, 4, 9, 16, 25, 36]
print(mapresShow)
# ----------------------------------------------------------


# -------------------reduce函数-----------------------------
# reduce函数接收两个参数，一个是函数，另一个是容器
# reduce函数的入参函数接收两个参数，所以reduce函数是累积处理容器当中的每一个元素的
# 例如一个序列  [x1, x2, x3, x4, x5]
# reduce的处理：func(func(func(func(x1, x2) ,x3) ,x4) ,x5)

def reducefunc(x, y):
    return x * 10 + y

ReduceRet = reduce(reducefunc, [1,4,5,6,7])
print('reduce function:' +str(ReduceRet))
# ----------------------------------------------------------





