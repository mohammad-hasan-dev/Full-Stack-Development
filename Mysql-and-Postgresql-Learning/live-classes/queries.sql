
SELECT
    *
FROM products;


SELECT
    name,
    price
FROM products;


SELECT
    name,
    price
FROM products
WHERE price > 50000
;


SELECT
    *
FROM employees
WHERE is_active=TRUE;



SELECT
    *
FROM customers
WHERE city 
    IN ('Dhaka', 'Chittagong')
;


SELECT
    *
FROM customers
WHERE city 
    NOT IN ('Dhaka', 'Chittagong')
;



SELECT
    name AS customer_name, 
    city
FROM customers
;

SELECT 
    name,
    price,
    price * 1.15 AS price_with_vat
FROM products;


SELECT 
    name,
    price,
    price * 1.15 AS price_with_vat
FROM products
ORDER BY price
;


SELECT 
    name,
    price
FROM products
ORDER BY price ASC
;


SELECT 
    name,
    price
FROM products
ORDER BY price DESC
;


SELECT
    id,
    name,
    price
FROM products
ORDER BY price DESC
LIMIT 3
;


SELECT
    id,
    name,
    price
FROM products
ORDER BY price DESC
LIMIT 3
OFFSET 9
;


SELECT
    *
FROM
    customers
WHERE
    email LIKE '%@gmail.com'
;
-- % -> 0 - inifinity character
SELECT
    *
FROM
    customers
WHERE
    email LIKE '%arif@gmail.com'
;

SELECT
    *
FROM
    customers
WHERE
    email LIKE 'sujon@gmail.com'
;


SELECT
    COUNT(*)
FROM products
;

SELECT
    MAX(price) as max_price
FROM products
;



SELECT * FROM employees;

SELECT
    department_id,
    COUNT(*)
FROM
    employees
GROUP BY department_id
;

SELECT * FROM products;



SELECT
    department_id,
    COUNT(*)
FROM
    employees
GROUP BY department_id
;


SELECT
    department_id,
    AVG(salary) as avg_salary
FROM
    employees
GROUP BY department_id
HAVING AVG(salary)>50000
;


-- JOIN Prerequisite

SELECT * FROM departments;
SELECT * FROM employees;
SELECT
    employees.name
FROM employees;
SELECT
    e.name
FROM employees e;

-- JOIN

SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
JOIN 
    departments d 
    ON e.department_id=d.id
;


SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
INNER JOIN 
    departments d 
    ON e.department_id=d.id
;


SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
LEFT JOIN 
    departments d 
    ON e.department_id=d.id
;


SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
RIGHT JOIN 
    departments d 
    ON e.department_id=d.id
;


SELECT
    e.name AS employee_name,
    d.name AS department_name
FROM
    employees e
FULL JOIN 
    departments d ON e.department_id=d.id
;


-- page = 2

-- LIMIT 20

-- offset -> limit * (page - 1)
