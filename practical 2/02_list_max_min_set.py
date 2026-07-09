list_num = int(input("Enter the number of item you want to store in the list :: "))
input_list = []

for i in range(0, list_num):
    item = input()
    input_list.append(item)

print("Your list is :: ", input_list)

max = input_list[0]
min = input_list[-1]

for i in range(0, list_num):
    if input_list[i] > max:
        max = input_list[i]
    if min > input_list[i]:
        min = input_list[i]

print(f"Maximun number form the list is :: {max}\nMinimum number from the list is :: {min}")

print(set(input_list))
