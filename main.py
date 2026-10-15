
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Credit Default Risk Prediction API",
    description="Experimental ML prediction service",
    version="1.0.0"
)

# Load the trained model
model = joblib.load("model.joblib")
feature_names = list(model.feature_names_in_)

class ModelInput(BaseModel):
    features: list[float] = Field(min_length=23, max_length=23)

@app.get("/")
def home():
    return {
        "message": "Credit Default Risk API is running",
        "model": "RandomForestClassifier"
    }

@app.post("/predict")
def predict(data: ModelInput):
    values = pd.DataFrame(
        [data.features],
        columns=feature_names
    )

    prediction = int(model.predict(values)[0])
    probabilities = model.predict_proba(values)[0]
    classes = list(model.named_steps["classifier"].classes_)

    default_probability = (
        float(probabilities[classes.index(1)])
        if 1 in classes else 0.0
    )

    return {
        "model": "RandomForestClassifier",
        "prediction": prediction,
        "default_probability": round(default_probability, 4),
        "note": "Experimental model; not for real lending decisions."
    }
