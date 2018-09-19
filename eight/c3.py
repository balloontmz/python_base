# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


def damage(skill1, skill2):
    return skill1*3, skill2*3  # 默认返回值为tuple


print(damage(1, 2))
# 获取返回结果的正确方法
# 序列解包
skill1_damage, skill2_damage = damage(1, 2)
# 不推荐通过索引获取，会造成可读性变差