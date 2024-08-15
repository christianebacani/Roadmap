# Roadmap

Welcome to my Roadmap repository! This repository contains a comprehensive collection of my projects as I progress through my learning journey in data engineering. Each folder represents a specific area of study and includes various types of projects, such as mini-projects, guided projects, hobby projects, and industry projects. This roadmap showcases my development and serves as a portfolio to demonstrate my skills and growth.

## Table of Contents
1. [Overview](#overview)
2. [Roadmap Files](#roadmap-files)
   - [Understanding Data Engineering](#understanding-data-engineering)
   - [Introduction to SQL](#introduction-to-sql)
   - [Intermediate SQL](#intermediate-sql)
   - [Joining Data in SQL](#joining-data-in-sql)
3. [Contact](#contact)
4. [Conclusion](#conclusion)

## Overview

This repository is structured to reflect my learning path in data engineering. The projects within each file showcase practical applications of the concepts I have learned. By organizing my projects in this manner, I aim to provide a clear and structured overview of my skills and capabilities.

## Roadmap Files

### Understanding Data Engineering

The `Understanding Data Engineering.md` file compiles key theoretical concepts and definitions that I learned from the DataCamp "Understanding Data Engineering" course. This file serves as a reference guide for important topics and terminologies in data engineering.

#### Key Concepts Covered

- **Airflow**: An open-source workflow management platform used to schedule data engineering tasks.
- **AWS (Amazon Web Services)**: Amazon's cloud computing services.
- **Azure**: Microsoft's cloud services.
- **Big Data**: The systematic storage, management, and analysis of datasets that are too large or complex for traditional data-processing applications. Key characteristics include volume, variety, velocity, veracity, and value.
- **Cloud Computing**: The use of a network of remote servers hosted on the internet to store, manage, and process data.
- **Database Schema**: The structure that represents the logical view of the entire database, including how data is organized and the relations among them.
- **Data Catalog**: A metadata management tool used to inventory and organize data within a system.
- **Data Engineering**: The process of transforming data into a format suited for analysis.
- **Data Ingestion**: The process of obtaining and importing data for immediate use or storage in a database.
- **Data Lake**: A repository of data stored in its natural/raw format.
- **Data Pipelines**: A series of data processing steps used by data engineers to process and move data.
- **Data Processing**: The collection and manipulation of data to produce meaningful information.
- **Data Science**: The process of extracting knowledge from data.
- **Data Warehouse**: A central repository of integrated data from one or more disparate sources.
- **ETL (Extract, Transform, Load)**: The process of pulling data from one database to move it to another.
- **Google Cloud**: Google's cloud services.
- **Luigi**: An open-source workflow management platform used to schedule data engineering tasks.
- **NoSQL**: A database mechanism for storing structured, semi-structured, and unstructured data that is modeled differently than in relational databases.
- **Parallel Computing/Processing**: The simultaneous use of multiple compute resources to solve a computational problem.
- **Query**: A request for information from a database.
- **Redshift**: Amazon's data warehouse service.
- **S3**: Amazon's object storage service.
- **Scheduling**: Organizing how tasks work together by running jobs in a specific order and resolving dependencies.
- **Structured Data**: Data organized into a formatted repository, typically a database.
- **Unstructured Data**: Information that does not have a pre-defined data model or organization.
- **Semi-Structured Data**: A mix of both structured and unstructured data, often stored in JSON, XML, or YAML formats.
- **View**: Output of a stored, frequent query on the data.

### Introduction to SQL

The `Stored Procedure.sql` and `Student Tables and Views.sql` files contain projects I created while learning Introduction to SQL. These are simple mini-projects that demonstrate concepts learned during the course, focusing on:

- **Stored Procedures**: Demonstrated in the `Stored Procedure.sql` file.
- **Creating Views in SQL**: Showcased in the `Student Tables and Views.sql` file.

### Intermediate SQL

The Intermediate SQL section includes five mini-projects and one guided project, each demonstrating the application of different SQL concepts and techniques learned in the DataCamp "Intermediate SQL" course.

1. **Analyzing Student's Mental Health (Guided Project in DataCamp).sql**
   
   This guided project is my first guided project in DataCamp (excluding the Introduction to Notebook Projects). This guided project taught me how to use notebooks properly and implement practical SQL skills. It includes concepts like `GROUP BY`, `WHERE`, `AVG`, `ROUND`, `ORDER BY`, `COUNT`, and `LIMIT`. These skills are essential for complex queries of SQL tables that I can use in my future projects. I have also committed the necessary dataset `students.csv` used in this guided project to the repository.

2. **Analyze International Debt's Statistics (Guided Project in DataCamp).sql**
   
   This guided project is my second project on DataCamp, where I used DataCamp Notebook and PostgreSQL. This project gradually built my confidence in creating projects related to my dream job. I learned to use various practical SQL skills such as `COUNT`, `DISTINCT`, `GROUP BY`, `SUM`, `ORDER BY`, `LIMIT`, `MIN`, and `WHERE`. This project ensures that I am continuously and steadily building a strong foundation to hopefully become a great Data Engineer someday!

3. **Exploring London`s Travel Network (Guided Project in DataCamp).sql**

   This guided project is my second project on DataCamp focusing on aggregate functions like `SUM` in `GROUP BY` keyword, sorted it `ORDER BY` into `DESC` or `ASC`. I also used filter keywords for a specific data fields `WHERE` and I used also `LIMIT` to limit the specific queries into 5 rows.

4. **Aggregation Functions, Order by, Group by, Round.sql**
   
   This project demonstrates the use of aggregation functions such as `SUM`, `AVG`, and `COUNT`, along with the `GROUP BY` clause to organize data into summary rows. It also demonstrates how to use `ORDER BY` to sort query results and the `ROUND` function to format numerical outputs.

5. **Comparison Operators, Arithmetic Operations, Having.sql**
   
   This project illustrates the application of comparison operators (e.g., `=`, `!=`, `>`, `<`), arithmetic operations (e.g., `+`, `-`, `*`, `/`), and the `HAVING` clause to filter grouped data based on aggregate conditions.

6. **Count with Order By and Limit.sql**
   
   This project shows how to use the `COUNT` function to count records and combine it with `ORDER BY` to sort the results, and `LIMIT` to restrict the number of rows returned.

7. **Distinct, Like, Not like, Is not null.sql**
   
   This project covers the use of `DISTINCT` to remove duplicate rows, pattern matching with `LIKE` and `NOT LIKE`, and checking for non-null values using `IS NOT NULL`.

8. **Where Clause with Between, And, Or.sql**
    
   This project focuses on using the `WHERE` clause with the `BETWEEN`, `AND`, and `OR` operators to filter data based on complex conditions. It includes examples of querying data within a specific range and combining multiple conditions to refine results.

### Joining Data in SQL

1. **Inner Join, Using.sql**, **Multiple Inner Joins with AND keyword.sql**, **One-to-one relationships in SQL.sql**, **One-to-Many Relationships in SQL.sql**, **Many-to-Many Relationships in SQL.sql**
   
   I created projects here demonstrating the practical concepts of `Inner Joins / Multiple Inner Joins / Relationship Schemas`. You can just download and export the script to your local environment to run the query.

3. **Left Join in SQL.sql**, **Right Join in SQL.sql**, **Full Join (Alternative using UNION) in MySQL.sql**, **Cross Join using Enum in MySQL.sql**, **Self Join in MySQL using AND.sql**
   
   Built multiple projects so that I can improved my skills in the concept of `Outer Joins, Cross Joins and Self Joins`

5. **Set Theory using Union ALL.sql**, **Multiple Intersect in Set Theory.sql**, **Except in Set Theory.sql**
   
   Learning and built projects from the concepts of `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT` in `Set Theory`.

6. **Subquery (Anti Joins).sql**, **Subquery (Semi Joins)**, **Subquery using Select Keyword.sql**, **Subquery using Where Keyword.sql**, **Subquery using Multiple From Clause and Where Keyword**

   I built a project using `Semi Joins` and `Anti Joins` in `Subquery`. You can export this script and run it into your Integrated Development Environment. I also built projects related to `Subquery` using `WHERE` keyword, `SELECT` keyword, `FROM` keyword and compare it to a traditional joins.   

## Contact

Feel free to reach out to me if you have any questions or would like to collaborate on a project. You can contact me through:

- **Email**: [christianbacani581@gmail.com](mailto:christianbacani581@gmail.com)
- **LinkedIn**: [Christian Bacani](https://www.linkedin.com/in/christianebacani/)
- **Portfolio**: [Christian Bacani on DataCamp](https://www.datacamp.com/portfolio/bioy7bp5)

## Conclusion

This repository not only tracks my progress but also serves as a portfolio to demonstrate my skills and knowledge in data engineering. Each file and project is a step towards mastering data engineering and achieving my career goals.
