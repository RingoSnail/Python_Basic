# 破解百度翻译
import requests
import json

word = input("enter an English word:")

headers = {
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/69.0.3497.100 Safari/537.36',
}
url = "https://fanyi.baidu.com/sug"
data = {
    "kw":word,
}
response = requests.post(url=url, data=data, headers=headers)
json_data = response.json()

fileName = word + ".json"
fp = open(fileName, "w", encoding="utf-8")
json.dump(json_data, fp, ensure_ascii=False)