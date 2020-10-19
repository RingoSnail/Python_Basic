class ShenXianBase:
    def fight(self):
        print("神仙祖宗在打架....")


class MonkeyBase:
    def fight(self):
        print("猿猴在打架....")


class ShenXian(ShenXianBase):
    """神仙类"""

    def fly(self):
        print("神仙都会飞...")
    def fight(self):
        print("神仙在打架...")


class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    def fight(self):
        print("猴子在打架...")


class MonkeyKing(ShenXian, Monkey):
    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")
    def fight(self):
        print("孙悟空打架")


swk = MonkeyKing()
swk.fight()


# MonkeyKing - ShenXian - ShenXianBase
#            - Monkey   - MonkeyBase
# 方法重名时按从左到右，深度搜索顺序

# 经典类 新式类 深度 广度 c3算法 不再深究
