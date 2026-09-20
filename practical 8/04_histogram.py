# Create a Histogram to show the distribution of ages in a given dataset.

import matplotlib.pyplot as plt

ages = [18, 19, 21, 22, 22, 23, 23, 24, 25, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 38, 40, 42, 45, 48, 50, 52, 55, 60]

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=8, color="teal", edgecolor="black", alpha=0.75)

plt.title("Age Distribution of Participants", fontsize=14)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

print("Displaying Histogram...")
plt.show()
