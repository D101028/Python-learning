import pandas as pd
# Series
data=pd.Series([30, 15, 20])
condition=[True, False, True]
filteredData=data[condition]
print(filteredData)

print("================")

data=pd.Series([30, 15, 20])
condition=data>18
print(condition)
filteredData=data[condition]
print(filteredData)

print("================")

data=pd.Series(["您好", "Python", "Pandas"])
condition=data.str.contains("P")
print(condition)
filteredData=data[condition]
print(filteredData)

print("================")
# DataFrame
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
condtion=data["salary"]>=40000
filteredData=data[condition]
print(filteredData)