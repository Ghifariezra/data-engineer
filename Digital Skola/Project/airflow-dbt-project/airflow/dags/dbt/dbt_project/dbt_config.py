# Import Cosmos Modules
from cosmos import ProfileConfig, ProjectConfig, ExecutionConfig, LoadMode
from cosmos.config import RenderConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
import os

# DBT Configuration
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/dbt_project"
DBT_EXECUTABLE_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"
MANIFEST_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/dbt_project/target/manifest.json"

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

project_config = ProjectConfig(
    dbt_project_path=DBT_PROJECT_PATH,
    manifest_path=MANIFEST_PATH
)

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)

# # Rendering Configuration
# staging_config = RenderConfig(
#     select=["path:models/staging"]
# )

# warehouse_config = RenderConfig(
#     select=["path:models/warehouse"]
# )

# marts_config = RenderConfig(
#     select=["path:models/marts"]
# )

render_config = RenderConfig(
    load_method=LoadMode.DBT_MANIFEST
)
