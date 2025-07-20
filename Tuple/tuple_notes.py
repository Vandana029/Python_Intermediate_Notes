# tuple: ordered, immutable, iterable, allows duplicates

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple2 = 1, 2, 3, 4, 5, 6, 7, 8, 9
my_tuple3 = ('A',) # Note: A single element tuple requires a comma at the end,  type('A') would return a string
my_tuple4 = tuple([1, 2, 3, 4, 5])  # Creating a tuple from a list
my_tuple5 = tuple(range(1, 10))  # Creating a tuple from a range
my_tuple6 = tuple('Hello')  # Creating a tuple from a string
my_tuple7 = tuple({1, 2, 3, 4, 5})  # Creating a tuple from a set
my_tuple8 = tuple((1, 2, 3, 4, 5))  # Creating a tuple from another tuple

print(my_tuple)  # Output: (1, 2, 3, 4, 5)
print(my_tuple2)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple3)  # Output: ('A',)
print(my_tuple4)  # Output: (1, 2, 3, 4, 5)
print(my_tuple5)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple6)  # Output: ('H', 'e', 'l', 'l', 'o')
print(my_tuple7)  # Output: (1, 2, 3, 4, 5)
print(my_tuple8)  # Output: (1, 2, 3, 4, 5)

# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1, accessing the first element
print(my_tuple[-1])  # Output: 5, accessing the last element
print(my_tuple[1:4])  # Output: (2, 3, 4), slicing the tuple from index 1 to 3

# Iterating through a tuple
for item in my_tuple:
    print(item)  # Output: 1, 2, 3, 4, 5

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Concatenating tuples
new_tuple = my_tuple + my_tuple2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Repeating tuples
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking the length of a tuple
print(len(my_tuple))  # Output: 5, returns the number of elements in the tuple

# Checking if an element exists in a tuple
print(3 in my_tuple)  # Output: True, checks if 3 is in the tuple
print(6 in my_tuple)  # Output: False, checks if 6 is in the tuple  

# Finding the maximum and minimum values in a tuple
print(max(my_tuple))  # Output: 5, returns the maximum value in the tuple
print(min(my_tuple))  # Output: 1, returns the minimum value in the tuple   

# Converting a tuple to a set
my_set = set(my_tuple)  # Output: {1, 2, 3, 4, 5}, converts the tuple to a set
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Converting a tuple to a dictionary (using index as key)
my_dict = {i: my_tuple[i] for i in range(len(my_tuple))}
print(my_dict)  # Output: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}, converts the tuple to a dictionary

# Converting a tuple to a frozenset
my_frozenset = frozenset(my_tuple)  # Output: frozenset({1, 2, 3, 4, 5}), converts the tuple to a frozenset
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})


# Converting a tuple to a string
my_string = str(my_tuple) # Output: '(1, 2, 3, 4, 5)', converts the tuple to a string
print(my_string)  # Output: '(1, 2, 3, 4, 5)'


# Converting a tuple to a list
my_list_from_tuple = list(my_tuple)
print(my_list_from_tuple)  # Output: [1, 2, 3, 4, 5], converts the tuple to a list


# Converting a list to a tuple
my_tuple_from_list = tuple(my_list_from_tuple)      
print(my_tuple_from_list)  # Output: (1, 2, 3, 4, 5), converts the list back to a tuple


# Checking the type of a tuple
print(type(my_tuple))  # Output: <class 'tuple'>, confirms that my_tuple is a tuple


# Checking if a tuple is empty
empty_tuple = ()
print(len(empty_tuple) == 0)  # Output: True, checks if the tuple is empty


# Tuple methods
# Note: Tuples have very few methods compared to lists, mainly count and index
print(my_tuple.count(2))  # Output: 1, counts the number of occurrences
print(my_tuple.index(3))  # Output: 2, finds the index of the first occurrence
# Note: If the element is not found, index() will raise a ValueError
# print(my_tuple.index(6))  # Uncommenting this line will raise a ValueError    


# Tuple comprehension (not directly supported, but can be done using generator expressions)
my_tuple_comp = tuple(x for x in range(5))  # Creating a tuple using a generator expression
print(my_tuple_comp)  # Output: (0, 1, 2, 3, 4)


# Tuple as a key in a dictionary
my_dict = {(1, 2): 'a', (3, 4): 'b'}
print(my_dict[(1, 2)])  # Output: 'a', accessing a value

# unpacking with asterisk
my_tuple_unpack = (1, 2, 3, 4, 5)
a, *b = my_tuple_unpack
c, *d, e = my_tuple_unpack # `c` gets the first element, `d` gets all elements in between, and `e` gets the last element
print(c)  # Output: 1
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]
print(d)  # Output: [2, 3, 4]
print(e)  # Output: 5

##############################################################################################################################

