age_of_old_boy = int(input("年龄:"))

if age_of_old_boy > 50:
    print("老了！")
else:
    print("还能折腾几年!")

score = int(input("输入分数:"))
if score > 100:
    print("我擦，最高分才100...")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")  # 从上到下执行
