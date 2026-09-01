import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("data/cleaned_telco_churn.csv")

# Target Encoding
df["Churn"] = df["Churn"].map({"No":0,"Yes":1})

X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------
# Feature Types
# --------------------------

categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

numerical_features = X.select_dtypes(exclude=["object"]).columns.tolist()

# --------------------------
# Preprocessing
# --------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)

# --------------------------
# Pipeline
# --------------------------

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# --------------------------
# Train
# --------------------------

pipeline.fit(X_train, y_train)

# --------------------------
# Predict
# --------------------------

pred = pipeline.predict(X_test)

print("\n===== MODEL TRAINED =====")

print(
    f"Accuracy: {accuracy_score(y_test,pred):.4f}"
)

print()

print(
    classification_report(
        y_test,
        pred
    )
)

# --------------------------
# Save Pipeline
# --------------------------

joblib.dump(
    pipeline,
    "models/churn_pipeline.pkl"
)

print("\nPipeline saved successfully.")