
# 這是一個funtion

"""
這是一個多行的註解


Version: 0.1
Author: TOMJR
"""


def one():
    return 1


print(type(one))


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def testFunc(func, a, b):
    return func(a, b)


# print(add(1, 2))

print(testFunc(add, 100, 200))
