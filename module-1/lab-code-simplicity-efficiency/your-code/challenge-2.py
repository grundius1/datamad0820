"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import sys
import random
import string

def RandomStringGenerator (l=12):
    numbers = list(map(str,range(10)))
    letters = list(string.ascii_lowercase)
    arr= letters+numbers
    s=''
    for item in range(l):
        s += random.choice(arr)
    return s

def BatchStringGenerator(n, a=8, b=12):
    r=[]
    for item in range(n):
        if a <= b:
            r.append(RandomStringGenerator(random.choice(range(a,b+1))))
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')


print(BatchStringGenerator(int(n), int(a), int(b)))
