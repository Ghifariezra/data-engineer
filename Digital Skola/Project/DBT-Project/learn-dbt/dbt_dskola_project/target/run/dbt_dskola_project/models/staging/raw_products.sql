
  
    

  create  table "datawarehouse_dbt"."public"."raw_products__dbt_tmp"
  
  
    as
  
  (
    select
    product_id,
    product_name,
    category
from
    "datawarehouse_dbt"."public"."products"
  );
  