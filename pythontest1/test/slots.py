# coding utf-8

# class Student(object):
#     pass
#
# s = Student();
# s.name = "junbang"
# print s.name
#
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
#
# Student.set_age = MethodType(set_age,None,Student)
# s.set_age(25)
# print s.age
#
# s2 = Student()
# s2.set_age(25)
# print s2.age

# class Student(object):
#     __slots__ = ("name", "score")
#
#
# s = Student()
# s.name = "junbang"
# print s.name
# s.age = 30
# print s.name


# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("score must be an integer!")
#         if value < 0 or value >100:
#             raise ValueError("score must between 0 ~ 100~")
#         self._score = value
#
# s = Student()
# s.set_score(99)
# print s.get_score()
#
# s.set_score(999)
# print s.get_score()




# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError("score must be an integer!")
#         if value < 0 or value >100:
#             raise ValueError("score must between 0 ~ 100~")
#         self._score = value
#
# s = Student()
# s.score = 99
# print s.score

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,birth):
        self._birth = birth

    @property
    def age(self):
        return 2017 - self._birth

s = Student()
s.birth = 1989
print s.birth
print s.age