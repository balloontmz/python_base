# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

# 自封闭性，没有去改变全局变量的值。而是自己保存上次执行完成之后的环境的变量，将变量的改变局限在函数内部。
origin = 0


def factory(pos):

    def move(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return move


f = factory(origin)
print(f.__closure__[0].cell_contents)
print(f(2))
print(f.__closure__[0].cell_contents)
print(f(3))
print(f.__closure__[0].cell_contents)
print(f(8))
print(f.__closure__[0].cell_contents)

