# 🚦 UrbanFlow AI
### AI-Powered Urban Traffic & Parking Intelligence System

UrbanFlow AI is an intelligent urban mobility system that predicts **traffic congestion**, **parking availability**, and **optimal departure times** using **Machine Learning models** and real-time visualization.

The platform helps commuters plan travel efficiently and supports smart city traffic optimization.

---

# 🌍 Project Overview

UrbanFlow AI combines **Machine Learning**, **data analytics**, and **interactive visualization** to provide:

• Traffic congestion prediction  
• Parking availability forecasting  
• Smart departure planning  
• Route recommendation  
• Personalized travel learning  
• 3-hour traffic forecasting  
• AI model explanation panel  
• Interactive Mumbai traffic map  

---

# 🧠 Machine Learning Models

| Model | Purpose |
|------|--------|
Random Forest Classifier | Traffic congestion prediction |
Random Forest Regressor | Parking availability prediction |

### Why Random Forest?

• High accuracy on tabular datasets  
• Handles nonlinear relationships  
• Robust against overfitting  
• Good feature importance interpretation

---

# 📊 Model Evaluation Metrics

### Traffic Prediction Model

Metric Used: **Classification Accuracy**

# 🚦 UrbanFlow AI
### AI-Powered Urban Traffic & Parking Intelligence System

UrbanFlow AI is an intelligent urban mobility system that predicts **traffic congestion**, **parking availability**, and **optimal departure times** using **Machine Learning models** and real-time visualization.

The platform helps commuters plan travel efficiently and supports smart city traffic optimization.

---

# 🌍 Project Overview

UrbanFlow AI combines **Machine Learning**, **data analytics**, and **interactive visualization** to provide:

• Traffic congestion prediction  
• Parking availability forecasting  
• Smart departure planning  
• Route recommendation  
• Personalized travel learning  
• 3-hour traffic forecasting  
• AI model explanation panel  
• Interactive Mumbai traffic map  

---

# 🧠 Machine Learning Models

| Model | Purpose |
|------|--------|
Random Forest Classifier | Traffic congestion prediction |
Random Forest Regressor | Parking availability prediction |

### Why Random Forest?

• High accuracy on tabular datasets  
• Handles nonlinear relationships  
• Robust against overfitting  
• Good feature importance interpretation

---

# 📊 Model Evaluation Metrics

### Traffic Prediction Model

Metric Used: **Classification Accuracy**

Traffic Model Accuracy: 95.46%


Evaluation Method:
- Train/Test Split (80/20)
- Accuracy Score from Scikit-Learn

---

### Parking Prediction Model

Metric Used: **Mean Absolute Error (MAE)**

Parking Model Error: ±0.54 spaces


Evaluation Method:
- Regression Error Analysis
- Mean Absolute Error

---

# 🏗 System Architecture

User Interface (Frontend)
│
│ API Requests
▼
FastAPI Backend Server
│
│
├── Traffic Prediction Model
├── Parking Prediction Model
├── Forecast Engine
└── Route Recommendation Engine
│
▼
ML Models (.pkl)
│
▼
Datasets (Traffic + Parking)


---

# 🔄 Data Pipeline

The ML pipeline consists of the following steps:

### 1️⃣ Data Collection
Datasets used:

Traffic Dataset

dataset/Traffic.csv


Parking Dataset

dataset/dataset.csv


---

### 2️⃣ Data Cleaning

• Removed null values  
• Standardized columns  
• Extracted required features  

Example features:

Traffic Dataset

CarCount
BikeCount
BusCount
TruckCount
Traffic Situation

Parking Dataset

Capacity
Occupancy
Available Spaces


---

### 3️⃣ Feature Engineering

Traffic Features

CarCount
BikeCount
BusCount
TruckCount


Parking Features


Capacity
Occupancy


Derived Feature:

Available = Capacity − Occupancy


---

### 4️⃣ Model Training

Training script:

train_models.py

Process:

Dataset → Train/Test Split → Model Training → Model Export


Models saved as:

models/traffic_model.pkl
models/parking_model.pkl


---

# 💻 Tech Stack

### Frontend

| Technology | Usage |
|-----------|------|
HTML5 | UI Structure |
Bulma CSS | Responsive layout |
Custom CSS | Animations & styling |
Chart.js | Data visualization |
Leaflet.js | Interactive map |

---

### Backend

| Technology | Usage |
|-----------|------|
Python | Core programming |
FastAPI | Backend API |
Uvicorn | ASGI server |
Pandas | Data processing |

---

### Machine Learning

| Library | Usage |
|-------|------|
Scikit-Learn | ML models |
Joblib | Model serialization |

---

# 📂 Project Structure

UrbanFlow-AI
│
├── backend
│ ├── main.py
│ └── requirements.txt
│
├── ai_features
│ ├── departure_planner.py
│ └── personalized_learning.py
│
├── dataset
│ ├── Traffic.csv
│ └── dataset.csv
│
├── models
│ ├── traffic_model.pkl
│ └── parking_model.pkl
│
├── frontend
│ ├── index.html
│ └── index.css
│
├── train_models.py
├── evaluate_models.py
│
├── README.md
└── .gitignore

the video and project strcture link :
https://drive.google.com/drive/folders/1J_9NP0S0I4XsWUkQMTx5EDyJE4lit8Xi?usp=sharing
