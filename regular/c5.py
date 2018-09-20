# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

# * 匹配 0 次或者无限多次
# + 匹配一次或者无限多此
# ？ 匹配0次或者1 次

a = "pytho0python1pythonn2"

r1 = re.findall("python*", a)
r2 = re.findall("python+", a)
r3 = re.findall("python?", a)

print(r1)
print(r2)
print(r3)
