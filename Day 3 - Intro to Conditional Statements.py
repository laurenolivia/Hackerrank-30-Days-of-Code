"""
Objective 
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

"""

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(raw_input())
    
    if N % 2 != 0:
        print "Weird"
    elif N % 2 == 0 and N in range(2,6):
        print "Not Weird"
    elif N % 2 == 0 and N in range(6, 21):
        print "Weird"
    elif N % 2 == 0 and N > 20:
        print "Not Weird"
