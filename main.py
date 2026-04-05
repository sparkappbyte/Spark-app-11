import asyncio, uvicorn, sqlite3
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен уже здесь
API_TOKEN = '8694731612:AAEAE9q6cg96CRS1kefQX_CUN_aJDfTB-Tc' 

app = FastAPI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def init_db():
    conn = sqlite3.connect('casino.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, balance REAL DEFAULT 1000)')
    conn.commit()
    conn.close()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/get_balance")
async def get_balance(user_id: int):
    conn = sqlite3.connect('casino.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    res = cursor.fetchone()
    conn.close()
    return {"balance": res[0] if res else 1000}

@app.post("/update_balance")
async def update_balance(request: Request):
    data = await request.json()
    conn = sqlite3.connect('casino.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance = balance + ? WHERE id = ?', (data['amount'], data['user_id']))
    conn.commit()
    conn.close()
    return {"status": "ok"}

@dp.message(Command("start"))
async def start(m: types.Message):
    init_db()
    conn = sqlite3.connect('casino.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (id) VALUES (?)', (m.from_user.id,))
    conn.commit()
    conn.close()
    # Ссылка на твой Render
    url = "https://onrender.app"
    kb =]
    await m.answer("Удачи в игре!", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=kb))

async def start_all():
    init_db()
    asyncio.create_task(dp.start_polling(bot))
    config = uvicorn.Config(app, host="0.0.0.0", port=10000)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(start_all())
    
