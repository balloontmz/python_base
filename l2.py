# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

a = [[1, 2, 3, 4], (5, 6, 7)]

for x in a:
    # print(x, end=" ")  # end 关键字用于定义结尾的方式 比如\n 空格 等
    for y in x:
        if y == 6:
            break  # 此break只是跳出了内部循环，外部for并未跳出，算正常执行完成
        print(y, end=" ")
else:
    print("end...")

# for i in range(0, 10, 2):
# 循环重复十次。
# for i in range(10, 0, -2): 递减数列
