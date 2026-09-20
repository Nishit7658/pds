# Generate a Scatter plot to show the relationship between study hours and
# exam scores.

import numpy as np
import matplotlib.pyplot as plt

study_hours = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5])
exam_scores = np.array([45, 50, 52, 58, 63, 67, 70, 74, 78, 82, 85, 88, 91, 95, 98])

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores, color="darkviolet", s=60, edgecolors="black", label="Student Score")

# Linear trend line
m, b = np.polyfit(study_hours, exam_scores, 1)
plt.plot(study_hours, m * study_hours + b, color="crimson", linestyle="--", linewidth=1.8, label=f"Trendline (y = {m:.2f}x + {b:.2f})")

plt.title("Relationship Between Study Hours and Exam Scores", fontsize=14)
plt.xlabel("Study Hours per Day", fontsize=12)
plt.ylabel("Exam Score", fontsize=12)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

print("Displaying Scatter Plot...")
plt.show()
