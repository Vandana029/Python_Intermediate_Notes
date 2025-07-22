### How to Create a Dictionary
d1 = {}  # Empty dictionary
d2 = dict()  # Another way to create an empty dictionary
d3 = {'a': 1, 'b': 2, 'c': 3}  # Dictionary with key-value pairs


# Using keyword arguments to create a dictionary, here keys (i.e., 'a', 'b', 'c') must be variable names, it cannot be a constant. 
d4 = dict(a=1, b=2, c=3)  
print(d4)  # {'a': 1, 'b': 2, 'c': 3}, # here, 'a', 'b', 'c' are converted to strings automatically to make it a key.
# Note: The keys must be valid identifiers, so you cannot use numbers or special characters as keys.
# Example of invalid key usage:
# d = dict(1='A', 2='B', 3='C')  # This will raise a SyntaxError because keys must be valid identifiers.

d5 = dict([('a', 1), ('b', 2), ('c', 3)])  # Using a list of tuples to create a dictionary
d6 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Using zip to create a dictionary from two lists

################################################################

### How to Access Elements in a Dictionary
d7 = {'a': 1, 'b': 2, 'c': 3}
print(d7['a'])  # Accessing value by key, prints 1
print(d7.get('b'))  # Using get method, prints 2
# If the key does not exist, get method returns None by default, or you can specify a default value
print(d7.get('d', 'Not Found'))  # Prints 'Not Found' since 'd' is not a key in the dictionary

################################################################

# Using a for loop to iterate over keys and values
for key, value in d7.items(): # unpacking the key-value pairs 
    print(f"Key: {key}, Value: {value}")

for t in d7.items():  # Iterating over key-value pairs (tuples of key and value), Example: ('a', 1)
    print(f"Key: {t[0]}, Value: {t[1]}")  # Accessing key and value in the loop

for key in d7:  # Iterating over keys
    print(f"Key: {key}, Value: {d7[key]}")  # Accessing value by key in the loop

for value in d7.values():  # Iterating over values
    print(f"Value: {value}")  # Prints each value in the dictionary

for key in d7.keys():  # Iterating over keys
    print(f"Key: {key}")  # Prints each key in the dictionary

################################################################

### How to Modify a Dictionary
d8 = {'a': 1, 'b': 2, 'c': 3}
d8['d'] = 4  # Adding a new key-value pair  
d8['a'] = 10  # Modifying an existing key's value
print(d8)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4}
d8.update({'e': 5, 'f': 6})  # Adding multiple key-value pairs using update method
print(d8)  # {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d8.pop('b')  # Removing a key-value pair by key
print(d8)  # {'a': 10, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(d8)  # {} 
d8.popitem()  # Removes and returns an arbitrary key-value pair, but this is not recommended for use in production code as it is unpredictable.
d8.clear()  # Removing all key-value pairs from the dictionary

# Updating a dictionary with key which is not present in the dictionary
d9 = {'x': 1, 'y': 2}
d9.setdefault('z', 3)  # Adds 'z' with value 3
print(d9)  # {'x': 1, 'y': 2, 'z': 3}

################################################################

### Built-in Functions for Dictionaries
d10 = {'a': 1, 'b': 2, 'c': 3}
print(len(d10))  # Returns the number of key-value pairs in the dictionary, prints 3
print(min(d10))  # Returns the smallest key in the dictionary, prints 'a'
print(max(d10))  # Returns the largest key in the dictionary, prints 'c'
print(sum(d10.values()))  # Returns the sum of all values in the dictionary, prints 6
print(sorted(d10))  # Returns a sorted list of keys, prints ['a', 'b', 'c']

################################################################

### How to Check for Existence of Keys
d10 = {'a': 1, 'b': 2, 'c': 3}
print('a' in d10)  # True, checks if 'a' is a key in the dictionary
print('d' in d10)  # False, checks if 'd' is a key in the dictionary
print('a' not in d10)  # False, checks if 'a' is not a key in the dictionary    
print('d' not in d10)  # True, checks if 'd' is not a key in the dictionary
print('a' in d10.keys())  # True, checks if 'a' is a key in the dictionary using keys() method

################################################################

# Comparing dictionaries
# Two dictionaries are considered equal if they have the same key-value pairs, regardless of the order of the pairs.
d11 = {'a': 1, 'b': 2}
d12 = {'b': 2, 'a': 1}  # Same key-value pairs as d11, but order is different
d13 = {'a': 1, 'b': 3}
print(d11 == d12)  # True, dictionaries are equal
print(d11 == d13)  # False, dictionaries are not equal
print(d11 != d12)  # False, dictionaries are equal
print(d11 != d13)  # True, dictionaries are not equal

################################################################

### Dictionary Comprehensions
# Creating a dictionary using dictionary comprehension
d14 = {x: x**2 for x in range(5)}  # Creates a dictionary of squares
print(d14)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

################################################################

# 1. Word Frequency Counter
def word_count(s):
    freq = {}
    for word in s.split():
        freq[word] = freq.get(word, 0) + 1
    return freq
## .get() handles unseen words safely.
print(word_count("apple banana apple orange banana apple"))
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 2. Invert a Dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}
print(invert_dict({'a': 1, 'b': 2}))  # {1: 'a', 2: 'b'}
## Assumes values are unique.

# 3. Merge Two Dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {**d1, **d2}  # d2 overwrites d1
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# 4. Sort Dictionary by Value
d = {'a': 3, 'b': 1, 'c': 2}
sorted_keys = sorted(d, key=d.get)
print(sorted_keys)  # ['b', 'c', 'a']

# 5. Remove Key with Max Value
d = {'a': 5, 'b': 2, 'c': 9}
max_key = max(d, key=d.get)
del d[max_key]
print(d)  # {'a': 5, 'b': 2}

# 6. Group Elements by First Character
from collections import defaultdict

def group_by_first_char(words):
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    return dict(grouped)

print(group_by_first_char(['apple', 'banana', 'avocado', 'berry']))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'berry']}
# defaultdict(list) avoids key errors.

# 7. Character Frequency (Case Insensitive)
def char_frequency(s):
    freq = {}
    for c in s.lower():
        if c.isalpha():
            freq[c] = freq.get(c, 0) + 1
    return freq

print(char_frequency("Hello World"))  # {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

# 8. Most Frequent Value
from collections import Counter

def most_common_value(d):
    counter = Counter(d.values())
    return counter.most_common(1)[0][0]

print(most_common_value({'Alice': 90, 'Bob': 70, 'Carol': 90, 'David': 70, 'Eva': 90}))  # 90



