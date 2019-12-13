"""
02 - 使用變數保存數據並進行算術運算
"""

import geometry.ftoc as fc

a = int(input("a = "))
b = int(input("b = "))


print("%d + %d = %d" % (a, b, a + b))
print("%d %% %d = %d" % (a , b, a % b))
print("%d ** %d = %d" % (a , b, a ** b))

# 100F = 37C
# (100-32)/1.8 = 37.777
ftempeture = int(input("請輸入華氏溫度數值: \n"))
ctempetuere = fc.ftocCalc(ftempeture)
print(f"攝氏溫度答案為: {ctempetuere}")


