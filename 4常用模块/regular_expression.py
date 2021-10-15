import re

f = open("os_test")
data = f.read()

print(re.search("\d{11}", data))  # 全局，找到一个就行
print(re.findall("\d{11}", data))  # 全局，匹配数字11次，找到所有的
print(re.match("\d{11}", data))  # 从第一个字符就开始匹配
print(re.split("\d", "alex1rog2"))  # 以匹配到的字符做分隔符  re.findall("[a-z]{1,4}", "alex1rog2")
print(re.sub("\d", "0", "19960806", count=4))  # 替换
print(re.fullmatch("Ringo", "ringo"))  # 完全匹配
print(re.fullmatch('\w+@\w+\.(com|cn|edu)', "alex@oldboyedu.cn"))
print("-----------------------------")

"""
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
'*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
'{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'
"""

print(re.search(".", data))  # "." 随意匹配一个除\n的字符
print(re.search("^t", data))  # 匹配开头是t
print(re.search("t*", data))  # 匹配0次或多次
print(re.findall("t+", data))  # 匹配1次或多次
print(re.search("t?", data))  # 匹配0次或1次
print("-----------------------------")
print(re.findall("t{2,3}", data))  # 指定匹配次数
print(re.search("abc|ABC", "ABCBabcCD"))  # 或
print(re.search("(t){1,3}est", data))
print("-----------------------------")

"""
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
'\Z'    匹配字符结尾，同$ 
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
"""

print(re.search("\At", data))
print(re.findall("\W+", data))

id_num = str(410182199608060333)
a = re.search("(?P<province>[0-9]{3})(?P<city>[0-9]{3})(?P<birth>[0-9]{4})", id_num)
print(a.groupdict())
print("-----------------------------")

p = re.compile("\d{11}")  # 提前编译好正则
print(p.findall(data))
print("-----------------------------")

# FLAGS
print(re.search("TEST", data, re.IGNORECASE))  # 无视大小写
print(re.search("tttest", data, re.MULTILINE))  # 换行模式
print(re.search(".", "\n", re.DOTALL))  # 匹配任何，包括转义符

x = re.compile(r"""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""",
               re.X)
# 写注释
# r即raw原生字符，取消转义
# y = re.compile(r"\d+\.\d*")
print("-----------------------------")

s = "1+2-3*4/5"
print(re.split("[\+\-\*\/]", s))  # \取消转义
