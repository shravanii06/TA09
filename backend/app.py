from flask import Flask, jsonify, request
from risk_model import calculate_risk_score
from disease import predict_disease 
from funding import recommend_funding

app = Flask(__name__)

@app.route('/')
def home():
    return "Resilience-Net Backend is Running."

@app.route('/risk_score', methods=['POST'])
def risk_score():
    try:
        data = request.get_json()
        
        if not all(k in data for k in ('temperature', 'rainfall', 'aqi', 'humidity')):
            return jsonify({'error': 'Missing required parameters'}), 400
        temp = data['temperature']
        rainfall = data['rainfall']
        aqi = data['aqi']
        humidity = data['humidity']
        
        score = calculate_risk_score(temp, rainfall, aqi, humidity)
        disease = predict_disease(temp, rainfall, aqi, humidity)
        funding = recommend_funding(temp, rainfall, aqi, humidity)
        return jsonify({'risk_score': score
                        , 'predicted_disease': disease
                        , 'funding_recommendation': funding})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)