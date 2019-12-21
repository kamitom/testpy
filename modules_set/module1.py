class studentClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s 正在學習 %s" % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watchSexMoviesOrNot(self):
        if self.age > 18:
            print("YES, you CAN")
        else:
            print("No, too young to see")


class teacherClass(object):
    def __init__(self, schoolName, schoolAddress):
        self.schoolName = schoolName
        self.schooleAddr = schoolAddress

    def teacherText(self):
        print("Schoole name is : %s" % (self.schoolName))


def foo1():
    print("hello foo1")


def foo2():
    print("hello foo2")
