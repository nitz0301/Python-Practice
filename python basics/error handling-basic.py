a = input("Enter are number between 5 & 9 ")

try:
    a = int(a)
    if 5 > int(a) or a > (9):
     raise ValueError("Number is smaller than 5 or greater than 9")
    else:
       print(f"Number is : {a}")
except:
    if a == 'quit':
       print(f"You have entered: {a}")
    else:
       print("Invalid input")

