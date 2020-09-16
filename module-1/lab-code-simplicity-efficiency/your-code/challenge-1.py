"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
from word2number import w2n

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


numbers= {
    0:'zero',
    1: 'one',
    2:'two',
    3:'three',
    4:'four',
    5: 'five',
    6: 'six' ,
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten'
}
a = w2n.word_to_num(a)
c = w2n.word_to_num(c)
if (a not in list(range(0,6))) or (c not in list(range(0,6))):
    print("I am not able to answer this question. Check your input.")
else:
    if b == 'plus':
        print(f"{numbers[a]} {b} {numbers[c]} equals {numbers[a+c]}")
    if b == 'minus':
        if a - c < 0:
            print(f"{numbers[a]} {b} {numbers[c]} equals {b} {numbers[abs(a-c)]}")
        else:
            print(f"{numbers[a]} {b} {numbers[c]} equals {numbers[a-c]}")

print("Thanks for using this calculator, goodbye :)")