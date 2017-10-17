# coding: utf-8

# print abs(-100)
# print abs(12.12)
# print abs(1,1)
# print abs("a")
# print abs(12)
# print cmp(1,2)
# print cmp(2,1)
# print cmp(3,3)
#
# print int("33")
#
# print str(1.23)
#
# a = cmp
# print a(1,2)
import math


# def my_abb(x):
#     if x>5:
#         print x
#     else:
#         print -x
#
# def my_abc(x):
#     if x>3:
#         return 5
#     else:
#         return 8
#
# #pass instand of TODO
# def my_abd(x):
#     pass
#
# def my_abe(x):
#     if not isinstance(x,int):
#         raise TypeError('bad operand type')
#     if x>5:
#         return 8
#     else:
#         return 9
#
# print my_abe(3)

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# r = move(1, 2, 3, 5)
# print r

# def power(x):
#     return x * x
# print power(3)
#
# def power(x,y=2):
#     s = 2
#     while y > 1:
#         y = y -1
#         s = s * x
#     return s;
# print power(3,2)
#
# print power(3)

# def enroll(name, gender,age=12,city="广州"):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city

# enroll("zhu", 123)
# enroll('Adam', 'M', city='Tianjin')
# enroll('Adam', 'M', age='Tianjin')

# def add_end(L=[]):
#     L.append('END')
#     return L

# print add_end([1, 2, 3])
# print add_end()
# print add_end()

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print add_end()
# print add_end()

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print calc(1,2,3)
# print calc(1,2,3,5,7)
# print calc()
# print calc()
#
# nums = [1, 2, 3]
# print calc(*nums)

# def person(name, age, **kw):
#     print 'name:', name, 'age:', age, 'other:', kw
#
# print person("junbang",12,city=3)
# print person("junbang",12,city=3,height=176)
#
# kw = {'city': 'Beijing', 'job': 'Engineer'}
# print person("junbang",12,**kw)

# def person(name, age=12, *args, **kw):
#     print "a=", name, "b=", age, "args=", args, "kw=", kw
#
# person(1, 2)
# person(1, 2, c=3)
# person(1, 2, 3, 'a', 'b')
# person(1, 2, 3, 'a', 'b', x=99)
#
# args = (1,2,3)
# kw = {"xz":90}
# person(*args,**kw)

# def fact(n):
#     if n == 2:
#         return 2
#     return fact(n-1) * n;
#
# print fact(5)

