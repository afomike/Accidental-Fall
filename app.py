from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import requests

app = Flask(__name__)

# Load the prediction model
model = pickle.load(open('models/baggedsvc.pkl', 'rb'))

def send_sms(message, mobile):
    username = 'temidayoafote@gmail.com'
    password = 'afo@@1234'
    sender = 'fall'
    api_url = 'https://portal.nigeriabulksms.com/api/'
    data = {'username': username, 'password': password, 'sender': sender, 'message': message, 'mobiles': mobile}
    response = requests.get(api_url, params=data)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    name = data['name']
    phone = data['phone']
    inputs = [
        float(data['distance']),
        float(data['pressure']),
        float(data['heart_rate']),
        float(data['sugar_level']),
        float(data['spo2_levels']),
        float(data['accelerometer'])
    ]
    print(inputs)
    prediction = model.predict([inputs])
    print(prediction)
    # prediction = model.predict([inputs])[0]

    if prediction == 0:
        message = f"{name} is fine, no fall detected."
    elif prediction == 1:
        message = f"{name} is likely to fall."
        send_sms(message, phone)
    else:
        message = f"{name} has fallen and needs urgent help."
        send_sms(message, phone)

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
