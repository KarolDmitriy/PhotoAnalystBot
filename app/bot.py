from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message
from app.analyzer import analyze_image
from app.config import BOT_TOKEN
import asyncio

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Привет! Я PhotoAnalyst — бот, который анализирует фотографии.\nОтправь мне фото, и я расскажу, что думаю 😉")

@dp.message(F.photo)
async def handle_photo(message: Message):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    await message.answer("📸 Фото получено, анализирую...")

    result = await analyze_image(bot, file_path)
    await message.answer(result)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
