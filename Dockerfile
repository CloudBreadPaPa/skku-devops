FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10 

COPY ./src /app
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt
