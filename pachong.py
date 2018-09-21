# -*- coding: utf-8 -*-
# 单线程爬虫，有待改进
import re
import requests
import urllib


def write(page):

    r = urllib.request.urlopen("http://www.0597zp.com/more.php?page=" + str(page))
    html = r.read()
    reg = re.compile('target=_blank>(.*?)</A>')  # 正则的用法
    html = html.decode('gb2312')  # 在网页中查找
    result = re.findall(reg, html)
    z = page // 10
    if (len(result) > 0):
        tempfile = open("mobile_%s.txt" % z, 'a')
        for i in result:
            tempfile.write(i)
            tempfile.write("\n")
        tempfile.close()


pages = 200
for i in range(130, pages + 1):
    write(i)