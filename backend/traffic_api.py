import random

def predict_traffic(hour):

    if 7 <= hour <= 9:
        traffic = "High Traffic"

    elif 10 <= hour <= 16:
        traffic = "Medium Traffic"

    elif 17 <= hour <= 20:
        traffic = "High Traffic"

    else:
        traffic = "Low Traffic"

    return traffic


def smart_departure(hour):

    traffic = predict_traffic(hour)

    if traffic == "High Traffic":
        return "Leave 20 minutes earlier"

    elif traffic == "Medium Traffic":
        return "Leave 10 minutes earlier"

    else:
        return "You can leave normally"