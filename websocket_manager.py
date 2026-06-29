from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.channels: dict[str, list[WebSocket]] = defaultdict(list)

    async def connect(self, ws: WebSocket, channel: str):
        await ws.accept()
        self.channels[channel].append(ws)

    def disconnect(self, ws: WebSocket, channel: str):
        self.channels[channel].remove(ws)

    async def broadcast(self, channel: str, data: dict):
        for ws in self.channels[channel]:
            await ws.send_json(data)
