# 判斷式
# if 布林值:
# 執行程式(縮排)
# elif 布林值:  (不縮排)
# 執行程式
# ...
# else:  (不縮排)
# 執行程式
# x=input("請輸入數字: ") # 取得字串形式的使用者輸入(note:是字串，不是數字)
# x=int(x) # 將字串型態轉換成數字型態(輸出為純整數)
# int()-->字串轉數字，且取整數(非數字會無法輸出)
# float()-->字串轉數字，包含浮點數(小數)(非數字會無法輸出)
# str()-->數字轉字串
# 自製四則運算
x1=int(input("選擇運算，1.加 2.減 3.乘 4.除 : "))
if x1==1:
    x11=int(input("數字: "))
    x12=int(input("數字: "))
    print(x11+x12)
elif x1==2:
    x11=int(input("數字: "))
    x12=int(input("數字: "))
    print(x11-x12)
elif x1==3:
    x11=int(input("數字: "))
    x12=int(input("數字: "))
    print(x11*x12)
elif x1==4:
    x11=int(input("數字: "))
    x12=int(input("數字: "))
    if x12==0:
        print('error')
    else:
        print(x11/x12)
else:
    print("error")
# 輸入也可為字串，去掉int(...)即可，不要忘記""
