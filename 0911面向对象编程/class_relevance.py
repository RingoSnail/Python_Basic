class RelationShip:
    """保存2个人的感情关联关系"""

    def __init__(self):
        self.couple = []

    def make_couple(self, obj1, obj2):
        self.couple.append(obj1)
        self.couple.append(obj2)
        print("[%s] 和 [%s] 正式结为对象..." % (obj1.name, obj2.name))

    def break_up(self):
        if self.couple:
            print("[%s] 和 [%s] 要分手了...真好" % (self.couple[0].name, self.couple[1].name))
            self.couple.clear()
        else:
            print("你根本就没对象，你分手个蛋呀...")

    def get_my_partner(self, obj):
        """返回我的另一半"""
        for i in self.couple:
            if obj != i:  # copule列表里有2个值，一个是我自己，一个是我对象，只要跟传进来的obj不相等，代表找到了我对象
                return i.name
        else:
            print("你没有对象，自己心里没有点数么....")


class Person:
    def __init__(self, name, age, sex, relation_obj):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation_obj  # 把RelationShip对象传进来
        # self.partner = None # 另一半，是个对象

    def do_private_stuff(self):
        """和男/女盆友干点羞羞的事"""
        print("%s is doing %s in the 7th hotel." % (self.name, self.relation.get_my_partner(self)))


relation_obj = RelationShip()
p1 = Person("武大郎", 25, "男", relation_obj)
p2 = Person("黑姑娘", 23, "女", relation_obj)
relation_obj.make_couple(p1, p2)  # 把2个人结合在一起
relation_obj.make_couple(p2, p1)
p1.do_private_stuff()
p2.do_private_stuff()
p1.relation.break_up()  # 要分手了
p1.relation.get_my_partner(p1)  # 再去查，就没有对象了
p2.relation.get_my_partner(p2)  # 再去查，就没有对象了
p1.do_private_stuff()
