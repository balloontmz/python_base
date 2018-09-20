# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re


def convert(value):
    print(dir(value))
    matched = value.group()
    return "!!" + matched


language = "PythonC#JavaPHPC#C#"

r = re.sub("C#", convert, language, 1)

print(r)

