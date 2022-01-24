# Lambda arguments : expression
from functools import reduce
from os import system
system("cls")
print("...LAMBDA...")
print("-"*15)

""" def add(x): return x+10
def add10(x): return x + 10


print(add10(20))
print(add(5)) """


""" def sort_by_y(x):
    return x[1]


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])  # key=sort_by_y
print(points2D)
print(points2D_sorted) """

# map(func,seq)

a = [1, 2, 3, 4, 5, 6]
""" b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c) """

# filte(func,seq)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

c = [x % 2 == 0 for x in a]
print(c)

d = [x for x in a if x % 2 == 0]
print(d)

#reduce(func, seq)
prod_a = reduce(lambda x, y: x*y, a)
print(prod_a)
