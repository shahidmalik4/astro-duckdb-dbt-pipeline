# Astro + DuckDB + dbt Pipeline 🚀

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/airflow-2.x-orange)](https://airflow.apache.org/)
[![dbt](https://img.shields.io/badge/dbt-1.x-red)](https://www.getdbt.com/)
[![DuckDB](https://img.shields.io/badge/duckdb-0.8-green)](https://duckdb.org/)

---

## 📊 Project Overview

This repository is an **end-to-end analytics pipeline** built on the **modern data stack**, designed using the **Jaffle Shop dataset**. It demonstrates how to:

- Orchestrate workflows with **Astro/Airflow**
- Transform data with **dbt**
- Query and store data using **DuckDB** (and Postgres for optional storage)
- Use **modular, production-ready analytics patterns**

Think of it as a **playground for modern data engineering practices**—but fully functional enough to be production-ready. 😎

---

## 🛠 Tech Stack

| Component       | Purpose                                   |
|-----------------|-------------------------------------------|
| Astro/Airflow   | Workflow orchestration & scheduling       |
| dbt             | Data modeling & transformations           |
| DuckDB          | Lightweight analytical database           |
| Postgres        | Optional production database              |
| Docker          | Containerization for reproducibility      |

---

## 🛠 Tech Stack

| Component       | Role / Purpose                                   | Logo |
|-----------------|-------------------------------------------------|------|
| **Astro / Airflow** | Workflow orchestration & scheduling           | ![Airflow](https://img.shields.io/badge/Airflow-2.x-orange) |
| **dbt**         | Data modeling, transformations & testing        | ![dbt](https://img.shields.io/badge/dbt-1.x-red) |
| **DuckDB**      | Lightweight analytical database for analytics   | ![DuckDB](https://img.shields.io/badge/DuckDB-0.8-green) |
| **Postgres**    | Optional production-grade database               | ![Postgres](https://img.shields.io/badge/Postgres-15-blue) |
| **Python**      | Programming language for DAGs & dbt             | ![Python](https://img.shields.io/badge/python-3.11-blue) |
| **Docker**      | Containerization for reproducibility & deployment | ![Docker](https://img.shields.io/badge/Docker-20-blue) |
| **pytest**      | Testing Airflow DAGs and dbt transformations    | ![pytest](https://img.shields.io/badge/pytest-7-purple) |

---


## ⚡ Features

- Modular **Airflow DAGs** for ETL orchestration
- dbt project structured with **staging + marts**
- Seed data included for quick experimentation
- Dockerized environment for **zero hassle setup**
- Full **tests** for DAGs and transformations

---

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/astro_duckdb_dbt_pipeline.git
cd astro_duckdb_dbt_pipeline
```

1. **Clone the repository**
```
python -m venv .env
source .env/bin/activate   # or .env\Scripts\activate on Windows
pip install -r requirements.txt
```

1. **Clone the repository**
```
astro dev start
```

1. **Clone the repository**
```
cd dbt/jaffle_shop_duckdb
dbt run
dbt test
```

1. **Clone the repository**
```
```

1. **Clone the repository**
```
├── dags/                 # Airflow DAGs
├── dbt/                  # dbt project
│   └── jaffle_shop_duckdb
├── include/              # DuckDB files
├── tests/                # Unit & integration tests
├── Dockerfile
├── docker-compose.yml
├── airflow_settings.yaml
└── README.md
```

