# Credit Default Risk Prediction API

An experimental Machine Learning project that predicts credit default risk using a Random Forest classifier and FastAPI.

## Features
- Trained Random Forest model
- REST API built with FastAPI
- Prediction probability in the API response
- Input validation using Pydantic
- Automated tests using pytest
- Docker support

## Project Files
- `main.py` - FastAPI application
- `model.joblib` - Trained ML model
- `test_api.py` - Automated tests
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration

## Dataset
UCI Default of Credit Card Clients dataset, containing historical credit-card customer records.

## Run Locally
Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs` to test the endpoints.

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
This is an educational prototype, not a validated credit-scoring system. Model predictions should not be used for real lending decisions.
