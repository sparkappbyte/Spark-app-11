import asyncio, uvicorn, sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен
TOKEN = "8694731612:AAEAE9q6cg96CRS1kefQX_CUN_aJDfTB-Tc"

app = FastAPI()
bot = Bot(token=TOKEN)
dp = Dispatcher()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@dp.message(Command("start"))
async def start(m: types.Message):
    # Прямая ссылка без лишних переменных
    url = "https://onrender.app"
    btn = types.InlineKeyboardButton(text="ИГРАТЬ", web_app=types.WebAppInfo(url=url))
    row = [btn]
    kb = types.InlineKeyboardMarkup(inline_keyboard=[row])
    await m.answer("Удачи!", reply_markup=kb)

async def main():
    asyncio.create_task(dp.start_polling(bot))
    conf = uvicorn.Config(app, host="0.0.0.0", port=10000)
    server = uvicorn.Server(conf)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
    
