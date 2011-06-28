#!/usr/bin/env python

# assign initial formatted strings values
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print out formatted strings
print x
print y

# repeat myself
print "I said: %r." % x
print "I also said: '%s'." % y

# it is kind of a tired joke
hilarious = False
joke_evaluation = "Isn't that so funny?! %r"

print joke_evaluation % hilarious

# define a couple strings
w = "This is the left side of..."
e = "a string with a right side."

# concatenate them and print
print w + e
