-- Django Batch 13 | Module 5 Assignment
-- Database: PostgreSQL
-- Scenario: Multi-Vendor SaaS E-commerce Platform
-- Each query is commented to explain its purpose.

-- =========================================================
-- PART A/B: DATABASE DESIGN AND SQL DDL
-- =========================================================

-- SubscriptionPlan: one plan can be used by many vendors.
CREATE TABLE IF NOT EXISTS SubscriptionPlan (
    plan_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL UNIQUE,
    price NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    features TEXT
);

-- Vendor: each vendor subscribes to exactly one plan at a time.
CREATE TABLE IF NOT EXISTS Vendor (
    vendor_id SERIAL PRIMARY KEY,
    business_name VARCHAR(200) NOT NULL,
    contact_person VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(30),
    business_address TEXT NOT NULL,
    plan_id INTEGER NOT NULL REFERENCES SubscriptionPlan(plan_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Product: each product belongs to one vendor.
CREATE TABLE IF NOT EXISTS Product (
    product_id SERIAL PRIMARY KEY,
    vendor_id INTEGER NOT NULL REFERENCES Vendor(vendor_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    product_name VARCHAR(200) NOT NULL,
    description TEXT,
    price NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    status VARCHAR(10) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'inactive'))
);

-- Category: products can belong to multiple categories.
CREATE TABLE IF NOT EXISTS Category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(120) NOT NULL UNIQUE,
    description TEXT
);

-- ProductCategory: junction table resolving Product <-> Category M:N.
-- Composite primary key prevents duplicate product/category pairs.
CREATE TABLE IF NOT EXISTS ProductCategory (
    product_id INTEGER NOT NULL REFERENCES Product(product_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES Category(category_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (product_id, category_id)
);

-- Customer: one customer can place many orders.
CREATE TABLE IF NOT EXISTS Customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(30),
    address TEXT
);

-- Orders: each order belongs to one customer.
-- "Orders" is quoted to preserve the table name; order is a SQL keyword.
CREATE TABLE IF NOT EXISTS "Order" (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES Customer(customer_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount NUMERIC(12, 2) NOT NULL DEFAULT 0 CHECK (total_amount >= 0),
    status VARCHAR(20) NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled'))
);

-- OrderItem: resolves the Order <-> Product relationship and stores line details.
CREATE TABLE IF NOT EXISTS OrderItem (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES "Order"(order_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES Product(product_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    subtotal NUMERIC(12, 2) NOT NULL CHECK (subtotal >= 0)
);

-- Payment: one payment record per order (1:1 relationship).
CREATE TABLE IF NOT EXISTS Payment (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL UNIQUE REFERENCES "Order"(order_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    method VARCHAR(30) NOT NULL
        CHECK (method IN ('Card', 'Bkash', 'PayPal', 'Cash on Delivery')),
    amount NUMERIC(12, 2) NOT NULL CHECK (amount >= 0),
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'paid', 'failed', 'refunded'))
);

-- =========================================================
-- PART C: SQL DML (INSERT / UPDATE / DELETE)
-- =========================================================

-- Seed the Basic plan so the vendor insert below can run on a fresh database.
INSERT INTO SubscriptionPlan (plan_name, price, duration_days, features)
VALUES ('Basic', 0.00, 30, 'Basic product listing and vendor dashboard')
ON CONFLICT (plan_name) DO NOTHING;

-- Q5. Insert SmartTech Ltd. under the Basic subscription plan.
INSERT INTO Vendor (business_name, contact_person, email, phone, business_address, plan_id)
SELECT 'SmartTech Ltd.', 'Rahim Khan', 'rahim@smarttech.com',
       '017XXXXXXXX', 'Dhaka, Bangladesh', plan_id
FROM SubscriptionPlan
WHERE plan_name = 'Basic'
ON CONFLICT (email) DO NOTHING;

-- Ensure the Electronics category exists before adding the product-category link.
INSERT INTO Category (category_name, description)
VALUES ('Electronics', 'Electronic devices and accessories')
ON CONFLICT (category_name) DO NOTHING;

-- Q6. Insert Laptop for SmartTech Ltd. and associate it with Electronics.
-- The CTE obtains the new/existing product ID and inserts the M:N link.
WITH inserted_product AS (
    INSERT INTO Product (vendor_id, product_name, description, price, stock_quantity, status)
    SELECT v.vendor_id, 'Laptop', 'Laptop computer', 75000.00, 10, 'active'
    FROM Vendor v
    WHERE v.business_name = 'SmartTech Ltd.'
      AND v.email = 'rahim@smarttech.com'
    RETURNING product_id
)
INSERT INTO ProductCategory (product_id, category_id)
SELECT ip.product_id, c.category_id
FROM inserted_product ip
CROSS JOIN Category c
WHERE c.category_name = 'Electronics'
ON CONFLICT (product_id, category_id) DO NOTHING;

-- Q7. Update the stock quantity of the Laptop product to 15.
UPDATE Product
SET stock_quantity = 15
WHERE product_name = 'Laptop'
  AND vendor_id = (
      SELECT vendor_id FROM Vendor
      WHERE email = 'rahim@smarttech.com'
  );

-- Q8. Delete the customer whose email is oldcustomer@gmail.com.
-- This will be blocked by the foreign key if the customer has existing orders.
-- Review/migrate those orders before deleting if the customer is linked to orders.
DELETE FROM Customer
WHERE email = 'oldcustomer@gmail.com';

-- =========================================================
-- PART D: SQL QUERIES (DQL)
-- =========================================================

-- Q9. Display all vendors with their subscription plan name and price.
SELECT v.vendor_id, v.business_name, sp.plan_name, sp.price AS plan_price
FROM Vendor v
JOIN SubscriptionPlan sp ON sp.plan_id = v.plan_id
ORDER BY v.business_name;

-- Q10. Find all products in the Electronics category with name, price, and stock.
SELECT p.product_name, p.price, p.stock_quantity
FROM Product p
JOIN ProductCategory pc ON pc.product_id = p.product_id
JOIN Category c ON c.category_id = pc.category_id
WHERE c.category_name = 'Electronics'
ORDER BY p.product_name;

-- Q11. List all orders placed by Karim Uddin.
SELECT o.order_id, o.order_date AS date, o.total_amount, o.status
FROM "Order" o
JOIN Customer c ON c.customer_id = o.customer_id
WHERE c.customer_name = 'Karim Uddin'
ORDER BY o.order_date DESC;

-- Q12. Show payment method, amount, and status for order_id = 1.
SELECT method, amount, status
FROM Payment
WHERE order_id = 1;

-- Q13. Find the top 5 best-selling products by total quantity sold.
SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity_sold
FROM OrderItem oi
JOIN Product p ON p.product_id = oi.product_id
JOIN "Order" o ON o.order_id = oi.order_id
WHERE o.status <> 'cancelled'
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC, p.product_name
LIMIT 5;
