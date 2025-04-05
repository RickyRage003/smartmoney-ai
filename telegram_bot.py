import os
from dotenv import load_dotenv
from telegram import Bot, InputFile

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_report():
    bot = Bot(token=TOKEN)

    # Отправляем график
    try:
        with open("data/filter_chart.png", "rb") as chart:
            bot.send_photo(chat_id=CHAT_ID, photo=InputFile(chart), caption="📊 График фильтрации")
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Ошибка с графиком: {e}")

    # Отправляем CSV
    try:
        with open("data/filtered_signals.csv", "rb") as doc:
            bot.send_document(chat_id=CHAT_ID, document=InputFile(doc), filename="filtered_signals.csv")
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Ошибка с CSV: {e}")
