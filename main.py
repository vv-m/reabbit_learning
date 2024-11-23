from fastapi import FastAPI

from api.routers import router

from brokers.rabbit_broker import broker


app = FastAPI(title="FastAPI & Kafka (KRaft)")
# Подключение маршрутов FastAPI
app.include_router(router)


# Подключение FastStream к FastAPI
@app.on_event("startup")
async def startup_event():
    await broker.start()


@app.on_event("shutdown")
async def shutdown_event():
    await broker.close()
