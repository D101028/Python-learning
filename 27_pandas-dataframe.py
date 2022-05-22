import pandas as pd
# 資料索引
data=pd.DataFrame({
    "name":["Yamada","Takaki","Saito"],
    "salary":[123456,3251123,5413543]
})
# 自訂索引
data=pd.DataFrame({
    "name":["Yamada","Takaki","Saito"],
    "salary":[123456,3251.123,5413543]
}, index=["a","b","c"])

# 觀察資料
print("資料數量", data.size)
print("資料形狀(列,欄)", data.shape)
print("資料索引", data.index)

# 取得列 (Row/橫向) 的 Series 資料: 根據順序、根據索引
print("取得第二列", data.iloc[1], sep="\n") # sep 換行
print("取得第 c 列", data.loc["c"], sep="\n")

# 取得欄 (Column/直向) 的 Series 資料: 根據欄位的名稱
print("取得 name 欄位", data["name"], sep="\n")


# 建立新的欄位
data["revenue"]=[500000, 400000, 300000]
data["rank"]=pd.Series([3, 6, 1], index=["a","b","c"])
data["cp"]=data["revenue"]/data["salary"]
print(data)
