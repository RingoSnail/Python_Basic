# local enclosing_function global builtins

level = 'L0'
n = 22


def func():
    level1 = 'L1'
    n = 1
    print("func:", locals(), n)

    def outer():
        n = 2
        level = 'L2'
        print("outer:", locals(), n)

        def inner():
            level = 'L3'  # 不同空间中的两个相同名字的变量之间没有任何联系
            print("inner:", locals(), n)  # 此外打印的n是多少？ 一层一层向外找
            print("global:", globals())

        inner()

    outer()


func()
