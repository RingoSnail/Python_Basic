def fib(f):
    a, b = 0, 1
    n = 0
    while n < f:
        n = a + b
        a = b
        b = n
        if n >= f:
            break
        yield n  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
        # yield相当于暂停, return是直接结束函数


print(fib(100))  # 并不输出函数结果，而是生成器的内存地址
print(fib(100).__next__())  # 生成器走一步
# 变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句暂停并返回数据到函数外，
# 再次被next()调用时从上次返回的yield语句处继续执行
print("-------------------")

for i in fib(100):
    print(i)

print("-------------------")
