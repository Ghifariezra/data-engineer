# Import Airflow Modules
from datetime import datetime, timedelta
from airflow.decorators import dag, task, task_group
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from cosmos import DbtTaskGroup
from dbt.dbt_project.dbt_config import profile_config, project_config, execution_config, render_config
from el_module.extractors import extract_func
from el_module.loaders import load_func
from el_module.filenames import names
import os

# Define Date & Run Schedule
startDate = datetime(2024, 6, 15)
schedule = '* */4 * * *'
# schedule = '* */6 * * *'


# DAG Configuration
default_args = {
    "owner": "Data-Ninja",
    "depends_on_past": False,
    "start_date": startDate,
    "retries":1,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="ELT-PROJECT",
    default_args=default_args,
    schedule_interval=None,
    # schedule='@daily',
    catchup=False,
    fail_stop=True,
    description="ELT Orchestrator",
    tags=['Pandas', 'Snowflake', 'DBT'],
    )
def elt_dag():
    @task(task_id="resource")
    def resource():
        return os.environ.get('RESOURCE')

    @task_group(group_id="extract")
    def extract_data(source):
        tg_extract = []

        # Generate Tasks
        for gen_name in names:
            @task(task_id=f'extract_{gen_name}')
            def extract(name, url):
                return extract_func(
                    url_git=url.format(names=name)
                )

            # Populate Task Group
            tg_extract.append(
                extract(name=gen_name, url=source)
            )
        
        return tg_extract

    @task_group(group_id="load")
    def load_data(dfs):
        tg_load = []

        # Generate Tasks
        for i, gen_name in enumerate(names):
            @task(task_id=f'load_{gen_name}')
            def load(df, table_name):
                load_func(
                    df=df, filename=table_name
                )

            # Populate Task Group
            tg_load.append(
                load(df=dfs[i], table_name=gen_name)
            )

        return tg_load

    wait = TimeDeltaSensor(
        task_id="wait_until_all_connections_closed",
        delta=timedelta(seconds=10)
    )

    transform_data = DbtTaskGroup(
        group_id="transform",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        render_config=render_config,
        operator_args={
            "install_deps": True
        }
    )

    end = DummyOperator(
        task_id="end"
    )

    # Task Flow: Mixing Operator
    resource = resource()
    extract = extract_data(source=resource)
    load_data(dfs=extract) >> wait
    wait >> transform_data >> end

elt_dag()