# Create a Boxplot to visualize the distribution of total bills across different
# days of the week.

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
tips = sns.load_dataset("tips")

# Set theme
sns.set_theme(style="whitegrid")

plt.figure(figsize=(9, 5))
sns.boxplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=tips,
    palette="Set2"
)

plt.title("Distribution of Total Bills Across Days of the Week", fontsize=14)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill ($)", fontsize=12)
plt.legend(title="Gender", loc="upper left")
plt.tight_layout()

print("Displaying Boxplot...")
plt.show()
