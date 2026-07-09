print("Welcome to the pizza delivery all !! ")
size = (input("What size of pizza you want S, M, L :: ")).lower()
pepperoni = (input("You want pepperoni on your pizza Y or N :: ")).lower()
extra_cheese = (input("Do you want extra cheese Y or N :: ")).lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Not the proper size.")

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is : {bill}")
