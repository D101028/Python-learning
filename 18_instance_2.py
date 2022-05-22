# 實體方法
# 封裝在實體物件中的函式

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(3,4)
p.show() # 呼叫實體方法 / 函式
print(p.distance(0,0))

# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self, name):
        self.name=name
        self.file=None # 尚未開啟檔案: 初期是 None
    # 實體方法
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一的檔案
f1=File("data1.txt")
f1.open()
data=f1.read()
print(data)
# 讀取第二個檔案
f2=File("data2.txt")
f2.open()
data=f2.read()
print(data)