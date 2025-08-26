import random
import string

def randstr(length: int = 3) -> str:
    """
    Generate a random string of lowercase letters.

    Args:
        length (int, optional): Length of the string. Defaults to 3.

    Returns:
        str: Randomly generated lowercase string.
    """
    # Use string.ascii_lowercase instead of rebuilding the char list each time
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

# Take user input
sen = input("Enter a sentence to encode: ")

# Split sentence into individual words
words = sen.split()
enc_sen = []  # List to hold encoded words

# Encoding logic
for word in words:
    if len(word) < 4:
        # For short words (<4 letters), reverse them
        enc_sen.append(word[::-1])
    else:
        # For longer words:
        # - Move the first character to the end
        # - Add random 3-letter prefix and suffix
        new_word = word[1:] + word[0]
        enc_sen.append(randstr() + new_word + randstr())

print("Encoded sentence")
new_sen = " ".join(enc_sen)
print(new_sen)

# Split encoded sentence into words for decoding
words = new_sen.split()
dec_sen = []  # List to hold decoded words

# Decoding logic
for word in words:
    if len(word) < 4:
        # Short words were only reversed, so reverse back
        dec_sen.append(word[::-1])
    else:
        # For longer words:
        # - Strip the random 3-letter prefix and suffix
        # - Move last character to the front (to restore original)
        new_word = word[3:-3]
        dec_sen.append(new_word[-1] + new_word[0:-1])

print("Decoded sentence")
new_sen = " ".join(dec_sen)
print(new_sen)
