# print abs(-10)
#
# print abs
#
# x = abs(-10)
#
# print x
#
# x = abs
# print x(-9)
#
# import __builtin__
#
# # abs = 11
#
# print abs(-11)
#
#
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print add(-9, 8, abs)
#
#
# def f(x):
#     return x * x + 1
#
#
# print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# L = []
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(i))
# print L


# def add(x, y):
#     return x + y
#
#
# print reduce(add, [1, 3, 5, 7, 9])
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print reduce(fn, [1, 3, 5, 8, 9])
#
# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print reduce(fn, map(char2num, '13579'))
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))
#
# def str2int(str):
#     def fn(x,y):
#         return x*10 +y
#     def char2num(str):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
#     return reduce(fn,map(char2num,str))
#
# print str2int('13579'),2
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# def str2int(s):
#     return reduce(lambda x,y:x*10+y,map(char2num,s))
#
# print str2int("13789")

#
# def is_odd(n):
#     return n + 5
# print filter(is_odd,[1,3,5,6,7])
#
# def is_empty(s):
#     return s and s.strip()
# print filter(is_empty, ["1","","2"])

# print sorted([36, 5, 12, 9, 21])

# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
#
# print sorted([36, 5, 12, 9, 21],reversed_cmp)
#
# # sorted(['bob', 'about', 'Zoo', 'Credit'])
#
# def cmp_ingore_case(s1,s2):
#     t1 = s1.upper()
#     t2 = s2.upper()
#     if t1 < t2:
#         return -1
#     if t1 > t2:
#         return 1
#     return 0
# print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ingore_case)

# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# print calc_sum(1,5,8)
#
# def lazy_count(*args):
#     def calc_sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return calc_sum
#
# print lazy_count(1,5,8)()

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print f1()
# print f2()
# print f3()
#
# def sum():
#     fs = []
#     for i in range(1,4):
#         def f(k):
#             def m():
#                 return k*k
#             return m
#         fs.append(f(i))
#     return fs
# k1,k2,k3 = sum()
# print k1()
# print k2()
# print k3()

# from test2 import function2

# def f(x):
#     return x * x
#
#
# print map(f, [1, 2, 3, 5, 6])
#
# print map(lambda x: x * x, [1, 5, 8])
#
# f = lambda x: x * x
# print map(f,[5,8])

# def k(x,y):
#     return lambda x:x*x +y
# m = k;
# print map(m(1,2),[1,3,9])

# def now():
#     print "xxx"
# k = now
# # k()
# print now.__name__

# def log(func):
#     def wrapper(*args,**kw):
#         print "call %s():" % func.__name__
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print "lll"
# now()
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
import functools


# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print "%s %s:" % (text,func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print 'call %s():' % func.__name__
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def have():
#     print "kkk"
# have()
# print have.__name__

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log("this")
# def have():
#     print "kkk"
# have()
# print have.__name__

# print int('12345')
# print int('12345', base = 8)
# print int('12345', base = 10)
# print int('12345', base = 16)
# print int('12345', base = 8)

def int2(x, base=2):
    return int(x,base)
print int2('1010101')

int2 = functools.partial(int,base=2)
print int2("1010101")
print int2("1010101", base=10)

max2 = functools.partial(max,23)
print max2(1,19,13)