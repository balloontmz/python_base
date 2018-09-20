# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

from enum import Enum, IntEnum # unique


# @unique
class VIP(Enum):  # 值可以是字符串，如果需要强制是整数，需要用到IntEnum
    YELLOW = 1
    GREEN = 2
    BLACK = 2
    RED = 4


print(VIP.YELLOW)
print(type(VIP.GREEN.name))
print(type(VIP.GREEN))
print(type(VIP["GREEN"]))

result = VIP.GREEN
assert result == VIP.BLACK, "false"  # 由于重复的赋值,导致两个成员值相等，并且调用BLACK返回的名字会是GREEN
assert result is VIP.GREEN, "false"

for v in VIP:  # 没有BLACK
    print(v)

for v in VIP.__members__:  # 有BLACK
    print(v)

print(VIP(1))

