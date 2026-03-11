def suggest_departure(hour):

    if 7 <= hour <= 9:
        return "Morning rush detected. Leave 20 minutes earlier."

    elif 10 <= hour <= 16:
        return "Moderate traffic expected. Leave 10 minutes earlier."

    elif 17 <= hour <= 20:
        return "Evening peak traffic. Leave 20 minutes earlier."

    else:
        return "Low traffic expected. You can leave normally."