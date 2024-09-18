import asyncpg
from .config import DATABASE

# Ma'lumotlar bazasi bilan ulanishni boshlash
async def init_db():
    return await asyncpg.connect(
        user=DATABASE['user'],
        password=DATABASE['password'],
        database=DATABASE['database'],
        host=DATABASE['host']
    )

# Foydalanuvchini bazaga qo'shish
async def add_user(db_conn, user_id, name):
    await db_conn.execute('''
        INSERT INTO users(id, name, status) 
        VALUES($1, $2, 'online') ON CONFLICT (id) DO UPDATE SET status = 'online';
    ''', user_id, name)

# Foydalanuvchi holatini offline qilish
async def set_user_offline(db_conn, user_id):
    await db_conn.execute('''
        UPDATE users SET status = 'offline' WHERE id = $1;
    ''', user_id)

# Xabarni bazaga saqlash
async def save_message(db_conn, sender_id, receiver_id, message):
    await db_conn.execute('''
        INSERT INTO messages(sender_id, receiver_id, message, timestamp) 
        VALUES($1, $2, $3, NOW())
    ''', sender_id, receiver_id, message)
