with raw_orders as (
    select * from {{ ref('raw_orders') }}
),

raw_customers as (
    select * from {{ ref('raw_customers') }}
),

raw_products as (
    select * from {{ ref('raw_products') }}
),

raw_payments as (
    select * from {{ ref('raw_payments') }}
)

select
    o.order_id,
    o.order_date,
    c.customer_name,
    c.customer_email,
    p.product_name,
    p.category,
    o.order_amount,
    py.payment_amount,
    py.payment_method
from
    raw_orders o
join
    raw_customers c on o.customer_id = c.customer_id
join
    raw_products p on o.product_id = p.product_id
join
    raw_payments py on o.order_id = py.order_id