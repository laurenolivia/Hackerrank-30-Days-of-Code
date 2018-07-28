"""
Objective 
Today we're expanding our knowledge of Strings and combining it with what 
we've already learned about loops.

Task 
Given a string, S, of length N that is indexed from 0 to N - 1, 
print its even-indexed and odd-indexed characters as 2 space-separated strings 
on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T (the number of test cases). 
Each line i of the T subsequent lines contain a String, S.

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())


for i in range(0,t):
    s = raw_input()
    even, odd = s[::2], s[1::2]
    print even + " " + odd
