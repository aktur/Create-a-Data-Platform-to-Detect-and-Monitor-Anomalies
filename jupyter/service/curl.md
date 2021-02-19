```bash
curl -X POST http://127.0.0.1:8000/prediction -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"feature_vector":[67.99, 10],"score":true}'
curl -X POST http://127.0.0.1:8000/prediction -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"feature_vector":[7.99, 10],"score":false}'
curl -X GET "http://127.0.0.1:8000/model_information"
```
