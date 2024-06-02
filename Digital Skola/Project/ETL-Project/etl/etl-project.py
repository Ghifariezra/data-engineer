from config.config import oltp_tables, warehouse_tables, dimension_columns, \
                          ddl_statements, ddl_marts, populate_data_marts
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

def create_tabels_DWH(*connections, **data_connections):
    """ Create DDL Statements for DWH"""
    engine_dwh = create_engine(url=connections[0])

    with engine_dwh.connect() as conn:
        # Create table data warehouse
        for key, val in data_connections.get('ddl').items():
            conn.execute(
                text(val)
            )
            conn.commit()
            print(f'Create {key} Success...')

def extract_data(*connections, **data_connections):
    """Extract data from OLTP"""
    engine_oltp = create_engine(url=connections[1])
    
    df_oltp = {}

    with engine_oltp.connect() as conn:
        # Extract all data from OLTP
        for key, val in data_connections.get('oltp_tables').items():
            query = f"SELECT * FROM {val}"
            df_oltp[key] = pd.read_sql(query, conn)
            print(f'Extract Data {key} Success...')

    return df_oltp

def transform_data(data_oltp: dict):
    """Transform data OLTP"""
    df_transform = {}

    for key, val in data_oltp.items():
        if warehouse_tables.get(key):
            columns = dimension_columns.get(
                warehouse_tables.get(key)
            )# Get columns from warehouse
            
            # Drop duplicate data & Append to df_transform
            dedup = data_oltp[key].drop_duplicates()
            df_transform[key] = dedup[columns]

            print(f'Transform Data {key} Success...')
        else:
            raise ValueError(f'Table {key} not found in warehouse_tables')

    return df_transform

def load_data(*connections, df):
    """Load the transformed data into the target table in the data warehouse."""
    engine_dwh = create_engine(url=connections[0])
    with engine_dwh.connect() as conn:
        try:
            # Insert into data warehouse
            for key, val in warehouse_tables.items():
                df_dwh = pd.read_sql(f"SELECT * FROM {val}", conn)
                if df_dwh.columns[0] == df[key].columns[0]:

                    # Merge data beetween warehouse and new data
                    new_df = pd.concat(
                        [df_dwh, df[key]],
                        names=df[key].columns.tolist()
                    ).drop_duplicates()

                    # Load data based on new data
                    new_df.to_sql(
                        val,
                        engine_dwh, 
                        index=False, 
                        if_exists='append',
                        method='multi'
                    )
                    print(f'Load Data {key} Success...')
                else:
                    raise ValueError(f'Table {key} not found in warehouse_tables')
        except IntegrityError:
            print('Data Already Exists...\nDuplicate Data Ignored...')

def create_data_mart(*connections, **data_connections):
    """ Create DDL Statements & Insert Data for Data Mart"""
    engine_dwh = create_engine(url=connections[0])

    with engine_dwh.connect() as conn:
        for key, val in data_connections.get('ddl').items():
            conn.execute(
                text(val)
            ) # Create table data mart

            conn.execute(
                text(
                    data_connections.get('insert_data').get(key)
                )
            ) # Insert data to data mart
            
            conn.commit()
            print(f'Create {key} Success...')

def etl_process():
    # Required Connection
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')
    HOST = os.environ.get('HOST')
    DWH = os.environ.get('DWH')
    OLTP = os.environ.get('OLTP')

    # Connections
    CONNECTIONS = [
        f'postgresql://{USER}:{PASSWORD}@{HOST}/{DWH}?sslmode=require',
        f'postgresql://{USER}:{PASSWORD}@{HOST}/{OLTP}?sslmode=require'
    ]

    # Process
    create_dwh = create_tabels_DWH(
        *CONNECTIONS,
        ddl=ddl_statements
    )

    extract_oltp = extract_data(
        *CONNECTIONS,
        oltp_tables=oltp_tables
    )

    transform_oltp = transform_data(
        data_oltp=extract_oltp
    )

    load_dwh = load_data(
        *CONNECTIONS,
        df=transform_oltp
    )

    create_dm = create_data_mart(
        *CONNECTIONS,
        ddl=ddl_marts,
        insert_data=populate_data_marts
    )

if __name__ == '__main__':
    etl_process()