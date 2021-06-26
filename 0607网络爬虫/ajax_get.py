# 爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据
import requests

if __name__ == "__main__":

    url = "https://movie.douban.com/j/chart/top_list?"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36',
    }

    param = {
        'type': '5',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }

    response = requests.get(url=url, headers=headers, params=param)

    print(response.json())