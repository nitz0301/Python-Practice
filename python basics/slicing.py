""" 
Key Takeaways

    - String/List/Tuple → full slicing support.

    - Set/Dict → not directly sliceable; convert to ordered form first.

    - Step slicing ([::-1]) is powerful for reversing sequences.

    - Use slicing for: subsetting, reversing, stepping, deleting, pagination, or partitioning. """


# 1. String Slicing
#       Strings are immutable sequences of characters.

s = "PythonSlicing"

# Basic slicing: s[start:end]
print(s[0:6])   # "Python" → characters from index 0 up to (not including) 6

# Omitting start: defaults to 0
print(s[:6])    # "Python"

# Omitting end: goes till the end
print(s[6:])    # "Slicing"

# Negative indices: count from the end
print(s[-7:])   # "Slicing"

# Full copy
print(s[:])     # "PythonSlicing"

# Step parameter: s[start:end:step]
print(s[::2])   # "PtoSlcn" → every 2nd character
print(s[::-1])  # "gnicilSnothyP" → reverse string

# Use case: extracting file extension
filename = "report.pdf"
print(filename[-3:])  # "pdf"


# 2. List Slicing
#       Lists are mutable ordered sequences.

nums = [10, 20, 30, 40, 50, 60]

# Slice sublist
print(nums[1:4])   # [20, 30, 40]

# Omit start or end
print(nums[:3])    # [10, 20, 30]
print(nums[3:])    # [40, 50, 60]

# Negative indexing
print(nums[-3:])   # [40, 50, 60]

# Step slicing
print(nums[::2])   # [10, 30, 50] → every 2nd element
print(nums[::-1])  # [60, 50, 40, 30, 20, 10] → reversed list

# Modify list in-place with slicing
nums[1:3] = [200, 300]
print(nums)        # [10, 200, 300, 40, 50, 60]

# Delete elements with slice
del nums[::2]      
print(nums)        # [200, 40, 60]


# 3. Tuple Slicing
#       Tuples are immutable, but slicing works the same as lists.

t = (1, 2, 3, 4, 5, 6)

# Extract a portion
print(t[1:4])     # (2, 3, 4)

# Negative slicing
print(t[-3:])     # (4, 5, 6)

# Reverse tuple
print(t[::-1])    # (6, 5, 4, 3, 2, 1)

# Use case: separate head and tail
head, tail = t[:2], t[2:]
print(head)  # (1, 2)
print(tail)  # (3, 4, 5, 6)


# 4. Set “Slicing”
#    Sets are unordered collections. They cannot be sliced directly because indexing requires order.
#    Workaround: convert to a list or tuple first.

s = {100, 200, 300, 400, 500}

# Convert to list to slice
lst = list(s)
print(lst[:3])   # e.g. [100, 200, 300] → order is arbitrary

# Example use case: extract first N elements
subset = set(list(s)[:2])
print(subset)    # e.g. {100, 200}

# Proper way for sets: use set operations instead of slicing
a = {1, 2, 3, 4, 5}
b = {4, 5, 6}
print(a - b)     # {1, 2, 3} → difference
print(a & b)     # {4, 5}   → intersection

#  5. Dictionary “Slicing”
#        Dictionaries preserve insertion order (Python 3.7+).
#        No direct slicing, but can slice after converting .keys(), .values(), or .items() to a list.

d = {"a": 1, "b": 2, "c": 3, "d": 4}

# Slice dictionary keys
keys = list(d.keys())
print(keys[:2])   # ['a', 'b']

# Slice dictionary items
items = list(d.items())
print(items[1:3]) # [('b', 2), ('c', 3)]

# Build a new dict from slice
sliced_dict = dict(items[1:3])
print(sliced_dict)  # {'b': 2, 'c': 3}

# Use case: pagination
records = {"id1": "Alice", "id2": "Bob", "id3": "Charlie", "id4": "David"}
page1 = dict(list(records.items())[:2])
print(page1)   # {'id1': 'Alice', 'id2': 'Bob'}
