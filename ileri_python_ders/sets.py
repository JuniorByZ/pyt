# Sets : unordered, mutable, no duplicates
from os import system

system("cls")
""" empty_set = set()

myset = {1, 2, 3, 2, 1, 2, 3, 4} """


""" empty_set.add(5)
empty_set.remove(5)

myset.discard(3)
print(myset)

print(myset.pop()) 

for i in myset:
    print(i)

if 4 in myset:
    print("yes")"""

""" odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diffA = setA.difference(setB)
diffB = setB.difference(setA)
print(diffA)
print(diffB)

diffAB = setA.symmetric_difference(setB)
diffBA = setA.symmetric_difference(setB)
print(diffAB)
print(diffBA) """

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

# setA.symmetric_difference_update(setB)
# print(setA)

""" AA = {1, 2, 3, 4, 5}
BB = {1, 2, 3}
print(AA.issubset(BB))
print(BB.issuperset(AA))

print(AA.issuperset(BB))
print(BB.issubset(AA))

print(AA.isdisjoint(BB))

CC = AA.copy()
CC.add(7)
print(CC)
print(AA) """

#a = frozenset([1, 2, 3, 4])

# a.add(5)
# a.remove(1)

# print(a)
