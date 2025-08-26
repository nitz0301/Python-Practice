import random 

def randstr() -> str:
    return "".join([((random.choice([chr(x) for x in range(ord('a'), ord('z'))]))) for x in range(3)])

sen = input("Enter a sentence to encode: ")
words = sen.split()
enc_sen = []

for word in words:
    new_word = ""
    if len(word) < 4:
        enc_sen.append(word[::-1])
    else: 
        new_word = word[1:] + word[0]
        enc_sen.append(randstr() + new_word + randstr())

print("Encoded sentence")
new_sen = " ".join(enc_sen)
print(new_sen)

words = new_sen.split()
dec_sen = []

for word in words:
    new_word = ""
    if len(word) < 4:
        dec_sen.append(word[::-1])
    else: 
        new_word = word[3:-3]
        dec_sen.append(new_word[-1] + new_word[0:-1])

print("Decoded sentence")
new_sen = " ".join(dec_sen)
print(new_sen)