from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv 
from service import *
from connection import *
import asyncio
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_bot(message: Message):
    if await  get_user_by_id(message.from_user.id):
        await message.answer(f"Hello @{message.from_user.username} welcome to the family")
    else:
        user = message.from_user
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Hello @{message.from_user.username}")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(f"""
Добро пожаловать:
    pack-открываеш новую тень, 
    my_shadow-сколько у тебя теней, 
    dungeon-идти в подземелье,
    sell_resources-продать ресурсы.
""")

@dp.message(Command("pack"))
async def pack(message: Message):
    await message.answer(f"Your first shadow Igris")

@dp.message(Command("my_shadows"))
async def My_shadows(message: Message):
    await message.answer(f"You have one shadow Igris")

@dp.message(Command("dungeon"))
async def dungeon(message: Message):
    await message.answer(f"""
You are in an A-rank dungeon.

----------------------------------
Your army goes through the dungeon
----------------------------------

Well done, you completed the dungeon.
""")

@dp.message(Command("sell_resources"))
async def Sell_resources(message: Message):
    await message.answer(f"You sold the resources, your profit is 15,000 coins.")

@dp.message(Command("get_all_user"))
async def help(message: Message):
    users = await get_users()
    for user in users:
        await message.answer(f"""
Username: {user['username']}  
Full name: {user['full_name']}
                             """) 

async def main():
    await create_table()
    print("Bot started")
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())