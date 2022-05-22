# 定義函式
# def 函式名稱(參數名稱): # ()內可不填
#   函式內容 # 要縮排
# 定義完畢即可利用 函式名稱(參數名稱) 呼叫函式
# 呼叫的函式會執行函式內部的程式，也會輸出一個值，其值由回傳值決定

# 回傳值 (沒有return 預設回傳值為None)
# def 函式名稱(參數名稱):
#     函式內部程式碼
#     retern 資料 # 結束函式，回傳「資料」 # 若無資料，回傳值為 None

# 回傳值範例
def say(msg):
    print(msg)
    return # ruturn後沒寫資料就等同於沒寫return
# 呼叫函式，取得回傳值
value1=say("Hello World") # 此處定義的add函式內的程式會執行一遍，輸出 Hello World
print(value1) # 印出回傳值: None

# ex2
def add(n1,n2):
    result=n1+n2
    return "Hello"
value2=add(3,4) # 執行函式，得到回傳值
print(value2) # 只印出"Hello"(回傳值)，不會輸出其他函式內部程式碼
# 但是若將return後的 "Hello"改為 result 輸出就會變成 n1+n2，即回傳值變為變數result

# 善用函式的兩個特點:執行內部程式、輸出回傳值。
# 可根據需求做兩個特點的取捨

# 程式的包裝--函式最重要的功能
# 將相似的程式設成一個函式，即可將程式縮減為一個函式呼叫指令
