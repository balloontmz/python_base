# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

day = 2


def get_return_wednesday():
    return "wednesday"


switcher = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: get_return_wednesday
}


dayName = switcher.get(day, "Saturday")() \
    if callable(switcher.get(day, "Saturday")) \
    else switcher.get(day, "Saturday")
print(dayName)
