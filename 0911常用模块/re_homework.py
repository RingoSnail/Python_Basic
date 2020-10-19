import re

phone = re.compile("\A1\d{10}")
print(re.fullmatch(phone, "15039087916"))

email = re.compile(r"^[\w\-]+@\w+(\.\w+){1,2}$")  # \w包含数字字母下划线
print(re.fullmatch(email, "tianyu_w-0289@bupt.edu.cn"))

expression = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
print(re.search(r"[^(]+", expression, re.DOTALL))

print(re.search("[^123]", ))
