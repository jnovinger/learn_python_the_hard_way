#!/usr/bin/env python

# this one is like you scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arg
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no args
def print_none():
    print "I got nothing."

print_two('Jason', 'Novinger')
print_two_again('Jason', 'Novinger')
print_one('First!')
print_none()