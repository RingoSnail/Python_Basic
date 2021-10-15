# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
name = "py"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi,{name}')  # Press Ctrl+F8 to toggle the breakpoint. f''即format格式输出


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Ringo")  # 主程序调用了之前定义的print_hi函数

print(__name__)  # __name__的主要作用就是用来区分，模块是直接被运行还是被导入
print(name)  # 全局变量并未被修改

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
