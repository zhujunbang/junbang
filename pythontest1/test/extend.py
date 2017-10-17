from SocketServer import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass
#
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass

class Mammal(Animal):
    pass

class RunnableMixin(object):
    def run(self):
        print("running ...")

class Flyable(object):
    def fly(self):
        print("Flying ...")


class Dog(Mammal,RunnableMixin):
    pass

class Bat(Mammal,Flyable):
    pass

class CarnivorousMixin(object):
    pass

class Dog(Mammal,RunnableMixin,CarnivorousMixin):
    pass

# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass

class MyTcpServer(TCPServer,ForkingMixIn):
    pass

# class MyUDPServer(UDPServer, ThreadingMixin):
#     pass

class MyUdpServer(UDPServer,ThreadingMixIn):
    pass