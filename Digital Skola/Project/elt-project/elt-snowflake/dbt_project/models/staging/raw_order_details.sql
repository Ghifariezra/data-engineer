-- CREATE OR REPLACE TABLE ELT_PROJECT.RAW.RAW_ORDER_DETAILS (
-- 	ORDERID INT NOT NULL,
--     PRODUCTID INT NOT NULL,
--     UNITPRICE NUMERIC(10, 2) NOT NULL,
--     QUANTITY SMALLINT NOT NULL,
--     DISCOUNT REAL NOT NULL,
--     PRIMARY KEY (ORDERID, PRODUCTID)
-- ) AS 
-- SELECT 
-- 	DISTINCT (TRIM(ORDERID)) AS ORDERID,
-- 	TRIM(PRODUCTID) AS PRODUCTID,
-- 	TRIM(UNITPRICE) AS UNITPRICE ,
-- 	TRIM(QUANTITY) AS QUANTITY ,
-- 	TRIM(DISCOUNT) AS DISCOUNT 
-- FROM {{ source('sources', 'order_details') }}
-- WHERE ORDERID IS NOT NULL AND PRODUCTID IS NOT NULL

select
	DISTINCT (TRIM(ORDERID)) AS ORDERID,
	TRIM(PRODUCTID) AS PRODUCTID,
	TRIM(UNITPRICE) AS UNITPRICE ,
	TRIM(QUANTITY) AS QUANTITY ,
	TRIM(DISCOUNT) AS DISCOUNT 
from
    {{ source('sources', 'order_details') }}
WHERE ORDERID IS NOT NULL AND PRODUCTID IS NOT NULL