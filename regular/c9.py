# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re


def convert(value):
    matched = int(value.group())
    if matched >= 6:
        return '9'
    else:
        return '0'


language = "A8C3721D86"

r = re.sub("\d", convert, language, 0)

print(r)
