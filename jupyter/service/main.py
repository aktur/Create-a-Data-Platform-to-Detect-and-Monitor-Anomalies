from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load


app = FastAPI()
model = load("model.joblib")

class Item(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = None


@app.get("/model_information")
def read_root():
    return model.get_params()


@app.post("/prediction")
def predict(request: Item):
    response = {}

    # Call model.predict(...) and
    # add to response the returned prediction,
    # For example, response["is_inlier"] = int(prediction[0])
    prediction = model.predict([request.feature_vector])
    response = {"is_inlier": int(prediction[0])}

    # Check if request.score is True, also call model.score_samples
    # If it is, call model.score_samples(...) and add to
    # response the returned anomaly score.
    if request.score is True:
        score = model.score_samples([request.feature_vector])
        response["anomaly_score"] = score[0]

    return response
