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

# 4. Reverse Words in a Sentence
def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))

print(reverse_words("I love Python"))  # Output: Python love I
# Explanation: split() → list of words → reverse → join

# 5. Remove Spaces Without replace()
def remove_spaces(s):
    return ''.join(char for char in s if char != ' ')

print(remove_spaces(" Hello   World "))  # Output: HelloWorld


# 6. Most Frequent Character
from collections import Counter

def most_frequent_char(s):
    s = s.replace(" ", "").lower()
    count = Counter(s)
    return count.most_common(1)[0][0]

print(most_frequent_char("aabbccccc"))  # Output: c


# 7. Longest Word Extractor
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python is fantastic"))  # Output: fantastic

# 8. String Compression
def compress_string(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

print(compress_string("aaabbc"))  # Output: a3b2c1
print(compress_string("abc"))     # Output: abc (original returned)




