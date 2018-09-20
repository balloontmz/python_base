# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

s = "Life is short, I use Python"

r = re.search("Life(.*)Python", s)

print(r.group(1))
