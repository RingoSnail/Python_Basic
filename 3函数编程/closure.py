def outer():
    name = 'alex'

    def inner():
        print("在inner里打印外层函数的变量", name)

    return inner  # 不加括号，注意这里只是返回inner的内存地址，并未执行


f = outer()  # .inner at 0x1027621e0>
f()  # 相当于执行的是inner()
