# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zqt8H4dqygMkMjdNUdpvgXxA1zj2XSxm
"""

# Install necessary libraries
!pip install seaborn matplotlib pandas

# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading a sample dataset (Iris dataset in this case)
from sklearn.datasets import load_iris

# Load dataset into a pandas DataFrame
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
df.head()

# Basic statistical summary
print(df.describe())

# Visualizing pairwise relationships between features
sns.pairplot(df, hue='species')
plt.show()

# Heatmap to visualize correlation between features
corr = df.iloc[:, :-1].corr()  # Excluding the target column ('species')
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Visualizing the distribution of each feature
for feature in iris.feature_names:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[feature], kde=True, bins=20, color='blue')
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

# Boxplot to visualize the distribution of features based on species
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='species', y='sepal length (cm)', palette='Set2')
plt.title("Boxplot of Sepal Length by Species")
plt.show()