# San Francisco Budgets Data Pipeline  

![San Francisco](docs/images/san_francisco.jpg)  

A modular ETL pipeline for processing and analyzing San Francisco's budget data from the [San Francisco Open Data APIs](https://datasf.org/opendata/), with Snowflake as the target data warehouse.

## 📌 Features
- **Batch Processing**: Scheduled or on-demand data ingestion from [SF Open Data Portal](https://data.sfgov.org/)
- **Snowflake Integration**: Optimized for cloud data warehousing
- **Reproducible Workflows**: Version-controlled transformations with different phases

## 🛠️ Pipeline Architecture  

### Data Sources
- Primary API: [SF Budget Datasets](https://data.sfgov.org/City-Management-and-Ethics/Budget/xdgd-c79v)
- Secondary API: [SF Financial Reports](https://data.sfgov.org/City-Management-and-Ethics/Financial-Reports/7j6h-6b2q)

### Core Components
| Component               | Purpose                                                                      | Documentation |
|-------------------------|------------------------------------------------------------------------------|---------------|
| **ETL Jobs**            | Orchestrates end-to-end pipeline execution                                   | -             |
| **Requests**            | Fetches raw data from [SF Open Data APIs](https://dev.socrata.com/foundry/data.sfgov.org) | [Docs](https://requests.readthedocs.io/) |
| **Pandas**              | Performs data cleaning and transformation                                    | [Docs](https://pandas.pydata.org/docs/) |
| **Snowflake Connector** | Handles secure data loading to Snowflake                                     | [Docs](https://docs.snowflake.com/en/user-guide/python-connector.html) |

## 🛠️ Pipeline Architecture  

### Core Components
| Component               | Purpose                                                                      |
|-------------------------|------------------------------------------------------------------------------|
| **ETL Jobs**            | Orchestrates end-to-end pipeline execution                                   |
| **Requests**            | Fetches raw data from (San Francisco Open Data Rest APIs)[https://data.sfgov.org/] using Request Library                                       |
| **Pandas**              | Performs data cleaning and transformation                                    |
| **Snowflake Connector** | Handles secure data loading to Snowflake                                     |
| **SQLAlchemy**          | Manages SQL Operation                                                        |

## 🔄 Workflow Overview
1. **Ingest**
   - Raw API data → `data/raw/` (CSV/JSON)
   - Ingested using [Request Module](https://requests.readthedocs.io/)
   - Paginated for faster processing

1. **Extract**  
   - CSV/JSON data → `data/staged`
   - Extracted using [Pandas](https://pandas.pydata.org/docs/)

2. **Transform**  
   - `data/staged`→ `data/processed/` (structured tables)
   - Business logic application
   - Different transformation phases such as (`Data Imputation`, `DataType Casting`, `Format Revisioning`, `Data Partitioning`, `Data Integration`, and `Data Deduplication`)

3. **Load**
   - Perform data schema revisioning before loading to temporary stage of Snowflake
   - `data/processed` → `@processed_datasets`
   - Load datasets from temporary stage to corresponding tables

4. **Testing SQL Queries**
   - Performing SQL Queries using SQL Alchemy Engine

## 🚀 Getting Started

### Prerequisites

#### System Requirements
- Python 3.8 or higher
- pip package manager
- Git version control

#### Accounts & Credentials
- Active Snowflake account with:
  - Warehouse privileges
  - Database create/modify permissions
  - Stage access
- Access to [SF Open Data Portal](https://data.sfgov.org/) (no account needed)

### Installation

1.**Create and activate a virtual environment (recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. **Install required Python packages:**
   pip install requests pandas snowflake-connector-python sqlalchemy snowflake-sqlalchemy

3. **Verify Installations:**
   python -c "import requests, pandas, snowflake.connector, sqlalchemy; print('All packages installed successfully')"