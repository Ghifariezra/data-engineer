WITH raw_employees AS (
    SELECT * FROM {{ ref('raw_employees') }}
)

SELECT * FROM raw_employees