#!/usr/bin/env python

def populate_numbers(numbers, start, stop, increment = 1):
    while start < stop:
        print "At the top i is %d" % start
        numbers.append(start)
        start += increment
        print "Numbers now:", numbers
        print "At the bottom i is %d" % start
    return numbers

start = 0
stop = 6
increment = 2
numbers = []
numbers = populate_numbers(numbers, start, stop, increment)

print "The numbers: "

for num in numbers:
    print num