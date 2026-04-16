# Marketplace Analytics System

## Project Overview

This project provides both data collection and analytics capabilities:

- Marketplace data ingestion (scraping)
- Data aggregation and analytics platform

It also exposes web API endpoints for accessing the processed data.

---

## API

### Overview

The service exposes a REST API for accessing marketplace data, analytics, and aggregated metrics.

All endpoints are served via **FastAPI** and follow standard HTTP semantics.

### Base URL

```
http://localhost:8080
```

### Interactive API Documentation

Once the server is running, you can explore the API via Swagger UI:

```
http://localhost:8080/docs
```

### Endpoints


#### Get Wildberries product data

```http
GET /api/wb/{product_id}
```

Returns detailed information about a specific product from Wildberries marketplace.

**Path parameters:**

* `wb_product_id` — unique Wildberries product identifier

**Response:**

```json
{
  "nm_id": 122268164,
  "name": "Светильник-ночник Майнкрафт Пчела",
  "basic_kop": 251000,
  "product_kop": 82500,
  "basic_rub": 2510.0,
  "product_rub": 825.0
}
```

### Error Handling

The API uses standard HTTP status codes:

* `200 OK` — successful request
* `422 Unprocessable Entity` — invalid `product_id` or request validation error
* `404 Not Found` — resource not found
* `500 Internal Server Error` — unexpected error

**Error response format:**

```json
{
  "detail": "Error description"
}
```
---

## Project Structure

```
project/
│
├── app/
│   ├── main.py                    # FastAPI application entry point + routers
│   ├── clients/
│   │   ├── base.py                # Abstract base client
│   │   └── wildberries.py         # Wildberries client
│   ├── routers/                   # API endpoints
│   └── core/
│       └── config.py              # Application configuration
├── tests/                         # Tests directory
│   ├── unit/                      # Unit tests
│   └── integration/               # Integration tests
├── Dockerfile                     # Instructions for building a Docker image
├── docker-compose.yaml            # Multi-container Docker setup
├── poetry.lock                    # Poetry dependency lock file
├── pyproject.toml                 # Main project configuration (Poetry, tooling, metadata)
├── .flake8                        # Flake8 linter configuration
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── .gitignore                     # Git ignored files
└── README.md                      # Project documentation
```

---

## Installation and Setup

### Prerequisites

* Python 3.13
* Poetry (can be installed via `pip`)

---

### 1. Clone the repository

```bash
git clone https://github.com/bezhanov/marketplace-analytics.git
cd marketplace-analytics
```

---

### 2. Configure Poetry to create a virtual environment inside the project

```bash
poetry config virtualenvs.in-project true
```

---

### 3. Create a virtual environment and install dependencies

```bash
poetry install
```

---

## Running the Application

### Run the server locally

```bash
poetry run python -m app.main
```

---

### Build and run Docker containers

```bash
docker compose up
```

---

### Stop and remove Docker containers

```bash
docker compose down
```

---

## Code Quality

### Run formatter

```bash
poetry run black .
```

### Run linter

```bash
poetry run flake8 .
```