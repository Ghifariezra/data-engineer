-- Tabel Customers
CREATE TABLE public.customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    signup_date DATE,
    country VARCHAR(50)
);

INSERT INTO public.customers (customer_name, customer_email, signup_date, country)
VALUES 
    ('Alice', 'alice@example.com', '2021-01-01', 'USA'),
    ('Bob', 'bob@example.com', '2021-01-02', 'Canada');

-- Tabel Orders
CREATE TABLE public.orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product_id INT,
    order_amount DECIMAL(10, 2)
);

INSERT INTO public.orders (order_date, customer_id, product_id, order_amount)
VALUES
    ('2021-01-10', 1, 1, 100.00),
    ('2021-01-11', 2, 2, 150.00);

-- Tabel Payments
CREATE TABLE public.payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT,
    payment_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    payment_date DATE
);

INSERT INTO public.payments (order_id, payment_amount, payment_method, payment_date)
VALUES
    (1, 100.00, 'Credit Card', '2021-01-10'),
    (2, 150.00, 'PayPal', '2021-01-10');

-- Tabel Products
CREATE TABLE public.products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

INSERT INTO public.products (product_name, category, price)
VALUES
    ('Product A', 'Category 1', 50.00),
    ('Product B', 'Category 2', 75.00);