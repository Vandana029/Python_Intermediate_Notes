# Part 1: Conceptual Answers

## 1. What is a dictionary in Python? How is it different from lists and sets?
- A dictionary is a collection of key-value pairs, where keys must be unique and hashable.
- Lists → ordered sequences of values (indexed by position).
- Sets → unordered collection of unique values (no key-value relationship).
- Dict → unordered (Python 3.6+, ordered), key-value mapping.

## 2. Are dictionaries mutable?
- Dictionaries are mutable: you can change, add, or delete key-value pairs after creation.

## 3. What type of objects can be used as dictionary keys?
- Valid keys must be hashable (immutable)

## 4. Are dictionaries ordered in Python? Since which version?
- From Python 3.7, dictionaries preserve insertion order by default.

## 5. What happens if you define a dictionary with duplicate keys?
```
d = {'a': 1, 'a': 2}
print(d['a']) 
```
- Last value wins. Output: 2

## 6. What are `keys()`, `values()`, and `items()` methods? When would you use them?
- `.keys()` returns all keys
- `.values()` returns all values
- `.items()` returns key-value pairs as tuples.

## 7. Why is using dict.get() safer than accessing keys directly?
- `.get()` returns `None` or a default value if the key doesn't exist:
```
d = {'x': 1}
print(d.get('y'))        # None
print(d['y'])            # KeyError
```



