# Campaign Data Pipeline

A local, end-to-end ETL pipeline that extracts, validates, transforms, and loads marketing campaign data — built to mirror how a real AWS-based campaign analytics pipeline (Glue, Lambda, Step Functions) is structured, using free, local-equivalent tools.

## Why this project exists

This project was built to demonstrate the specific skills listed in a **Data Engineer — Campaign & Analytics** job posting (Python pipelines, SQL, data quality/monitoring, Git/CI-CD, and AWS Glue/Lambda/Step Functions/Spark), using a public dataset that mirrors a telecom/marketing campaign use case, without needing paid AWS resources.

## Dataset

[Kaggle "Marketing Campaign" dataset](https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign) — customer demographics and their response to past marketing campaigns.

Not committed to this repo (kept out of version control on purpose). To run the pipeline:
1. Download the dataset from the link above
2. Place `marketing_campaign.csv` in the `data/` folder

## Pipeline stages

Each script represents one stage, structured to map directly onto its AWS-managed equivalent:

| Script | What it does | AWS equivalent |
|---|---|---|
| `extract.py` | Loads the raw CSV into a DataFrame | Lambda (event-driven extraction) |
| `quality_checks.py` | Validates data: missing values, duplicates, out-of-range income — logs pass/fail per check | Glue Data Quality / monitoring & alerting |
| `transform.py` | Feature engineering (total spend, total campaigns accepted) and segment-level aggregation, using **PySpark** — the same engine Glue runs on under the hood | Glue ETL job |
| `load.py` | Writes results into a local SQL (SQLite) database | Data warehouse layer |
| `orchestrator.py` | Runs all stages in order, logs each step, and continues with a warning if quality checks fail rather than hard-blocking | Step Functions state machine |

## Design decisions worth noting

- **Quality gate is a soft warning, not a hard block.** The real dataset has genuine issues (missing income values, one outlier) — the pipeline flags them clearly and continues rather than halting entirely, a deliberate choice reflecting how many real pipelines treat minor data quality issues.
- **PySpark, not just pandas, for transformation.** AWS Glue ETL jobs run on Apache Spark — using PySpark here means the transform logic is genuinely transferable to a real Glue job, not just an analogy.
- **AWS services (Glue/Lambda/Step Functions) are simulated locally**, not deployed to real AWS, to keep this project free to build and run. The code is structured so each script maps cleanly onto its AWS equivalent if it were deployed.

## Tech stack

Python · pandas · PySpark · SQLAlchemy (SQLite) · pytest · GitHub Actions

## Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Download the dataset (see [Dataset](#dataset) above) into `data/marketing_campaign.csv`.

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

Campaign acceptance rate by education level (from `get_campaign_performance_by_segment`):

| Education | Avg. campaigns accepted |
|---|---|
| PhD | 33.7% |
| Graduation | 30.4% |
| Master | 27.8% |
| 2n Cycle | 25.1% |
| Basic | 11.1% |
