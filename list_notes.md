# List
    - A list is a class. It is a **mutable**, **growable**, ordered collection of items (i.e **iterable sequence**).
    - Lists can contain elements of different types (heterogeneous data).
    - Lists elements are indexed.

# How to create a list object?
- Use square brackets: `my_list = [1, 2, 3]`
- Use the `list()` constructor: `my_list = list((1, 2, 3))`
- Use list comprehension: `my_list = [x for x in range(5)]`
- Use the `*` operator to unpack: `my_list = [*range(5)]`
- Use the `list` function on an iterable: `my_list = list('hello')`  # Output: ['h', 'e', 'l', 'l', 'o']
- Use the `list` function on a string: `my_list = list('hello')`  # Output: ['h', 'e', 'l', 'l', 'o']
- Use the `list` function on a range: `my_list = list(range(5))`  # Output: [0, 1, 2, 3, 4]
- Use the `list` function on a set: `my_list = list({1, 2, 3})`  # Output: [1, 2, 3] (order may vary)
- Use the `list` function on a dictionary: `my_list = list({'a': 1, 'b': 2})`  # Output: ['a', 'b'] (keys only)
- Use the `list` function on a tuple: `my_list = list((1, 2, 3))`  # Output: [1, 2, 3]
- Use the `list` function on a generator: `my_list = list(x for x in range(5))`  # Output: [0, 1, 2, 3, 4]
- Use the `list` function on a file object:
  ```python
  with open('file.txt') as f:
      my_list = list(f)
  ```             
- Use the `list` function on a numpy array: `import numpy as np; my_list = list(np.array([1, 2, 3]))`  # Output: [1, 2, 3]
- Use the `list` function on a pandas Series: `import pandas as pd; my_list = list(pd.Series([1, 2, 3]))`  # Output: [1, 2, 3]
- Use the `list` function on a range with a step: `my_list = list(range(0, 10, 2))`  # Output: [0, 2, 4, 6, 8]
- Use the `list` function on a string with a step: `my_list = list('hello'[::2])`  # Output: ['h', 'l', 'o']
- Use the `list` function on a set with a step: `my_list = list({1, 2, 3, 4, 5})[::2]`  # Output: [1, 3, 5] (order may vary)
- Use the `list` function on a dictionary with a step: `my_list = list({'a': 1, 'b': 2, 'c': 3})[::2]`  # Output: ['a', 'c'] (keys only)
- Use the `list` function on a tuple with a step: `my_list = list((1, 2, 3, 4, 5))[::2]`  # Output: [1, 3, 5]
- Use the `list` function on a generator with a step: `my_list = list(x for x in range(10))[::2]`  # Output: [0, 2, 4, 6, 8]
- Use the `list` function on a file object with a step:
  ```python
  with open('file.txt') as f:
      my_list = list(f)[::2]
  ```
# How to delete an element from a list by value
`del my_list[0]`  # Deletes the first element

# How to add elements to a list
 - Use `append()`, `extend()`, or `insert()` methods.
 - `append()` adds a single element to the end.
 - `extend()` adds multiple elements to the end.
 - `insert(index, value)` adds an element at a specific index. (if index > last index,  it will be added at the end.)