import secrets
import random

from os import system
system("cls")
print("...RANDOM NUMBERS...")
print("-"*20)

# a = int(random.random()*10)+1
# print(a)

# b = random.randint(1, 10)
# print(b)

# c = random.normalvariate(0, 1)
# print(c)

# my_list = list("ABCDEFGHIJKL")
# d = random.choice(my_list)
# print(d)

# e = random.choices(my_list, k=3)  # multiple
# print(e)

# f = random.sample(my_list, 3)  # unique
# print(f)

# random.shuffle(my_list)
# print(my_list)

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

a = secrets.randbelow(10)
print(a)
a = secrets.randbits(4)
print(a)
a = secrets.randbits(8)
print(a)
a = secrets.randbits(16)
print(a)
a = secrets.randbits(32)
print(a)
a = secrets.randbits(64)
print(a)
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)
