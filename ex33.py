#!/usr/bin/env python

def populate_numbers(numbers, start, stop):
    while start < stop:
        print "At the top i is %d" % start
        numbers.append(start)
        start += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % start
    return numbers

start = 0
stop = 6
numbers = []
numbers = populate_numbers(numbers, start, stop)

print "The numbers: "

for num in numbers:
    print num