import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(sys.getsizeof(my_list), 'bytes')  # Output: Size of the list in bytes
print(sys.getsizeof(my_tuple), 'bytes')  # Output: Size of the tuple in bytes
# Output: Tuples are generally smaller in size compared to lists
# because they are immutable and have a fixed size, while lists are dynamic and can grow or shrink in size.
# This means that tuples have less overhead and are more memory-efficient than lists.
# Note: The size difference may vary based on the elements in the tuple or list, but generally, tuples are more memory-efficient.
# Note: Tuples are generally faster than lists for iteration and access due to their immutability.

import timeit
# Timing tuple creation
tuple_creation_time = timeit.timeit('my_tuple = (1, 2, 3, 4, 5)', globals=globals(), number=1000000)
list_creation_time = timeit.timeit('my_list = [1, 2, 3, 4, 5]', globals=globals(), number=1000000)
print(f"Tuple creation time: {tuple_creation_time} seconds")
print(f"List creation time: {list_creation_time} seconds")  
# Output: Tuples are generally faster to create than lists due to their immutability and fixed size.

##############################################################################################################################

############## -------EASY------- ##############
# 1. Tuple Immutability Trick
t = ([1, 2], [3, 4])
t[0].append(5)
print(t)
# Explanation:
# This code creates a tuple `t` containing two lists. Since the lists are mutable,
# we can modify them even though they are inside a tuple. 

# 2. Tuple Packing & Unpacking
a, b = 10, 20
a, b = b, a
print(a, b)
# Explanation: how swapping works without using a temporary variable
# This code swaps the values of `a` and `b` using tuple unpacking.

# 3. Singleton Tuple Confusion
x = (5)
y = (5,)
print(type(x), type(y))
# Explanation:
# This code demonstrates the difference between a single value in parentheses (which is an integer) and
# a single value followed by a comma (which is a tuple).

# 4. Tuple in a Set
a = {(1, 2), (3, 4)}
print((1, 2) in a)
# Explanation:
# This code checks if the tuple `(1, 2)` is present in the set `a`. Tuples can be used as elements in a set because they are hashable.

# Why are tuples usable inside sets?
# Tuples are hashable because they are immutable, meaning their contents cannot change over time.
# This makes them suitable for use as keys in dictionaries and as elements in sets, which require their elements to be hashable.

# 5. Mutable Element in Tuple
my_tuple = ([1, 2, 3], 'hello')
my_tuple[0][0] = 99
print(my_tuple)
# Explanation:
# This code modifies the first element of the list inside the tuple. Since lists are mutable,
# we can change their contents even though they are inside a tuple.

# 6. Tuple vs List Speed Test
# Q: Why are tuples faster than lists?
# Ans: Tuples are generally faster than lists because they are immutable and have a fixed size.
# This means that the Python interpreter can optimize their storage and access patterns more effectively.   

# 7. Count Occurrences
t = (1, 2, 3, 2, 4, 2)
print(t.count(2))
# Explanation:
# This code counts the number of occurrences of the value `2` in the tuple `t`. The `count` method returns the number of times the specified value appears in the tuple.

# 8.Nested Tuple Indexing
t = (1, (2, 3), (4, (5, 6)))
print(t[2][1][0])
# Explanation:
# This code accesses the nested tuple and retrieves the value `5`. The indexing works as follows:
# - `t[2]` accesses the third element of the outer tuple, which is `(4, (5, 6))`.
# - `t[2][1]` accesses the second element of the tuple `(4, (5, 6))`, which is `(5, 6)`.        
# - `t[2][1][0]` accesses the first element of the tuple `(5, 6)`, which is `5`.

# 9. Tuple Sorting Trick
t = (3, 1, 2)
print(sorted(t))
# Explanation:
# This code sorts the tuple `t` and returns a new sorted list. The `sorted` function returns a new list containing the elements of the tuple in ascending order.

# 10. Tuple Concatenation
a = (1, 2)
b = (3, 4)
c = a + b
print(c)
# Explanation:
# This code concatenates the two tuples `a` and `b` to create a new tuple `c`. The `+` operator is used to concatenate tuples in Python.

# IMPORTANT NOTE:
# In Python:
    # - An object is hashable if it has a fixed hash value during its lifetime.
    # - Immutable objects like integers, strings, tuples are hashable.
    # - Mutable objects like lists, sets, and dictionaries are not hashable.
# ✅ Hashable objects can be safely used as keys in dictionaries or as elements in sets because their value won’t change, so the hash won’t change.
my_set = {[1, 2], [3, 4]}  # ❌ TypeError

t = ([1, 2], 3)  # Tuple containing a list
print(hash(t))   # ❌ Error
# Even though `t is a tuple (which is normally hashable), it contains a list, which is mutable → this makes the whole tuple unhashable.
# ✅ A tuple is hashable if all its elements are hashable.
# ❌ If a tuple contains any mutable element (like a list or dictionary), it becomes unhashable.

############################################################################################################################## 
############## -------MEDIUM------- ##############
# 1. Tuple as Function Arguments
t = (x for x in range(5))
print(type(t)) # Output: <class 'generator'>, Using parentheses with comprehension creates a generator, not a tuple.
# Explanation:
# This code creates a generator expression, not a tuple. To create a tuple, you need to use parentheses with a comma, like this:
t = tuple(x for x in range(5))

