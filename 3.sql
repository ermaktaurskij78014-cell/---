CREATE DATABASE IF NOT EXISTS tourism;
USE tourism;

CREATE TABLE IF NOT EXISTS countries (
    country_id   INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    continent    VARCHAR(50) NOT NULL,
    visa         BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS hotels (
    hotel_id     INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(150) NOT NULL,
    stars        TINYINT NOT NULL,
    country_id   INT NOT NULL,
    city         VARCHAR(100) NOT NULL,
    price        DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE IF NOT EXISTS tours (
    tour_id      INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(200) NOT NULL,
    country_id   INT NOT NULL,
    hotel_id     INT NOT NULL,
    days         INT NOT NULL,
    type         VARCHAR(50) NOT NULL,
    base_price   DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (hotel_id)   REFERENCES hotels(hotel_id)
);

CREATE TABLE IF NOT EXISTS clients (
    client_id    INT AUTO_INCREMENT PRIMARY KEY,
    last_name    VARCHAR(100) NOT NULL,
    first_name   VARCHAR(100) NOT NULL,
    middle_name  VARCHAR(100),
    passport     VARCHAR(20) NOT NULL UNIQUE,
    phone        VARCHAR(20) NOT NULL,
    email        VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id       INT AUTO_INCREMENT PRIMARY KEY,
    client_id      INT NOT NULL,
    tour_id        INT NOT NULL,
    order_date     DATE NOT NULL,
    departure_date DATE NOT NULL,
    persons        INT NOT NULL DEFAULT 1,
    total_price    DECIMAL(10,2) NOT NULL,
    status         VARCHAR(30) NOT NULL DEFAULT 'Новый',
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (tour_id)   REFERENCES tours(tour_id)
);

INSERT INTO countries (name, continent, visa) VALUES
('Турция', 'Азия', FALSE),
('Египет', 'Африка', FALSE),
('Испания', 'Европа', TRUE),
('Таиланд', 'Азия', FALSE),
('Италия', 'Европа', TRUE);

INSERT INTO hotels (name, stars, country_id, city, price) VALUES
('Rixos Bodrum', 5, 1, 'Бодрум', 250.00),
('Coral Beach', 4, 2, 'Хургада', 120.00),
('Hotel Arts', 5, 3, 'Барселона', 320.00),
('Anantara', 5, 4, 'Бангкок', 180.00),
('Excelsior Venice', 4, 5, 'Венеция', 210.00);

INSERT INTO tours (name, country_id, hotel_id, days, type, base_price) VALUES
('Отдых в Турции', 1, 1, 10, 'Пляжный', 85000.00),
('Египет - Красное море', 2, 2, 7, 'Пляжный', 60000.00),
('Барселона', 3, 3, 8, 'Экскурсионный', 95000.00),
('Таиланд', 4, 4, 12, 'Экзотический', 110000.00),
('Венеция', 5, 5, 5, 'Экскурсионный', 70000.00);

INSERT INTO clients (last_name, first_name, middle_name, passport, phone, email) VALUES
('Иванов', 'Иван', 'Иванович', '1234 567890', '+79001234567', 'ivanov@mail.ru'),
('Петрова', 'Мария', 'Сергеевна', '9876 543210', '+79009876543', 'petrova@mail.ru'),
('Сидоров', 'Алексей', 'Петрович', '5555 111222', '+79005551122', NULL),
('Козлова', 'Анна', 'Витальевна', '3333 444555', '+79003334455', 'kozlova@gmail.com');

INSERT INTO orders (client_id, tour_id, order_date, departure_date, persons, total_price, status) VALUES
(1, 1, '2024-03-01', '2024-06-15', 2, 170000.00, 'Оплачен'),
(2, 3, '2024-03-10', '2024-07-01', 1, 95000.00, 'Подтверждён'),
(3, 2, '2024-03-15', '2024-05-20', 2, 120000.00, 'Новый'),
(4, 5, '2024-03-20', '2024-09-10', 2, 140000.00, 'Оплачен');

SELECT o.order_id,
       CONCAT(c.last_name, ' ', c.first_name) AS client,
       t.name AS tour,
       co.name AS country,
       o.departure_date,
       o.persons,
       o.total_price,
       o.status
FROM orders o
JOIN clients c  ON o.client_id  = c.client_id
JOIN tours t    ON o.tour_id    = t.tour_id
JOIN countries co ON t.country_id = co.country_id
ORDER BY o.departure_date;
