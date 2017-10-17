# -*- coding:utf-8 -*-

# taskmanager.py
'''''
1.建立队列，作为共享消息的通道。 服务进程
任务队列task_queue作为服务进程传递任务给任务进程的通道，而结果队列result_queue作为任务进程完成任务后回传给服务进程的通道。
值得注意的是，在【一台机器上】写多进程程序时，创建的Queue可以直接拿来用
然而，在分布式多进程环境下，不可以直接添加任务到原始的task_queue，那样就绕过了Queuemanager的封装，
必须通过manager.get_task_queue()获得的【Queue接口】添加任务。
2.把1.中建立的队列在网络上注册，暴露给其他进程(主机)，注册后获得【网络队列】(可以认为是1.中队列的'映像')
3.建立一个对象(Queuemanager(BaseManager))实例manager，绑定端口和验证码
4.启动3.中建立的实例，以便监听连接(启动管理 manager，监管信息通道)
5.通过管理实例的方法获得通过网络访问的Queue对象，即再把网络队列实体化成可以使用的本地队列(通过本地上传到网络)
6.创建任务到“本地”队列中，自动上传任务到网络队列中，以供分配给
'''

import random, time, Queue
from multiprocessing.managers import BaseManager

# 建立两个队列，分别存放任务和结果，它们用来进行进程间通信，交换对象。换言之，这两个队列就是交换对象
task_queue = Queue.Queue()
result_queue = Queue.Queue()


class Queuemanager(BaseManager):
    pass


# 把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
# typeid is a “type identifier”(类型标识符) which is used to identify a particular type of shared object. This must be a string.
# callable is a callable used for creating objects for this type identifier.——后者用来创建前者，后者是具体的对象，而前者是利用后者创造出来的“影子”
Queuemanager.register('get_task_queue', callable=lambda: task_queue)
Queuemanager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000，设置验证码‘abc’。这个相当于对象的初始化
# address is the address on which the manager process listens for new connections
manager = Queuemanager(address=('', 5000), authkey='abc')

# 启动管理
manager.get_server().serve_forever()

# 通过管理实例的方法获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print 'put task %d ...' % n
    task.put(n)  # task是本地队列

print 'try get result...'
for i in range(10):
    print 'result is %s' % result.get(timeout=10)

# 关闭管理
manager.shutdown()