# 2. Tuple and Function Return
def return_tuple():
    return 1, 2, 3

result = return_tuple()
print(type(result)) # Multiple return values are packed into a tuple automatically in Python.
# Explanation:
# This code defines a function that returns a tuple. When the function is called, it returns a tuple containing the values `1`, `2`, and `3`. The type of `result` will be `<class 'tuple'>`.

# 3. Tuple Slicing Trick 
t = (10, 20, 30, 40, 50)
print(t[-3:-1])
# Explanation:
# The result will be `(30, 40)`.

# 4. Tuple Indexing Edge Case
t = (1, 2, 3)
print(t[3])
# Explanation:
# This code attempts to access the fourth element of the tuple `t`, which does not exist. It will raise an `IndexError`.

# 5. Nested Tuple Mutation Trap
t = ((1, 2), [3, 4])
t[1].append(5)
print(t)
# Explanation:
# This code modifies the list inside the tuple `t`. Since lists are mutable, we can change their contents even though they are inside a tuple. The output will be `((1, 2), [3, 4, 5])`.

# 6. Tuple of Tuples Flattening
t = ((1, 2), (3, 4), (5, 6))
# One-liner list comprehension to flatten it into (1, 2, 3, 4, 5, 6).
flattened = [item for sublist in t for item in sublist]
print(flattened)
# Explanation:
# This code uses a list comprehension to flatten the tuple of tuples `t` into a single list containing all the elements. The output will be `[1, 2, 3, 4, 5, 6]`.

# 7. Tuple Memory Consumption
# Q: Why are tuples more memory-efficient than lists?
# Ans: Tuples use less memory than lists because they are immutable and don’t store overhead for operations like appending/removing elements.

# 8. Tuples and Default Mutable Argument Trap
def func(arg=()):
    arg += (1,)
    print(arg)

func()
func()
# Explanation:
# This code defines a function `func` that takes a default argument of an empty tuple. When the function is called without an argument, it uses the default empty tuple. 
# The `+=` operator creates a new tuple with the added element, leaving the original tuple unchanged. The output will be `(1,)` for the first call and `(1,)` for the second call as well.

# 9. Tuple vs NamedTuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
# Explanation:
# This code demonstrates the use of `namedtuple` from the `collections` module to create a tuple with named fields.
# The `Point` named tuple has fields `x` and `y`, which can be accessed like attributes. The output will be `10 20`.

# 10. Tuple Dictionary Key Puzzle
t = (1, 2)
d = {t: "Tuple as key"}
print(d)
# Explanation:
# This code creates a dictionary with a tuple as the key. Tuples can be used as keys in dictionaries because they are hashable. The output will be `{(1, 2): 'Tuple as key'}`.

############################################################################################################################## 
############## -------HARD------- ##############
# 1. Tuple Hash Consistency
a = (1, 2, 3)
b = (1, 2, 3)
print(hash(a) == hash(b))
# Explanation: ✅ Same contents → same hash value. Hashing is content-based for immutable types.
# This code checks if the hash values of two identical tuples `a` and `b` are equal. Since tuples are immutable and their contents are the same, their hash values will also be the same. The output will be `True`.

# 2. Deep Immutability Trap
t = (1, [2, 3])
print(hash(t))
# Explanation:
# This code attempts to hash a tuple that contains a mutable list. Since the list is mutable, the tuple becomes unhashable, and the code will raise a `TypeError`. The output will be an error message indicating that the tuple is unhashable.

# 3. Recursive Tuple Construction
t = (1, 2)
for _ in range(3):
    t = (t,)
print(t)
# Explanation:
# This code constructs a nested tuple by wrapping the existing tuple `t` in another tuple three times. The output will be a deeply nested tuple structure: `(((1, 2),),)`.

# 4. Deeply Nested Tuple Indexing
t = (((1, 2),),)
print(t[0][0][1])
# Explanation:
# This code accesses the deeply nested element in the tuple `t`. The output will be `2`.

# 5. Tuple Generator in Function Scope
def generate_tuples(n):
    for i in range(n):
        yield (i, i + 1)

gen = generate_tuples(3)
print(next(gen))
print(next(gen))
print(next(gen))
# Explanation:
# This code defines a generator function that yields tuples. When the generator is called, it produces tuples one by one. The output will be:
# `(0, 1)`
# `(1, 2)`
# `(2, 3)`  


def gen():
    return (i*i for i in range(4))

t = gen()
print(sum(t))
print(sum(t))
# Explanation:
# This code defines a generator function `gen` that yields the squares of numbers from 0 to 3. When `sum(t)` is called the first time, it calculates the sum of the squares (0 + 1 + 4 + 9 = 14).
# When `sum(t)` is called the second time, the generator has already been exhausted, so it returns 0 because there are no more values to sum. The output will be:
# `14`
# `0`

# Note: Generators are iterators that produce values on-the-fly and can only be iterated once. After the first iteration, they are exhausted.


