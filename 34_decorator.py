# # 定義裝飾器
# def myDeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb()
#     return run

# # 使用裝飾器
# @myDeco
# def test(): # test 會被丟進 cb 當作回呼函式
#     print("普通函式的程式碼")

# test()
# # 先執行裝飾器內部的函式
# # 再執行被裝飾的函式 (test)


# # 定義裝飾器
# def myDeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb(3)
#     return run

# # 使用裝飾器 (加入參數)
# @myDeco
# def test(n): # test 會被丟進 cb 當作回呼函式
#     print("普通函式的程式碼", n)

# test(3)

# 定義 sigma(n=1-->50)n
def calculate(callback):
    def run():
        result = 0
        for n in range(51):
            result += n
        # print(result)
        callback(result) # 把計算結果透過參數傳給被裝飾的函式
    return run

@calculate
def show(n):
    # print("普通函式的程式碼")
    print("計算結果", n)

@calculate
def showEnglish(n):
    print("Result is", n)

show()
showEnglish()

