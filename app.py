import os

# Telecom Customer Churn Prediction System

# Model path
model_path = "models/churn_model.pkl"

# Verify serialized model availability
if os.path.exists(model_path):
    print("Serialized churn model detected successfully.")
else:
    print("Model file missing.")

# Prediction workflow
def prediction_pipeline():
    print("Customer Input")
    print("→ Feature Processing")
    print("→ Model Prediction")
    print("→ Churn Output")

prediction_pipeline()