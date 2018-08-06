"""
Objective 
Today, we're working with binary numbers.

Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and 
print the base-10 integer denoting the maximum number of consecutive 1's in n's 
binary representation.

"""

#!/bin/python

import sys


if __name__ == '__main__':
    n = int(raw_input())
    
    count = 0
    maximum = 0

    while n > 0:
        if n % 2 == 1:
            count += 1
            if  count > maximum:
                maximum = count
        else:
            count = 0
        
        n //= 2

print(maximum)
            