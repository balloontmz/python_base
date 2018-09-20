# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

a = "C6C++7Java8C#9Python4Javascript"

re_dict = re.findall("\d", a)  # \d表示所有数字

print(re_dict)

"""
Python -> 普通字符
\d  -> 元字符
"""