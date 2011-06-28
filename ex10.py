#!/usr/bin/env python

tabby_cat = "%sI'm tabbed in." % '\t'
persian_cat = "I'm split%son a line." % '\n'
backslash_cat = "I'm %s a %s cat." % ('\\', '\\')

r_formatter = "%r %r" % (tabby_cat, persian_cat)
s_formatter = "%s %s" % (tabby_cat, persian_cat)

print r_formatter
print s_formatter

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
