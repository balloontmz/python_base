# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

# map

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]


r1 = map(lambda x: x * x, list_x)
print(r1)  # 生成的是惰性的序列
print(list(r1))

r2 = map(lambda x, y: x + y, list_x, list_y)
print(r2)
print(list(r2))

