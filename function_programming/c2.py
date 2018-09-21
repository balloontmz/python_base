# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

# map

list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def f1(x):
    return x * x


list_y = map(f1, list_x)
print(list_y)  # 生成的是惰性的序列
print(list(list_y))
