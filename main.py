from fastapi import FastAPI

from api.routers import router

from brokers.rabbit_broker import broker
from brokers.tasks import send_task


import ddtrace
from ddtrace import config, patch_all

# Настройка Datadog
config.service = "my-fastapi-service"
config.env = "development"
patch_all()


app = FastAPI(title="FastAPI & Kafka (KRaft)")
# Подключение маршрутов FastAPI
app.include_router(router)

# Подключение FastStream к FastAPI
@app.on_event("startup")
async def startup_event():
    await broker.start()
    await send_task("Hi")

@app.on_event("shutdown")
async def shutdown_event():
    await broker.close()
