from faststream.rabbit import RabbitBroker, RabbitQueue

# Настройка Kafka с использованием KRaft
broker = RabbitBroker("amqp://guest:guest@localhost:5672/")

task_topic = RabbitQueue("task-topic", durable=True)
