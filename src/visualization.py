import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("data/cleaned_telco_churn.csv")

# Create output folders
os.makedirs("images/week3", exist_ok=True)
os.makedirs("images/week4", exist_ok=True)

# -----------------------------
# Week 3 Visualizations
# -----------------------------

# Churn Distribution
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.savefig("images/week3/churn_distribution.png")
plt.clf()

# Gender vs Churn
sns.countplot(x='gender', hue='Churn', data=df)
plt.title("Gender vs Churn")
plt.savefig("images/week3/gender_vs_churn.png")
plt.clf()

# Senior Citizen vs Churn
sns.countplot(x='SeniorCitizen', hue='Churn', data=df)
plt.title("Senior Citizen vs Churn")
plt.savefig("images/week3/senior_vs_churn.png")
plt.clf()

# Contract Type vs Churn
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=10)
plt.savefig("images/week3/contract_vs_churn.png")
plt.clf()

print("Week 3 visualizations generated successfully.")

# -----------------------------
# Week 4 Visualization
# -----------------------------

# Correlation Heatmap
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.savefig("images/week4/correlation_heatmap.png")
plt.clf()

print("Week 4 correlation heatmap generated successfully.")