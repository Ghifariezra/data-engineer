-- CREATE OR REPLACE TABLE ELT_PROJECT.RAW.RAW_SHIPPERS (
-- 	SHIPPERID INT PRIMARY KEY,
--     COMPANYNAME VARCHAR(40) NOT NULL,
--     PHONE VARCHAR(24)
-- ) AS
-- SELECT 
--   DISTINCT SHIPPERID,
--   TRIM(COMPANYNAME) AS COMPANYNAME,
--   REGEXP_REPLACE(TRIM(PHONE), '[^0-9]', '') AS PHONE
-- FROM {{ source('sources', 'shippers') }}
-- WHERE SHIPPERID IS NOT NULL


select
  DISTINCT SHIPPERID,
  TRIM(COMPANYNAME) AS COMPANYNAME,
  REGEXP_REPLACE(TRIM(PHONE), '[^0-9]', '') AS PHONE
from
    {{ source('sources', 'shippers') }}
WHERE SHIPPERID IS NOT NULL