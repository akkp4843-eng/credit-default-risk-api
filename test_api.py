
from fastapi.testclient import TestClient
from main import app
import joblib

client = TestClient(app)
model = joblib.load("model.joblib")

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["model"] == "RandomForestClassifier"

def test_prediction():
    # Model ke expected 23 features ke liye valid test input
    features = [0.0] * 23

    response = client.post(
        "/predict",
        json={"features": features}
    )

    assert response.status_code == 200
    result = response.json()
    assert result["prediction"] in [0, 1]
    assert 0 <= result["default_probability"] <= 1

def test_invalid_feature_count():
    response = client.post(
        "/predict",
        json={"features": [1, 2, 3]}
    )
    assert response.status_code == 422
