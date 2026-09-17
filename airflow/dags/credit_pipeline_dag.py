import sys
sys.path.insert(0, "/opt/airflow/pipeline")
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator
from extract import extract_data
from quality_checks import run_quality_checks
from transform import transform_data, get_credit_profile_by_purpose
from load import load_data

def extract_task():
    df = extract_data()
    print(f"Extracted {len(df)} rows")

def quality_check_task():
    df = extract_data()
    passed = run_quality_checks(df)
    if not passed:
        print("WARNING: Quality checks failed continuing anyway")

def transform_and_load_task():
    df = extract_data()
    transformed_df = transform_data(df)
    load_data(transformed_df, "applicants")
    profile = get_credit_profile_by_purpose(transformed_df)
    load_data(profile, "credit_profile_by_purpose")

with DAG(
    dag_id="credit_risk_pipeline",
    start_date=datetime(2026, 9, 17),
    schedule=None,
    catchup=False)as dag:

    extract=PythonOperator(
        task_id="extract_task",
        python_callable=extract_task
    ) 

    quality_check=PythonOperator(
        task_id= "quality_check_task",
        python_callable=quality_check_task
    )

    transform_and_load = PythonOperator(
        task_id="transform_and_load_task",
        python_callable=transform_and_load_task
    )
    extract >> quality_check >> transform_and_load