SELECT
  DISTINCT SHIPPERID,
  TRIM(COMPANYNAME) AS COMPANYNAME,
  REGEXP_REPLACE(TRIM(PHONE), '[^0-9]', '') AS PHONE
FROM
    {{ source('sources', 'shippers') }}
WHERE SHIPPERID IS NOT NULL