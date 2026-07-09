year = int(input("Enter the year you want to check whether it's leap or not :: "))
year = year % 2

if year == 0:
    print("It is leap year. ")
else:
    print("It's not the leap year. ")