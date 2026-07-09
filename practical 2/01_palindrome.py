string = str(input("Enter the string you want to check whether it is palindeome or not :: "))
reverse_string = string[::-1]

if reverse_string == string:
    print("String is palindrome.")
else:
    print("String is not palindrome.")
