# -*- coding: utf-8 -*-

"""
this is a module
"""

__author__ = 'tomtiddler'


import re
from urllib import request


class Spider(object):
    # reg = re.compile(
    #     r"""<div[\s]*?class="video-info">[\s\S]*?nickname"[\s]*?title="([\s\S]*?)">[\s\S]*?number">([\s\S]*?)</span>"""
    # )
    # 匹配全部内容 -> [\s\S]  . [\d\D] [\w\W]
    # 以下 参数 应该可 配置，增加可复用性。
    url = "https://www.panda.tv/cate/{0}?pdt=1.24.s1.3.7udc0vft7s5".format("lol")
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '[\s\S]*?nickname"[\s]*?title="([\s\S]*?)">'
    number_pattern = '[\s\S]*?number">([\s\S]*?)</span>'

    def __feach_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        return htmls

        # assert htmls, "没有返回值"
        # with open("test.txt", "wb") as f:
        #     f.write(htmls)

    def __analysis(self, htmls):
        # result = Spider.reg.findall(htmls)
        # print(result)
        root_html = re.findall(Spider.root_pattern, htmls)
        re_dict = []
        for result in root_html:
            name = re.findall(Spider.name_pattern, result)
            number = re.findall(Spider.number_pattern, result)
            anchor = {"name": name, "number": number}
            re_dict.append(anchor)

        return re_dict

    def __refine(self, re_dict):
        l = lambda re_dict:{"name": re_dict["name"][0], "number": re_dict["number"][0]}
        return map(l, re_dict)

    def __sort(self, re_dict):
        re_dict = sorted(re_dict, key=self.__sort_seed, reverse=True)
        return re_dict

    def __sort_seed(self, re_dict):  # 排序种子，对应re_dict的一个元素
        r = re.findall("\d*", re_dict["number"])
        number = float(r[0])
        if "万" in re_dict["number"]:
            number *= 10000

        return number

    def __show(self, re_dict):
        for rank in range(0, len(re_dict)):
            print("rank:" + str(rank + 1) + "---" + re_dict[rank]["name"] + "----" + re_dict[rank]["number"])

    def go(self):
        htmls = self.__feach_content()
        htmls = htmls.decode("utf-8")  # 提取大块数据
        re_dict = self.__analysis(htmls)  # 分析数据
        re_dict = self.__refine(re_dict)  # 数据精炼
        re_dict = self.__sort(re_dict)
        self.__show(re_dict)


spider = Spider()
spider.go()
