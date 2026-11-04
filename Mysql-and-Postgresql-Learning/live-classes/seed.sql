-- ============================================================
-- SQL Seed File
-- Topics: SELECT, WHERE, Functions, IN, ORDER BY, LIKE,
--         Data Types, GROUP BY, HAVING, JOINs
-- ============================================================

-- ============================================================
-- TABLES
-- ============================================================

-- Data types demo:
-- INT          → whole numbers (age, quantity, price in taka)
-- VARCHAR(n)   → text with a max length (names, emails, cities)
-- DATE         → calendar date (order date, birth date)
-- BOOLEAN      → true / false (is_active, is_paid)
-- NUMERIC(p,s) → decimal numbers (salary, product price with paisa)

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;

-- departments table (used for JOIN examples)
CREATE TABLE departments (
    id          INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(100)
);

-- employees table (used for JOIN examples)
CREATE TABLE employees (
    id              INT PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    department_id   INT,           -- FK → departments.id  (some may be NULL)
    salary          NUMERIC(10,2),
    hire_date       DATE,
    is_active       BOOLEAN DEFAULT TRUE
);

-- customers table
CREATE TABLE customers (
    id          INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(100),
    email       VARCHAR(150),
    joined_date DATE
);

-- products table
CREATE TABLE products (
    id          INT PRIMARY KEY,
    name        VARCHAR(150) NOT NULL,
    category    VARCHAR(100),
    price       NUMERIC(10,2),
    stock       INT
);

-- orders table
CREATE TABLE orders (
    id              INT PRIMARY KEY,
    customer_id     INT,   -- FK → customers.id
    order_date      DATE,
    is_paid         BOOLEAN DEFAULT FALSE
);

-- order_items table (links orders ↔ products)
CREATE TABLE order_items (
    id          INT PRIMARY KEY,
    order_id    INT,       -- FK → orders.id
    product_id  INT,       -- FK → products.id
    quantity    INT,
    unit_price  NUMERIC(10,2)
);


-- ============================================================
-- SEED DATA
-- ============================================================

INSERT INTO departments (id, name, city) VALUES
(1,  'Engineering',   'Dhaka'),
(2,  'Marketing',     'Chittagong'),
(3,  'HR',            'Dhaka'),
(4,  'Finance',       'Sylhet'),
(5,  'Design',        'Dhaka');
-- Note: Department 5 (Design) has NO employees → useful for RIGHT/FULL JOIN demo

INSERT INTO employees (id, name, department_id, salary, hire_date, is_active) VALUES
(1,  'Rahim Uddin',      1,  75000.00, '2020-03-15', TRUE),
(2,  'Karim Hossain',    1,  82000.00, '2019-07-01', TRUE),
(3,  'Nusrat Jahan',     2,  55000.00, '2021-01-20', TRUE),
(4,  'Farhan Ahmed',     2,  60000.00, '2022-06-10', FALSE),
(5,  'Sumaiya Begum',    3,  48000.00, '2020-11-05', TRUE),
(6,  'Tanvir Islam',     3,  51000.00, '2023-02-28', TRUE),
(7,  'Ritu Akter',       4,  90000.00, '2018-09-12', TRUE),
(8,  'Mehedi Hasan',     4,  87000.00, '2019-04-03', TRUE),
(9,  'Sadia Rahman',     1,  70000.00, '2022-08-17', TRUE),
(10, 'Jobayer Alam',     NULL, 45000.00, '2023-12-01', TRUE);
-- Note: Employee 10 has NULL department_id → useful for LEFT JOIN demo

INSERT INTO customers (id, name, city, email, joined_date) VALUES
(1,  'Arif Chowdhury',   'Dhaka',       'arif@gmail.com',    '2022-01-10'),
(2,  'Mitu Akter',       'Chittagong',  'mitu@yahoo.com',    '2022-03-22'),
(3,  'Sujon Mia',        'Sylhet',      'sujon@gmail.com',   '2021-07-05'),
(4,  'Puja Das',         'Dhaka',       'puja@hotmail.com',  '2023-02-14'),
(5,  'Rubel Khan',       'Rajshahi',    'rubel@gmail.com',   '2021-12-30'),
(6,  'Nasrin Sultana',   'Dhaka',       'nasrin@gmail.com',  '2023-05-18'),
(7,  'Imran Hossain',    'Khulna',      'imran@gmail.com',   '2020-09-09'),
(8,  'Lima Begum',       'Barisal',     'lima@gmail.com',    '2022-11-01'),
(9,  'Sajid Ahmed',      'Dhaka',       'sajid@gmail.com',   '2024-01-15'),
(10, 'Tania Islam',      'Chittagong',  'tania@gmail.com',   '2023-08-20');

INSERT INTO products (id, name, category, price, stock) VALUES
(1,  'Xiaomi Redmi 12',     'Mobile',       18500.00,  50),
(2,  'Samsung A35',         'Mobile',       32000.00,  30),
(3,  'HP Laptop 15s',       'Laptop',       65000.00,  15),
(4,  'Dell Inspiron 15',    'Laptop',       72000.00,  10),
(5,  'Walton TV 43"',       'Television',   42000.00,  20),
(6,  'Sony Earbuds WF',     'Accessories',   4500.00, 100),
(7,  'Logitech Mouse M185', 'Accessories',    950.00, 200),
(8,  'Asus Router',         'Networking',   6800.00,  40),
(9,  'iPad 10th Gen',       'Tablet',       75000.00,   8),
(10, 'Anker Power Bank',    'Accessories',   2800.00, 150);

INSERT INTO orders (id, customer_id, order_date, is_paid) VALUES
(1,  1, '2024-01-05', TRUE),
(2,  2, '2024-01-12', TRUE),
(3,  3, '2024-02-03', FALSE),
(4,  4, '2024-02-20', TRUE),
(5,  1, '2024-03-01', TRUE),
(6,  5, '2024-03-15', FALSE),
(7,  6, '2024-04-10', TRUE),
(8,  7, '2024-04-22', TRUE),
(9,  8, '2024-05-07', FALSE),
(10, 9, '2024-05-18', TRUE),
(11, 2, '2024-06-01', TRUE),
(12, 10,'2024-06-15', TRUE);

INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES
(1,  1,  1,  1, 18500.00),
(2,  1,  7,  2,   950.00),
(3,  2,  2,  1, 32000.00),
(4,  3,  3,  1, 65000.00),
(5,  4,  5,  1, 42000.00),
(6,  5,  6,  2,  4500.00),
(7,  5,  10, 1,  2800.00),
(8,  6,  4,  1, 72000.00),
(9,  7,  8,  1,  6800.00),
(10, 8,  1,  2, 18500.00),
(11, 9,  9,  1, 75000.00),
(12, 10, 7,  3,   950.00),
(13, 11, 2,  1, 32000.00),
(14, 11, 6,  1,  4500.00),
(15, 12, 3,  1, 65000.00);
