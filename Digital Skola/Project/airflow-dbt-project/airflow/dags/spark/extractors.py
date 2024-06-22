from pyspark.sql import SparkSession
from el_module.filenames import names
import pandas as pd
import os

sparkSess = SparkSession \
            .builder \
            .appName("Extractors") \
            .master("local[*]") \
            .config("spark.jars.packages", "org.postgresql:postgresql:42.2.18") \
            .getOrCreate()
            
sparkCont = sparkSess.sparkContext
sparkCont.setLogLevel("WARN")

HOST = os.environ.get('HOSTNAME')
DB_NAME = os.environ.get('DB')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

JDBC_CONN = f'jdbc:postgresql://{HOST}/{DB_NAME}'
properties = {
    "user": USER,
    "password": PASSWORD,
    "sslmode": "require",
    "driver": "org.postgresql.Driver"
}

