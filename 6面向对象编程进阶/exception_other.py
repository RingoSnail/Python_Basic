s1 = 'hello'
try:
    # int(s1)
    print(d)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print("最后的万能异常", e)

# 异常结构
# try:
#     # 主代码块
#     pass
# except KeyError,e:
#     # 异常时，执行该块
#     pass
# else:
#     # 主代码块执行完，若未触发任何异常，执行该块
#     pass
# finally:
#     # 无论监测的代码是否发生异常，都执行该处代码
#     pass


# 主动触发异常
#     try:
#     raise Exception('错误了。。。')
# except Exception as e:
#     print(e)


# 自定义异常
# class MyException(BaseException): # BaseException是所有异常的基类
#     def __init__(self,msg):
#         self.message = msg
#     def __str__(self):
#         return self.message
# try:
#     raise MyException("我的错误")
# except MyException as e:
#     print(e)
