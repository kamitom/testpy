
from faker import Faker
# faketTest = Faker("zh_TW")
faketTest = Faker()


class FileCls(object):
    def __init__(self, *args):
        self.name = args[0]
        self.theFile = None  # 初始未開啟檔案, 預設是: None

    def xOpen(self):
        self.theFile = open(self.name, mode="r", encoding="utf-8")

    def xRead(self):
        return self.theFile.read()


class PointCls1(object):
    def __init__(self, *args):
        if len(args) >= 2:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = 3
            self.y = 4


class PointCls2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PeopleCls(object):
    def __init__(self, *args):
        self.first = args[0]
        self.last = ""
        self.heigh = args[2]

    # 定義實體方法 sayHello

    def sayHello(self, *args):
        print(self.first, "say hello")

    def urHeigh(self, *args):
        print(self.first, "heigh:", self.heigh)


originP1 = PointCls1()
originP2 = PointCls1(30, 40)

objP2 = PointCls2(1.1, 2.2)

print(originP1.x, originP1.y)
print(originP2.x, originP2.y)

print(objP2.x)


objFull = PeopleCls(faketTest.name(), "", "200")
print(objFull.first, objFull.last, objFull.heigh)

objFull.sayHello()
objFull.urHeigh()

f1 = FileCls("a1.txt")
f1.xOpen()
data1 = f1.xRead()
print(data1)


f2 = FileCls("a2.txt")
f2.xOpen()
data2 = f2.xRead()
print("日文: \n", data2)
