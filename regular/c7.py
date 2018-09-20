# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

a = "PythonPythonPythonPythonPython"

r = re.findall("(Python){3}", a)

print(r)
