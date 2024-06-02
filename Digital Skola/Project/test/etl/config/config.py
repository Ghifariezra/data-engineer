#!python config 

oltp_tables = {
    "users": "tb_users",
    "payments": "tb_payments",
    "shippers": "tb_shippers",
    "ratings": "tb_ratings",
    "vouchers": "tb_vouchers",
    "product_category": "tb_product_category",
    "products": "tb_products",
    "orders": "tb_orders",
    "order_items": "tb_order_items"
}

warehouse_tables = {
    "users": "dim_user",
    "payments": "dim_payment",
    "shippers": "dim_shipper",
    "ratings": "dim_rating",
    "vouchers": "dim_voucher",
    "product_category": "dim_product_category",
    "products": "dim_products",
    "orders": "fact_orders",
    "order_items": "fact_order_items"
}

dimension_columns = {
    "dim_user": ["user_id", "user_first_name", "user_last_name", "user_gender", "user_address", "user_birthday", "user_join"],
    "dim_payment": ["payment_id", "payment_name", "payment_status"],
    "dim_shipper": ["shipper_id", "shipper_name"],
    "dim_rating": ["rating_id", "rating_level", "rating_status"],
    "dim_voucher": ["voucher_id", "voucher_name", "voucher_price", "voucher_created","user_id"], 
    "dim_product_category": ["product_category_id", "product_category_name"],
    "dim_products": ["product_id", "product_category_id", "product_name", "product_created", "product_price", "product_discount"],
    "fact_orders": ['order_id', 'order_date', 'user_id', 'payment_id', 'shipper_id', 'order_price','order_discount', 'voucher_id', 'order_total', 'rating_id'],
    "fact_order_items": ['order_item_id', 'order_id', 'product_id', 'order_item_quantity', 'product_discount', 'product_subdiscount', 'product_price', 'product_subprice']
}

ddl_statements = {
    "dim_user": """
        CREATE TABLE IF NOT EXISTS dim_user (
            user_id INT NOT NULL PRIMARY KEY,
            user_first_name VARCHAR(255) NOT NULL,
            user_last_name VARCHAR(255) NOT NULL,
            user_gender VARCHAR(50) NOT NULL,
            user_address VARCHAR(255),
            user_birthday DATE NOT NULL,
            user_join DATE NOT NULL
        );
    """,
    "dim_payment": """
        CREATE TABLE IF NOT EXISTS dim_payment (
            payment_id INT NOT NULL PRIMARY KEY,
            payment_name VARCHAR(255) NOT NULL,
            payment_status BOOLEAN NOT NULL
        );
    """,
    "dim_shipper": """
        CREATE TABLE IF NOT EXISTS dim_shipper (
            shipper_id INT NOT NULL PRIMARY KEY,
            shipper_name VARCHAR(255) NOT NULL
        );
    """,
    "dim_rating": """
        CREATE TABLE IF NOT EXISTS dim_rating (
            rating_id INT NOT NULL PRIMARY KEY,
            rating_level INT NOT NULL,
            rating_status VARCHAR(255) NOT NULL
        );
    """,
    "dim_voucher": """
        CREATE TABLE IF NOT EXISTS dim_voucher (
            voucher_id INT NOT NULL PRIMARY KEY,
            voucher_name VARCHAR(255) NOT NULL,
            voucher_price INT,
            voucher_created DATE NOT NULL,
            user_id INT NOT NULL
        );
    """,
    "dim_product_category": """
        CREATE TABLE IF NOT EXISTS dim_product_category (
            product_category_id INT NOT NULL PRIMARY KEY,
            product_category_name VARCHAR(255) NOT NULL,
            FOREIGN KEY (product_category_id) REFERENCES dim_products(product_category_id)
        );
    """,    
    "dim_products": """
        CREATE TABLE IF NOT EXISTS dim_products (
            product_id INT NOT NULL PRIMARY KEY,
            product_category_id INT NOT NULL,
            product_name VARCHAR(255) NOT NULL,
            product_created DATE NOT NULL,
            product_price INT NOT NULL,
            product_discount INT,
            FOREIGN KEY (product_category_id) REFERENCES dim_product_category(product_category_id),
            FOREIGN KEY (product_id) REFERENCES fact_order_items(product_id) 
        );
    """,
    "fact_orders": """
        CREATE TABLE IF NOT EXISTS fact_orders (
            order_id INT NOT NULL PRIMARY KEY,
            order_date DATE NOT NULL,
            user_id INT NOT NULL,
            payment_id INT NOT NULL,
            shipper_id INT NOT NULL,
            order_price INT NOT NULL,
            order_discount INT,
            voucher_id INT,
            order_total INT NOT NULL,
            rating_id INT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
            FOREIGN KEY (payment_id) REFERENCES dim_payment(payment_id),
            FOREIGN KEY (shipper_id) REFERENCES dim_shipper(shipper_id),
            FOREIGN KEY (voucher_id) REFERENCES dim_voucher(voucher_id),
            FOREIGN KEY (rating_id) REFERENCES dim_rating(rating_id)
        );
    """,
    "fact_order_items": """
        CREATE TABLE IF NOT EXISTS fact_order_items (
            order_item_id INT NOT NULL PRIMARY KEY,
            order_id INT NOT NULL,
            product_id INT NOT NULL,
            order_item_quantity INT,
            product_discount INT,
            product_subdiscount INT,
            product_price INT NOT NULL,
            product_subprice INT NOT NULL,
            FOREIGN KEY (order_id) REFERENCES fact_orders(order_id),
            FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
        );
    """
}

