# class Student(object):
#     pass
#
# t = Student()
# print t
# print Student
#
# t.name = "junjun"
# print t.name

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score > 99 :
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# bang = Student("king",100)
# print bang.name
# print bang.get_grade()

# class Student(object):
#     def __init__(self,name,score):
#         self._Student__name = name
#         self.__score = score
#
#     def get_grade(self):
#         if self.__score > 99 :
#             return 'A'
#         elif self.__score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#     def get_name(self):
#         return self._Student__name
#
#     def set_name(self,name):
#         self._Student__name = name
# bang = Student("junjun",100)
# print bang.set_name("junbang")
# print bang.get_name()
# print bang._Student__name

# class Animal(object):
#     def run(self):
#         print "animail is running"
#
# class Dog(Animal):
#     def run(self):
#         print "dog is running"
# class Cat(Animal):
#     def run(self):
#         print "cat is running"
#
# d = Dog()
# d.run()
#
# a = list()
# b = Animal()
# c = Dog()
#
# print isinstance(a,list)
# print isinstance(b,Animal)
# print isinstance(c,Animal)
# print isinstance(c,Animal)
# print isinstance(b,Dog)
#
# def run_twice(nimal):
#     nimal.run()
#     nimal.run()
#
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Animal())
#
# class Tortoise(Animal):
#     def run(self):
#         print 'Tortoise is running slowly'
#
# run_twice(Tortoise())
# import types
#
# print type(123)
# print type("abc")
# print type(None)
#
# ab = "s"
# print type(ab)
# print type(None)
#
# print type(123) == types.StringType
# print type([]) == types.ListType
# print isinstance(123,int)

# print dir("ABC")
# print len("ABCDE")
# 
# class MyO(object):
#     def __len__(self):
#         return 100
# 
# d = MyO()
# print len(d)
# 
# print 'ABC'.lower()

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
print hasattr(obj, "x")
print obj.x
print hasattr(obj, 'y')
setattr(obj,"y","33")
print hasattr(obj,"y")
print obj.y
print getattr(obj,"k","404")
print hasattr(obj, 'power')
print getattr(obj,"power")
k = getattr(obj,"power")
print k
print k()