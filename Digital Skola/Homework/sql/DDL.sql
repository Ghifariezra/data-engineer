CREATE TABLE sales (
sale_id SERIAL PRIMARY KEY,
product_id INT,
employee_id INT,
quantity INT,
price DECIMAL,
sale_date DATE
);
CREATE TABLE products (
product_id SERIAL PRIMARY KEY,
product_name VARCHAR(255),
category VARCHAR(255),
price DECIMAL
);
CREATE TABLE employees (
employee_id SERIAL PRIMARY KEY,
name VARCHAR(255),
department_id INT,
salary DECIMAL
);
CREATE TABLE departments (
department_id SERIAL PRIMARY KEY,
department_name VARCHAR(255)
);
INSERT INTO departments (department_name)
VALUES
('Sales'),
('Marketing'),
('IT'),
('HR'),
('Finance');
INSERT INTO employees (name, department_id, salary)
VALUES
('John Doe', 1, 50000),
('Jane Smith', 2, 55000),
('Alice Johnson', 3, 60000),
('Robert Brown', 4, 45000),
('Emily Davis', 5, 70000);
INSERT INTO products (product_name, category, price)
VALUES
('Laptop', 'Electronics', 1000),
('Smartphone', 'Electronics', 800),
('Tablet', 'Electronics', 500),
('Headphones', 'Accessories', 100),
('Charger', 'Accessories', 20);
INSERT INTO sales (product_id, employee_id, quantity, price, sale_date)
VALUES
(1, 1, 5, 1000, '2024-05-01'),
(2, 2, 10, 800, '2024-05-02'),
(3, 3, 7, 500, '2024-05-03'),
(4, 4, 15, 100, '2024-05-04'),
(5, 5, 20, 20, '2024-05-05');
