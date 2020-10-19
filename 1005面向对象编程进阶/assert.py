def my_interface(name, age, score):
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float


my_interface("alex", 22, 89.2)

assert type(1) is int
assert 1 + 1 == 2
assert 1 + 1 == 3  # 会报AssertionError
