import requests
from fake_useragent import UserAgent

ua = UserAgent(use_cache_server=False, verify_ssl=False).random
headers = {
    'User-Agent': ua
}
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
pageNum = 3
for page in range(3, 5):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    json_text = requests.post(url=url, data=data, headers=headers).json()
    all_id_list = []
    for dict in json_text['list']:
        id = dict['ID']  # 用于二级页面数据获取
        # 下列详情信息可以在二级页面中获取
        # name = dict['EPS_NAME']
        # product = dict['PRODUCT_SN']
        # man_name = dict['QF_MANAGER_NAME']
        # d1 = dict['XC_DATE']
        # d2 = dict['XK_DATE']
        all_id_list.append(id)
    # 该url是一个ajax的post请求
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in all_id_list:
        post_data = {
            'id': id
        }
        response = requests.post(url=post_url, data=post_data, headers=headers)
        if response.headers['Content-Type'] == 'application/json;charset=UTF-8':
            # print(response.json())
            # 进行json解析
            json_text = response.json()
            print(json_text['businessPerson'])
