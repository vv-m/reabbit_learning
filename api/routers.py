from fastapi import APIRouter

from brokers.tasks import send_task

router = APIRouter()

@router.post("/tasks/")
async def create_task(message: str):
    """Отправляет задачу в Rabbit"""
    await send_task(message)
    return {"status": "Task sent", "message": message}