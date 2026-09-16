# Write a Python program (using the statistics module) to calculate Mean,
# Median, Mode, Variance, and Standard Deviation for a given list of student
# marks.

import statistics

marks = list(map(float, input("Enter the marks separated by space :: ").split()))

print("Mean :: ", statistics.mean(marks))
print("Median :: ", statistics.median(marks))
print("Mode :: ", statistics.mode(marks))
print("Variance :: ", statistics.variance(marks))
print("Standard deviation :: ", statistics.stdev(marks))