from contextlib import asynccontextmanager
from fastapi import FastAPI
from faststream.rabbit import RabbitQueue

from api.routers import router
from brokers.rabbit_broker import broker, task_topic


# Определяем жизненный цикл приложения с помощью декоратора @asynccontextmanager
# Этот метод позволяет управлять ресурсами, которые нужно запускать и закрывать с приложением
@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await broker.start()  # Запуск Kafka брокера при старте приложения
    await broker.declare_queue(task_topic)
    # scheduler.start()  # Запуск планировщика задач
    yield
    await broker.close()  # Закрытие Kafka брокера при остановке приложения
    # scheduler.shutdown()  # Завершение работы планировщика задач


app = FastAPI(title="FastAPI & Rabbit", lifespan=lifespan)
app.include_router(router)
