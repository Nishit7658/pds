right_ang_tri_pyramid = int(input("Enter the number of level you want to print :: "))

for i in range(1, right_ang_tri_pyramid + 1):
    for j in range(1, i + 1):
        print("*",end = " ")
    print()

print()

for i in range(right_ang_tri_pyramid, 0, -1):
    for j in range(1, i):
        print(" ", end = "")
    for k in range(i, right_ang_tri_pyramid + 1):
        print("*", end = " ")
    print()

