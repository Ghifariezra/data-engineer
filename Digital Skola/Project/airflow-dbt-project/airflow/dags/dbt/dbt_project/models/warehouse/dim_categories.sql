WITH RAW_CATEGORIES AS (
    SELECT * FROM {{ ref('raw_categories') }}
)

SELECT * FROM RAW_CATEGORIES