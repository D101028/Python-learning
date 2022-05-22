# 實體屬性
# 封裝在實體物件的變數
# class 類別名稱:
#     # 定義初始化函式
#     def __init__(self):
#         透過操作 self 來定義實體屬性
# # 建立實體物件，放入變數 obj 中
# obj=類別名稱() # 呼叫初始化函式

# ex1
class Point:
    def __init__(self):
        self.x=3
        self.y=4
# 建立實體物件，並放到變數 p 裡
# 此實體物件包含函式 x 和 y 兩個實體屬性
p=Point()

# ex2
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
# 建立實體物件
# 建立時，可以直接傳入參數資料
p=Point(1,5)

# 使用實體--> 實體物件.實體屬性名稱
# 接續ex2
print(p.x+p.y)

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
# 建立第一個實體物件
p1=Point(3,4)
print(p1.x, p1.y)
# 建立第二個實體物件
p2=Point(5,6)
print(p2.x, p2.y)

# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=FullName("Y.H.", "Chan")
print(name1.first, name1.last)
name2=FullName("Shikake", "Hirayo")
print(name2.first, name2.last)
