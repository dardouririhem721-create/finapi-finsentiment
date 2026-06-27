![CI](https://github.com/dardouririhem721-create/finapi-finsentiment/actions/workflows/ci.yml/badge.svg)

# FinAPI — Financial Sentiment Analysis Engine

> **Python · Flask · FinBERT · SQLite · Streamlit · Hugging Face Transformers**

A production-ready REST API that fetches real-time stock prices and financial news,
stores them in a SQLite database, enriches them with AI-powered sentiment analysis
using FinBERT, and displays everything in an interactive Streamlit dashboard.

---

## Author

**Rihem Dardouri**
Master en Économie et Finance Quantitatives
École Polytechnique de Tunisie

---

## Project Roadmap

| Lab | Theme | Technologies | Status |
|-----|-------|-------------|--------|
| Lab 1 | REST API — Real-time stock prices | Flask · yfinance | ✅ Done |
| Lab 2 | ETL Pipeline — Data storage | SQLAlchemy · SQLite | ✅ Done |
| Lab 3 | NLP — Financial sentiment analysis | FinBERT · Transformers | ✅ Done |
| Lab 4 | Dashboard — Interactive UI | Streamlit · Plotly | ✅ Done |
| Lab 5 | Versioning, Tests & CI/CD | Git · pytest · Ruff · GitHub Actions | ✅ Done |

---

## Installation

git clone https://github.com/dardouririhem721-create/finapi-finsentiment
cd finapi-finsentiment
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
pip install -e .

---

## Quick Start

1 — Ingest prices and news
python scripts/run_etl.py AAPL MSFT GOOGL

2 — Enrich news with FinBERT sentiment
python scripts/enrich_sentiment.py

3 — Launch the API server
python -m finapi.app

Server runs at http://localhost:5000

---

## Launch the Dashboard (Lab 4)

The Streamlit dashboard consumes the Flask API — launch both :

Terminal 1 — API
python -m finapi.app

Terminal 2 — Dashboard
streamlit run dashboard/app.py

Then open http://localhost:8501

![dashboard](docs/screenshots/dashboard.png)

---

## Tests & CI (Lab 5)

Run tests locally :
pytest -v

Run tests with coverage :
pytest --cov=finapi --cov-report=term-missing

Lint with Ruff :
ruff check .

The CI pipeline runs automatically on every push to main via GitHub Actions.

---

## 📡 API Endpoints

### Lab 1 — Real-time Market Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Server health check |
| GET | /price/<ticker> | Latest closing price |
| GET | /history/<ticker>?days=N | Price history (1–365 days) |

### Lab 2 — Database

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /db/prices/<ticker> | Stored prices from SQLite |
| GET | /db/news/<ticker> | Stored news from SQLite |
| GET | /db/stats | Global database statistics |

### Lab 3 — FinBERT Sentiment Analysis

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /sentiment | Analyze sentiment of a single text |
| POST | /sentiment/batch | Analyze up to 100 texts at once |
| GET | /db/sentiment-summary/<ticker> | Sentiment distribution for a ticker |

---

## Usage Examples

Health check
curl http://localhost:5000/health

Latest price AAPL
curl http://localhost:5000/price/AAPL

Price history 5 days MSFT
curl "http://localhost:5000/history/MSFT?days=5"

Stored prices
curl http://localhost:5000/db/prices/AAPL

Stored news
curl http://localhost:5000/db/news/AAPL

Sentiment analysis single text
curl -X POST http://localhost:5000/sentiment -H "Content-Type: application/json" -d "{\"text\": \"Apple stock soared after earnings beat expectations.\"}"

Sentiment analysis batch
curl -X POST http://localhost:5000/sentiment/batch -H "Content-Type: application/json" -d "{\"texts\": [\"Apple stock soared after blockbuster earnings\", \"Tesla missed estimates, shares plunge\", \"The Fed kept interest rates unchanged\"]}"

Sentiment summary AAPL
curl http://localhost:5000/db/sentiment-summary/AAPL

---

## Database Migration

python -c "from finapi.db import init_db; init_db()"
python scripts/run_etl.py AAPL MSFT GOOGL
python scripts/enrich_sentiment.py

---

## Project Structure

finapi-finsentiment/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── finapi/
│   ├── __init__.py
│   ├── app.py
│   ├── prices.py
│   ├── db.py
│   ├── models.py
│   ├── sentiment.py
│   └── etl/
│       ├── __init__.py
│       ├── prices_etl.py
│       └── news_etl.py
│
├── dashboard/
│   ├── __init__.py
│   ├── app.py
│   ├── api_client.py
│   └── charts.py
│
├── scripts/
│   ├── run_etl.py
│   └── enrich_sentiment.py
│
├── docs/
│   └── screenshots/
│       └── dashboard.png
│
├── data/
│   └── finapi.db
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_app_health.py
│   ├── test_history_validation.py
│   └── test_sentiment.py
│
├── pyproject.toml
├── requirements.txt
├── requirements-ci.txt
└── README.md

---

## About FinBERT

FinBERT is a BERT model fine-tuned on financial corpora (analyst reports, Reuters, Bloomberg).
It classifies text into positive, neutral, or negative sentiment with high accuracy
on financial jargon such as "beat estimates", "guidance raised", or "missed targets".

---
