# 模組載入
# 範例:sys模組(內建)
import sys
# 使用 sys 模組
print(sys.platform) # 印出作業系統
print(sys.maxsize) # 印出整數型態最大值
print(sys.path) # 印出搜尋模組的捷徑
# 別名操作模組
import sys as s
print(s.platform)
print(s.maxsize)
# 建立 geometry 模組, 載入使用
from modules import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,2,5,6)
print(result)
# 調整搜尋模組的路徑
import sys
sys.path.append("d:\python\lesson\modules") # 新增python模組搜尋資料夾
print(sys.path)
from modules import geometry
print(geometry.distance(1,1,5,5))
