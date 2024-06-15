WITH RAW_SUPPLIERS AS (
  SELECT * FROM {{ ref('raw_suppliers') }}
)

SELECT * FROM RAW_SUPPLIERS