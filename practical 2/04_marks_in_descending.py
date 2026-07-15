students = {
    "Nick": 100,
    "Alice": 95,
    "Bob": 87,
    "Charlie": 42,
    "David": 68,
    "Eva": 91,
    "Frank": 35,
    "Grace": 78,
    "Henry": 49,
    "Isabella": 98,
    "Jack": 56,
    "Karen": 72,
    "Liam": 83,
    "Mia": 64,
    "Nathan": 27,
    "Olivia": 94,
    "Peter": 51,
    "Quinn": 39,
    "Ryan": 76,
    "Sophia": 89,
    "Thomas": 44,
    "Uma": 67,
    "Victor": 31,
    "William": 93,
    "Xavier": 18,
    "Yvonne": 85,
    "Zachary": 59,
    "Aarav": 73,
    "Vivaan": 47,
    "Aditya": 81,
    "Diya": 96,
    "Ananya": 88,
    "Ishaan": 53,
    "Krishna": 62,
    "Meera": 79,
    "Rohan": 25,
    "Priya": 70,
    "Sneha": 92,
    "Rahul": 38,
    "Kiran": 57,
    "Neha": 84
}

value = list(students.items())

for i in range(len(value)):
    for j in range(i + 1, len(value)):
        if value[i][1] < value[j][1]:
            # Swap
            value[i], value[j] = value[j], value[i]

desc = dict(value)
print(desc.values())

# for i in students.values():
#     for j in students.values():
#         if i < j:
#             i, j = j, i
#         value = [i]
# for i in students.values():
#     print(value)

