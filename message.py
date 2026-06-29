from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.websocket_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/{channel_id}/{user_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id: str, user_id: str):
    await manager.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_json()
            # Broadcast to everyone in the channel
            await manager.broadcast(channel_id, {
                "user_id": user_id,
                "message": data["message"],
                "timestamp": str(datetime.utcnow())
            })
    except WebSocketDisconnect:
        manager.disconnect(websocket, channel_id)
