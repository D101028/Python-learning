# 集合運算
s1={1,2,3,4,5}
print(2 in s1)
print(10 not in s1)
s1={1,2,3,4}
s2={78,34,2,5}
s3=s1&s2 #交集
s4=s1|s2 #聯集
s5=s1-s2 #差集
s6=s1^s2 #反交集
s=set("Hello") #把字串拆解:set(字串)
print("H" in s)
# 字典的運算: key-value 配對
a={"I":"我","you":"shit"}
print("apple" in a) #判斷 key 是否存在
del a["I"] # 刪除鍵質對
b={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(b)
