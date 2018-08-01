"""
Objective 
Today, we're learning about Key-Value pair mappings using a Map or Dictionary 
data structure.

Task 
Given n names and phone numbers, assemble a phone book that maps friends' 
names to their respective phone numbers. You will then be given an unknown 
number of names to query your phone book for. For each name queried, print the 
associated entry from your phone book on a new line in the form 
name=phoneNumber; if an entry for name is not found, print Not found instead.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
phoneBook = {}

for i in range(0,n):
    entry = raw_input().split(" ")
    name, number = entry[0], entry[1]
    phoneBook[name] = number

for key in range(0,n):
    search_name = raw_input()
    if search_name in phoneBook:
        print "{}={}".format(search_name, phoneBook[search_name])
    else:
        print "Not found"
    