# 網路連線
# 下載特定網址資料
import urllib.request as request
with request.urlopen("https://www.google.com") as response:
    data=response.read() # 看到原始碼(HTML、CSS、JS)
print(data)
with request.urlopen("https://www.google.com") as response:
    data=response.read().decode("utf-8") # 解碼中文字
print(data)
# 串接、擷取、下載公開資料 (API)
# EX.台北市政府
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/bdc97a62-4da4-43f9-8c35-c0e6157d3d68?scope=resourceAquire"
with request.urlopen(src) as response:
       data=json.load(response) # 利用 json 模組處理 json 資料格式
# 將區域名稱列表出來
clist=data["result"]["results"] # 去看 json 
for area in clist:
    print(area["區"])
# 抓到檔案裡
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/bdc97a62-4da4-43f9-8c35-c0e6157d3d68?scope=resourceAquire"
with request.urlopen(src) as response:
       data=json.load(response)
clist=data["result"]["results"] 
with open("data.txt", "w", encoding="utf-8") as file:
    for area in clist:
        file.write(area["區"]+"\n")
