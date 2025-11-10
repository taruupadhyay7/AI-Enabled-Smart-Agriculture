📘 Project Overview

Agriculture is one of the most vital sectors in India, yet traditional methods often lead to water wastage and low productivity.
This project introduces an AI-enabled Smart Agriculture System that helps farmers decide when irrigation is needed using simple environmental data such as temperature, humidity, and soil moisture.

The model uses a Decision Tree Classifier (Machine Learning) to predict whether irrigation is required or not, enabling data-driven and water-efficient farming.

⚙️ Technologies Used

 Python 3.13

 Pandas, NumPy, Matplotlib

 Scikit-Learn (DecisionTreeClassifier)

 CSV Dataset (Simulated sensor readings)

VS Code

🌱 How It Works

Sensor data (Temperature, Humidity, Soil Moisture) is collected or simulated.

The AI model is trained on this data to learn irrigation patterns.

Based on new readings, the model predicts whether irrigation is needed (Yes or No).

Output is displayed directly in the console.

Dataset Example-
| Temperature | Humidity | Soil Moisture | Irrigation Needed |
| ----------- | -------- | ------------- | ----------------- |
| 30          | 60       | 30            | Yes               |
| 25          | 80       | 70            | No                |
| 28          | 65       | 45            | Yes               |
| 35          | 40       | 25            | Yes               |
| 20          | 90       | 85            | No                |


Model Output Example-
Test Accuracy: 1.00

Decision Rules:
|--- humidity <= 66.50 → Irrigation Needed = Yes
|--- humidity >  66.50 → Irrigation Needed = No

Sample Reading → temperature=29, humidity=55, soil_moisture=40  
Prediction: Irrigation Needed = Yes


Code Structure-
AI-Enabled-Smart-Agriculture/
│
├── smart_agri.py        
├── farm_data.csv      
├── .gitignore           
└── README.md

Result & Impact-
Achieved 100% accuracy on simulated data.

Helps farmers make smart irrigation decisions.

Reduces water waste and improves crop productivity.

Can be extended to real IoT sensors and cloud-based dashboards.

Future Scope-
Integrate IoT sensors for real-time data collection.

Deploy on mobile/web apps for farmers.

Use advanced ML models like Random Forest or XGBoost for better generalization.
