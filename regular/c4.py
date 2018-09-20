# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

a = "python 1111java678php"

r = re.findall("[a-z]{3,6}", a)

print(r)
