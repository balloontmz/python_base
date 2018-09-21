# -*- coding: utf-8 -*-

"""天眼查"""

__author__ = 'tomtiddler'

import urllib
from urllib import request, parse
import re

"""手机版，查询字数过多直接重定向回登录页面了，电脑版header暂时没加，正则表达式有点乱"""


def deal_result(results):
    for result in results:
        result = result.replace('"', "")
        req = urllib.request.urlopen(result)
        html = req.read()
        reg = re.compile(r'style="width:\s59%;"\s>\s(.*)\s</div>')  # 正则的用法
        html = html.decode('utf-8')  # 在网页中查找
        with open("tyc3.txt", "w") as f:
            f.write(html)

        # if len(result) == 1:
        #     tempfile = open("tyc2.txt", 'a')
        #     for i in result[:3]:
        #         tempfile.write(i)
        #         tempfile.write("\n")
        #     tempfile.close()


def findhtml(req):  # 找到相似的公司网址
    r = urllib.request.urlopen(req)
    html = r.read()
    with open("tyc3.html", "wb") as file:
        file.write(html)
    reg = re.compile(r'<a href=(.*?)\sstyle="word')  # 正则的用法
    html = html.decode('utf-8')  # 在网页中查找
    results = re.findall(reg, html)[:3]
    deal_result(results)


with open('tyc00.txt', 'r') as f:
    reads = f.readlines()
    for read in reads:
        req = request.Request("https://m.tianyancha.com/search?key=" + parse.quote(read))
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS'
                                     '8_0 like Mac OS X) AppleWebKit/536.26'
                                     ' (KHTML, like Gecko) Version/8.0 Mobile/'
                                     '10A5376e Safari/8536.25')
        findhtml(req)

