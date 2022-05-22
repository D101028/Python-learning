# 抓取 Medium.COM 的文章標題
import urllib.request as req
url="https://medium.com/_/api/home-feed" # 真正的取得標題網址
# 建立一個 Request 物件(模組裡的物件)，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4530.3 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式

# 解析 JSON 格式的資料，取的每筆彈幕
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的形式
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])