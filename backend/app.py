from flask import Flask, jsonify, request
from risk_model import calculate_risk_score
from disease import predict_disease 
from funding import recommend_funding

app = Flask(__name__)

@app.route('/')
def home():
    return "Resilience-Net Backend is Running."

@app.route('/risk_score', methods=['GET', 'POST'])
def risk_score():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No JSON data provided'}), 400

            temp = data.get('temperature')
            rainfall = data.get('rainfall')
            aqi = data.get('aqi')
            humidity = data.get('humidity')

        else: 
            temp = request.args.get('temperature')
            rainfall = request.args.get('rainfall')
            aqi = request.args.get('aqi')
            humidity = request.args.get('humidity')

        
        if not all([temp, rainfall, aqi, humidity]):
            return jsonify({'error': 'Missing required parameters'}), 400
        temp = float(temp)
        rainfall = float(rainfall)
        aqi = float(aqi)
        humidity = float(humidity)

        score = calculate_risk_score(temp, rainfall, aqi, humidity)
        disease = predict_disease(temp, rainfall, aqi, humidity)
        funding = recommend_funding(temp, rainfall, aqi, humidity)

        return jsonify({
            'risk_score': score,
            'predicted_disease': disease,
            'funding_recommendation': funding
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)