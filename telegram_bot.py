import os
from aiogram import Bot
from aiogram.types import InputFile
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)


async def send_telegram_report(filtered_csv_path, chart_path, accuracy):
    msg = f"✅ Фильтрованные сигналы\n🎯 Accuracy: {accuracy:.4f}"

    # Отправляем текст
    await bot.send_message(chat_id=CHAT_ID, text=msg)

    # Отправляем график (как путь к файлу)
    await bot.send_photo(chat_id=CHAT_ID, photo=InputFile(chart_path, filename="filter_chart.png"))

    # Отправляем CSV-файл (как путь к файлу)
    await bot.send_document(chat_id=CHAT_ID, document=InputFile(filtered_csv_path, filename="filtered_signals.csv"))
