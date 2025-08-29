from flask import Flask, request, jsonify, session
from flask_cors import CORS
import logging
import os
from datetime import datetime
import uuid
import mysql.connector
from mysql.connector import Error
from functools import wraps
from dotenv import load_dotenv
import time

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'super-secret-session-key') 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_HOST = os.getenv('DB_HOST', 'mysql-db')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'bus_reservation')


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

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'message': 'Unauthorized: Login required'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        logger.info(f"Incoming booking data: {data}")
        bus_id = data.get('bus_id')
        origin = data.get('origin')
        destination = data.get('destination')
        travel_date = data.get('travel_date')
        seat_numbers = data.get('seat_numbers', [])
        total_amount = data.get('total_amount')

        session_email = session.get('email', 'user@example.com')
        passenger_email = data.get('passenger_email', session_email)
        passenger_name = data.get('passenger_name', session_email.split('@')[0].capitalize())
        passenger_phone = data.get('passenger_phone', '')

        if not all([bus_id, origin, destination, travel_date, seat_numbers, total_amount]):
            logger.error("Missing required booking fields in incoming data.")
            return jsonify({'error': 'Missing required booking fields'}), 400

        try:
            parsed_travel_date = datetime.strptime(travel_date, '%Y-%m-%dT%H:%M:%S.%fZ').date() # Assuming ISO format from frontend
        except ValueError:
            try:
                parsed_travel_date = datetime.strptime(travel_date, '%Y-%m-%d').date()
            except ValueError:
                logger.error(f"Invalid travel_date format: {travel_date}")
                return jsonify({'error': 'Invalid travel_date format. Expected YYYY-MM-DD or ISO string.'}), 400

        logger.info(f"Parsed travel date: {parsed_travel_date}")

        booking_id = f"BUS{datetime.now().strftime('%Y%m%d%H%M%S')}{str(uuid.uuid4())[:4].upper()}"

        logger.info(f"Attempting to create booking with ID: {booking_id} for user: {session['user_id']}")
        
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            insert_sql = "INSERT INTO reservations (booking_id, user_id, bus_id, passenger_name, passenger_email, passenger_phone, origin, destination, travel_date, seat_numbers, total_amount, status, payment_status) " \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert_params = (booking_id, session['user_id'], bus_id, passenger_name, passenger_email, passenger_phone, origin, destination, parsed_travel_date, ",".join(seat_numbers), total_amount, 'confirmed', 'completed')
            
            logger.info(f"Executing INSERT SQL: {insert_sql}")
            logger.info(f"With parameters: {insert_params}")
            
            cursor.execute(
                insert_sql,
                insert_params
            )
            connection.commit()

            logger.info(f"Decrementing available seats for bus_id: {bus_id}, seats: {len(seat_numbers)}")
            update_bus_sql = "UPDATE bus_schedule.buses SET available_seats = available_seats - %s WHERE id = %s"
            update_bus_params = (len(seat_numbers), bus_id)
            logger.info(f"Executing UPDATE BUS SQL: {update_bus_sql}")
            logger.info(f"With parameters: {update_bus_params}")
            cursor.execute(
                update_bus_sql,
                update_bus_params
            )
            connection.commit()
        finally:
            cursor.close()
            connection.close()

        logger.info(f"Booking created: {booking_id} for user {session['user_id']}")

        return jsonify({
            'booking_id': booking_id,
            'status': 'confirmed',
            'message': 'Booking created successfully',
        }), 201

    except Exception as e:
        logger.error(f"Booking creation error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Booking failed'}), 500

@app.route('/bookings/<booking_id>', methods=['GET'])
def get_booking(booking_id):
    try:
        logger.info(f"Fetching booking details for booking ID: {booking_id} for user: {session['user_id']}")
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            select_sql = "SELECT * FROM reservations WHERE booking_id = %s AND user_id = %s"
            select_params = (booking_id, session['user_id'])
            logger.info(f"Executing SELECT SQL: {select_sql}")
            logger.info(f"With parameters: {select_params}")
            cursor.execute(select_sql, select_params)
            booking = cursor.fetchone()

            if booking:
                booking['seat_numbers'] = booking['seat_numbers'].split(',')
                logger.info(f"Found booking: {booking_id}")
                return jsonify(booking), 200
            else:
                logger.warning(f"Booking not found or unauthorized for booking ID: {booking_id}")
                return jsonify({'error': 'Booking not found or unauthorized'}), 404
        finally:
            cursor.close()
            connection.close()

    except Exception as e:
        logger.error(f"Get booking error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Failed to get booking'}), 500

@app.route('/bookings/user', methods=['GET'])
@login_required 
def get_user_bookings():
    try:
        user_id = session.get('user_id')
        if not user_id:
            logger.warning("User not logged in for get_user_bookings.")
            return jsonify({'error': 'User not authenticated'}), 401

        logger.info(f"Fetching bookings for user ID: {user_id}")
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            select_sql = """
                SELECT 
                    r.booking_id, r.user_id, r.bus_id, r.passenger_name, r.passenger_email, r.passenger_phone, 
                    br.origin AS origin, br.destination AS destination, r.travel_date, r.seat_numbers, r.total_amount, r.status, r.payment_status,
                    b.bus_type, b.departure_time, b.arrival_time, b.price AS bus_price, b.image_url AS bus_image
                FROM reservations r
                JOIN bus_schedule.buses b ON r.bus_id = b.id
                JOIN bus_schedule.bus_routes br ON b.route_id = br.id
                WHERE r.user_id = %s
                ORDER BY r.travel_date DESC, b.departure_time DESC
            """
            cursor.execute(select_sql, (user_id,))
            bookings = cursor.fetchall()

            for booking in bookings:
                if booking.get('seat_numbers'):
                    booking['seat_numbers'] = booking['seat_numbers'].split(',')

            logger.info(f"Found {len(bookings)} bookings for user {user_id}.")
            return jsonify({'bookings': bookings, 'count': len(bookings)}), 200
        finally:
            cursor.close()
            connection.close()

    except Exception as e:
        logger.error(f"Get user bookings error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Failed to retrieve user bookings'}), 500


@app.route('/bookings/<booking_id>/cancel', methods=['PUT'])
@login_required 
def cancel_booking(booking_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'Unauthorized: Login required'}), 401

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT user_id, status, seat_numbers, bus_id FROM reservations WHERE booking_id = %s", (booking_id,))
            booking_data = cursor.fetchone()

            if not booking_data:
                return jsonify({'error': 'Booking not found'}), 404

            if booking_data['user_id'] != user_id:
                return jsonify({'error': 'Unauthorized: You can only cancel your own bookings'}), 403

            if booking_data['status'] == 'cancelled':
                return jsonify({'message': 'Booking already cancelled'}), 200

            cursor.execute(
                "UPDATE reservations SET status = 'cancelled', cancellation_time = %s WHERE booking_id = %s",
                (datetime.now().isoformat(), booking_id)
            )

            seat_count = len(booking_data['seat_numbers'].split(','))
            bus_id = booking_data['bus_id']
            cursor.execute(
                "UPDATE bus_schedule.buses SET available_seats = available_seats + %s WHERE id = %s",
                (seat_count, bus_id)
            )
            connection.commit()
        finally:
            cursor.close()
            connection.close()

        logger.info(f"Booking {booking_id} cancelled by user {user_id}")
        return jsonify({'message': 'Booking cancelled successfully'}), 200

    except Exception as e:
        logger.error(f"Cancel booking error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Failed to cancel booking'}), 500

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
        'service': 'reservation-service',
        'database_status': db_status,
        'timestamp': datetime.now().isoformat(),
    }), 200

if __name__ == '__main__':
    logger.info("Starting Reservation Service...")
    app.run(host='0.0.0.0', port=5002, debug=True)