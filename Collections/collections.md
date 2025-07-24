# What is `collections` in Python?
`collections` is a built-in module in Python that provides specialized container datatypes. These containers are alternatives to Python’s general-purpose built-in containers like `dict`, `list`, `set` and `tuple`.

## Core Classes in collections Module
| Class                                | Purpose                                              |
| ------------------------------------ | ---------------------------------------------------- |
| `namedtuple()`                       | Tuple with named fields                              |
| `deque`                              | Double-ended queue                                   |
| `Counter`                            | Count hashable objects                               |
| `OrderedDict`                        | Remember the order entries were added (Python < 3.7) |
| `defaultdict`                        | Dictionary with default values                       |
| `ChainMap`                           | Combine multiple dictionaries or mappings            |
| `UserDict`, `UserList`, `UserString` | Wrapper classes to create custom container types     |

## 1️⃣ `namedtuple()`
A tuple with named fields for readability.
```
from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2
```
### Why use it?
- Great for immutability + readability
- Used instead of classes for simple structures.
**NOTE:** Namedtuples are still tuples, so they’re immutable and indexable.

## 2️⃣ `deque` (Double-ended Queue)
```
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4])
```
- Efficient O(1) append and pop operations on both ends. Much faster than list’s `.insert(0, val)`.
- **Common uses**: BFS, LRU cache, sliding window problems

## 3️⃣ Counter
Common for frequency counting. Returns a subclass of dict.
```
from collections import Counter

c = Counter('mississippi')
print(c)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```
Returns top 2 most common occurance.
`c.most_common(2)  # [('i', 4), ('s', 4)]`

**Trick**: You can do arithmetic!
`Counter('aab') - Counter('ab')  # Counter({'a': 1})`

## 4️⃣ defaultdict
Like a `dict`, but returns a default value when key not found.
```
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d['a'])  # 1
print(d['b'])  # 0 (default)
```
✅ Avoids `KeyError` — great for grouping, counting, etc.
**Example for grouping:**
```
d = defaultdict(list)
for k, v in [('a', 1), ('a', 2), ('b', 3)]:
    d[k].append(v)

# {'a': [1, 2], 'b': [3]}
```

## 5️⃣ `OrderedDict` (Python < 3.7)
```
from collections import OrderedDict

d = OrderedDict()
d['one'] = 1
d['two'] = 2
print(d)  # Maintains insertion order
```
- In Python 3.7+, `dict` itself maintains order — so `OrderedDict` is only needed for older versions or methods like `move_to_end()`.

## 6️⃣ `ChainMap`
Combines multiple dicts into one view:
```
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)
print(cm['b'])  # 2 (from dict1, since it comes first)
```
- Good for implementing variable scopes, overriding configurations.

## 7️⃣ UserDict, UserList, UserString
Used to create your own customized versions of built-in types by inheriting:
```
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        if isinstance(value, int):
            super().__setitem__(key, value)
        else:
            raise ValueError("Only integers allowed")

d = MyDict()
d['x'] = 5  # OK
d['y'] = 'hi'  # ❌ Raises ValueError
```

---

## Quiz
1. How is Counter different from a dict?
- Built-in most_common()
- Arithmetic operations
- Automatically counts frequencies

2. Group words by anagram
```
words = ["bat", "tab", "tap", "pat", "apt"]
# Expected:
# [["bat", "tab"], ["tap", "pat", "apt"]]
```

Solution using `defaultdict`:
```
from collections import defaultdict

anagrams = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

print(list(anagrams.values()))
```

3. `deque` Use Case in Sliding Window Maximum
```
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---
# CONCEPTUAL QUESTIONS
**Q 1. When would you use `defaultdict` over a regular `dict`?**
Use `defaultdict` when you want to automatically assign a default value to a key that doesn't exist, avoiding a KeyError.

**Q 2. Difference between `Counter` and `defaultdict(int)`?**
- Both can count.
- `Counter` is built for counting. It has extras like `.most_common()`, `.elements()`.
- `defaultdict(int)` is generic; you build counting logic manually.

**Q 3. What is a `namedtuple` and how is it better than a `tuple`?**
- `namedtuple` gives fields names, so you can access them like object attributes. More readable than tuple[index].

**Q 4. What does deque support that lists don't?**
- Efficient O(1) append/pop from both ends.

**Q 5. What is a ChainMap and when is it useful?**
- Combines multiple dicts into a single view.
- Lookups go left to right (first found wins).
- Useful for variable scoping or layered configs.

---

# CODING CHALLENGES
1. Count frequency of characters in a string using `Counter`.
```
from collections import Counter
s = "banana"
print(Counter(s))
# Output: {'a': 3, 'b': 1, 'n': 2}
```

2. Implement a simple task queue using `deque`.
```
from collections import deque
q = deque()
q.append('task1')
q.appendleft('task0')
print(q.pop())      # task1
print(q.popleft())  # task0
```

3. Group items by first letter using defaultdict.
```
from collections import defaultdict
words = ["apple", "ant", "bat", "ball"]
d = defaultdict(list)
for word in words:
    d[word[0]].append(word)
print(d)  # {'a': ['apple', 'ant'], 'b': ['bat', 'ball']}
```
4. Merge two Counters and get top-2 most common letters
```
from collections import Counter

c1 = Counter("aabbc")
c2 = Counter("bccdd")