ddl_marts = {
    "total_sales_monthly": """
        CREATE TABLE IF NOT EXISTS dm_total_sales_monthly (
            year_month TEXT,
            total_sales NUMERIC
        );
    """,
    "sales_per_category": """
        CREATE TABLE IF NOT EXISTS dm_sales_per_category (
            product_category_name VARCHAR(255),
            total_sales NUMERIC
        );
    """,
    "sales_payment_method": """
        CREATE TABLE IF NOT EXISTS dm_sales_payment_method (
            payment_name VARCHAR(255),
            total_sales NUMERIC
        );
    """,
    "sales_per_sender": """
        CREATE TABLE IF NOT EXISTS dm_sales_per_sender (
            shipper_name VARCHAR(255),
            total_sales NUMERIC
        );
    """,
    "sales_per_user": """
        CREATE TABLE IF NOT EXISTS dm_sales_per_user (
            user_name TEXT,
            total_sales NUMERIC
        );
    """,
    "discount_voucher": """
        CREATE TABLE IF NOT EXISTS dm_discount_voucher (
            voucher_name VARCHAR(255),
            use_voucher INT
        );
    """,
    "sales_per_region": """
        CREATE TABLE IF NOT EXISTS dm_sales_per_region (
            region TEXT,
            total_sales NUMERIC
        );
    """,
    "profit_per_category": """
        CREATE TABLE IF NOT EXISTS dm_profit_per_category (
            product_category_name VARCHAR(255),
            total_laba NUMERIC
        );
    """,
    "average_order_user": """
        CREATE TABLE IF NOT EXISTS dm_average_order_user (
            user_id INT,
            user_name TEXT,
            average_order_value NUMERIC
        );
    """,
    "conversion_rate_voucher":"""
        CREATE TABLE IF NOT EXISTS dm_conversion_rate_voucher (
            total_orders INT,
            total_orders_with_voucher INT,
            conversion_rate NUMERIC
        );
    """
}

