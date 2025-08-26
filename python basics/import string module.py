import string

string.ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters     # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits            # '0123456789'
string.hexdigits         # '0123456789abcdefABCDEF'
string.octdigits         # '01234567'
string.punctuation       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace        # ' \t\n\r\x0b\x0c'
string.printable         # digits + letters + punctuation + whitespace


# Random password generator

import random, string

chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(12))
print(password)


# Validate input
s = "1234D"
all(ch in string.digits for ch in s)  # True, All() checks if all iterations of "ch in string.digits" is true .. works like AND
any(ch in string.digits for ch in s) # True, Any () checks if any iterations of "ch in string.digits" is true .. works like OR


# Strip unwanted characters

"hello!!!".strip(string.punctuation)  # 'hello'
