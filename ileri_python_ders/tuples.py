""" # tuples: ordered, immutable, allows duplicate elements"""
import timeit
import sys
from os import system
system("cls")
print("...TUPLES...")
print("-"*15)


# comma = ("Max") #string
# comma = ("Max",) #tuple


"""
def listele(liste):
    say  = len(liste)
    x=1
    for item in liste:
        if x == say:
            print(item,end="\n")
        else:
            print(item,end=",")
            x += 1  


mytuple = ("Max",20,"Boston")
listele(mytuple)

item = mytuple[0]
print(item)

mytuple = ("a","p","p","l","e")
print(len(mytuple))
print(mytuple.count('p'))
print(mytuple.index('p'))

mylist = list(mytuple)
print(mylist)
mytuple = tuple(mylist)
print(mytuple)

a = (1,2,3,4,5,6,7,8,9,10)
b = a[3:6]
print(b)
b = a[::2]
print(b)
b = a[0::1]
print(b)

mytuple = ("Max",28,"Boston")
name,age,city = mytuple
print(name,age,city)


mytuple = (1,2,3,4)
i1, *i2, i3 = mytuple
print(i1)
print(i3)
print(i2)
print("*"*30)
print("*"*30)
print("*"*30)
print("*"*30) """


""" system("cls")
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
print("-"*30)
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) """
