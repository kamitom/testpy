# 有序 可變動的列表 list

grades = [100, 99, 23, 45, 92]

grades[2] = 88  # 異動99 改為88

for gradeValue in grades:
    print(gradeValue)

print(grades[1:4])
grades[1:4] = []  # 連續刪除 1開始 4結束(不包含4)
print(grades)
grades = grades + [98, 43]  # list 串接
print(grades)
print("length: ", len(grades))

dataList = [[1, 2, 3], [5, 2.2, 9.9, 13]]
print(dataList[0][1])
print(dataList[1][2])
print(dataList[1][0:2])

dataList[1][0:2] = [22, 99, 97]
print(dataList[1])

# 有序 不可變動的列表 Tuple
testTuple2 = (100, 200, 23, 53, (11, 22))
print(testTuple2[0:2])
print(testTuple2[4])


testTuple2[0] = 5 # raise error: tuple 不可異動

print(grades[0])
