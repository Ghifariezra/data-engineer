
  
    

  create  table "datawarehouse_dbt"."public"."raw_customers__dbt_tmp"
  
  
    as
  
  (
    select
    customer_id,
    customer_name,
    customer_email,
    signup_date
from
    "datawarehouse_dbt"."public"."customers"
  );
  