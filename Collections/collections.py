# collections: Counter, namedtuple, OrderDict, defaultdict, deque 

# 1. Counter (A container that stores the elements as dictionary keys and their counts as dictionary values.)
from collections import Counter
a = 'aaaaaaaaaabbbbbccccccc'
my_counter = Counter(a) 
print(my_counter) # Counter({'a': 10, 'c': 7, 'b': 5})
print(my_counter.items()) # dict_items([('a', 10), ('b', 5), ('c', 7)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])

print(my_counter.most_common(2)) # print top 2 most common elements like this: [('a', 10), ('c', 7)]

# This gives iterable over elements repeating each as many times as it counts.
print(my_counter.elements()) # <itertools.chain object at 0x0000025D7BBC5810>
print(sorted(my_counter.elements())) 
['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c']


########################################################################################################

# 2. namedtuple ()
from collections import namedtuple
# Creates a class called 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', 'x,y') 
pt = Point(1, 2)
print(pt) # Point(x=1, y=2)
print(pt.x, pt.y) # 1 2


########################################################################################################

# 3. OrderedDict (normal dictionary but they remember the order that the items were inserted. BTW, In latest version (from python 3.7 ig)
# built-in dictionary also remembers order.)
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])


########################################################################################################

# 4. defaultdict (It is also same as usual dictionary, with only difference is that it will have default if key has not been inserted yet.)
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] = 1
print(default_dict['b']) # will return default value of int i.e 0

default_dict2 = defaultdict(list)
print(default_dict2['a']) # will return default value of list i.e empty list ([])


########################################################################################################

# 5. deque (double ended queue, can add/remove from both ends)
from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d)    # deque([1, 2]) 
d.appendleft(5)
print(d)    # deque([5, 1, 2])
d.pop()
print(d)    # deque([5, 1])
d.extend([9,8,7])
d.popleft()
print(d)    # deque([1, 9, 8, 7])
d.remove(1)
print(d)    # deque([9, 8, 7])
d.clear()
print(d)    # deque([])
d.extendleft([6,12, 18, 24, 30])
print(d)    # deque([30, 24, 18, 12, 6])
d.rotate(1) # rotate all elements, one place to the right side
print(d)    # deque([6, 30, 24, 18, 12])
d.rotate(-2) # rotate all elements, two place to the left side
print(d)    # deque([24, 18, 12, 6, 30])