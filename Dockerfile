FROM python:3.9-slim-buster

WORKDIR /app

COPY . .    
Expose '5000'

RUN pip install -r requirements.txt

RUN python customerchurnprediction.py

ENTRYPOINT mlflow ui --host="0.0.0.0" --port="5000"

