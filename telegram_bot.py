import os
from aiogram import Bot
from aiogram.types.input_file import BufferedInputFile
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)


async def send_telegram_report(filtered_csv_path, chart_path, accuracy):
    msg = f"✅ Фильтрованные сигналы\n🎯 Accuracy: {accuracy:.4f}"
    await bot.send_message(chat_id=CHAT_ID, text=msg)

    # Отправляем график
    with open(chart_path, "rb") as image:
        photo = BufferedInputFile(image.read(), filename="filter_chart.png")
        await bot.send_photo(chat_id=CHAT_ID, photo=photo)

    # Отправляем CSV
    with open(filtered_csv_path, "rb") as file:
        document = BufferedInputFile(file.read(), filename="filtered_signals.csv")
        await bot.send_document(chat_id=CHAT_ID, document=document)
