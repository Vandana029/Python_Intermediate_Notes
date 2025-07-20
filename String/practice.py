# 1. String Immutability
s = "cat"
s[0] = "b"  # Error: 'str' object does not support item assignment

# Fix: Strings can't be modified, create new strings
s = "bat"

# 2. Common Coding Scenarios

## 2.1 Reverse a String
s[::-1]

## 2.2 Check if a String is a Palindrome
s == s[::-1]

## 2.3 Anagram Check
sorted(s1) == sorted(s2)

## 2.4 Count Vowels
sum(1 for char in s if char.lower() in 'aeiou')

## 2.5 Frequency Count
from collections import Counter
Counter(s)

# 3. String Formatting
## f-strings (Python 3.6+):
name = "Alice"
f"Hello, {name}!"

## format() method:
"Hello, {}".format(name)

# Performance 
## Inefficient
res = ""
for ch in ["a", "b", "c"]:
    res += ch   # O(n^2)

## Efficient
res = "".join(["a", "b", "c"])  # O(n)
