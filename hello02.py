"""
02 - 使用變數保存數據並進行算術運算
"""

# import geometry.ftoc as fc
from geometry import ftoc
from modules_set.module2 import devide2


a = int(input("a = "))
b = int(input("b = "))


print("%d + %d = %d" % (a, b, a + b))
print("%d %% %d = %d" % (a, b, a % b))
print("%d ** %d = %d" % (a, b, a ** b))

# 100F = 37C
# (100-32)/1.8 = 37.777
ftempeture = int(input("請輸入華氏溫度數值: \n"))
# ctempetuere = fc.ftocCalc(ftempeture)
ctempetuere = ftoc.ftocCalc(ftempeture)
print(f"攝氏溫度答案為: {ctempetuere}")

a1 = int(input("a11 = "))
b1 = int(input("b = "))

testAns = devide2(a1, b1)
# print("%d + %d = %d" % (a1, testAns, a1 + testAns))
print(f"{a1} // {b1} 整除答案: {testAns}")
# print(type(devide2(a, b)))
