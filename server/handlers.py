import json
from .database import add_user, save_message, set_user_offline
from .utils import format_message

# Ulashgan mijozlar ro'yxati
connected_clients = {}

# Foydalanuvchini ulash va xabarlarni boshqarish
async def handle_client(websocket, db_conn):
    try:
        # Foydalanuvchi ma'lumotlarini qabul qilish
        user_data = await websocket.recv()
        user_info = json.loads(user_data)
        user_id = user_info['user_id']
        name = user_info['name']

        # Foydalanuvchini ro'yxatga olish va bazaga qo'shish
        await add_user(db_conn, user_id, name)
        connected_clients[user_id] = websocket
        print(f"User {user_id} connected")

        # Mijozdan xabarlarni qabul qilish va ulash
        while True:
            message_data = await websocket.recv()
            message = json.loads(message_data)
            sender_id = message['sender_id']
            receiver_id = message['receiver_id']
            text = message['text']

            # Xabarni saqlash
            await save_message(db_conn, sender_id, receiver_id, text)

            # Qabul qiluvchi foydalanuvchi onlayn bo'lsa, unga xabar yuborish
            if receiver_id in connected_clients:
                receiver_ws = connected_clients[receiver_id]
                await receiver_ws.send(format_message(sender_id, text))
            else:
                print(f"User {receiver_id} is not connected")

    except Exception as e:
        print(f"User {user_id} disconnected: {e}")
        await set_user_offline(db_conn, user_id)
        if user_id in connected_clients:
            del connected_clients[user_id]
