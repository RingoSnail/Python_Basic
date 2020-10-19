name = input("Name:")
age = int(input("Age:"))  # 将input输入的str转为int类型
job = input("Job:")
hobby = input("Hobby:")
info = '''
------------ info of %s ----------- 
Name  : %s  
Age   : %d  
job   : %s  
Hobby : %s  
------------- end -----------------
''' % (name, name, age, job, hobby)

"""
这行的 %号就是把前面的字符串与拓号后面的变量关联起来，需要按顺序！
%s就是代表字符串占位符，除此之外，还有%d,是数字占位符，%f是浮点数占位符， 如果把上面的age后面的换成%d，就代表你必须只能输入数字
input接收的所有输入默认都是字符串格式！
"""

print(info)
