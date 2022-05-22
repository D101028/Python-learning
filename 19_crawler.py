# 抓取 ptt 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html" # 直接貼網址通常會被拒絕存取
# 建立一個 Request 物件(模組裡的物件)，附加 Request Headers 的資訊
# 打開網址
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4530.3 Safari/537.36"
})
# 讀取 HTML
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# 解析原始碼，取的每篇文章的標題 # 第三方程式下載-->pip install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 協助解析 HTML 格式文件
# print(root.title.string) # 印出網頁標題
# titles=root.find("div", class_="title") # 尋找 class="title" 的 div 標籤
# print(titles.a.string) # 印出
titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤(note:直接打 class="title" 會出現判斷錯誤，加一個 _ 即可避免)
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
        print(title.a.string)
