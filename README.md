# Astro + DuckDB + dbt Pipeline

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

Think of it as a **playground for modern data engineering practices**—but fully functional enough to be production-ready.

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

## ⚡ Features

- Modular **Airflow DAGs** for ETL orchestration
- dbt project structured with **staging + marts**
- Seed data included for quick experimentation
- Dockerized environment for **zero hassle setup**
- Full **tests** for DAGs and transformations

---

## 📂 Project Structure
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
---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/shahidmalik4/astro_duckdb_dbt_pipeline.git
cd astro_duckdb_dbt_pipeline
```

2. **Set up the Python environment**
```
python -m venv .env
source .env/bin/activate   # or .env\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Run Airflow**
```
astro dev start
```

