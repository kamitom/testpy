from faker import Faker

from modules_set.module1 import studentClass
from modules_set.module1 import foo1
from modules_set.module1 import foo2
from modules_set.module1 import teacherClass
# import modules_set.module1 as testmodule1



# stu1 = testmodule1.student("tom", 17)
stu1 = studentClass("tom", 17)

stu1.study("python 的相關modules 概念")
stu1.watchSexMoviesOrNot()

# testmodule1.foo()
# foo1()

# foo2()

# testFaker = Faker()
testFaker = Faker(['it_IT', 'en_US', 'ja_JP'])


teach1 = teacherClass(testFaker.name(), testFaker.address())
print(teach1.schooleAddr)
teach1.teacherText()


# stu2 = testmodule1.student("Hellen", 28)
stu2 = studentClass("Hellen", 28)
stu2.study("Mobile Knowledge")
stu2.watchSexMoviesOrNot()
