a=('a','b','c','d')
b="1","2","3",4,5
print(type(a))
print(type(b))
c=a+b
print (c)

#字典
dict1={'key1':'value1','key2':2}
#元组
tuple1=('first','second','third','fourth')
tuple2='break1','break2','break3','break4'
#列表
list1=['1','2','3','4']


print(type(dict1),type(tuple1),type(list1))
print(dict1)

a=set('google')
print(type(a))
print(a)

d=2**4
print(d)

a, b = 0, 1
while b < 10:
    print(b,end=',')
    a, b = b, a+b

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

