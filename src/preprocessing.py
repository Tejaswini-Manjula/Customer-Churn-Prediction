import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# ==========================
# LOAD DATASET
# ==========================
df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)
df = df.astype(int, errors='ignore')


print("\n===== BEFORE CLEANING =====")
print(df.info())


# ==========================
# CLEANING
# ==========================

# Fix TotalCharges
df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove missing values
df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

# Remove customerID
df.drop(
    "customerID",
    axis=1,
    inplace=True
)


print("\n===== AFTER CLEANING =====")
print(df.info())


# ==========================
# ENCODING
# ==========================

# Binary column mapping
binary_columns = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
    "Churn"
]

binary_mapping = {
    "Yes": 1,
    "No": 0,
    "Male": 1,
    "Female": 0
}

for column in binary_columns:
    df[column] = df[column].map(binary_mapping)


# One-hot encoding
multi_category_columns = [
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaymentMethod"
]

df = pd.get_dummies(
    df,
    columns=multi_category_columns,
    drop_first=True
)


print("\n===== AFTER ENCODING =====")
print(df.head())

print("\nDataset Shape After Encoding:")
print(df.shape)

# Convert boolean columns to integers
bool_columns = df.select_dtypes(include='bool').columns
df[bool_columns] = df[bool_columns].astype(int)

print("\n===== DATA TYPES AFTER ENCODING =====")
print(df.dtypes)

# ==========================
# SPLIT FEATURES & TARGET
# ==========================
X = df.drop("Churn", axis=1)
y = df["Churn"]


# ==========================
# TRAIN TEST SPLIT
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\n===== TRAIN TEST SHAPES =====")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)


# ==========================
# FEATURE SCALING
# ==========================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


print("\n===== SCALING COMPLETE =====")
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape :", X_test_scaled.shape)


# ==========================
# SAVE FILES
# ==========================
pd.DataFrame(X_train_scaled).to_csv(
    "data/X_train_scaled.csv",
    index=False
)

pd.DataFrame(X_test_scaled).to_csv(
    "data/X_test_scaled.csv",
    index=False
)

y_train.to_csv(
    "data/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/y_test.csv",
    index=False
)

print("\nProcessed files saved successfully.")