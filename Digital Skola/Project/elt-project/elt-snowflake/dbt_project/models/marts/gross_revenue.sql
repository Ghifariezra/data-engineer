WITH fact_order_details AS (
    SELECT * FROM {{ ref('fact_order_details') }}
),

fact_orders AS (
    SELECT * FROM {{ ref('fact_orders') }}
),

dim_products AS (
    SELECT * FROM {{ ref('dim_products') }}
),

dim_suppliers AS (
    SELECT * FROM {{ ref('dim_suppliers') }}
)

SELECT
    MONTH,
    SUPPLIER_NAME,
    GROSS_REVENUE AS datamart_monthly_supplier_gross_revenue
FROM(
    SELECT
        DATE_TRUNC('month', FO.ORDERDATE) AS MONTH,
        DS.COMPANYNAME AS SUPPLIER_NAME,
        SUM((FOD.UNITPRICE - (FOD.UNITPRICE * FOD.DISCOUNT)) * FOD.QUANTITY) AS GROSS_REVENUE,
        ROW_NUMBER () OVER (
            PARTITION BY DATE_TRUNC('month', FO.ORDERDATE) 
            ORDER BY SUM((FOD.UNITPRICE - (FOD.UNITPRICE * FOD.DISCOUNT) )* FOD.QUANTITY) DESC
            ) AS SHORTING
    FROM fact_order_details FOD
    
    JOIN fact_orders FO ON FOD.ORDERID = FO.ORDERID
    JOIN dim_products DP ON FOD.PRODUCTID = DP.PRODUCTID
    JOIN dim_suppliers DS ON DP.SUPPLIERID = DS.SUPPLIERID

    WHERE FO.ORDERDATE IS NOT NULL
    GROUP BY DS.COMPANYNAME, DATE_TRUNC('month', FO.ORDERDATE)
)
WHERE SHORTING = 1