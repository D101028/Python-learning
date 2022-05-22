import pandas as pd
# 資料索引
# 內建索引
data=pd.Series([3, 10, 20, 5, -12])
print(data)
# 自訂索引
data=pd.Series([3, 10, 20, 5, -12], index=["a","b","c","d","e"])
print(data)

# 觀察資料
data=pd.Series([3, 10, 20, 5, -12], index=["a","b","c","d","e"])
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)

# 取得資料
data=pd.Series([3, 10, 20, 5, -12], index=["a","b","c","d","e"])
print(data[2]) # 取得第三筆資料
print(data["e"]) # 取得索引 e 的對應資料

# 數字運算
data=pd.Series([3, 10, 20, 5, -12], index=["a","b","c","d","e"])
data.sum() # 加法總和
data.max() # 最大值
data.prod() # 全部相乘
data.mean() # 平均數
data.median() # 中位數
data.std() # 標準差
data.nlargest(3) # 前三大數字
data.nsmallest(2) # 最小的兩個數字

# 字串運算
data=pd.Series(["你好","Python","Pandas"])
# 定義在 str 底下
data.str.lower() # 全部變小寫
data.str.upper() # 全部變大寫
data.str.len() # 得到每個字串的長度
data.str.cat(sep=",") # 將所有自串串起來，並用逗號隔開
data.str.contains("P") # 判斷字串是否包含 P
data.str.replace("您好","Hello") # 將 您好 取代為 Hello
