# Credit Risk Data Pipeline

A local, end-to-end ETL pipeline that extracts, validates, transforms, and loads loan applicant data — built to demonstrate the kind of Python/SQL data pipeline work used in a regulated banking/rating environment.

## Why this project exists

This project demonstrates skills relevant to data engineering roles in banking/risk-analytics contexts: Python pipeline development, SQL, data quality checks and monitoring, workflow orchestration, testing, and CI/CD — using a public credit-risk dataset instead of confidential banking data.

## Dataset

[German Credit Risk dataset](https://www.kaggle.com/datasets/uciml/german-credit) (Statlog/UCI) — 1,000 loan applicants with features like age, job, housing status, savings/checking account status, credit amount, duration, and loan purpose.

Not committed to this repo (kept out of version control on purpose). To run the pipeline:
1. Download the dataset from the link above
2. Place `german_credit_data.csv` in the `data/` folder

## Pipeline stages

| Script | What it does |
|---|---|
| `extract.py` | Loads the raw CSV into a DataFrame |
| `quality_checks.py` | Validates data: missing values (a real, common issue in this dataset — ~39% of applicants have no recorded checking account), duplicate applicant records, and out-of-range credit amounts — logs pass/fail per check |
| `transform.py` | Feature engineering (estimated monthly payment = credit amount ÷ duration) and segment-level analysis, using **PySpark** — the same engine behind managed Spark/ETL services like AWS Glue or Databricks | 
| `load.py` | Writes results into a local SQL (SQLite) database |
| `orchestrator.py` | Runs all stages in order, logs each step, and continues with a warning if quality checks fail rather than hard-blocking — mirroring how a workflow orchestrator (e.g. Airflow, Step Functions) would sequence and monitor a real pipeline |

## Design decisions worth noting

- **Quality gate is a soft warning, not a hard block.** Real applicant data has genuine gaps (missing account info) — the pipeline flags them clearly and continues rather than halting entirely, reflecting how many real pipelines triage minor data quality issues rather than stopping everything.
- **PySpark, not just pandas, for transformation.** Managed ETL/Spark services in the cloud (AWS Glue, Databricks) run on Apache Spark — using PySpark here means the transform logic is genuinely transferable, not just an analogy.
- **No ground-truth risk label used.** This version of the dataset doesn't include a "good/bad credit" outcome column — so instead of just reading a label, the pipeline builds its own simple derived risk indicator (`MonthlyPayment`) and segment-level analysis, which is closer to the kind of feature-engineering work a rating/risk system actually requires.

## Tech stack

Python · pandas · PySpark · SQLAlchemy (SQLite) · pytest · GitHub Actions

## Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Download the dataset (see [Dataset](#dataset) above) into `data/german_credit_data.csv`.

## Running the pipeline

```bash
python orchestrator.py
```

Runs extract → quality checks → transform → load in sequence, logging each stage.

## Running tests

```bash
python -m pytest tests/ -v
```

## CI/CD

Every push to `main` automatically runs the test suite via GitHub Actions (`.github/workflows/ci.yml`) — install dependencies, run pytest, report pass/fail.

## Sample result

Average credit amount by loan purpose (from `get_credit_profile_by_purpose`):

| Purpose | Avg. credit amount (€) |
|---|---|
| vacation/others | 8,209 |
| business | 4,158 |
| car | 3,768 |
| furniture/equipment | 3,067 |
| education | 2,879 |
| repairs | 2,728 |
| radio/TV | 2,488 |
| domestic appliances | 1,498 |
