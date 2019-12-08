# break sample code

n = 0
while n < 5:
  if n == 3:
    break
  print(n)
  n+=1

print("final n: ", n)


# continue sample
nn = 0
for x in [0,1,2,3]:
  if x % 2 == 0:
    continue
  print(x)
  nn += 1
print("final nn: ", nn)


# esle sample
tSum = 0
for n in range(11):
  tSum += n
else:
  print("1 ++ 10: ", tSum) # 回圈結束前, 印出 tSum


# total 輸入 9: 得到 3, 輸入11: 得到{沒有}整數的平方根
testInput = int(input("正整數: "))
for i in range(testInput):
  if i * i == testInput:
    print("平方根 is: ", i)
    break
else:
  print("沒有整數平方根!!")



