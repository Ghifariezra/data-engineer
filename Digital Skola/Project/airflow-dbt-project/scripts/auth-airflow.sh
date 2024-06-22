#!/bin/bash
airflow db init

# Deactivate authentication for webserver
echo "AUTH_ROLE_PUBLIC = 'Admin'" >> webserver_config.py

# Connections to Postgres, 
# if you confused for it you can read airflow cheat sheet in website 
# or in container webserver-airflow.

airflow connections add 'postgres' \
    --conn-type 'postgres' \
    --conn-login $POSTGRES_USER \
    --conn-password $POSTGRES_PASSWORD \
    --conn-host $POSTGRES_CONTAINER \
    --conn-port $POSTGRES_PORT \
    --conn-schema $POSTGRES_DB
    
airflow webserver