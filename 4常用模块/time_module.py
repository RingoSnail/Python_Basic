import time
import datetime

"""
元组（struct_time）
索引（Index）    属性（Attribute）    值（Values）
0     tm_year（年）                 比如2011
1     tm_mon（月）                  1 - 12
2     tm_mday（日）                 1 - 31
3     tm_hour（时）                 0 - 23
4     tm_min（分）                  0 - 59
5     tm_sec（秒）                  0 - 61
6     tm_wday（weekday）            0 - 6（0表示周日）
7     tm_yday（一年中的第几天）       1 - 366
8     tm_isdst（是否是夏令时）        默认为-1
"""
print(time.localtime())
print(time.gmtime())
print(time.time())
print(time.asctime())
print("-----------------------")

print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time()))