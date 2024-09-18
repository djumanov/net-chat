import asyncio
import websockets
from .database import init_db
from .handlers import handle_client

# WebSocket serverni ishga tushirish
async def main():
    # Ma'lumotlar bazasi bilan bog'lanish
    db_conn = await init_db()

    # WebSocket serverni boshlash
    async with websockets.serve(lambda ws, path: handle_client(ws, db_conn), "localhost", 8765):
        await asyncio.Future()  # Serverni doimiy ishlashini ta'minlaydi

if __name__ == "__main__":
    asyncio.run(main())
