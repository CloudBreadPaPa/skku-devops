# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}
