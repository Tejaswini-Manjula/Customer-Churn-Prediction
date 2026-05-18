import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("\n===== BEFORE CLEANING =====")
print(df.info())


# Replace blank spaces with NaN
df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)


# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)


print("\n===== MISSING VALUES AFTER FIX =====")
print(df.isnull().sum())


# Remove missing rows
df.dropna(inplace=True)


# Drop customerID column
df.drop("customerID", axis=1, inplace=True)


print("\n===== AFTER CLEANING =====")
print(df.info())

print("\nDataset Shape After Cleaning:")
print(df.shape)


# Save cleaned dataset
df.to_csv(
    "data/cleaned_telco_churn.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")