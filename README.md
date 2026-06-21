# Distributed Machine Learning on Banking Data

End-to-End Distributed Data Engineering and Machine Learning System built using Apache Spark, PySpark, Hadoop, Hive, Spark ML, Spark Structured Streaming, and Local MapReduce Simulation for Large-Scale Banking Analytics.

---

# Project Overview

This project demonstrates how distributed computing and machine learning technologies can be used to process, analyze, and generate insights from large-scale banking datasets.

The system simulates a real-world distributed banking analytics environment capable of handling:

- Distributed data storage
- Batch analytics
- Real-time streaming analytics
- Distributed machine learning
- SQL-based distributed querying
- Parallel data processing

The project was implemented using:

- Apache Spark
- PySpark
- Hadoop HDFS
- Hive
- Spark ML
- Spark Structured Streaming
- Python
- Java

---

# Problem Statement

Traditional banking systems face several challenges when processing massive datasets:

- Scalability issues
- Real-time analytics limitations
- Distributed storage challenges
- High-volume transaction processing
- Complex analytical workloads
- Machine learning deployment difficulties

This project demonstrates how distributed systems solve these challenges using:

- Distributed storage (HDFS)
- Distributed computing (Spark)
- Distributed SQL analytics (Hive)
- Real-time streaming systems
- Distributed ML pipelines

---

# Dataset Information

Dataset Used:

```text
bank.csv
```

Dataset Size:

- Rows: 4521
- Columns: 17

Target Variable:

```text
y → Term Deposit Subscription (yes/no)
```

Dataset Features:

| Feature | Description |
|---|---|
| age | Customer age |
| job | Job type |
| marital | Marital status |
| education | Education level |
| default | Credit default status |
| balance | Account balance |
| housing | Housing loan status |
| loan | Personal loan status |
| contact | Contact communication type |
| day | Last contact day |
| month | Last contact month |
| duration | Call duration |
| campaign | Number of campaign contacts |
| pdays | Days since previous contact |
| previous | Previous contacts |
| poutcome | Previous campaign outcome |
| y | Deposit subscription |

---

# System Architecture

```text
Raw Banking Data
        ↓
HDFS Storage Layer
        ↓
Spark Batch Processing
        ↓
Spark ML Pipeline
        ↓
Spark Structured Streaming
        ↓
Hive SQL Analytics
        ↓
Business Insights & Predictions
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Hadoop HDFS | Distributed Storage |
| Apache Spark | Distributed Processing |
| PySpark | Python-based Spark Analytics |
| Spark ML | Machine Learning |
| Spark Structured Streaming | Real-Time Analytics |
| Hive | Distributed SQL Querying |
| Python | Programming Language |
| Java 8 | Hadoop/Spark Runtime |
| Jupyter Notebook | Development Environment |

---

# Project Workflow

1. Environment Setup
2. Hadoop and HDFS Configuration
3. Spark Session Initialization
4. Dataset Loading
5. Exploratory Data Analysis
6. Data Parallelism Analysis
7. Spark SQL Analytics
8. Feature Engineering
9. Distributed ML Pipeline
10. Logistic Regression Training
11. AUC Evaluation
12. Spark Structured Streaming
13. Window Operations & Watermarking
14. Local MapReduce Simulation
15. Hive Analytics
16. Final Validation

---

# Project Structure

```text
Financial-Forecasting-Distributed-ML/
│
├── data/
│   ├── raw/
│   │   └── bank.csv
│   │
│   └── processed/
│
├── models/
│   └── bank_model/
│
├── streaming_data/
│   ├── input/
│   ├── output/
│   └── checkpoint/
│
├── hadoop_jobs/
│   ├── mapper.py
│   ├── reducer.py
│   ├── mapper2.py
│   ├── reducer2.py
│   ├── mapper3.py
│   └── reducer3.py
│
├── screenshots/
│
├── Financial_Forecasting_Frontier_Distributed_ML_Final.ipynb
│
├── README.md
│
└── Technical_Documentation.docx
```

---

# Spark and PySpark Analytics

## Exploratory Data Analysis

EDA tasks performed:

- Dataset inspection
- Schema analysis
- Missing value checks
- Duplicate checks
- Aggregations
- Spark SQL analytics
- Feature engineering
- Visualizations

### Key Insights

- Most customers did not subscribe to term deposits.
- Management and technician jobs showed higher average balances.
- Call duration strongly influenced subscription likelihood.
- Education level impacted campaign success rates.

---

# Data Parallelism

The dataset was repartitioned to improve distributed execution efficiency.

Implemented Concepts:

- Dataset partitioning
- Distributed aggregations
- Parallel transformations
- Task scheduling
- Spark execution optimization

Example:

```python
partitioned_df = df.repartition(4)
```

---

# Spark SQL Analytics

Implemented SQL-based distributed analytics using Spark SQL.

Example Query:

```sql
SELECT
job,
AVG(balance) AS avg_balance
FROM bank
GROUP BY job
ORDER BY avg_balance DESC
```

---

# Machine Learning Pipeline

A distributed ML pipeline was implemented using Spark ML.

## Pipeline Components

- StringIndexer
- OneHotEncoder
- VectorAssembler
- Logistic Regression
- BinaryClassificationEvaluator

## Model Used

```text
Logistic Regression
```

## Evaluation Metrics

- AUC Score
- Prediction Accuracy

## ML Pipeline Workflow

```text
Raw Features
      ↓
