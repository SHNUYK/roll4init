import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN
from rolls import roll_check
from damage import roll_damage

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("roll"))
async def roll_handler(message: types.Message):
    result = roll_check(message.text)
    await message.reply(result)

@dp.message(Command("damage"))
async def damage_handler(message: types.Message):
    result = roll_damage(message.text)
    await message.reply(result)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
