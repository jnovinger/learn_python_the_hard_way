#!/usr/bin/env python

def populate_numbers(numbers, start, stop, increment = 1):

    for number in range(start, stop, increment):
        print "At the top i is %d" % number
        numbers.append(number)
        print "Numbers now:", numbers
        print "At the bottom i is %d" % number
        
    return numbers


start = 0
stop = 6
increment = 2
numbers = []
numbers = populate_numbers(numbers, start, stop, increment)

print "The numbers: "

for num in numbers:
    print num