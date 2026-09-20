# Plot a Heatmap of the correlation matrix of the iris dataset. Annotate
# the heatmap with correlation values.

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
iris = sns.load_dataset("iris")

# Calculate correlation matrix for numeric columns
correlation_matrix = iris.corr(numeric_only=True)
print("Iris Correlation Matrix ::\n", correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"label": "Correlation Coefficient"}
)

plt.title("Correlation Heatmap of Iris Dataset Features", fontsize=14)
plt.tight_layout()

print("Displaying Heatmap...")
plt.show()
