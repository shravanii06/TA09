def recommend_funding(temp, rainfall, aqi, humidity):

    if temp > 35 or aqi > 200:
        return "High emergency funding required"

    elif rainfall > 150 or humidity > 85:
        return "Moderate disaster relief funding recommended"

    else:
        return "Minimal funding required"