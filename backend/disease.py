def predict_disease(temp, rainfall, aqi, humidity):

    if temp > 30 and rainfall > 100 and aqi > 150 and humidity > 80:
        return "High risk of disease outbreak"

    elif temp > 25 and rainfall > 50 and aqi > 100 and humidity > 60:
        return "Moderate risk of disease outbreak"

    else:
        return "Low risk of disease outbreak"