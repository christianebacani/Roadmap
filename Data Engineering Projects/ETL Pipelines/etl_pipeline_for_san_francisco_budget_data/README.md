# San Francisco Budgets Data Pipeline  

![San Francisco](docs/images/san_francisco.jpg)  

A modular ETL pipeline for processing San Francisco budget data and loading it into Snowflake.  

## 🔧 Pipeline Components  

| Component               | GitHub Link                                                                 | Purpose                          |
|-------------------------|-----------------------------------------------------------------------------|----------------------------------|
| **ETL Jobs**            | [pyetl/pyetl](https://github.com/pyetl/pyetl)                               | Core ETL framework               |
| **Requests**           | [psf/requests](https://github.com/psf/requests)                             | API data fetching                |
| **Pandas**             | [pandas-dev/pandas](https://github.com/pandas-dev/pandas)                   | Data transformation              |
| **Snowflake Connector**| [snowflake-connector-python](https://github.com/snowflakedb/snowflake-connector-python) | Snowflake Python interface       |
| **SQLAlchemy**         | [sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy)           | Database ORM                     |
| **Snowflake SQLAlchemy**| [snowflake-sqlalchemy](https://github.com/snowflakedb/snowflake-sqlalchemy) | SQLAlchemy dialect for Snowflake |