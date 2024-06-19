WITH raw_orders AS (
    SELECT * FROM {{ ref('raw_orders') }}
),

dim_employees AS (
    SELECT * FROM {{ ref('dim_employees') }}
)

SELECT
    O.ORDERID,
    D.EMPLOYEEID,
    O.ORDERDATE,
    O.REQUIREDDATE
FROM
    raw_orders O
JOIN
    dim_employees D ON O.EMPLOYEEID = D.EMPLOYEEID