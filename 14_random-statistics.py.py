# 模組1
import random
# 從列表中隨機顯取1個資料
random.choice([0,1,5,8])
# 從列表中隨機選取2個資料
random.sample([0,1,5,8],2)
# 將列表的資料「就地」隨機調換順序
data=[0,1,5,8]
random.shuffle(data) # shuffle:洗牌
print(data) # 他會將data本身的順序調換，所以要印出data
# 取的 0.0 ~1.0 之間的隨機亂數
random.random()
# 相當於
random.uniform(0.0, 1.0) # 代表出現機率相等
# 常態分配亂數
# 取得平均數 100、標準差 10 的
# 常態分佈亂數
random.normalvariate(100, 10) # (平均數,標準差)

# 模組2
import statistics # statistics:數據統計
# 平均數
statistics.mean([1,4,6,9])
# 中位數
statistics.median([1,4,6,9])
# 標準差 (standard deviation)
statistics.stdev([1,4,6,9])