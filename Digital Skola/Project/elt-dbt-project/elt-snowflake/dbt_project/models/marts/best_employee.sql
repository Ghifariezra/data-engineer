WITH fact_order_details AS (
    SELECT * FROM {{ ref('fact_order_details') }}
),

fact_orders AS (
    SELECT * FROM {{ ref('fact_orders') }}
),

dim_employees AS (
    SELECT * FROM {{ ref('dim_employees') }}
),

employee_revenue AS (
    SELECT
        CONCAT(e.FirstName, ' ', e.LastName) AS employee_name,
        DATE_TRUNC('month', o.OrderDate) AS month,
        SUM((od.UnitPrice - (od.UnitPrice * od.Discount)) * od.Quantity) AS gross_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY DATE_TRUNC('month', o.OrderDate) 
            ORDER BY SUM((od.UnitPrice - (od.UnitPrice * od.Discount)) * od.Quantity) DESC
            ) AS shorting
    FROM fact_order_details od
    JOIN fact_orders o ON od.OrderID = o.OrderID
    JOIN dim_employees e ON o.EmployeeID = e.EmployeeID
    WHERE o.OrderDate IS NOT NULL
    GROUP BY CONCAT(e.FirstName, ' ', e.LastName), DATE_TRUNC('month', o.OrderDate)
)
SELECT
    month,
    employee_name,
    gross_revenue AS datamart_monthly_best_employee
FROM employee_revenue
WHERE shorting = 1