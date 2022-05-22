# 基本語法: 檔案物件=open(檔案路徑,mode=開啟模式)
# 開啟模式
# 讀取模式 - r
# 寫入模式 - w
# 讀寫模式 - r+
# 儲存檔案 (變數 file 裝檔案物件)
file=open("data.txt", mode="w") # 開啟
file.write("Hello File\nSecond Line") # 操作 # 此處寫入會將原有檔案內的資料覆蓋
file.close() # 關閉(很重要)
# 中文問題
file2=open("data.txt", mode="w", encoding="utf-8") # 還可指定編碼(utf-8使中文可以正常處理(日文德文韓文大概都行))
file2.write("你好棒棒\n1棒棒")
file2.close()
# 開啟寫入檔案的最佳實務(自動關閉檔案)
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("你好棒棒棒\n棒")
# 讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)
# 一行一行讀取 # 計算總和
with open("data2.txt", mode="w") as file3:
    file3.write("5\n3\n4\n7")
sum=0
with open("data2.txt", mode="r", encoding="utf-8") as file3:
    for line in file3: # 一行一行讀取
        sum+=int(line)
print(sum)

# 使用 json 格式讀取、複寫檔案
# 學完 json 再來看
import json
with open("config.json", mode='r') as file:
    data=json.load(file)
print(data) # data 是一個字典
print('name: ', data['name'])
print('version: ', data["version"])

# 修改
import json
with open("config.json", mode='r') as file:
    data=json.load(file) # 將JSON格式轉換為字典
print(data)
data["name"]='New Name' # 修改變數中的資料
# 把最新的資料更新到檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)