import asyncio, uvicorn, sqlite3
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

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

@dp.message(Command("start"))
async def start(m: types.Message):
    init_db()
    conn = sqlite3.connect('casino.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (id) VALUES (?)', (m.from_user.id,))
    conn.commit()
    conn.close()
    
    url = "https://onrender.app"
    # Здесь теперь нет переменной kb, код прямой:
    await m.answer("Удачи!", reply_markup=types.InlineKeyboardMarkup(inline_keyboard=]))

async def start_all():
    init_db()
    asyncio.create_task(dp.start_polling(bot))
    config = uvicorn.Config(app, host="0.0.0.0", port=10000)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(start_all())
    
