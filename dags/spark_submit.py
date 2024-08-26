from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "spark_hello_world",
    default_args=default_args,
    description="A simple Spark Hello World DAG",
    schedule_interval=None,
    catchup=False,
)


# Define the SparkSubmitOperator
spark_submit = SparkSubmitOperator(
    task_id="submit_hello_world",
    application="/usr/local/airflow/include/hello.py",  # Change this to the path of your script
    conn_id="spark_default",
    dag=dag,
)

# Set task dependencies
spark_submit
