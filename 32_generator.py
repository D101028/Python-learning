# for 變數名稱 in 生成器:
#     將稱成器產生的資料
#     逐一取出

# # 建立稱生成器
# def test():
#     yield 3
# # 呼叫函式, 回傳生成器
# gen=test()
# print(gen)
# # 拿出資料
# for d in gen:
#     print(d)

# def test():
#     print("階段一")
#     yield 3
#     print("階段一")
#     yield 5
# # 函式內程式暫時不會執行 (有兩個以上的 yield 的話)
# gen=test()
# # 利用 for 迴圈執行函式內部程式
# for d in gen:
#     print(d)

# def generateEven():
#     number=0
#     yield number
#     number+=2
#     yield number
#     number+=2
#     yield number

# evenGenerator=generateEven()
# for data in evenGenerator:
#     print(data)


def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGenerator=generateEven(16)
for data in evenGenerator:
    print(data)
