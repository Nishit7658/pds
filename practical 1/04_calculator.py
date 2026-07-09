first_num = int(input("Enter the first number :: "))
operator = str(input("Entre the operator from (*, /, +, -) :: "))
second_num = int(input("Enter the second number :: "))

if operator == "*" or operator == "/" or operator == "+" or operator == "-":
    if operator == "*":
        print(first_num * second_num)
    elif operator == "/":
        print(first_num / second_num)
    elif operator == "+":
        print(first_num + second_num)
    elif operator == "-":
        print(first_num - second_num)
    else:
        print("Some thing went wrong.")
else:
    print("Select proper operator.")

