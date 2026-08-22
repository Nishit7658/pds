# Write a program to read a text file, count the number of words, lines, and
# characters, and write the output to a new file.

import os

if not os.path.exists("example.txt"):
    with open ("example.txt", "w") as f:
        f.write("Hello World.\n")
        f.write("The Earth Is Flat.\n")
        f.write("No The Earth Is Donut.\n")

character_count = 0
word_count = 0
count = 0

with open ("example.txt", "r") as f:
    for line in f:
        count += 1

        for word in line.split():
            word_count += 1

        character_count += len(line)

print("Total number of line in the file is :: ",count)
print("The total number of word in the file is :: ",word_count)
print("Total number of character in the file is :: ",character_count)
