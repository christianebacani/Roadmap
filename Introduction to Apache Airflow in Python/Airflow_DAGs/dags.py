from airflow import DAG
from datetime import datetime

default_arguments = {
    "owner": "John Doe", # Owner of the DAG
    "email": "john_doe@gmail.com", # Define email for alerting
    "start_date": datetime(2026, 2, 21) # Define the start date for the datetime of DAG
}

# Method to define the DAG from Airflow 2.x version
# Define the DAG object (context manager) using `with` statement and use the attributes
# `default_arguments` dictionary
with DAG("etl_workflow", default_args=default_arguments) as etl_dag:
    None
    # The remainder of the code will appear in the context manager (etl_workflow)

# Method to define the DAG before Airflow 2.x version
etl_dag = DAG("etl_workflow", default_args=default_arguments)