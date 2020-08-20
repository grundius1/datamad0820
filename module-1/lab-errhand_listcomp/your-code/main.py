#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
from os import walk, listdir
import random

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [math.sqrt(i) for i in range(20)]
print(square)


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two = [i**2 for i in range(50)]
print(power_of_two)


#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [math.sqrt(i) for i in range(100)]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = [i for i in range(-10,1)]
print(my_list)


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odd = [i for i in range(100) if i%2 != 0]
print(odd)


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [i for i in range(1,1001) if i%7 == 0]
print(divisible_by_seven)


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
vowels_list = ['a','e','i','o','u','A','E','I','O','U']
non_vowels = "".join([i for i in teststring if i not in vowels_list])
print(non_vowels)



#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

text = "The Quick Brown Fox Jumped Over The Lazy Dog"
capital_letters = [i for i in text if ord(i) in range(65,91)]
print(capital_letters)


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

consonants = [i for i in text if i not in vowels_list]
print(consonants)



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

files = [x for x in listdir("/home/borja/Desktop/Ironhack/datamad0820")]
print(files)
'''
f = []
for (dirpath, dirnames, filenames) in walk("/home/borja/Desktop/Ironhack/datamad0820"):
    f.extend(filenames)
print(f)'''


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists = [[random.randint(0,100) for i in range(10)] for x in range(4)]
print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
list_of_lists = [num for lista in list_of_lists for num in lista]
print(list_of_lists)



#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]
floats = [float(num) for lista in list_of_lists for num in lista]
print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 

try:
    for i in ['a','b','c']:
        print (i**2)
except Exception as e:
    print(e)

print("excepcion manejada")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("dont divide by Zero")




#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print("error en el indice del array")

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

def division():
    a = float(input("introduzca primer numero "))
    b = float(input("introduzca segundo numero "))
    print(a/b)
    return
    

while True:
    try:
        division()
        break
    except ZeroDivisionError:
        print("No dividas por cero! Que haces, Felipe?")
    except TypeError:
        print("Tipo invalido. a y b deben ser int o float")
    except Exception as e:
        print("Ha fallado, verifique error")
        print(e)

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("file not found revise path")



#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')
    try:
        line = f.readline()
        i = int(s.strip())
    except IndentationError:
        print("indentation error error")
except FileNotFoundError:
    print("file not found revise path")



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
try:
    def linux_interaction():
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
except Exception as e:
    print(e)


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

def squaref():
    while True:
        try:
            num = input("give me a number: ")
            print(float(num)**2)
            return
        except ValueError as e:
            print(e)

squaref()


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

results = [[i for i in range(1000) if i%e == 0] for e in range(2,10)]
'''tree = [i for i in range(1000) if i%3 == 0]
four = [i for i in range(1000) if i%4 == 0]
five = [i for i in range(1000) if i%5 == 0]
six = [i for i in range(1000) if i%6 == 0]
eight  = [i for i in range(1000) if i%8 == 0]
nine = [i for i in range(1000) if i%9 == 0]
'''
print(results)
'''print(tree)
print(four)
print(five)
print(six)
print(divisible_by_seven)
print(eight)
print(nine)'''



# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
Total_Marks = -1
while Total_Marks < 0:
    try:
        Total_Marks = int(input("Enter Num oTotal marks: "))
    except ValueError:
        print("value must be an integuer")
Num_of_Sections = 0
while Num_of_Sections < 2:
    try:
        Num_of_Sections = int(input("Enter Num of Sections: "))
    except ValueError:
        print("value must be bigger than 1")

