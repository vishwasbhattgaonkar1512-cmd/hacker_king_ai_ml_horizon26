import random 
 
def predict_parking(): 
    availability = random.randint(20,90) 
    return str(availability) + " percent parking available" 
