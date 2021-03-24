import requests
import random
import pandas as pd

url = 'http://localhost:8000/prediction'

X_test = pd.read_csv('jupyter/test.csv')


def predict(feature_vector):
    score = random.randrange(10) < 3
    response = requests.post(url, json={
      'feature_vector': [feature_vector['mean'], feature_vector['sd']],
      'score': score
    })
    print(response.text)

print(X_test.describe())
X_test.apply(predict, axis=1)