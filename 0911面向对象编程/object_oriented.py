dog_attack_level = {
    "京巴": 20,
    "藏獒": 80,
    "平头哥": 60
}


def dog(name, d_type):
    if d_type in dog_attack_level:
        d = {
            "name": name,
            "type": d_type,
            "life_val": 100
        }
    else:
        print("未知物种，不易接近")
        return None

    def bite(person_obj):  # 把这个方法写在dog里面，表示这是dog独有的功能
        person_obj["life_val"] -= dog_attack_level[d["type"]]
        print("疯狗[%s]咬了[%s],掉血[%s]..." % (d["name"], person_obj['name'], dog_attack_level[d["type"]]))

    d["bite"] = bite
    return d


def person(name, age, sex):
    d = {
        "name": name,
        "age": age,
        "sex": sex,
        "life_val": 100
    }
    if age > 18:
        d["attack_level"] = 50
    else:
        d["attack_level"] = 30

    def beat(dog_obj):  # 把这个方法写在person里面，表示这是person独有的功能
        dog_obj["life_val"] -= d['attack_level']
        print("[%s] 打了 疯狗[%s],狗掉血[%s]..." % (d["name"], dog_obj["name"], d["attack_level"]))

    d["beat"] = beat
    return d


dog1 = dog("majj", "平头哥")  # 生成角色
dog2 = dog("二哈", "京巴")
p1 = person("alex", 22, "male")
dog1["bite"](p1)  # 调用时只传递要咬谁就行了
p1["beat"](dog2)
print(dog1, dog2)