FROM python:3.7-slim

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY model.joblib /
COPY main.py /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
