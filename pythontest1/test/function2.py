# L=[]
# n = 3
# while n<111:
#     L.append(n)
#     n=n+2
#
# print (L)
#
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# k = []
# n = 5
# for i in range(5):
#     k.append(L[i])
# print k
#
# x = L[0:3]
# print x
#
# z = L[:3]
# print z
#
# z = L[1:3]
# print z
#
# print L[-2:]
# print L[-3:-1]
#
# L = range(100)
# print L
# print L[:10]
# print L[-10:]
# print L[10:20]
# print L[:10:2]
# print L[::5]
# print L[:]
# from collections import Iterable
#
# print (0, 1, 2, 3, 4, 5)[:3]
#
# print 'ABCDEFG'[:3]
# print 'ABCDEFG'[::2]
#
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print key
#
# d = "efg"
# for key in d:
#     print key
#
# print isinstance('abc', Iterable)
# print isinstance(["a","b","c"], Iterable)
# print isinstance(123, Iterable)
#
# for i, value in enumerate(['A', 'B', 'C']):
#     print i,value
# import os
#
# print range(1, 11)
#
# L = []
# for x in range(1, 11):
#     L.append(x * x)
# print L
#
# print [x * x for x in range(1, 11)]
#
# print [x * x for x in range(1, 11) if x > 1]
#
# [m + n for m in 'ABC' for n in 'XYZ']
#
# print [m + n for m in 'ABc' for n in "xkb"]
#
# [d for d in os.listdir('.')]
#
# print [d for d in os.listdir('.')]
#
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
#
# for k, v in d.iteritems():
#     print k, "=", v
#
# [k + '=' + v for k, v in d.iteritems()]
# print [k + "=" + v for k, v in d.iteritems()]
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# [s.lower() for s in L]
# print [s.lower() for s in L]
#
# L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() for s in L if isinstance(s, str)]
#
# g = (x * x for x in range(10))
# print g
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# print g.next()
# for n in g:
#     print n

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


print fib(6)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print fib(6)


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


o = odd()
print o.next()
print o.next()
print o.next()

for n in fib(6):
    print n

import __builtin__
__builtin__.abs = 10
