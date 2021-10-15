goods = [
    ["电脑", 1999],
    ["鼠标", 10],
    ["游艇", 20],
    ["美女", 998]
]
shop_list = []
count = 0

salary = int(input("请输入工资"))
print("请选择商品：")
for i in goods:
    print((goods.index(i) + 1), i[0], i[1])


while count <= 10:
    choose = int(input("请输入序号选购")) - 1
    if goods[choose][1] <= salary:
        count += 1
        shop_list.append(goods[choose][0])
        salary -= goods[choose][1]
        if salary < 10:
            break
    elif goods[choose][1] >= salary:
        print("工资不足")

print("购物清单：", shop_list[0:], "工资余额：", salary)