#!/usr/bin/env python

numbers = []

def populate_numbers(numbers):
    i = 0
    limit = 6
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)
        i += 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = populate_numbers(numbers)

print "The numbers: "

for num in numbers:
    print num