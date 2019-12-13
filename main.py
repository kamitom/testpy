import sys
import geometry.point as pp
import geometry.line as ll

import geometry.emojiconvert as emoji


# print(sys.path)
result = pp.distance(3, 4)
print("距離: ", result)

# 計算斜率
print("斜率: ", ll.slope(1, 1, 3, 3))

# 練習
print("phase please: ")
msg = input(">\n")
print(emoji.emoji(msg))