Categorical Encoding
      ↓
Feature Vector Assembly
      ↓
Logistic Regression
      ↓
Predictions
      ↓
AUC Evaluation
```

---

# Real-Time Streaming Analytics

Spark Structured Streaming was implemented using file-based streaming simulation.

## Features Implemented

- Real-time aggregation
- Streaming predictions
- Window operations
- Watermarking
- Checkpointing
- Trend analysis

## Streaming Workflow

```text
Streaming CSV Files
        ↓
Structured Streaming
        ↓
Window Aggregations
        ↓
Real-Time Predictions
        ↓
Console Output
```

---

# Hadoop MapReduce Simulation

Due to Hadoop Streaming limitations on Windows, local MapReduce simulation was implemented using Python mapper and reducer scripts.

Implemented Tasks:

- Average balance by job type
- Housing loan count by education
- Monthly contact analytics

MapReduce Flow:

```text
Input Data
    ↓
Mapper
    ↓
Shuffle & Sort
    ↓
Reducer
    ↓
Output
```

---

# Hive Analytics

HiveQL queries were executed for distributed SQL analytics.

## Queries Performed

- Total customer count
- Average age by job
- Average balance by job
- Subscription analysis
- Contact month trends
- Poutcome impact analysis
- Education vs default analysis

Example Query:

```sql
SELECT
job,
AVG(balance)
FROM client_info
GROUP BY job;
```

---

# Model Evaluation

The Logistic Regression model was evaluated using:

- Area Under ROC Curve (AUC)
- Prediction Accuracy

The model successfully predicted customer subscription behaviour for banking marketing campaigns.

---

# Business Impact

This project demonstrates how distributed analytics systems help banks perform:

- Customer segmentation
- Marketing optimization
- Risk analysis
- Real-time monitoring
- Predictive analytics
- Scalable distributed computation

---

# Future Improvements

Possible production-level improvements:

- Apache Kafka Integration
- Cloud Deployment
- Kubernetes Orchestration
- Spark on Cloud Clusters
- MLOps Pipeline
- Feature Store
- Model Registry
- Real-Time Dashboards
- CI/CD Automation
- Lakehouse Architecture

---

# Screenshots Included

The project documentation includes screenshots for:

- HDFS Running
- JPS Output
- Spark Session
- Dataset Schema
- Partition Analysis
- Visualizations
- ML Predictions
- AUC Score
- Streaming Output
- Watermark Analytics
- MapReduce Output
- Hive Queries
- Final Validation

---

# Final Validation

The project successfully demonstrated:

✅ Distributed Data Processing  
✅ Data Parallelism  
✅ Distributed Machine Learning  
✅ Real-Time Streaming Analytics  
✅ Distributed SQL Querying  
✅ Hadoop and Hive Integration  
✅ Spark ML Pipeline  
✅ Window Operations and Watermarking  

---

# Author

Akshat Mishra

---

# License

This project is intended for academic, learning, portfolio, and demonstration purposes.
