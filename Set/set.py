### How to create a set
s1 = set([1, 2, 3]) # Using the set constructor
s2 = {1, 2, 3}  # Using curly braces
s3 = set()  # Empty set

# This will raise a TypeError because int is not iterable, argument must be iterable or it should be empty.
# s4 = set(10)
# Example of creating a set with iterables
s4 = set((1, 2, 3)) # Using a tuple
s5 = set("hello")  # Set of characters in the string
s6 = set(range(5))  # Set of numbers from 0 to 4
s7 = set([1, 2, 3, 4, 5])  # Using a list

#########################################################
# WAP to remove duplicates from input
l1 = list(set([int(x) for x in input('Enter numbers separated by comma: ').split(',')]))
print(l1)  # This will print the list without duplicates

#########################################################
### How to access elements in a set
s8 = {1, 2, 3, 4, 5}
for elem in s8:
    print(elem)
# NOTE: We cannot access elements by index in a set, as sets are unordered collections.

#########################################################

### Example of using set methods
s9 = {1, 2, 3}
s9.add(4)  # Adds 4 to the set
s9.remove(2)  # Removes 2 from the set
s9.discard(5)  # Does nothing, as 5 is not in the set
s9.pop()  # Removes and returns an arbitrary element (could be any element)
s9.clear()  # Removes all elements from the set

#########################################################
### Set Comprehension
s10 = {x for x in range(10) if x % 2 == 0}  # Creates a set of even numbers from 0 to 9

#############################  Coding Questions  ############################
# Remove Duplicates from a List
lst = [1, 2, 2, 3]
unique = list(set(lst))  # [1, 2, 3]

# Intersection of two lists
def intersection(a, b):
    return list(set(a) & set(b))

# Check if Two Lists Have Any Common Elements
def has_common(a, b):
    return bool(set(a) & set(b))

has_common([1, 2], [3, 2])  # True

# Unique vowels in a string
def unique_vowels(s):
    vowels = set('aeiou')
    return set(s.lower()) & vowels

# Count Unique Words in a Sentence
sentence = "Python is great and Python is fun"
unique = set(sentence.lower().split())
print(len(unique))  # 6

# Find Missing Numbers from a Range
nums = [1, 2, 4, 5]
missing = set(range(1, 6)) - set(nums)
print(missing)  # {3}

# Symmetric Difference Example
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)  # {1, 4}




