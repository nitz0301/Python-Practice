""" 
Summary

    Case handling: capitalize, title, upper, lower, casefold, swapcase

    Search/validate: find, rfind, index, rindex, startswith, endswith

    Classification: isalpha, isdigit, isnumeric, isdecimal, isalnum, islower, isupper, isspace, istitle, isidentifier, isprintable

    Modify/trim: replace, removeprefix, removesuffix, strip, lstrip, rstrip

    Format/alignment: center, ljust, rjust, zfill, format

    Split/join: split, rsplit, splitlines, join

    Encoding/translation: encode, translate, maketrans

    Misc: expandtabs, count """

# 1. Case Conversion

s = "hello world"
print(s.capitalize())   # "Hello world" → First letter capital
print(s.title())        # "Hello World" → Title case
print(s.upper())        # "HELLO WORLD"
print(s.lower())        # "hello world"
print(s.casefold())     # "hello world" → Aggressive lower (for Unicode, e.g. "ß" → "ss")
print(s.swapcase())     # "HELLO WORLD" → Swap upper/lower

# 2. Search and Check

s = "Python is powerful"
print(s.startswith("Python"))   # True
print(s.endswith("ful"))        # True
print(s.find("is"))             # 7 (first index)
print(s.rfind("o"))             # 15 (last index)
print(s.index("power"))         # 10 (like find but raises ValueError if not found)
print(s.rindex("o"))            # 15

# 3. Character Classification (Boolean checks)

""" Rule:

- Use isdecimal() for strict base-10 digit validation.
- Use isdigit() when superscripts or other digit forms should pass.
- For parsing numbers with signs or separators, prefer int()/float() and handle errors. 
- If you need all numeric characters (fractions, Roman numerals, CJK numerals), use str.isnumeric()."""

print("123".isdigit())      # True
print("Ⅷ".isnumeric())      # True (handles fractions, Roman numerals, CJK numerals too)
print("123".isdecimal())    # True (strict decimal only)


print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("hello".islower())    # True
print("HELLO".isupper())    # True
print("   ".isspace())      # True
print("Title Case".istitle()) # True
print("var".isidentifier()) # True (valid Python identifier)
print("π".isprintable())    # True (not control chars)

# 4. Modification and Replacement

s = "apple banana apple"
print(s.replace("apple", "orange"))     # "orange banana orange"
print(s.removeprefix("apple "))         # "banana apple" (Python 3.9+)
print(s.removesuffix(" apple"))         # "apple banana"

# 5. Trimming (whitespace or custom chars)

s = "   hello world   "
print(s.strip())       # "hello world"
print(s.lstrip())      # "hello world   "
print(s.rstrip())      # "   hello world"
print("xxhelloxx".strip("x"))   # "hello"

# 6. Alignment and Padding

s = "42"
print(s.center(6, "*"))   # "**42**"
print(s.ljust(6, "-"))    # "42----"
print(s.rjust(6, "-"))    # "----42"
print(s.zfill(6))         # "000042"

# 7. Formatting

# Format() method on strings
print("Hello {}, you are {} years old".format("Nishith", 42)) # Positional substitution
print("Coordinates: {0}, {1}".format(10, 20)) # Indexed substitution 
print("Name: {name}, Age: {age}".format(name="Nishith", age=42)) # Named substitution
# Alignment and width
print("{:<30} is left aligned".format("Hello"))    # left aligned → 'Hello                          is left aligned'
print("{:>10}".format("right"))   # right aligned → '     right'
print("left {:^10} right".format("center"))  # centered     → '  center  '
# format numbers
print("Binary: {0:b}, Hex: {0:x}, Octal: {0:o}".format(42)) # This uses format specifiers to convert the number e.g. 42 into different bases.
#here 0 is the first arugment which is 42, b is binary, x is Hexadecimal, o is Octal.

print("Pi ≈ {0:.3f}".format(3.14159)) # specify places after decimal

# 8. Splitting and Joining

s = "a,b,c"
print(s.split(","))       # ['a','b','c']
print(s.rsplit(",", 1))   # ['a,b','c'] (from right side)
print(s.splitlines())     # split by \n, \r
print(" ".join(['Python','3'])) # "Python 3"

# 9. Encoding and Translation

print("hello".encode("utf-8"))   # b'hello'

tbl = str.maketrans({"a":"@", "e":"3"})  # this example of str.maketrans() and str.translate()
print("apple".translate(tbl))    # "@ppl3"

# 10. Expansion and Tabs
""" 
- \t is a control character — rendering depends on the environment (console, editor, etc.).
- .expandtabs(n) makes it deterministic by converting \t into actual spaces, aligned to n-column tab stops.
- So .expandtabs() is for consistent, portable spacing regardless of display settings. """

print("Line1\tLine2".expandtabs(12))   # Replace \t with spaces
print("Line1\tLine2")  

# 11. Counting

s = "banana"
print(s.count("an"))  # 2