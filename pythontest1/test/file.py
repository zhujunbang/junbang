# -*- coding: utf-8 -*-
# f = open('E:/test.txt', 'r')
#
# print f.read()
# f.close()

# try:
#     f = open('/path/to/file', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()

# try:
#     f = open("E:/test.txt", "r")
#     print f.read()
# finally:
#     if f:
#         f.close()

# with open('/path/to/file', 'r') as f:
#     print f.read()

# with open("E:/test.txt", "r") as f:
#     print f.read()


# try:
#     f = open("E:/test.txt", "r")
#     for line in f.readlines():
#         print(line.strip())  # 把末尾的'\n'删掉
# finally:
#     if f:
#         f.close()

# f = open('E:/test.png', 'rb')
# print f.read()

# f = open('E:/test2.txt', 'w')
# f.write('Hello, world!')
# f.close()

# with open('E:/test3.txt', 'w') as f:
#     f.write('Hello, world!')
import os

# print os.name
# print os.environ
# print os.getenv('PATH')
# print os.path.abspath('.')
# # print os.mkdir('E:/test')
# print os.rmdir('E:/test')

# print os.path.split('/Users/michael/testdir/file.txt')
# print os.path.splitext('/path/to/file.txt')

# os.rename('E:/test8.txt',"E:/test9.txt")
# os.remove("E:/test9.txt")

[x for x in os.listdir("E:/") if os.path.isdir(x)]
 # print x
