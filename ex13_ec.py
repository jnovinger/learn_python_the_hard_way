#!/usr/bin/env python

'''
LPTHW Exercise 13
'''

from sys import argv

script, first, last = argv


print "Hello, %s!" % first
middle = raw_input("What is your middle name? ")
print "Well, hello then %s %s %s. My name is %s." % (first, middle, last, script)