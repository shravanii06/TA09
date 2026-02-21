def normalize(value, max_value):
    return min(value/max_value, 1.0)

def calculate_risk_score(temp, rainfall,aqi,humidity):
    temp_score = normalize(temp, 50) * 0.25
    rainfall_score = normalize(rainfall, 200) * 0.25
    aqi_score = normalize(aqi, 500) * 0.25
    humidity_score = normalize(humidity, 100) * 0.25
    
    total_score = temp_score + rainfall_score + aqi_score + humidity_score
    return total_score * 100 