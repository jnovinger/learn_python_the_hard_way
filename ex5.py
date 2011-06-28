#!/usr/bin/env python

'''

'''

name = 'Zed A. Shaw'
age = 35
height_in = 74
height_cm = height_in * 2.54
weight_lbs = 180
weight_kg = weight_lbs * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall. That's %d feet, %d inches" % (height_in, height_in / 12, height_in % 12)
print "In metric that is %f cm, or %f m" % (height_cm, height_cm / 100)
print "He's %d pounds heavy (or %f kg)." % (weight_lbs, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_in, weight_lbs, age + height_in + weight_lbs)
