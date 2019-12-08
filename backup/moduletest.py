# import geometry as g
import modules.geometry as g
import sys
sys.path.append("modules")  # 模組path 中,新增路徑


print(sys.platform)
print(sys.maxsize)  # 系統最長的整數形態最大值

# 建立geometry模組,載入使用
# 算2點距離
print(g.distance(1, 1, 5, 5))
# 算斜率
print(g.slope(1, 2, 5, 6))

# 調整搜尋模組的路徑
print(sys.path)  # 印出模組的搜尋路徑,所以才能找到 geometry module
