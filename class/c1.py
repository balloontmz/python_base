# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


# 类最基本的作用：封装代码
class StudentHomework(object):
    # 类属性、最好不与实例属性相同名字
    # name = ""
    # age = 0
    sum1 = 0

    def __init__(self, name, age):  # self 可替换为别的 名字
        self.name = name
        self.age = age
        # 以下两种操作等价。第二种更好，个人感觉，使实例方法看上去更加独立。
        StudentHomework.sum1 += 1
        self.__class__.sum1 += 1

    def print_file(self):
        print("name: " + self.name)
        print("age: " + str(self.age))


student = StudentHomework("tom", 18)
student2 = StudentHomework("ttt", 19)

print(student.name)
print(student.__dict__)
print(StudentHomework.__dict__)
