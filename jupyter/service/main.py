from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

import prometheus_client
from prometheus_client import Counter, Histogram
import time

app = FastAPI()
model = load("model.joblib")

metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

class Item(BaseModel):
    feature_vector: List[float]
    score: Optional[bool] = None

mi = Counter('model_information', 'Model counter')
pr = Counter('prediction', 'Prediction counter')
hi = Histogram('prediction_response', 'Prediction histogram')
sc = Histogram('score_response', 'Score histogram')
lt = Histogram('response_latency', 'Latency histogram')

@app.get("/model_information")
def read_root():
    mi.inc()
    return model.get_params()


@app.post("/prediction")
def predict(request: Item):
    pr.inc()
    response = {}

    # Call model.predict(...) and
    # add to response the returned prediction,
    # For example, response["is_inlier"] = int(prediction[0])
    start = time.time()
    prediction = model.predict([request.feature_vector])
    end = time.time()
    lt.observe(end-start)
    hi.observe(prediction)
    response = {"is_inlier": int(prediction[0])}

    # Check if request.score is True, also call model.score_samples
    # If it is, call model.score_samples(...) and add to
    # response the returned anomaly score.
    if request.score is True:
        score = model.score_samples([request.feature_vector])
        sc.observe(score)
        response["anomaly_score"] = score[0]

    return response
