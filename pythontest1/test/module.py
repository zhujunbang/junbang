# coding utf-8

' a test module '
import sys

try:
    import cStringIO as StringIO
except ImportError:
    import  StringIO

try:
    import json
except ImportError:
    import simplejson as json

__author__ = "zhujunbang"

def test():
    args = sys.argv
    if len(args) == 2:
        print "hello kitty"
    elif len(args) == 3:
        print "hello, %s!" % args[1]
    else:
        print "too many argument!"

if __name__ == "__main__":
    test();


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)