# 爬取天眼查中任意的企业对应的页面数据：https://www.tianyancha.com/
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

headers = {
    'Cookie': 'csrfToken=VtbnK1tn9NoUb0fUqHVlS0Xc; jsid=SEM-BAIDU-PZ0824-SY-000001; bannerFlag=false; '
              'Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1600135387; show_activity_id_4=4; '
              '_gid=GA1.2.339666032.1600135387; relatedHumanSearchGraphId=23402373; '
              'relatedHumanSearchGraphId.sig=xQxyUIDqVdMkulWk5m_htP28Pzw8_eM8tUMIyK4_qqs; refresh_page=0; '
              'RTYCID=69cd6d574b1c4116995bab3fd96a9466; CT_TYCID=a870d4ebb91849b094668d1d969c7702; '
              'token=899079c4b21e4d22916083d22f72e1e3; _utm=dac53239b45f49709262be264fd289f3; '
              'cloud_token=bb4c875aed794641966b7f7536187e80; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1600147199; '
              '_gat_gtag_UA_123487620_1=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/75.0.3770.100 Safari/537.36 '
}

key_words = ['小米', '华为', '知乎']
num = 0
for key_word in key_words:
    url = 'https://www.tianyancha.com/search?key={}'.format(quote(key_word))  # 汉字转码
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    info = soup.select('.result-list .content a')[0]
    company_name = info.text
    company_url = info['href']
    print(company_name, company_url)  # 过渡页面

    html_detail = requests.get(company_url, headers=headers)
    soup_detail = BeautifulSoup(html_detail.text, 'lxml')
    data_infos = soup_detail.select('.table.-striped-col tbody tr td')  # 只要这个标签的数据

    with open('company.txt', 'a+', encoding='utf-8') as f:
        if num != 0:
            num = 1
        f.write('\n' * num + company_name + " : " + '\n')
        for info in data_infos:
            print(info.text)
            f.write(info.text)  # 存进txt文件
        num += 1
