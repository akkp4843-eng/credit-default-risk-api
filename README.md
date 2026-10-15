
# Credit Default Risk Prediction API

An experimental credit-default prediction API built with FastAPI and a trained Random Forest classifier.

## Features
- Machine learning predictions
- REST API with FastAPI
- Input validation
- Automated tests using pytest
- Docker support

## Project Structure
- `main.py` — API application
- `model.joblib.gz` — compressed trained model
- `test_api.py` — automated tests
- `requirements.txt` — dependencies
- `Dockerfile` — Docker configuration

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open `/docs` on your local server to test the API.

## Run Tests

```bash
pytest -v test_api.py
```

## Run with Docker

```bash
docker build -t credit-default-api .
docker run -p 8000:8000 credit-default-api
```

## Limitations

This is an educational prototype, not a validated credit-scoring system. Do not use its predictions for real lending decisions.



## Live Demo

- **API Base URL:** https://credit-default-risk-api.onrender.com
- **Interactive API Documentation:** https://credit-default-risk-api.onrender.com/docs
- **Prediction Endpoint:** `POST /predict`

## Note

The free hosting service may take around a minute to respond after a period of inactivity. This project is an educational prototype and should not be used for real lending decisions.


## System Architecture

1. Client sends a JSON request to the FastAPI `/predict` endpoint.
2. Pydantic validates the 23 numeric input features.
3. The API uses the trained Random Forest model to make a prediction.
4. The API returns the prediction and default probability as JSON.

**Technology Stack:** Python, FastAPI, Scikit-learn, Joblib, Docker, pytest, GitHub Actions and Render.
