# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import re
from urllib import request


class Spider(object):
    url = "https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7udc0vft7s5"
    reg = re.compile(
        r"""<div[\s]*?class="video-info">[\s\S]*?class="video-nickname"[\s]*?title="([\s\S]*?)">[\s\S]*?class="video-number">([\s\S]*?)</span>"""
    )

    def __feach_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        return htmls

        # assert htmls, "没有返回值"
        # with open("test.txt", "wb") as f:
        #     f.write(htmls)

    def __analysis(self, htmls):
        result = Spider.reg.findall(htmls)
        print(result)

    def go(self):
        htmls = self.__feach_content()
        htmls = htmls.decode("utf-8")
        self.__analysis(htmls)


spider = Spider()
spider.go()
