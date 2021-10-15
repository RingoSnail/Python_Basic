# 爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据
import requests

if __name__ == "__main__":

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }

    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10'
    }

    response = requests.post(url=url,headers=headers,data=data)

    print(response.json())