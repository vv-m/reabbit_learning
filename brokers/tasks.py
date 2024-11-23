from trace import Trace

from brokers.rabbit_broker import broker, task_topic


# Обработка задачи (subscriber)
@broker.subscriber(task_topic)
async def process_task(message: str):
    print(f"Processing task: {message} ✅")
    return {"message": message}


# Отправка задачи (publisher)
async def send_task(message: str):
    print(f"Sending task: {message} ➡️")
    await broker.publish(message, queue="task-topic", persist=True)
