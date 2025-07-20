### 1. What are iterables?
# - Iterables are objects in Python that contains a countable number of values that can be looped over or iterated through. 
# - You can iterate through all the values from beginning to end.
# - Examples of iterables include lists, tuples, sets, dictionaries, and strings.
# - An iterable can be traversed using a loop, and it provides a way to access its elements one at a time.

# Technically, an iterable is any object that implements the `__iter__()` method, `__next__()` or the `__getitem__()` method.
# - The `__iter__()` method returns an iterator object, which implements the `__next__()` method to return the next value in the sequence.
# - The `__getitem__()` method allows access to elements by index, which is common in sequences like lists and tuples.


### 2. various iterables in Python
# - **List**: An ordered collection of items that can be changed (mutable).
# - **Tuple**: An ordered collection of items that cannot be changed (immutable).
# - **Set**: An unordered collection of unique items.
# - **Dictionary**: A collection of key-value pairs.
# - **String**: A sequence of characters.
# - **Range**: A sequence of numbers, often used in loops.
# - **Bytes**: A sequence of bytes, often used for binary data.
# - **Bytearray**: A mutable sequence of bytes.
# - **Memoryview**: A memory view object that allows you to access the internal data of an object without copying it.
# - **Generator**: An iterable that generates values on the fly, often used for large datasets or streams of data.
# - **Frozen Set**: An unordered collection of unique items that cannot be changed (immutable).


### 3. range
# - range is a class in Python that represents an **immutable** sequence of numbers.
# - range can contain only int values.
# - range contains sequential numbers starting from a specified start value (default is 0) up to, but not including, a specified end value with an optional step value (default is 1).
# - The range class is memory efficient because it generates numbers on the fly and does not store them in memory.


### 3.1 Creating a range
# - You can create a range using the `range()` function, which takes up to three
# r = range(begin, end, step)  
r = range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 0-inclusive, 10-exclusive, by default step of 1 and beggin is 0.
r = range(2, 10)  # [2, 3, 4, 5, 6, 7, 8, 9] 2-inclusive, 10-exclusive, by default step of 1
r = range(1, 10, 2)  # [1, 3, 5, 7, 9] 1-inclusive, 10-exclusive, step of 2
r1 = range(10, 1, -2)  # [10, 8, 6, 4, 2] 10-inclusive, 1-exclusive, step of -2
print(r) # Output: range(1, 10, 2)


### ✅ 4. Key Interview Points (Conceptual)
# - **Memory Efficiency**: The `range` object does not store all the numbers in memory; it generates them on demand, making it memory efficient for large ranges.
# - **Immutability**: The `range` object is immutable, meaning you cannot change its values after creation.
# - **Lazy Evaluation**: Generates numbers one by one, not a list.
# - **Supports Membership**: `x in range()` is efficient (O(1)).



### 5. Practice with range
print(list(range(5, 2)))
# Output: []  # Empty list because the start is greater than the end with default step of 1

# **Internal Behavior & Efficiency**
# - Python does not generate a list—it creates a range object (an iterable).
r = range(1_000_000_000)
print(type(r))  # <class 'range'>
print(list(r))  # This will not create a list in memory; it will just show the range object.

# Memory Comparison Example
import sys
print(sys.getsizeof(range(1_000_000)))  # ~48 bytes
print(sys.getsizeof(list(range(1_000_000))))  # ~8MB
# - The `range` object is much more memory efficient than a list, especially for large ranges.

## Check Membership (O(1)):
print(100 in range(1, 1000))  # ✅ True
#✅ in operator is fast → no iteration needed.

## Reversing Range:
print(list(reversed(range(5))))
# Output: [4, 3, 2, 1, 0]
# - The `reversed()` function can be used to reverse a range object, returning an iterator that yields the elements in reverse order.

### 6. Tricky Interview Scenarios
# - What happens if you use a float in range?
#   - `range(1.5, 5)` will raise a TypeError.
# - Can you use range with non-integer types?
#   - No, range only accepts integers.
# - What is the output of `list(range(5, 2))`?
#   - Output: [] (Empty list because start > end with default step of 1)

# Edge Case: Step = 0
range(1, 5, 0)
# ❌ Raises ValueError
# ✅ Explanation: Step cannot be zero because range wouldn’t progress.

# Negative Step with Start < Stop
print(list(range(1, 5, -1)))  # []
# ✅ Explanation: Range only works if direction matches step sign.


# | Question Type                        | Example                        |
# | ------------------------------------ | ------------------------------ |
# | Simple Loop                          | `for i in range(5): print(i)`  |
# | Reverse Loop                         | `for i in range(10, 0, -1)`    |
# | Memory Difference                    | `sys.getsizeof(range vs list)` |
# | **Efficient Membership**             | `5 in range(1000)` (O(1))      |
# | Negative Step & Empty Ranges         | `range(5, 1, 1)` → `[]`        |
# | Working with Strings                 | `for idx in range(len(s)):`    |
# | **Range with Slicing (not allowed)** | ❌ `range(10)[::2]` not valid   |


### 8. One-Liner Rapidfire
# Get even numbers from 1 to 10:
print(list(range(2, 11, 2)))

# Reverse count from 5 to 1:
for i in range(5, 0, -1): print(i)

# Get index of elements in a list
# for i in range(len(my_list)):

### 9. Summary
# | Functionality         | Example                     | Notes   |
# | --------------------- | --------------------------- | ------- |
# | Default start         | `range(5)` → 0 to 4         | Step=+1 |
# | Custom start & stop   | `range(2, 6)` → 2 to 5      | Step=+1 |
# | With step             | `range(1, 10, 3)` → 1,4,7   |         |
# | Negative step         | `range(10, 0, -2)` → 10,8,… |         |
# | Empty range traps     | `range(5, 1)` → `[]`        |         |
# | Memory efficient      | `range()` uses O(1) space   |         |
# | Fast membership check | `100 in range(1000)` ✅O(1) |         |


