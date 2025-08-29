from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from functools import wraps
import time

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'super-secret-session-key')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'bus_schedule') 

def get_db_connection():
    retries = 10 
    delay = 5 
    for i in range(retries):
        try:
            conn = mysql.connector.connect(host=DB_HOST,
                                       user=DB_USER,
                                       password=DB_PASSWORD,
                                       database=DB_NAME)
            if conn.is_connected():
                logger.info("Successfully connected to MySQL database")
                return conn
        except Error as e:
            logger.warning(f"Attempt {i+1} to connect to MySQL failed: {e}")
            if i < retries - 1:
                time.sleep(delay)
    logger.error("Failed to connect to MySQL database after multiple retries.")
    raise Exception("Could not connect to database")



@app.route('/buses/search', methods=['GET'])
def search_buses():
    try:
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        date = request.args.get('date')

        logger.info(f"Searching buses: {origin} -> {destination} on {date}")

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT b.id, bo.name AS operator, b.bus_type AS type, b.departure_time AS departure, "
                "b.arrival_time AS arrival, b.price, b.available_seats AS available, b.total_seats, "
                "b.amenities, b.rating, b.image_url AS image "
                "FROM buses b "
                "JOIN bus_routes br ON b.route_id = br.id "
                "JOIN bus_operators bo ON b.operator_id = bo.id "
                "WHERE br.origin = %s AND br.destination = %s",
                (origin, destination)
            )
            buses = cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

        return jsonify({"buses": buses, "count": len(buses)}), 200

    except Exception as e:
        logger.error(f"Bus search error: {str(e)}")
        return jsonify({'error': 'Search failed'}), 500

@app.route('/buses/<int:bus_id>', methods=['GET'])
def get_bus_details(bus_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT b.id, bo.name AS operator, b.bus_type AS type, b.departure_time AS departure, "
                "b.arrival_time AS arrival, b.price, b.available_seats AS available, b.total_seats, "
                "b.amenities, b.rating, b.image_url AS image "
                "FROM buses b "
                "JOIN bus_operators bo ON b.operator_id = bo.id "
                "WHERE b.id = %s",
                (bus_id,)
            )
            bus = cursor.fetchone()
        finally:
            cursor.close()
            connection.close()

            if bus:
                return jsonify(bus), 200
            else:
                return jsonify({'error': 'Bus not found'}), 404

    except Exception as e:
        logger.error(f"Bus details error: {str(e)}")
        return jsonify({'error': 'Failed to get bus details'}), 500

@app.route('/routes', methods=['GET'])
def get_routes():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT origin, destination, distance, duration FROM bus_routes")
            routes = cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
        return jsonify({"routes": routes}), 200
    except Exception as e:
        logger.error(f"Get routes error: {str(e)}")
        return jsonify({'error': 'Failed to get routes'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    try:
        conn = get_db_connection()
        conn.close()
        db_status = 'healthy'
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        db_status = 'unhealthy'

    return jsonify({
        'status': 'healthy',
        'service': 'bus-service',
        'database_status': db_status,
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    logger.info("Starting Bus Service...")
    app.run(host='0.0.0.0', port=5001, debug=True)