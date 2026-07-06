import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load datasets
X_train = pd.read_csv("data/X_train_scaled.csv")
X_test = pd.read_csv("data/X_test_scaled.csv")
y_train = pd.read_csv("data/y_train.csv")
y_test = pd.read_csv("data/y_test.csv")

# Convert target column to 1D
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load processed data
X_train = pd.read_csv("data/X_train_scaled.csv")
X_test = pd.read_csv("data/X_test_scaled.csv")

y_train = pd.read_csv("data/y_train.csv")
y_test = pd.read_csv("data/y_test.csv")



# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Train model
model.fit(X_train, y_train.values.ravel())


# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model trained successfully")
print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/churn_model.pkl")

print("\n💾 Model saved as models/churn_model.pkl")


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n===== MODEL TRAINED =====")
print("Accuracy:", accuracy)
