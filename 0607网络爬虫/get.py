# 爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
import requests

word = input("enter a word you want to research:")

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
url = "https://www.sogou.com/web"
param = {
    "query":word,
}

response = requests.get(url=url, params=param, headers=headers)
page_text = response.text

fileName = word + ".html"
with open(fileName, "w", encoding="utf-8") as fp:
    fp.write(page_text)
