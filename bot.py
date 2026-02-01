import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN
from rolls import roll_check
from damage import roll_damage

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("r"))
async def roll_handler(message: types.Message):
    result = roll_check(message.text)
    await message.reply(result)

@dp.message(Command("d"))
async def damage_handler(message: types.Message):
    result = roll_damage(message.text)
    await message.reply(result)

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    help_text = (
        "Список команд:\n\n"
        "/r [пул] [+/-модификаторы...] - бросок проверки навыка или характеристики.\n"
        "  Пример: /r 50 +10 -5\n\n"
        "/D XdY [+/-модификаторы...] - бросок урона.\n"
        "  Пример: /D 2d10 +5 -2\n\n"
        "/start - активировать бота, если он заснул.\n"
        "/help - показать это сообщение."
    )
    await message.reply(help_text)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Бот активирован и готов к работе! Используйте /help для списка команд.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
