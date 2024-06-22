from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import os

def load_func(**kwargs):
    # Connect to Snowflake
    USER = os.environ.get('SNOWFLAKE_USER')
    PASSWORD = os.environ.get('SNOWFLAKE_PASSWORD')
    ACCOUNT = os.environ.get('SNOWFLAKE_ACCOUNT')
    DATABASE = os.environ.get('SNOWFLAKE_DATABASE')
    SCHEMA = os.environ.get('SNOWFLAKE_SCHEMA')
    WAREHOUSE = os.environ.get('SNOWFLAKE_WAREHOUSE')
    ROLE = os.environ.get('SNOWFLAKE_ROLE')

    # Connector
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        database=DATABASE,
        schema=SCHEMA,
        warehouse=WAREHOUSE,
        role=ROLE,
        insecure_mode=True,
        ocsp_fail_open=False,
        autocommit=True
    )

    cur = conn.cursor()

    print(f"Nama kolom di DataFrame: {kwargs.get('df').columns}")

    # Create table based on table name into snowflake
    write_pandas(
        conn=conn,
        df=kwargs.get('df'),
        table_name=kwargs.get('filename'),
        quote_identifiers=False,
        overwrite=True
    )
    
    print(f"Done {kwargs.get('filename')}.")

    cur.close()
    conn.close()