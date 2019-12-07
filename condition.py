
testHello = input("please input No: ")

testHello = int(testHello)  # 轉型

print(testHello)

if testHello > 100:
    print("over 100")
elif testHello > 50:
    print("between 100 - 50 ")
else:
    print("smaller then 50")

# 四則運算
n1 = int(input("please number1: "))
n2 = int(input("please number2: "))

xx = input("please +-*/: ")

if xx == "+":
  print(n1 + n2)
elif xx == "-":
  print(n1 - n2)
elif xx == "*":
  print(n1 * n2)
elif xx == "/":
  print(n1 / n2)
else:
  print("???")

