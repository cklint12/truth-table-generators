#!/usr/bin/python

import itertools 

num_flips = input("Enter number of flips: ") 
table  = itertools.product('HT', repeat = num_flips)

# Generate the table
for outcome in table:
    print(outcome)

