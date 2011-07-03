#!/usr/bin/env python

print "How old are you?",
age = raw_input('(in years) --> ')
print "How tall are you?",
height = raw_input('(in feet an inches) --> ')
print "How much do you weigh?",
weight = raw_input('(in lbs) --> ')

print "So, you're %s years old, %s inches tall, and %s lbs heavy." % (
    age, height, weight)

# BMI = (weight in lbs * 703) / (height in inches)^2
bmi = (float(weight) * 703) / (float(height) ** 2)
print "And your BMI is %f." % bmi
