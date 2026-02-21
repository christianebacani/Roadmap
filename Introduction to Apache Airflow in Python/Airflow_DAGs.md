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