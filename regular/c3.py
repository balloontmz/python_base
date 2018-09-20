# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

s = "abc, acc, adc, aec, afc, ahc"

r = re.findall("a[cf]c", s)

print(r)
