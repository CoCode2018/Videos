# -*- encoding: utf-8 -*-

print('Hello World')
print('我爱中国')

# 基本数据类型
print(type(1))
print(type(1.0))
print(type(1 + 1.0J))
print(type(False))
print(type('1'))

# 交互
name = input("名字：")
age = input("年龄：")
# 字符串可以拼接，相邻的字符串使用 , 时会加一个空格
print('我的名字是' + name, '我的年龄是' + age + '岁。')
# (<class 'str'>, <class 'str'>)
print((type(name), type(age)))

