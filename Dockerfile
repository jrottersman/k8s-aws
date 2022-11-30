FROM python:3.11.0-alpine3.17

COPY index.py .
COPY requirements.txt .

EXPOSE 5000
RUN pip install -r requirements.txt
CMD flask --app index run --host=0.0.0.0
