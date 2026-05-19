from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Set the Backend URL from an environment variable (defaults to localhost for local development)
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5000')

@app.route('/')
def index():
    # List of cities required by the assignment
    cities = [
        {"key": "new_york", "name": "New York"},
        {"key": "sydney", "name": "Sydney"},
        {"key": "cape_town", "name": "Cape Town"},
        {"key": "bangkok", "name": "Bangkok"}
    ]
    return render_template('index.html', cities=cities)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_key = request.form.get('city')
    if not city_key:
        return jsonify({"error": "No city selected"}), 400
    
    # Call the Backend microservice
    try:
        response = requests.get(f"{BACKEND_URL}/weather/{city_key}")
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
