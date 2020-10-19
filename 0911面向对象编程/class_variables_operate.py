class Person:
    nationality = "Chinese"


p = Person()
p.name = "Alex"  # 随时可给实例增加属性
print(p.name, p.nationality)

Person.race = "Yellow"  # 给类增加属性
print(p.race)

# del p.sex
# del Person.addr
