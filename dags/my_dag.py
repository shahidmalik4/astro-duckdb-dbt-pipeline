from cosmos import ProjectConfig, ProfileConfig, DbtDag, ExecutionConfig, RenderConfig # 👈 IMPORT RenderConfig
from cosmos.profiles.duckdb import DuckDBUserPasswordProfileMapping
from cosmos.profiles.postgres import PostgresUserPasswordProfileMapping
from datetime import datetime
from airflow.models.baseoperator import chain
from airflow.models.dag import DAG 
import os

# --- Configuration Variables ---
DBT_PROJECT_PATH = "/usr/local/airflow/dbt/jaffle_shop_duckdb"
DBT_EXECUTABLE_PATH = f"{os.getenv('AIRFLOW_HOME')}/dbt_venv/bin/dbt"
POSTGRES_CONN_ID = "postgres_local" 
DUCKDB_CONN_ID = "duckdb_default"   
DUCKDB_PATH = "/usr/local/airflow/include/jaffle_shop.duckdb" 

# --- Base Configurations ---
_project_config = ProjectConfig(dbt_project_path=DBT_PROJECT_PATH)
_execution_config = ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE_PATH)

# --- Shared Render Configuration ---
_render_config = RenderConfig( # 👈 EXPLICITLY DEFINED RenderConfig object
    dbt_models_dir=os.path.join(DBT_PROJECT_PATH, "models"),
    load_method="dbt_ls",
)

# --- 1. DuckDB Profile (For Seeds and Raw Data) ---
duckdb_profile_config = ProfileConfig(
    profile_name="jaffle_shop", 
    target_name="duckdb",
    profile_mapping=DuckDBUserPasswordProfileMapping(
        conn_id=DUCKDB_CONN_ID,
        profile_args={"path": DUCKDB_PATH, "schema": "main"},
    )
)

# --- 2. PostgreSQL Profile (For Staging and Marts) ---
postgres_profile_config = ProfileConfig(
    profile_name="jaffle_shop", 
    target_name="postgres",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id=POSTGRES_CONN_ID,
        profile_args={"schema": "public"}, 
    )
)

# --- Standard Airflow DAG Definition (Wrapper) ---
with DAG(
    dag_id="jaffle_shop_multi_target_etl",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["dbt", "cosmos"],
) as dag:

    # 1. TaskGroup to Load Seeds/Raw Data into DuckDB
    load_seeds_to_duckdb = DbtDag(
        dag_id="load_duckdb_seeds",
        project_config=_project_config,
        profile_config=duckdb_profile_config, 
        execution_config=_execution_config,
        default_args={"models": "config.materialized:seed"}, 
        render_config=_render_config, # 👈 Passed the object
    )

    # 2. TaskGroup to Build Clean Models (Staging/Marts) into PostgreSQL
    build_postgres_models = DbtDag(
        dag_id="build_postgres_models",
        project_config=_project_config,
        profile_config=postgres_profile_config, 
        execution_config=_execution_config,
        default_args={"exclude": "config.materialized:seed"}, 
        render_config=_render_config, # 👈 Passed the object
    )
    
    # Define the dependency flow
    chain(load_seeds_to_duckdb, build_postgres_models)