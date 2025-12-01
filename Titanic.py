# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 18:34:34 2025

@author: hp
"""

# -------------------------------
# Titanic Data Cleaning & EDA (No Seaborn)
# -------------------------------

# 1️⃣ Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2️⃣ Load dataset
# Using seaborn dataset via URL, no seaborn import needed
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)
print("Dataset preview:")
print(titanic.head())
print("\nDataset info:")
print(titanic.info())

# 3️⃣ Data Cleaning

# Check for missing values
print("\nMissing values before cleaning:\n", titanic.isnull().sum())

# Fill missing numeric values with median
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)

# Fill missing categorical values with mode
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)

# Drop unnecessary columns
titanic.drop(['Cabin', 'Ticket', 'Name'], axis=1, inplace=True)

print("\nMissing values after cleaning:\n", titanic.isnull().sum())

# Save cleaned dataset
titanic.to_csv('titanic_cleaned.csv', index=False)
print("\n✅ Cleaned dataset saved as 'titanic_cleaned.csv'")

# 4️⃣ Exploratory Data Analysis (EDA)

# 4.1 Summary Statistics
print("\nSummary Statistics:\n", titanic.describe(include='all'))

# 4.2 Survival count
plt.figure(figsize=(6,4))
titanic['Survived'].value_counts().plot(kind='bar', color=['red','green'])
plt.title('Survival Count')
plt.xlabel('Survived (0=No, 1=Yes)')
plt.ylabel('Count')
plt.show()

# 4.3 Survival by Gender
plt.figure(figsize=(6,4))
titanic.groupby(['Sex','Survived']).size().unstack().plot(kind='bar', stacked=False, color=['red','green'])
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

print("\nSurvival rate by gender:\n", titanic.groupby('Sex')['Survived'].mean())

# 4.4 Survival by Passenger Class
plt.figure(figsize=(6,4))
titanic.groupby(['Pclass','Survived']).size().unstack().plot(kind='bar', stacked=False, color=['red','green'])
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class (1=Upper, 3=Lower)')
plt.ylabel('Count')
plt.show()

print("\nSurvival rate by class:\n", titanic.groupby('Pclass')['Survived'].mean())

# 4.5 Age distribution by survival
plt.figure(figsize=(8,5))
plt.hist(titanic[titanic['Survived']==1]['Age'], bins=20, alpha=0.7, color='green', label='Survived')
plt.hist(titanic[titanic['Survived']==0]['Age'], bins=20, alpha=0.7, color='red', label='Did Not Survive')
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()

# 4.6 Correlation heatmap (numeric variables)
plt.figure(figsize=(8,6))
corr = titanic.corr()
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Correlation Matrix')
plt.show()
print("\nCorrelation values:\n", corr)

# 4.7 Survival by Embarkation Port
plt.figure(figsize=(6,4))
titanic.groupby(['Embarked','Survived']).size().unstack().plot(kind='bar', stacked=False, color=['red','green'])
plt.title('Survival by Embarkation Port')
plt.xlabel('Port of Embarkation')
plt.ylabel('Count')
plt.show()

print("\nSurvival rate by embarkation port:\n", titanic.groupby('Embarked')['Survived'].mean())

# 5️⃣ Key Observations
print("\n--- Key Insights ---")
print("💡 Women had higher survival rates than men.")
print("💡 1st class passengers survived more than 3rd class.")
print("💡 Younger passengers had slightly higher survival rates.")
print("💡 Higher fare often correlates with higher survival.")
print("💡 Passengers from port 'C' had higher survival rates.")
