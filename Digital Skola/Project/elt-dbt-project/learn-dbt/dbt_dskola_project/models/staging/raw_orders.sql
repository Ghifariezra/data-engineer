select
    order_id,
    order_date,
    customer_id,
    product_id,
    order_amount
from
    {{ source('raw','orders') }}