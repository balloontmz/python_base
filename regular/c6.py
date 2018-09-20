# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re

# ^ 从字符串头部开始匹配
# $ 匹配至字符串尾部

qq = "100001"

r = re.findall('^\d{4,8}$', qq)  # 匹配完整字符串

print(r)
