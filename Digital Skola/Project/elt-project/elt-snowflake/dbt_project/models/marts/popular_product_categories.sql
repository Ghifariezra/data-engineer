WITH dim_categories AS (
    SELECT * FROM {{ ref('dim_categories') }}
),

fact_order_details AS (
    SELECT * FROM {{ ref('fact_order_details') }}
),

fact_orders AS (
    SELECT * FROM {{ ref('fact_orders') }}
),

dim_products AS (
    SELECT * FROM {{ ref('dim_products') }}
)

SELECT
    MONTH,
    CATEGORYNAME,
    TOTAL_QUANTITY_SOLD AS datamart_montly_category_sold
FROM (
    SELECT
        DATE_TRUNC('month', FO.ORDERDATE) AS MONTH,
        DC.CATEGORYNAME,
        SUM(FOD.QUANTITY) AS TOTAL_QUANTITY_SOLD,
        ROW_NUMBER() OVER (
            PARTITION BY DATE_TRUNC('month', FO.ORDERDATE) ORDER BY SUM(FOD.QUANTITY) DESC
            ) AS SHORTING
    FROM dim_categories DC
    JOIN
        dim_products DP ON DC.CATEGORYID = DP.CATEGORYID
    JOIN
        fact_order_details FOD ON DP.PRODUCTID = FOD.PRODUCTID
    JOIN
        fact_orders FO ON FOD.ORDERID = FO.ORDERID
    WHERE FO.ORDERDATE IS NOT NULL
    GROUP BY DC.CATEGORYNAME, DATE_TRUNC('month', FO.ORDERDATE)
)
WHERE SHORTING = 1