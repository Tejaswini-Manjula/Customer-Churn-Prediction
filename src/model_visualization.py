import pandas as pd
import matplotlib.pyplot as plt

# Load comparison results
results = pd.read_csv("data/model_comparison_results.csv")

plt.figure(figsize=(8,5))
plt.bar(results["Model"], results["Accuracy"])

plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")

plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("images/model_comparison.png")
plt.show()

print("Model comparison chart saved successfully!")