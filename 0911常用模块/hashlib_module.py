import hashlib

# md5
m = hashlib.md5()
m.update(b"Hello")
print(m.digest())
print(m.hexdigest())

# sha1
s1 = hashlib.sha1()
s1.update("小猿圈".encode("utf-8"))
print(s1.hexdigest())

# sha256
s256 = hashlib.sha256()
s256.update("小猿圈".encode("utf-8"))
print(s256.hexdigest())

# sha512
s512 = hashlib.sha256()
s512.update("小猿圈".encode("utf-8"))
print(s512.hexdigest())
