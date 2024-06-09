from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

def extract():
    # Get list of file names
    filename = open('scripts/list-filename/name.txt', 'r')
    filenames = [name.strip() for name in filename.readlines()]

    url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/{name}.csv"

    # Extract data from github
    dfs = [
        pd.read_csv(url.format(name=name))
        for name in filenames
    ]

    return dfs

def load(dfs):
    # Get list of table names
    tables = open('scripts/list-filename/tables.txt', 'r')
    table_names = [name.strip() for name in tables.readlines()]

    # Connect to Snowflake
    USER = os.getenv('SNOWFLAKE_USER')
    PASSWORD = os.getenv('KEY_PAIR')
    ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
    DATABASE = os.getenv('SNOWFLAKE_DATABASE')
    SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
    WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
    ROLE = os.getenv('SNOWFLAKE_ROLE')

    # Connector
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        database=DATABASE,
        schema=SCHEMA,
        warehouse=WAREHOUSE,
        role=ROLE,
        autocommit=True
    )

    cur = conn.cursor()

    for idx, table in enumerate(table_names):
        # Create table based on table name into snowflake
        write_pandas(
            conn=conn,
            df=dfs[idx],
            table_name=table,
            quote_identifiers=False,
            overwrite=True
        )
        
        print(f"Done {table}")

    cur.close()
    conn.close()

def main():
    dfs = extract()
    load(dfs=dfs)

if __name__ == "__main__":
    main()