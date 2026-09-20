# Create a Bar chart comparing the marks of 5 students in Math vs. Science.

import numpy as np
import matplotlib.pyplot as plt

students = ["Nick", "Rock", "Nicky", "Rockety", "Alice"]
math_marks = [85, 78, 92, 65, 88]
science_marks = [80, 85, 89, 72, 94]

x = np.arange(len(students))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, math_marks, width, label="Math", color="royalblue", edgecolor="black")
plt.bar(x + width/2, science_marks, width, label="Science", color="coral", edgecolor="black")

plt.xlabel("Students", fontsize=12)
plt.ylabel("Marks", fontsize=12)
plt.title("Marks Comparison: Math vs Science", fontsize=14)
plt.xticks(x, students)
plt.ylim(0, 100)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

print("Displaying Bar Chart...")
plt.show()
