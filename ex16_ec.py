#!/usr/bin/env python

# import argv module
from sys import argv

# unpack argv and assign to vars
script, filename = argv

# open txt file for reading
txt = open(filename)

# echo back contents of the txt file
print txt.read()

# close the file
txt.close()