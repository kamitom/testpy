

n = 1
# while n < 4:
#     print(n)
#     n += 1

# 1+2+3...+10
testSUM = 0
while n <= 10:
    testSUM = testSUM + n
    n += 1
print("while 測試 1+...+10: ", testSUM)

for aa in [1, 2, 5]:
    print(aa)

for bb in "Hello":
    print(bb)

for testRange in range(5, 10):
    print(testRange)

testSUM1 = 0
for testRn in range(11):
    testSUM1 = testSUM1 + testRn
print("for 測試 1+..+10: ", testSUM1)