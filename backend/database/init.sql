CREATE DATABASE IF NOT EXISTS bus_schedule;
CREATE DATABASE IF NOT EXISTS bus_reservation;

USE bus_schedule;

CREATE TABLE IF NOT EXISTS bus_routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    distance VARCHAR(50),
    duration VARCHAR(50),
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bus_operators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    rating DECIMAL(3,2) DEFAULT 4.0,
    logo_url VARCHAR(500),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS buses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT NOT NULL,
    operator_id INT NOT NULL,
    bus_type VARCHAR(50) NOT NULL,
    departure_time VARCHAR(10) NOT NULL,
    arrival_time VARCHAR(10) NOT NULL,
    price INT NOT NULL,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,
    amenities TEXT,
    image_url VARCHAR(500),
    rating DECIMAL(3,2) DEFAULT 4.0,
    FOREIGN KEY (route_id) REFERENCES bus_routes(id),
    FOREIGN KEY (operator_id) REFERENCES bus_operators(id)
);

INSERT INTO bus_routes (origin, destination, distance, duration, image_url) VALUES
('Delhi', 'Manali', '570 km', '12-14 hours', 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4'),
('Mumbai', 'Pune', '150 km', '3-4 hours', 'https://images.unsplash.com/photo-1567157577867-05ccb1388e66'),
('Bangalore', 'Chennai', '350 km', '6-7 hours', 'https://images.unsplash.com/photo-1582510003544-4d00b7f74220'),
('Delhi', 'Jaipur', '280 km', '5-6 hours', 'https://images.unsplash.com/photo-1599661046289-e31897846e41'),
('Kolkata', 'Darjeeling', '650 km', '10-12 hours', 'https://images.unsplash.com/photo-1544735716-392fe2489ffa');

INSERT INTO bus_operators (name, rating, contact_phone) VALUES
('Himachal Tourism', 4.5, '+91-9876543210'),
('RedBus Travels', 4.2, '+91-9876543211'),
('Shivshahi Travels', 4.0, '+91-9876543212'),
('VRL Travels', 4.6, '+91-9876543213'),
('SRS Travels', 4.5, '+91-9876543214');

INSERT INTO buses (route_id, operator_id, bus_type, departure_time, arrival_time, price, total_seats, available_seats, amenities, rating) VALUES
(1, 1, 'Volvo AC Sleeper', '20:00', '08:00', 1200, 40, 12, 'AC,WiFi,Charging Points,Blanket,Entertainment', 4.5),
(1, 2, 'Semi-Sleeper AC', '21:30', '10:00', 900, 35, 8, 'AC,Charging Points,Water Bottle', 4.2),
(2, 3, 'AC Seater', '06:00', '09:30', 450, 45, 15, 'AC,Comfortable Seats', 4.0),
(2, 4, 'Volvo AC', '14:00', '17:30', 600, 40, 22, 'AC,WiFi,Charging Points,Snacks', 4.6);

USE bus_reservation;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email, phone, password) VALUES
('Test User', 'test@example.com', '1234567890', 'password123'),
('Another User', 'another@example.com', '0987654321', 'password456');


CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id VARCHAR(64) NOT NULL UNIQUE,
    user_id INT NOT NULL,
    bus_id INT NOT NULL,
    passenger_name VARCHAR(255) NOT NULL,
    passenger_email VARCHAR(255) NOT NULL,
    passenger_phone VARCHAR(32),
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    travel_date DATE NOT NULL,
    seat_numbers TEXT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(32) NOT NULL DEFAULT 'confirmed',
    payment_status VARCHAR(32) NOT NULL DEFAULT 'completed',
    cancellation_time DATETIME NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_res_user FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
);