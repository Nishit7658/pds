# Use the csv module to create a CSV file containing student details (Name,
# Roll No, CGPA). Read the CSV and display only students with CGPA > 7.5.

import os
import csv

student_detail = [
    ["Name", "Roll NO.", "CGPA"],
    ["Nick", 21, 9.69],
    ["Rock", 22, 9.01],
    ["Nicky", 23, 8.0],
    ["Rockety", 24, 9.3]
]

if not os.path.exists("student.csv"):
    with open("student.csv", "w", newline="") as f:
        write_csv = csv.writer(f)
        write_csv.writerows(student_detail)

with open("student.csv", "r") as f:
    reade_csv = csv.reader(f)
    for cpi in reade_csv:
        if cpi[0] != "Name" and float(cpi[2]) > 7.5:
            print(cpi[2])
