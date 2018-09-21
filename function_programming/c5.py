# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

list_x = [1, 0, 1, 0, 1]

re_d = filter(lambda x: True if x == 1 else False, list_x)
print(list(re_d))

list_u = ["a", "B", "c", "F", "e"]

re_d2 = filter(lambda s: True if s.isupper() else False, list_u)

print(list(re_d2))
