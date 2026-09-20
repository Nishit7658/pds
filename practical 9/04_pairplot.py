# Create a Pairplot to visualize pairwise relationships in the dataset,
# colored by the species/target column.

import matplotlib.pyplot as plt
import seaborn as sns

# Load iris dataset
iris = sns.load_dataset("iris")

print("Iris Species Distribution ::\n", iris["species"].value_counts())

# Generate Pairplot
pair_plot = sns.pairplot(
    iris,
    hue="species",
    palette="Dark2",
    markers=["o", "s", "D"],
    diag_kind="kde"
)

pair_plot.fig.suptitle("Pairwise Relationships in Iris Dataset by Species", y=1.02, fontsize=14)

print("Displaying Pairplot...")
plt.show()
