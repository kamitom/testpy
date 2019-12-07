# set 的運算

testSet = {3, 4, 5}
testSet2 = {"tom", 4, "nsa", 0.227}
print(31 in testSet)
print("nsa" in testSet2)

testS1 = {3, 4, 5}
testS2 = {4, 5, 6, 7}
testS3 = testS1 & testS2  # 交集
print("交集: ", testS3)

testS4 = testS1 | testS2
print("聯集(不重複)： ",  testS4)  # 聯集 不重複
testS5 = testS1 - testS2  # 差集, S5 只剩下 3
print("差集: ", testS5)

testS6 = testS1 ^ testS2  # 反交集， 取不重疊的部分
print("反交集: ", testS6)

testT = set("Hello")  # 把字串拆解成集合 set, 排除重複的部分
print("h" in testT)

# dict 的運算

testD1 = {"A": "Apple", "G": "Google", "F": "Facebook", "S": "Sony", "bug": 100, 1: "ONE", 2: "NSA", 3: "White House"}

print(testD1[1])
print(testD1["G"])

print("S" in testD1)
print(4 in testD1)
print(3 in testD1)
print("S" not in testD1)

print(testD1)
del testD1["S"]  # 刪除dict中的建值對（key-value pair)
print(testD1)


# 從list 中產生 dict
testD2 = {kk: kk * 2 for kk in [2, 4, 6]}
print(testD2)




