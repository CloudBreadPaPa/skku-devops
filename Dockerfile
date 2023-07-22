FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 

COPY ./src /app
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt