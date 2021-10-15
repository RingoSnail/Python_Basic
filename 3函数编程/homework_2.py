import math


def area(item, *args):
    def roundness(R):
        dimension = math.pi * (R ** 2)
        return dimension

    def square(A):
        dimension = A ** 2
        return dimension

    def rectangle(L, W):
        dimension = L * W
        return dimension

    if item == "圆形":
        print(roundness(*args))
    if item == "正方形":
        print(square(*args))
    if item == "长方形":
        print(rectangle(*args))


area("圆形", 3)
area("正方形", 3)
area("长方形", 4, 5)


def factorial(n):
    fn = 1
    for i in range(1, n + 1):
        fn *= i
    return fn


print(factorial(10))
