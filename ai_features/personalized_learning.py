user_history = {}

def update_user(user_id,hour):

    user_id=int(user_id)
    hour=int(hour)

    if user_id not in user_history:
        user_history[user_id]=[]

    user_history[user_id].append(hour)


def recommend_time(user_id):

    user_id=int(user_id)

    if user_id not in user_history:
        return "No travel history available yet."

    history=user_history[user_id]

    avg_hour=sum(history)//len(history)

    return f"Based on your travel history, best departure time is around {avg_hour}:00"