# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


class Human(object):
    sum1 = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_file(self):
        print("this is a parent method")


# 类最基本的作用：封装代码
class StudentHomework(Human):
    # 类属性、最好不与实例属性相同名字
    # name = ""
    # age = 0

    def __init__(self, name, age):  # self 可替换为别的 名字
        super(StudentHomework, self).__init__(name, age)
        # 以上等价于 Human.__init__(self, name, age)
        # 以下两种操作等价。第二种更好，个人感觉，使实例方法看上去更加独立
        StudentHomework.sum1 += 1
        self.__class__.sum1 += 1
        self.__score = age  # 外部访问变量名编程_classname__score

    def print_file(self):
        super(StudentHomework, self).print_file()
        print("name: " + self._do_english())
        print("age: " + str(self.age))

    def _do_english(self):  # 私有方法
        return self.name

    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print("当前学生数为" + str(cls.sum1))

    @staticmethod
    def add(x, y):
        print("this is a static method")
        return x + y


student = StudentHomework("tom", 18)
StudentHomework.plus_sum()
student2 = StudentHomework("ttt", 19)
StudentHomework.plus_sum()
student.print_file()

# print(student.name)
# print(student.__dict__)
# print(StudentHomework.__dict__)
