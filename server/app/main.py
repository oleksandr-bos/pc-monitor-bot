import logging

from fastapi import FastAPI

from app.routers import metrics

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",

)

app = FastAPI()

app.include_router(metrics.router)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "PC Monitor Bot server is alive"}