from fastapi import FastAPI 
from ai_features.departure_planner import suggest_departure 
from ai_features.personalized_learning import update_user, recommend_time 
 
app = FastAPI() 
 
@app.get("/departure") 
def departure(hour:int): 
    return {"departure_advice": suggest_departure(hour)} 
 
@app.get("/learn") 
def learn(user_id:int, hour:int): 
    update_user(user_id, hour) 
    return {"message":"User travel recorded"} 
 
@app.get("/recommend") 
def recommend(user_id:int): 
    return {"recommended_time": recommend_time(user_id)} 