populate_data_marts = {
    "total_sales_monthly": """
        TRUNCATE TABLE dm_total_sales_monthly;
        INSERT INTO dm_total_sales_monthly (year_month, total_sales)
        SELECT
            TO_CHAR(order_date, 'YYYY-MM') AS year_month,
            SUM(order_total) AS total_sales
        FROM fact_orders
        GROUP BY TO_CHAR(order_date, 'YYYY-MM')
        ORDER BY year_month;
    """,
    "sales_per_category": """
        TRUNCATE TABLE dm_sales_per_category;
        INSERT INTO dm_sales_per_category (product_category_name, total_sales)
        SELECT
            c.product_category_name,
            SUM(oi.product_subprice) AS total_sales
        FROM fact_order_items oi
        JOIN dim_products p ON oi.product_id = p.product_id
        JOIN dim_product_category c ON p.product_category_id = c.product_category_id
        GROUP BY c.product_category_name
        ORDER BY total_sales DESC;
    """,
    "sales_payment_method": """
        TRUNCATE TABLE dm_sales_payment_method;
        INSERT INTO dm_sales_payment_method (payment_name, total_sales)
        SELECT
            p.payment_name,
            SUM(o.order_total) AS total_sales
        FROM fact_orders o
        JOIN dim_payment p ON o.payment_id = p.payment_id
        GROUP BY p.payment_name
        ORDER BY total_sales DESC;
    """,
    "sales_per_sender": """
        TRUNCATE TABLE dm_sales_per_sender;
        INSERT INTO dm_sales_per_sender (shipper_name, total_sales)
        SELECT
            s.shipper_name,
            SUM(o.order_total) AS total_sales
        FROM fact_orders o
        JOIN dim_shipper s ON o.shipper_id = s.shipper_id
        GROUP BY s.shipper_name
        ORDER BY total_sales DESC;
    """,
    "sales_per_user": """
        TRUNCATE TABLE dm_sales_per_user;
        INSERT INTO dm_sales_per_user (user_name, total_sales)
        SELECT
            CONCAT(u.user_first_name, ' ', u.user_last_name) AS user_name,
            SUM(o.order_total) AS total_sales
        FROM fact_orders o
        JOIN dim_user u ON o.user_id = u.user_id
        GROUP BY user_name
        ORDER BY total_sales DESC;
    """,
    "discount_voucher": """
        TRUNCATE TABLE dm_discount_voucher;
        INSERT INTO dm_discount_voucher (voucher_name, use_voucher)
        SELECT 
            voucher_name, 
            COUNT(voucher_id) AS use_voucher
        FROM  dim_voucher 
        GROUP BY voucher_name
        ORDER BY use_voucher ;
    """,
    "sales_per_region": """
        TRUNCATE TABLE dm_sales_per_region;
        INSERT INTO dm_sales_per_region (region, total_sales)
        SELECT
            u.user_address AS region,
            SUM(o.order_total) AS total_sales
        FROM fact_orders o
        JOIN dim_user u ON o.user_id = u.user_id
        GROUP BY region
        ORDER BY total_sales DESC;
    """,
    "profit_per_category": """
        TRUNCATE TABLE dm_profit_per_category;
        INSERT INTO dm_profit_per_category (product_category_name, total_laba)
        SELECT
            c.product_category_name,
            SUM((oi.product_price - COALESCE(oi.product_discount, 0)) * oi.order_item_quantity) AS total_laba
        FROM fact_order_items oi
        JOIN dim_products p ON oi.product_id = p.product_id
        JOIN dim_product_category c ON p.product_category_id = c.product_category_id
        GROUP BY c.product_category_name
        ORDER BY total_laba DESC;
    """,
    "average_order_user": """
        TRUNCATE TABLE dm_average_order_user;
        INSERT INTO dm_average_order_user (user_id, user_name, average_order_value)
        SELECT
            u.user_id,
            CONCAT(u.user_first_name, ' ', u.user_last_name) AS user_name,
            AVG(o.order_total) AS average_order_value
        FROM fact_orders o
        JOIN dim_user u ON o.user_id = u.user_id
        GROUP BY u.user_id, user_name
        ORDER BY average_order_value DESC;
    """,
    "conversion_rate_voucher":"""
        TRUNCATE TABLE dm_conversion_rate_voucher;
        INSERT INTO dm_conversion_rate_voucher (total_orders, total_orders_with_voucher, conversion_rate)
        SELECT
            COUNT(DISTINCT o.order_id) AS total_orders,
            COUNT(DISTINCT o.voucher_id) AS total_orders_with_voucher,
            COUNT(DISTINCT o.voucher_id) / COUNT(DISTINCT o.order_id) AS conversion_rate
        FROM fact_orders o;
    """
}
