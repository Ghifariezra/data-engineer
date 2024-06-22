import os
import sys
from pathlib import Path
from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/dbt_project"

profile_config = ProfileConfig(
    profile_name="dbt_project",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snow_conn", 
        profile_args={
            "database": "ELT_PROJECT",
            "schema": "PUBLIC"
        },
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_path=DBT_PROJECT_PATH,),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)