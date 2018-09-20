# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

from enum import Enum

Month2 = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month2.__members__.items())
print(Month2.Jan.name)
