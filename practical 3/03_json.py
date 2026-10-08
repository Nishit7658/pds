# Create a JSON file containing book details (Title, Author, Price). Read and
# parse the JSON file to display the details.

import json
import os

data = ""

if "book.json" == 0:
    with open("book.json", "r") as f:
        data = json.load(f)

for book in data:
    print("Title :: ", book["Title"])
    print("Author :: ", book["Author"])
    print("Price :: ", book["Price"])
    print()
