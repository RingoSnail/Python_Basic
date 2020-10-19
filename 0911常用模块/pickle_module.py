import pickle

data = {'k1': 123, 'k2': 'Hello'}

# pickle.dumps 将数据通过特殊的形式转换位只有python语言认识的字符串
p_str = pickle.dumps(data)  # 注意dumps会把数据变成bytes格式
print(p_str)

# pickle.dump 将数据通过特殊的形式转换位只有python语言认识的字符串，并写入文件
with open('result.pkl', "wb") as fp:
    pickle.dump(data, fp)

# pickle.load  从文件里加载
f = open("result.pkl", "rb")
d = pickle.load(f)
print(d)
