# San Francisco Budgets Data Pipeline  

![San Francisco](docs/images/san_francisco.jpg)  

A modular ETL pipeline for processing and analyzing San Francisco's budget data from the [San Francisco Open Data APIs](https://datasf.org/opendata/), with Snowflake as the target data warehouse.

## 📌 Features
- **Batch Processing**: Scheduled or on-demand data ingestion from [SF Open Data Portal](https://data.sfgov.org/)
- **Data Validation**: Automated quality checks at each stage
- **Snowflake Integration**: Optimized for cloud data warehousing
- **Reproducible Workflows**: Version-controlled transformations

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
| **SQLAlchemy**          | Manages database schema and SQL operations                                   |

## 🔄 Workflow Overview
1. **Extract**  
   - API data → `data/raw/` (CSV/JSON)
   - Initial quality validation

2. **Transform**  
   - Raw → `data/staged/` (structured tables)
   - Business logic application
   - Schema standardization

3. **Load**  
   - Processed → `data/processed/` (analysis-ready)
   - Snowflake staging area → Production tables
   - Data lineage tracking

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Snowflake account with proper privileges
- API access to SF budget data

### Installation
```bash
git clone https://github.com/your-repo/sf-budget-pipeline.git
cd sf-budget-pipeline
pip install -r requirements.txt