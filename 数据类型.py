### 整数

a=1
b=10
c=100000
# 对于位数多的整数可以使用“_”的方式来表明位数
d=1_00_000

# 16进制表示
hex=0xaf15
# 16位整数也可以用下划线'_'来隔开
hex2=0xaf_ffff_ffff

### 浮点数
a=1.23
b=3.123
c=-9.123
# 用科学计数法来表示一些很大的浮点数
d=1.23*10**9
# 但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等
b=1.23e9
d=1.2e-5

### 字符串
# 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等
a='abc'
b="abc"
c="I\'m Ok"
d='我打印出\\n'
e='我打印出\\\\n'


### 布尔值
a=True
b=False
c=2>3
# 布尔值可以用and、or和not运算。
a=True and False
b=True or False
c=not True #运算是非运算，它是一个单目运算符，把True变成False，False变成True

age=19
if age>=18:
    print('已成年')
else:
    print('未成年')

### 空值
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

### 常量 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
# 事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
P=123

### 数据类型转换
print(int(123))
print(int(12.3))
print(int('12'))
print(float('12.3'))
print(float(12))
print(str(1))
print(str(12.3))