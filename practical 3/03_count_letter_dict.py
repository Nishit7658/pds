# Write a program to count the frequency of each character in a given string
# using a Dictionary.

str_input = input("Enter the string you want to count the frequency of character :: ")

char_frequency = {}

for char in str_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("\nCharacter frequencies:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")
