# 載入 pandas 模組
import pandas as pd
# 建立 Series
data=pd.Series([20,21,35])
# 基本 Series 操作
print(data)
print(data.max()) # 最大值
print(data.median()) # 中位數
data=data*2
print(data)
data=data==20
print(data)


# 建立 DataFrame
data=pd.DataFrame({
    "name":["Yamada","Takaki","Saito"],
    "salary":[123456,3251.123,5413543]
})
# 基本 DataFrame 操作
# print(data)
# 取的特定的欄位
print(data["name"])
# 取的特定的列
print(data.iloc[0]) # 第一列