def test():
    print('开始啦')
    yield 1
    print('第一次')
    yield 2
    print('第二次')


t = test()
res = t.__next__()  # __next__() 执行到yield 1
print(res)  # 打印yield的返回值：1
print(next(t))  # next() 执行到yield 2
