from fastapi import APIRouter

from fastapi.responses import StreamingResponse
from swaplang.utils.events import event


router = APIRouter()


@router.get("/sse")
async def server_sent_events():
    return StreamingResponse(
        event.stream(),
        media_type="text/event-stream",
    )
