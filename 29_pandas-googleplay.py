import pandas as pd
# 
data=pd.read_csv("googleplaystore.csv") # 把 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("==========================================")
# 分析資料 : 評分的各種統計資料
print(data["Rating"])
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("前一百個應用程式的平均", data["Rating"].nlargest(100).mean()) # 出問題了
print("==========================================")
condition=data["Rating"]<=5
data=data[condition]
print(data["Rating"])
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("分數前二百七十四個應用程式的平均", data["Rating"].nlargest(274).mean()) # 出問題了

print("==========================================")

# 分析資料 : 安裝數量的各種統計數據
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
print("平均數", data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於100000" , data[condition].shape[0])

# 基於資料的應用 : 關鍵資蒐尋城市名稱
keyword=input("請輸入關鍵字: ")
condition=data["App"].str.contains(keyword)
print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])
print("==========================================")
condition=data["App"].str.contains(keyword, case=False) # 忽略大小寫
print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])
