# Beyond Syllabus Practical 1: Mini-Project - Exploratory Data Analysis (EDA)
# Tasks:
# 1. Use groupby to find survival rates by gender and passenger class (or
#    equivalent dataset metrics).
# 2. Create at least 4 different visualizations using Matplotlib/Seaborn to
#    represent findings (e.g., Bar chart for survival by class, Histogram for age
#    distribution, Heatmap for feature correlation).
# 3. Write a brief text summary within the Jupyter Notebook/Python script
#    explaining what each graph represents and the business insights derived
#    from it.

import os
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure dataset exists
csv_path = "titanic.csv" if os.path.exists("titanic.csv") else os.path.join("bs practical 1", "titanic.csv")
if not os.path.exists(csv_path):
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    urllib.request.urlretrieve(url, csv_path)

df = pd.read_csv(csv_path)

# Data Preprocessing
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Sex_Code"] = df["Sex"].map({"male": 0, "female": 1})

print("Dataset loaded successfully! Total records :: ", len(df))

# ---------------------------------------------------------
# Task 1: Groupby Survival Rates
# ---------------------------------------------------------
print("\n--- 1. Survival Rate by Gender ---")
survival_gender = df.groupby("Sex")["Survived"].mean() * 100
print(survival_gender.apply(lambda x: f"{x:.2f}%"))

print("\n--- 2. Survival Rate by Passenger Class ---")
survival_pclass = df.groupby("Pclass")["Survived"].mean() * 100
print(survival_pclass.apply(lambda x: f"{x:.2f}%"))

print("\n--- 3. Survival Rate by Gender and Passenger Class ---")
survival_gender_class = df.groupby(["Pclass", "Sex"])["Survived"].mean().unstack() * 100
print(survival_gender_class.round(2))


# ---------------------------------------------------------
# Task 2 & 3: Four Distinct Visualizations & Business Insights
# ---------------------------------------------------------
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Graph 1: Bar Chart - Survival Rate by Passenger Class and Gender
sns.barplot(
    ax=axes[0, 0],
    data=df,
    x="Pclass",
    y="Survived",
    hue="Sex",
    palette="muted",
    errorbar=None
)
axes[0, 0].set_title("Graph 1: Survival Rate by Passenger Class & Gender", fontsize=12, fontweight="bold")
axes[0, 0].set_xlabel("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", fontsize=10)
axes[0, 0].set_ylabel("Survival Probability", fontsize=10)
axes[0, 0].set_ylim(0, 1.05)

# Graph 2: Histogram / KDE - Age Distribution by Survival Status
sns.histplot(
    ax=axes[0, 1],
    data=df,
    x="Age",
    hue="Survived",
    kde=True,
    palette={0: "red", 1: "green"},
    bins=25,
    alpha=0.5
)
axes[0, 1].set_title("Graph 2: Age Distribution by Survival Status", fontsize=12, fontweight="bold")
axes[0, 1].set_xlabel("Age (Years)", fontsize=10)
axes[0, 1].set_ylabel("Passenger Count", fontsize=10)
axes[0, 1].legend(title="Status", labels=["Survived", "Did Not Survive"])

# Graph 3: Correlation Heatmap
numeric_cols = ["Survived", "Pclass", "Sex_Code", "Age", "SibSp", "Parch", "Fare"]
corr = df[numeric_cols].corr()
sns.heatmap(
    ax=axes[1, 0],
    data=corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"label": "Correlation"}
)
axes[1, 0].set_title("Graph 3: Feature Correlation Heatmap", fontsize=12, fontweight="bold")

# Graph 4: Boxplot - Fare Distribution across Passenger Classes
sns.boxplot(
    ax=axes[1, 1],
    data=df,
    x="Pclass",
    y="Fare",
    hue="Survived",
    palette="Set2",
    showfliers=False
)
axes[1, 1].set_title("Graph 4: Fare Distribution by Class and Survival (Excl. Outliers)", fontsize=12, fontweight="bold")
axes[1, 1].set_xlabel("Passenger Class", fontsize=10)
axes[1, 1].set_ylabel("Fare ($)", fontsize=10)
axes[1, 1].legend(title="Survived", labels=["No", "Yes"])

plt.tight_layout()
print("\nDisplaying 4 Visualizations...")
plt.show()

# ---------------------------------------------------------
# Task 3: Text Summary and Business Insights
# ---------------------------------------------------------
insights = """
================================================================================
                    BUSINESS INSIGHTS & STORYTELLING SUMMARY
================================================================================
1. Graph 1 (Survival by Class & Gender):
   - Insight: Gender and socio-economic class were the strongest determinants of survival.
   - Females in 1st Class had an extraordinary ~96.8% survival rate, whereas 3rd class
     males suffered the lowest survival rate (~13.5%).
   - Protocol "women and children first" was strictly applied, alongside class privilege.

2. Graph 2 (Age Distribution vs Survival):
   - Insight: Young infants and children (under 10 years) had higher survival ratios,
     confirming evacuation prioritization.
   - Adults aged 20-35 formed the largest group of casualties.

3. Graph 3 (Correlation Heatmap):
   - Insight: 'Sex_Code' (positive correlation of +0.54 with survival) and 'Pclass'
     (negative correlation of -0.34 with survival) are the strongest linear predictors.
   - Fare also correlates positively (+0.26) because higher class passengers paid more.

4. Graph 4 (Fare Distribution & Survival):
   - Insight: Even within the same ticket class, passengers who paid higher fares
     tended to have higher chances of survival, likely due to better cabin proximity
     to the lifeboats on upper decks.
================================================================================
"""
print(insights)
