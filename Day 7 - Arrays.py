"""
Objective 
Today, we're learning about the Array data structure.

Task 
Given an array, A, of N integers, print A's elements in reverse order as a 
single line of space-separated numbers.

"""


#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    for i in arr[::-1]:
        print i,
