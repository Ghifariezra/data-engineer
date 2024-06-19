
  
    

  create  table "datawarehouse_dbt"."public"."raw_orders__dbt_tmp"
  
  
    as
  
  (
    select
    order_id,
    order_date,
    customer_id,
    product_id,
    order_amount
from
    "datawarehouse_dbt"."public"."orders"
  );
  