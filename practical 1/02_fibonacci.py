fibo = int(input("Enter the integer till where you want to print the fibonacci series :: "))
first_num = 0
second_num = 1

print(first_num)
print(second_num)

for i in range(1,fibo):
    sum = first_num + second_num
    print(sum)

    first_num = second_num
    second_num = sum
