from flask import Flask, request, jsonify, session
from flask_cors import CORS
import datetime
import logging
import os
import requests

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:4200', 'http://frontend:4200'])
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'super-secret-session-key')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://localhost:5000')
BUS_SERVICE_URL = os.getenv('BUS_SERVICE_URL', 'http://localhost:5001')
RESERVATION_SERVICE_URL = os.getenv('RESERVATION_SERVICE_URL', 'http://localhost:5002')

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    logger.warning(f"Gateway received unhandled request for path: /{path}, method: {request.method}, data: {request.get_json(silent=True)}")
    return jsonify({'message': f'Unhandled route in Gateway: /{path}'}), 404

@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/register", json=request.get_json(), cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax') 
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with auth service: {e}")
        return jsonify({'message': 'Authentication service unavailable'}), 503

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/login", json=request.get_json(), cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with auth service: {e}")
        return jsonify({'message': 'Authentication service unavailable'}), 503



@app.route('/api/auth/logout', methods=['POST'])
def logout():
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/logout", cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with auth service: {e}")
        return jsonify({'message': 'Authentication service unavailable'}), 503

@app.route('/api/auth/@me', methods=['GET'])
def get_current_user_gateway():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/@me", cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with auth service: {e}")
        return jsonify({'message': 'Authentication service unavailable'}), 503

@app.route('/cities', methods=['GET'])
def get_cities():
    cities = [
        'Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata',
        'Hyderabad', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi',
        'Manali', 'Goa', 'Rishikesh', 'Haridwar', 'Shimla',
        'Darjeeling', 'Ooty', 'Mysore', 'Udaipur', 'Jodhpur',
        'Agra', 'Varanasi', 'Amritsar', 'Chandigarh', 'Indore'
    ]
    return jsonify({'cities': cities}), 200

@app.route('/buses/search', methods=['GET'])
def search_buses():
    try:
        params = request.args.to_dict()
        response = requests.get(f"{BUS_SERVICE_URL}/buses/search", params=params, cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with bus service: {e}")
        return jsonify({'message': 'Bus service unavailable'}), 503

@app.route('/buses/<int:bus_id>', methods=['GET'])
def get_bus_details(bus_id):
    try:
        response = requests.get(f"{BUS_SERVICE_URL}/buses/{bus_id}", cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with bus service: {e}")
        return jsonify({'message': 'Bus service unavailable'}), 503

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    try:
        logger.info(f"Gateway received booking request: {request.get_json()}")
        response = requests.post(f"{RESERVATION_SERVICE_URL}/bookings", json=request.get_json(), cookies=request.cookies)
        logger.info(f"Response from reservation service: Status Code {response.status_code}, Body: {response.text}")
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with reservation service: {e}", exc_info=True)
        return jsonify({'message': 'Reservation service unavailable'}), 503

@app.route('/api/bookings/user', methods=['GET'])
def get_user_bookings():
    try:
        response = requests.get(f"{RESERVATION_SERVICE_URL}/bookings/user", cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with reservation service: {e}")
        return jsonify({'message': 'Reservation service unavailable'}), 503

@app.route('/api/bookings/<booking_id>/cancel', methods=['PUT'])
def cancel_booking(booking_id):
    try:
        response = requests.put(f"{RESERVATION_SERVICE_URL}/bookings/{booking_id}/cancel", cookies=request.cookies)
        res = jsonify(response.json())
        for name, value in response.cookies.items():
            res.set_cookie(name, value, httponly=True, secure=False, samesite='Lax')
        return res, response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with reservation service: {e}")
        return jsonify({'message': 'Reservation service unavailable'}), 503

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'api-gateway',
        'timestamp': datetime.datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

@app.route('/health/services', methods=['GET'])
def services_health():
    services = {}
    try:
        auth_health_response = requests.get(f"{AUTH_SERVICE_URL}/health")
        auth_health_response.raise_for_status() 
        auth_health = auth_health_response.json()
        services['auth-service'] = auth_health['status']
    except requests.exceptions.RequestException:
        services['auth-service'] = 'unhealthy'

    try:
        bus_health_response = requests.get(f"{BUS_SERVICE_URL}/health")
        bus_health_response.raise_for_status()
        bus_health = bus_health_response.json()
        services['bus-service'] = bus_health['status']
    except requests.exceptions.RequestException:
        services['bus-service'] = 'unhealthy'

    try:
        reservation_health_response = requests.get(f"{RESERVATION_SERVICE_URL}/health")
        reservation_health_response.raise_for_status()
        reservation_health = reservation_health_response.json()
        services['reservation-service'] = reservation_health['status']
    except requests.exceptions.RequestException:
        services['reservation-service'] = 'unhealthy'

    return jsonify(services), 200

if __name__ == '__main__':
    logger.info("Starting API Gateway...")
    app.run(host='0.0.0.0', port=5000, debug=True)
