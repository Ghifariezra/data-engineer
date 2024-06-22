WITH raw_order_details AS (
    SELECT * FROM {{ ref('raw_order_details') }}
),

fact_orders AS (
    SELECT * FROM {{ ref('fact_orders') }}
),

dim_products AS (
    SELECT * FROM {{ ref('dim_products') }}
)

SELECT
    ROD.ORDERID AS ORDERDETAILID,
    FO.ORDERID,
    DM.PRODUCTID,
    ROD.UNITPRICE,
    ROD.QUANTITY,
    ROD.DISCOUNT
FROM
    raw_order_details ROD
JOIN
    fact_orders FO ON ROD.ORDERID = FO.ORDERID
JOIN
    dim_products DM ON ROD.PRODUCTID = DM.PRODUCTID