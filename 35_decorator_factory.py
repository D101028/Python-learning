# 用來"生產"裝飾器的"函式"

# # 定義
# def 裝器工廠名稱(參數名稱, ...):
#     def 裝飾器名稱(回呼函式名稱):
#         def 內部函數名稱():
#             # 裝飾器內部程式碼
#             回呼函示名稱()
#         return 內部函式名稱
#     return 裝飾器名稱

# # 使用
# @裝飾器工廠名稱(參數資料, ...)
# def 函式名稱():
#     # 函式內部的程式碼
# 函式名稱() # 呼叫帶有裝飾器的函式


# def myFactory(base):
#     def myDeco(cb):
#         def run():
#             print("裝飾器內的程式", base)
#             result = base*2
#             cb(result)
#         return run
#     return myDeco

# @myFactory(3)
# def test(result):
#     print("普通函式的程式", result)

# test()

# 計算 1+2+3+...+n 的裝飾器
def calculateFactory(max):
    def calculate(callback):
        def run():
            total = 0
            for n in range(max):
                total+=n
            callback(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("結果是", result)

@calculateFactory(10)
def showEnglish(result):
    print("Result is", result)

show()
showEnglish()

