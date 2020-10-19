import os


print("-------带path-------")
print(os.name)  # 返回当前平台，对于Windows是'nt'，而对于Linux/Unix用户是'posix'
print(os.getcwd())  # 当前工作路径
print(os.listdir())  # 当前目录下所有文件和目录名
# os.mkdir()
# os.rmdir()
# os.remove()
# os.system()

print("-------不带path-------")
print((os.path.isfile("C:/Users/Ringo/PycharmProjects/Hi_python/0911常用模块/os_test")))  # 判断指定路径下的一些内容
print((os.path.isdir("C:/Users/Ringo/PycharmProjects/Hi_python/0911常用模块")))
print((os.path.exists("C:/Users/Ringo/PycharmProjects/Hi_python/0911常用模块")))
print((os.path.getsize("C:/Users/Ringo/PycharmProjects/Hi_python/0911常用模块/os_test")))
print((os.path.split("C:/Users/Ringo/PycharmProjects/Hi_python/0911常用模块/os_test")))
print((os.path.abspath("os_test")))  # 获取绝对路径
print((os.path.basename("C:/Users/Ringo/PycharmProjects/Hi_python")))

