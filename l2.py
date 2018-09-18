# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

a = [[1, 2, 3, 4], (5, 6, 7)]

for x in a:
    # print(x, end=" ")  # end 关键字用于定义结尾的方式 比如\n 空格 等
    for y in x:
        if y == 6:
            break
        print(y, end=" ")
else:
    print("end...")
