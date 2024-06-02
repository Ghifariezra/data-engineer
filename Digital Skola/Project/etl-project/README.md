# About this Project

Perform data extraction from **OLTP** then we move the data from OLTP to **Datawarehouse** and then connect Datawarehouse to **Looker** to create **Dashboards**.

![Group 4 Project](architecture/Group%204.png)

## How to use this Project ?
Make sure you change requirement connections
```pycon
# Required Connection
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
DWH = os.environ.get('DWH')
OLTP = os.environ.get('OLTP')
```