# Introduction to Apache Airflow

- What is Data Engineering?
    - Taking any action involving data to make it reliable, maintainable, and repeatable process.

- What is workflow?
    - Set of steps to accomplish to any given data engineering task such as downloading files, copying data, filtering information, writing to a database, etc.
    - Worfklows varies on their complexities because some of them have only 2 or 3 steps but some of them consist of hundreds of components.
    - The complexity of the workflow totally depends on the needs of the user.
    - `NOTE`: Workflow comes with various meaning depending on the context.

- What is Apache Airflow?
    - Platform to program workflows, including:
        - Creation
        - Scheduling
        - Monitoring
    - Apache Airflow can implement any programs in any tools or languages but the actual workflow code is written in Python.
    - Apache Airflow implement workflows as `Directed Acyclic Graphs (DAGS)`
    - Airflow can be accessed via code, command-line, via web interface, or even REST API.
    - There are different tools to run workflows besides Airflow such as Spotify's Luigi, Microsoft's SSIS, Bash Scripting.

- What is Directed Acyclic Graphs?
    - In Apache Airflow, this represents the set of task that make up your workflow
    - Consist of task and dependencies between tasks.
    - It is created with details about that specific DAGs including the name, start date, owner, email alerting options, etc.
    - Example of creating a new DAG:<br>
        ```
        etl_dag = DAG(
            dag_id='etl_pipeline',
            default_args={
                "start_date": "2026-02-17"
            }
        )
        ```
        - **NOTE**: In *Python* the created DAG is referred as **etl_dag** but within *Airflow Shell Command* we must use the **dag_id**.
    - We call it task for the component of a workflow that is implemented using DAGs.