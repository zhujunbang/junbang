# from __future__ import unicode_literals
# from __future__ import division
#
# print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# print '\'xxx\' is str?', isinstance('xxx', str)
# print 'b\'xxx\' is str?', isinstance(b'xxx', str)
#
# print 10 / 3
# print 10.0 / 3
# print 10.0 // 3

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print '%s: %s' % (std['name'], std['score'])
print_score(std1)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

gg = Student("junbang","99")
mm = Student("miaoling","90")
gg.print_score();
mm.print_score();

