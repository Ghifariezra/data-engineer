WITH RAW_PRODUCTS AS (
  SELECT * FROM {{ ref('raw_products') }}
),

dim_categories AS (
  SELECT * FROM {{ ref('dim_categories') }}
),

dim_suppliers AS (
  SELECT * FROM {{ ref('dim_suppliers') }}
)

SELECT
  P.PRODUCTID,
  P.PRODUCTNAME,
  S.SUPPLIERID,
  C.CATEGORYID,
  P.QUANTITYPERUNIT,
  P.UNITPRICE,
  P.UNITSINSTOCK,
  P.UNITSONORDER,
  P.REORDERLEVEL,
  P.DISCONTINUED
FROM
  RAW_PRODUCTS P
JOIN
  dim_categories C ON P.CATEGORYID = C.CATEGORYID
JOIN
  dim_suppliers S ON P.SUPPLIERID = S.SUPPLIERID