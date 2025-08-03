# San Francisco Budgets Data Pipeline  

![San Francisco](docs/images/san_francisco.jpg)  

A modular ETL pipeline for processing and analyzing San Francisco's budget data, with Snowflake as the target data warehouse.

## 📌 Features
- **Batch Processing**: Scheduled or on-demand data ingestion
- **Data Validation**: Automated quality checks at each stage
- **Snowflake Integration**: Optimized for cloud data warehousing
- **Reproducible Workflows**: Version-controlled transformations

## 🛠️ Pipeline Architecture  

### Core Components
| Component               | Purpose                                                                      |
|-------------------------|------------------------------------------------------------------------------|
| **ETL Jobs**            | Orchestrates end-to-end pipeline execution                                   |
| **Requests**            | Fetches raw data from (San Francisco Open Data Rest APIs)[https://data.sfgov.org/] using Request Librart                                       |
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