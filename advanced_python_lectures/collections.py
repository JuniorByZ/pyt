# collections : counter, namedtuple, orderedDict,defaultdict,deque
""" from collections import Counter
from os import system
system("cls")
print("...COLLECTIONS...")
print("...COUNTER...")
print("-"*15)
a = "aaaaaaabbbbbcccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements())) """

""" from collections import namedtuple
from os import system
system("cls")
print("...COLLECTIONS...")
print("...NAMEDTUPLE...")
print("-"*15)
a = "aaaaaaabbbbbcccccccc"
Point = namedtuple("Point", 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y) """

""" from collections import OrderedDict
from os import system
system("cls")
print("...COLLECTIONS...")
print("...ORDEREDDICT...")
print("-"*15)
Ordered_dict = OrderedDict()
Ordered_dict['a'] = 1
Ordered_dict['b'] = 2
Ordered_dict['c'] = 3
Ordered_dict['d'] = 4
print(Ordered_dict) """


""" from collections import defaultdict
from os import system
system("cls")
print("...COLLECTIONS...")
print("...DEFAULTDICT...")
print("-"*15)
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for i in d:
    print(i) """

from collections import deque
from os import system
system("cls")
print("...COLLECTIONS...")
print("...DEQUE...")
print("-"*15)
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.extendleft([5, 6, 7])
print(d)
d.rotate(-1)
print(d)
