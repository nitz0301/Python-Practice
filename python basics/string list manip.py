"""
This script demonstrates different ways to iterate over a Python string.
It covers:
- Converting a string to a list of characters
- Joining a list back into a string
- Iterating using direct loops, enumerate, range, zip, and reversed
- Working with sentences: splitting into words and joining words back into a sentence
"""

# ----------------------------
# Working with characters
# ----------------------------

s = "abc"

# Convert string to list of characters
ls = list(s)
print(ls)        # ['a', 'b', 'c']

# Join list of characters back into a string
st = "".join(ls)
print(st)        # "abc"

# Iterate directly over characters
for ch in s:
    print(ch)    # prints 'a', 'b', 'c'

# Iterate using enumerate (gives index + character as tuple)
for ch in enumerate(s):
    print(ch)    # prints (0, 'a'), (1, 'b'), (2, 'c')

# Iterate using range and string indexing
for i in range(len(s)):
    print(s[i])  # prints 'a', 'b', 'c'

# Iterate with enumerate for index and character
for index, ch in enumerate(s):
    print(index, ch)   # prints "0 a", "1 b", "2 c"

# List comprehension to convert string to list of characters
print([ch for ch in list(s)])  # ['a', 'b', 'c']

# Using range with indexing (side-effect: prints index + char)
[print(idx, s[idx]) for idx in range(len(s))]

# Using zip to combine range of indices with list of characters
[print(idx, ch) for idx, ch in zip(range(len(s)), list(s))]

# Same as above but simpler with enumerate on list
[print(idx, ch) for idx, ch in enumerate(list(s))]

# Iterate in reverse order using range
for i in range(len(s) - 1, -1, -1):  
    print(i, s[i])  # prints "2 c", "1 b", "0 a"

# Iterate in reverse order using reversed()
for ch in reversed(s):
    print(ch)   # prints "c", "b", "a"


# ----------------------------
# Working with words in a sentence
# ----------------------------

sentence = "Python makes string manipulation easy"

# Convert sentence string to list of words
word_list = sentence.split()
print(word_list)  
# ['Python', 'makes', 'string', 'manipulation', 'easy']

# Iterate over list of words
for word in word_list:
    print(word)  
# prints each word in new line

# Iterate with index using enumerate
for index, word in enumerate(word_list):
    print(index, word)
# prints "0 Python", "1 makes", "2 string", "3 manipulation", "4 easy"

# Convert list of words back into a sentence
new_sentence = " ".join(word_list)
print(new_sentence)  
# "Python makes string manipulation easy"
