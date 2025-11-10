# smart_agri.py
# Simple demo: Decision Tree model to predict "Irrigation Needed" from sensor data

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1) Load data
df = pd.read_csv('farm_data.csv')
print("Loaded data (first 5 rows):")
print(df.head(), "\n")

# 2) Prepare features and label
X = df[['temperature', 'humidity', 'soil_moisture']]
y = df['irrigation_needed']

# 3) Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 4) Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 5) Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {acc:.2f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 6) Show tree rules (text)
r = export_text(model, feature_names=list(X.columns))
print("\nDecision Rules (simplified):")
print(r)

# 7) Predict for a new sample (simulate real-time sensor)
sample = pd.DataFrame({'temperature':[29], 'humidity':[55], 'soil_moisture':[40]})
pred = model.predict(sample)[0]
print(f"\nSample reading -> temperature=29, humidity=55, soil_moisture=40  => Prediction: Irrigation Needed = {pred}")

# 8) Optional: plot soil_moisture vs humidity colored by irrigation_needed (visual proof)
colors = df['irrigation_needed'].map({'Yes':'red', 'No':'green'})
plt.scatter(df['soil_moisture'], df['humidity'], c=colors)
plt.xlabel('Soil Moisture')
plt.ylabel('Humidity')
plt.title('Soil Moisture vs Humidity (red=Irrigate, green=No)')
plt.grid(True)
plt.show()