merged = c1 + c2
print(merged.most_common(2))
# [('b', 3), ('c', 3)] or similar
```

5. Create namedtuple to represent a Person
```
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
p = Person('Alice', 25)
print(p.name, p.age)  # Alice 25
```

6. Use defaultdict to sum numbers grouped by category
```
from collections import defaultdict
data = [('food', 10), ('clothes', 20), ('food', 5)]
d = defaultdict(int)
for category, amount in data:
    d[category] += amount
print(d)  # {'food': 15, 'clothes': 20}
```

---

# MCQ QUIZ
1. What is the output?
```
from collections import Counter
print(Counter("aabbbc").most_common(1)[0])
```
A) ('a', 1)
B) ('b', 3) ✅
C) ('c', 1)
D) Error

2. Which data structure maintains insertion order in Python 3.6+?
A) dict
B) OrderedDict
C) Both ✅
D) None

3. What’s the time complexity of deque.appendleft()?
A) O(log n)
B) O(1) ✅
C) O(n)
D) O(n log n)

---

# TRICKY EDGE CASES

1. `defaultdict(list).update()` works unexpectedly
```
from collections import defaultdict
d = defaultdict(list)
d.update({'a': 1})
print(d['a'])  # 1, not list! ⚠️ Overwrites the list behavior.
```

2. `Counter` subtraction removes negatives
```
from collections import Counter
a = Counter(a=4, b=2)
b = Counter(a=1, b=3)
a.subtract(b)
print(a)  # Counter({'a': 3, 'b': -1})
```

3. `ChainMap` write affects only first dict
```
from collections import ChainMap
a = {'x': 1}
b = {'x': 2}
cm = ChainMap(a, b)
cm['x'] = 99
print(a)  # {'x': 99}
print(b)  # unchanged
```

## Tips

### ✅ 1. `defaultdict` vs `dict.get(key, default)`

#### **Tip**: Use `defaultdict` when you're repeatedly initializing missing keys with a default value.

#### Without `defaultdict`:

```python
d = {}
for word in ["a", "b", "a"]:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
```

#### With `defaultdict`:

```python
from collections import defaultdict

d = defaultdict(int)
for word in ["a", "b", "a"]:
    d[word] += 1  # no need to check if key exists
```

#### 💡 Interview insight:

If the operation is **write-heavy** and you want to avoid conditional key checks, use `defaultdict`. If it’s mostly **read** or **safe access**, use `dict.get()`:

```python
value = d.get("missing_key", 0)
```

---

### ✅ 2. Manual `Counter` implementation

#### **Tip**: Be ready to implement your own `Counter` if libraries are restricted.

#### With `Counter`:

```python
from collections import Counter
print(Counter("mississippi"))  # {'i': 4, 's': 4, 'p': 2, 'm': 1}
```

#### Manual version:

```python
freq = {}
for ch in "mississippi":
    freq[ch] = freq.get(ch, 0) + 1
```

#### 💡 Interview insight:

You're expected to understand the **underlying logic**. If asked to “avoid libraries,” show this approach.

---

### ✅ 3. `deque` O(1) append/pop operations

#### **Tip**: Use `deque` for efficient insert/remove at both ends. Regular lists are O(n) for `pop(0)`.

```python
from collections import deque

dq = deque()
dq.append(1)       # [1]
dq.appendleft(2)   # [2, 1]
dq.pop()           # [2]
dq.popleft()       # []

# All of these are O(1), unlike list.pop(0)
```

#### 💡 Interview insight:

Use `deque` in:

* **Sliding window problems**
* **BFS algorithms**
* **Queue/stack simulations**

---

### ✅ 4. Use `namedtuple` over class for simple records

#### **Tip**: If all you need is a lightweight, immutable container, use `namedtuple`.

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")
p1 = Point(3, 4)
print(p1.x, p1.y)  # 3 4
```

####  Compared to a class:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

#### 💡 Interview insight:

Mention `namedtuple` when asked about lightweight alternatives to classes or ways to return multiple values with names.

---

### ✅ 5. `ChainMap` is view-based, not merged!

#### **Tip**: Understand that `ChainMap` combines dictionaries **without merging them**.

```python
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
cm = ChainMap(d1, d2)
print(cm['b'])   # 2 — looks in d1 first
print(cm['c'])   # 4

# Changes affect original dicts:
cm['a'] = 100
print(d1)  # {'a': 100, 'b': 2}
```

#### 💡 Interview insight:

ChainMap is great for:

* **Scoped variables (like config layers)**
* Avoiding dict copies

Be careful: it does **not merge** into one dict — it’s just a **linked view**.

---

### Summary Table

| Collection       | Use When                             | Interview Insight                                         |
| ---------------- | ------------------------------------ | --------------------------------------------------------- |
| `defaultdict`    | Repeatedly initializing missing keys | Avoid repetitive `if key not in dict` logic               |
| Manual `Counter` | Can't use libraries                  | Shows logic and implementation understanding              |
| `deque`          | Need fast queue/stack behavior       | O(1) `appendleft()`, `pop()`, `popleft()` — unlike list   |
| `namedtuple`     | Simple read-only records             | More readable and memory efficient than custom classes    |
| `ChainMap`       | Combine scopes, layered configs      | View-based, not merged — live updates to underlying dicts |






