import json

data = {'k1':123,'k2':'Hello'}

# json.dumps 将数据通过特殊的形式转换为所有程序语言都认识的字符串
j_str = json.dumps(data)  # 注意json dumps生成的是字符串，不是bytes
print(j_str)

# dump入文件
with open('result.json', 'w') as fp:
    json.dump(data, fp)

# 从文件里load
with open("result.json") as f:
    d = json.load(f)
    print(d)