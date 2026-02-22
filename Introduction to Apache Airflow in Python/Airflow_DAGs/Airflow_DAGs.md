# Airflow DAGs
## Data: February 21, 2026

- What is DAG?
    - Components of DAG:
        - **Directed**
            - There is an essential flow representing the dependencies between components.
            - The dependencies provides context to the tools on how to run the components in a specific order.
        - **Acyclic**
            - It does not loop or repeat.
            - DAG can be re-run but the component only executed once per run.
        - **Graph**
            - The actual set/s of component.
    - The term DAG is found often in data engineering such as Apache Spark, Airflow, dbt, etc.
    - DAGs are written in *Python* but can use components written in other languages or tools (for example using Bash scripts, spark jobs, etc).
    - Consist of components (usually tasks) to be executed like operators, sensors, etc.
    - Dependencies of DAGs are defined explicitly or implicitly.
        - Copy the data to a server before trying to import it to a database service.

- Defining DAG with the version Airflow 2 and up
    ```
    from airflow import DAG
    from datetime import datetime

    default_arguments = {
        "owner": "John Doe",
        "email": "john_doe@gmail.com", # Define email for alerting
        "start_date": datetime(2026, 2, 21) # Define the start date for the datetime of DAG
    }

    with DAG("etl_workflow", default_args=default_arguments) as etl_dag:
        # Use the DAG object here
    ```

- Defining DAG before the version Airflow 2
    ```
    from airflow import DAG

    default_arguments = {
        "owner": "John Doe",
        "email": "john_doe@gmail.com", # Define email for alerting
        "start_date": datetime(2026, 2, 21) # Define the start date for the datetime of DAG
    }

    etl_dag = DAG("etl_worflow", default_args=default_arguments)
    ```

- The official command line program of Apache Airflow:
    ```
        airflow
    ```

- Get help and descriptions of various subcommands of Apache Airflow in command line:
    ```
        airflow -h
    ```

- See all recognized DAGs in the command line:
    ```
        airflow dags list
    ```