from faststream.rabbit import RabbitBroker

# Настройка Kafka с использованием KRaft
broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
