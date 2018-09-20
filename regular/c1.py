# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

a = "C|C++|Java|C#|Python|Javascript"

re_dict = re.findall("Python", a)

if len(re_dict):
    print("字符串包含 Python")
else:
    print("字符串不包含 Python")

print(re_dict)
print(a.index("Python") > -1)
print("Python" in a)
