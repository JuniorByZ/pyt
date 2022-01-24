# Strings: ordered, immutable, text representation
from os import system
from re import sub
from typing import Type
system("cls")
print("...STRINGS...")
print("-"*15)
""" my_string = "Hello World"
print(my_string)

mystring = \"""Hello \
    World\"""
print(mystring)

char = my_string[-2]
print(char)
substring = my_string[::-1]
print(substring)
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for char in greeting:
    print(char)

if 'p' in greeting:
    print('yes')
else:
    print('no') """

""" my_string = "Hello World"
print(my_string.strip())
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('H'))
print(my_string.endswith('d'))
print(my_string.find('o'))
print(my_string.count('o'))
print(my_string.replace('World', 'Universe'))
string = "lorem upsum co more"
my_list = string.split(" ")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)
liste = list(string)
print(liste)
print(type(liste))
yeni_cumle = ''
for i in liste:
    print(i)
    yeni_cumle += i
print(yeni_cumle) """

"""my_list = ['a']*6
my_string = "".join(my_list)
print(my_string)"""

# format operators
# %, .format(), f-strings
system("cls")
var = "Tom"
num = 3.1234567
num2 = 6
"""my_string = "The Variable is %s" % var
print(my_string)
my_number = "The Variable is %.2f" % num
print(my_number)"""

"""my_string = "The variable is {}".format(var)
my_number = "The variable is {:.2f} and {}".format(num, num2)
print(my_string + ", " + my_number)"""

sentence = f"the variable as string {var}, as floating number  {num:.2f} and integer {num2}"
print(sentence)
