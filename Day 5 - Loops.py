"""
Objective 
In this challenge, we're going to use loops to help us do some simple math.

Task 
Given an integer, n, print its first 10 multiples. Each multiple 
n x i(where 1 <= i <= 10) should be printed on a new line in the form:

n x i = result

"""

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,11):
        result = n * i
        print str(n) + " x " + str(i) + " = " + str(result)
        