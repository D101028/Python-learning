# 參數的預設資料
def power(base,exp=0): # exp給定預設值
    print(base**exp)
power(3,2)
power(4) # exp預設為 0
# 使用參數名稱對應
power(exp=2,base=3) #等同於 power(3,2)
# 無限(不定)參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))
avg(3,4)
avg(3.4,23.4,1234,582,-23.1)