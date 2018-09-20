# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import json

json_str = """{"name":"tom", "age":18}"""

a = json.loads(json_str)

print(a)

b = json.dumps(a)

print(b)
