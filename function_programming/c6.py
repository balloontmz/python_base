# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import time


def time_dec(func):
    def func__():
        print(time.time())
        return func()
    return func__


@time_dec
def f1():
    print("This is a function")


f1()



# unix 时间戳
