
# 參數的預設


def power(base, exp=0):
    print(base ** exp)


power(9, 2)

# 參數的名稱對應


def devide(n1, n2=1):
    print(n1 / n2)


devide(100, 9)

devide(n2=100, n1=12)


# 無限參數範例, numbers以 (1,2,3) tuple 呈現
def avg(*numbers):
  testS = 0
  for i in numbers:
    testS = testS + i
  return (testS/len(numbers))

print("avg", avg(3,4,4,3))