# coding=utf-8
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#
# print Student('Michael')
#
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "Student object(name:%s)" % self.name
#     __repr__ = __str__
#
#
# s = Student("junbang")
# print s

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def next(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration();
#         return self.a  # 返回下一个值
#
#
# for n in Fib():
#     print n
#
#
# # print Fib()[1]
#
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
# f = Fib()
# print f[0]
# print f[1]
# print f[2]
# print f[0:5]

# print range(100)[5:10]

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#         return L


# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#         return L
#
#
# f = Fib()
# print f[0:3]
# print f[:3]
# print f[:12]
# print f[:12:5]


# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, item):
#         if item == "score":
#             return 100
#         if item == "age":
#             return lambda: 30
#         raise AttributeError("student object has no attribute %s" % item)
#
# s = Student()
# print s.name
# print s.score
# print s.age()


# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
# c = Chain()
# # print c.status
# print c.status.user.timeline.list
#
# print c.users.repos

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)

# s = Student("junbang")
# s()

# print callable(Student("jun"))
#
# print callable(max)
#
# print callable(None)