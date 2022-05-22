# Iterable 資料型態
# 字串、列表、集合、字典

# for 迴圈
for x in [3, 5, 2]:
    print(x)
for x in "abc":
    print(x)
for x in {3, 5, 'abc', 2}: # 沒順序
    print(x)
for key in {"a":3, "x":5}:
    print(key)
dic={"a":3, "x":5}
for key in dic:
    print(dic[key])

# 內建函式
# max(可疊代資料)
print(max([3,124,345,2,66,2]))
print(max("slkdfhskzjdsf"))
print(max({"d":3,"c":532,"b":23,"a":653}))
# sorted(可疊代資料)
print(sorted("qwertyuiopasdfghjklzxcvbnm"))
