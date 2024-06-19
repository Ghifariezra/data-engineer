
  
    

  create  table "datawarehouse_dbt"."public"."raw_payments__dbt_tmp"
  
  
    as
  
  (
    select
    payment_id,
    order_id,
    payment_amount,
    payment_method
from
    "datawarehouse_dbt"."public"."payments"
  );
  