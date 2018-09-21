# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

from functools import reduce

move_list = [(1, 1), (-2, 1), (1, -3), (2, -4)]

result = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), move_list, (10, 10))

print(result)
