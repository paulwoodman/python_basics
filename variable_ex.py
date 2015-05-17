#!/usr/bin/python
# Created by Paul Woodman
# Basic script to understand that a variable is something that can change.
# In this example I have used if/else statments

#import the random module
from random import randint

# x is the variable. Each time the script is run it will generate
# number beween 1 to 10. 
x = randint(1,10)

# the if state will print if x is less than 6
if x <= 5:
  print 'Under 6'  
  print x 
# the elif will print if x is equal to 6
elif x == 6:
  print 'It was a six! grab a cookie'
  print x
# The elif will print if x is greater than 6
elif x >= 5:
  print "Over 6"
  print x
