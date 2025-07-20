# 1. Mutable Trap
```
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
```
**Explanation**: Lists are mutable, `a` and `b` point to same object.

# 2. Copying Lists (Correct Way)
```
b = a.copy()           # OR
b = a[:]               # OR
import copy; b = copy.deepcopy(a)  # For nested lists
```

# 3. List Slicing
```
lst = [10, 20, 30, 40, 50]
print(lst[1:4])  # [20, 30, 40]
print(lst[::-1])  # Reverse list
```

# 4. Common Interview Questions
| Problem Type        | Example                                                    |
| ------------------- | ---------------------------------------------------------- |
| Reverse List        | `lst[::-1]`                                                |
| Remove Duplicates   | `list(set(lst))` (order changes), or use `dict.fromkeys()` |
| Flatten Nested List | `[item for sub in nested for item in sub]`                 |
| Find Max/Min        | `max(lst)`, `min(lst)`                                     |
| Sort/Sorted         | `lst.sort()` (in-place), `sorted(lst)` (new list)          |

# 5. Must-Know 
## Q 1: What's the output?
```
lst = [[]] * 3
lst[0].append(1)
print(lst)
```
**Answer**: `[[1], [1], [1]]`
**Why?** → Same list reference copied 3 times.
**Fix:**:
`lst = [[] for _ in range(3)]  # Separate lists`

## Q 2: Mutable Default Argument
```
def f(x, l=[]):
    l.append(x)
    return l
print(f(1))
print(f(2))
```
**Answer**: `[1], [1, 2]`
**Why?** → Default argument l=[] is mutable → reused across calls
In Python, default arguments are evaluated only once—at the time the function is defined, not each time it is called.
**How to Check This Behavior**:
```
print(id(f(1)))
print(id(f(2)))
```
They will give the same ID (same memory address).

**Fix**:
```
def f(x, l=None):
    if l is None:
        l = []
```
A new list is created each time because of `None` in argument and initialize l = [] inside the function.
**Conclusion**: In Python, mutable default arguments like lists or dictionaries retain state across function calls. To avoid bugs, Use None and create a new object inside the function.

# 6. Big O Complexity
| Operation              | Complexity     |
| ---------------------- | -------------- |
| Index access `lst[i]`  | O(1)           |
| Append `lst.append(x)` | Amortized O(1) |
| Insert/Delete (middle) | O(n)           |
| Search `x in lst`      | O(n)           |
| Sorting `lst.sort()`   | O(n log n)     |


