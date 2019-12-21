"""


"""

import sys

f = [x for x in range(1, 10)]

print(f)

f1 = [y + x for x in 'ABCD' for y in '1234567']
print(f1)

for a100 in f1:
  if '3D' in a100:
    print('YES', a100)
  # print(a100)

f2 = [x2 ** 2 for x2 in range(1, 8)]
print(f2)
print(type(f2))
print("getsizeof f2: ", sys.getsizeof(f2))

# 創建一個generator
f3 = (x3 ** 2 for x3 in range(1, 8))
print(f3)
print("getsizeof f3 ", sys.getsizeof(f3))
print(type(f3))
for val in f3:
  print(val)