import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")

# 1. Survival rates
print("Survival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean())

print("\nSurvival Rate by Class:")
print(df.groupby("Pclass")["Survived"].mean())

# 2. Visualizations

# Graph 1: Survival by Gender
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Survival Rate by Gender")
plt.show()

# Graph 2: Survival by Class
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

# Graph 3: Age Distribution
sns.histplot(df["Age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.show()

# Graph 4: Correlation Heatmap
corr = df[["Survived", "Pclass", "Age", "Fare"]].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 3. Summary
print("\nInsights:")
print("1. Females had a higher survival rate than males.")
print("2. First-class passengers had better survival rates.")
print("3. Most passengers were young to middle-aged adults.")
print("4. Passenger class and fare show a relationship with survival.")