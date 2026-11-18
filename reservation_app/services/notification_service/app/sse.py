from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import asyncio
router=APIRouter()
@router.get("/events/{user_id}")
async def stream():
    async def event_generator():
        while True:
            yield{"event":"ping","data":"keep alive"}
            await asyncio.sleep(15)
    return EventSourceResponse(event_generator())