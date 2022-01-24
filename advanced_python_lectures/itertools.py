
# from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
from itertools import count, cycle, repeat
from os import system
import operator
system("cls")

""" a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

a = [1, 2, 3, 4]
comb1 = combinations(a, 2)
print(list(comb1))

a = [1, 2, 3, 4]
comb2 = combinations_with_replacement(a, 2)
print(list(comb2))

a = [1, 2, 3, 4]
accm = accumulate(a)
print(a)
print(list(accm))

b = [1, 2, 3, 4]
accm1 = accumulate(b, func=operator.mul)
print(b)
print(list(accm1))

c = [1, 2, 7, 3, 4]
accm2 = accumulate(b, func=max)
print(c)
print(list(accm2))


def smaller_than_5(x):
    return x < 5


d = [1, 2, 5, 7, 9, 3, 4, 11, 12]
group_obj = groupby(d, key=smaller_than_5)
for key, value in group_obj:
    print(key, list(value))
 """
for i in count(10):
    print(i)
    if i == 20:
        break

a = [1, 2, 3]
say = 0
for i in cycle(a):
    print(i)
    say += 1
    if say == 21:
        break

a = [1, 2, 3]
for i in repeat(1, 3):
    print(i)
