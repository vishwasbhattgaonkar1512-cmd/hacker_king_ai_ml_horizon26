import sys
import os
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder   # ✅ added

# allow backend to access root folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# load ML models
traffic_model = joblib.load("../models/traffic_model.pkl")
parking_model = joblib.load("../models/parking_model.pkl")

# load datasets
traffic_df = pd.read_csv("../dataset/Traffic.csv")
parking_df = pd.read_csv("../dataset/dataset.csv")

from ai_features.departure_planner import suggest_departure
from ai_features.personalized_learning import update_user, recommend_time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "UrbanFlow AI Backend Running"}

# ---------------- TRAFFIC ----------------

@app.get("/traffic")
def traffic(hour:int):

    data_hour = traffic_df[traffic_df["Time"] == hour]

    if len(data_hour) == 0:
        row = traffic_df.sample(1)
    else:
        row = data_hour.sample(1)

    cars = row["CarCount"].values[0]
    bikes = row["BikeCount"].values[0]
    buses = row["BusCount"].values[0]
    trucks = row["TruckCount"].values[0]

    X = pd.DataFrame(
        [[cars,bikes,buses,trucks]],
        columns=["CarCount","BikeCount","BusCount","TruckCount"]
    )

    prediction = traffic_model.predict(X)[0]

    labels = {
        0:"Low Traffic",
        1:"Normal Traffic",
        2:"High Traffic",
        3:"Heavy Traffic"
    }

    return {
        "traffic_prediction": labels.get(prediction,"Normal Traffic"),
        "cars": int(cars),
        "bikes": int(bikes),
        "buses": int(buses),
        "trucks": int(trucks)
    }

# ---------------- PARKING ----------------

@app.get("/parking")
def parking():

    row = parking_df.sample(1)

    capacity = row["Capacity"].values[0]
    occupancy = row["Occupancy"].values[0]

    X = pd.DataFrame(
        [[capacity,occupancy]],
        columns=["Capacity","Occupancy"]
    )

    available = parking_model.predict(X)[0]

    return {
        "parking_availability": int(available),
        "capacity": int(capacity),
        "occupancy": int(occupancy)
    }

# ---------------- ROUTE ----------------

@app.get("/route")
def route(traffic:str):

    if traffic in ["High Traffic","Heavy Traffic"]:
        return {"route":"Use alternate route to avoid congestion"}

    elif traffic == "Normal Traffic":
        return {"route":"Expect slight delay"}

    else:
        return {"route":"Route clear"}

# ---------------- DEPARTURE ----------------

@app.get("/departure")
def departure(hour:int):
    return {"departure_advice": suggest_departure(hour)}

# ---------------- PERSONALIZED LEARNING ----------------

@app.get("/learn")
def learn(user_id:int,hour:int):
    update_user(user_id,hour)
    return {"message":"User travel recorded"}

@app.get("/recommend")
def recommend(user_id:int):
    return {"recommended_time": recommend_time(user_id)}

# ---------------- MODEL ACCURACY ----------------

@app.get("/model_accuracy")
def model_accuracy():

    # encode traffic labels same as training
    le = LabelEncoder()
    y_t = le.fit_transform(traffic_df["Traffic Situation"])

    X_t = traffic_df[["CarCount","BikeCount","BusCount","TruckCount"]]

    pred_t = traffic_model.predict(X_t)

    traffic_acc = accuracy_score(y_t, pred_t)

    X_p = parking_df[["Capacity","Occupancy"]]
    y_p = parking_df["Capacity"] - parking_df["Occupancy"]

    pred_p = parking_model.predict(X_p)

    parking_mae = mean_absolute_error(y_p, pred_p)

    return {
        "traffic_model_accuracy": f"{round(traffic_acc*100,2)}%",
        "parking_model_error": f"±{round(parking_mae,2)} spaces"
    }

# ---------------- TRAFFIC FORECAST ----------------

@app.get("/traffic_forecast")
def traffic_forecast(hour:int):

    forecast = []

    for i in range(1,4):

        future_hour = (hour + i) % 24

        data_hour = traffic_df[traffic_df["Time"] == future_hour]

        if len(data_hour) == 0:
            row = traffic_df.sample(1)
        else:
            row = data_hour.sample(1)

        cars = row["CarCount"].values[0]
        bikes = row["BikeCount"].values[0]
        buses = row["BusCount"].values[0]
        trucks = row["TruckCount"].values[0]

        X = pd.DataFrame(
            [[cars,bikes,buses,trucks]],
            columns=["CarCount","BikeCount","BusCount","TruckCount"]
        )

        pred = traffic_model.predict(X)[0]

        labels = {
            0:"Low Traffic",
            1:"Normal Traffic",
            2:"High Traffic",
            3:"Heavy Traffic"
        }

        forecast.append({
            "hour":future_hour,
            "traffic":labels[pred]
        })

    return {"forecast":forecast}

# ---------------- AI MODEL EXPLANATION ----------------

@app.get("/explain")
def explain():

    return {
        "model": "RandomForestClassifier",
        "traffic_features": [
            "CarCount",
            "BikeCount",
            "BusCount",
            "TruckCount"
        ],
        "reason": "The model predicts traffic congestion using vehicle counts from the dataset. Higher vehicle counts increase congestion probability."
    }