from brokers.rabbit_broker import broker

# Обработка задачи (subscriber)
@broker.subscriber("task-topic")
async def process_task(message: str):
    print(f"Processing task: {message} ✅")
    return {"message": message}

# Отправка задачи (publisher)
async def send_task(message: str):
    print(f"Sending task: {message}")
    await broker.publish(message, queue="task-topic")
