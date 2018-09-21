# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


class Test(object):
    def __len__(self):
        return 0


test = Test()

if test:
    print("S")
else:
    print("F")
