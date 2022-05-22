# 抓取 ptt 八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件(模組裡的物件)，附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1", # 加入 cookie
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4530.3 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼，取的每篇文章的標題 # 第三方程式下載-->pip install beautifulsoup4
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 協助解析 HTML 格式文件
    titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁") #找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]
# 呼叫函式
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1