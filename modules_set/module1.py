class student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s 正在學習 %s" % (self.name, course_name))



def foo():
    print("hello foo2")

def foo():
    print("hello foo1")