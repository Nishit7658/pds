# Write a program that deliberately divides a number by zero and handles the
# ZeroDivisionError. Also, handle FileNotFoundError when trying to open a
# non-existent file.

try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

filename = input("Enter filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The requested file was not found.")