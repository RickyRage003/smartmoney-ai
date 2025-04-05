import os
import asyncio
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="🤖 SmartMoney AI Бот активен!")

    # Отправим график
    try:
        with open("data/filter_chart.png", "rb") as photo:
            await context.bot.send_photo(chat_id=CHAT_ID, photo=photo, caption="📊 График фильтрации")
    except Exception as e:
        await context.bot.send_message(chat_id=CHAT_ID, text=f"❌ Ошибка с графиком: {e}")

    # Отправим CSV
    try:
        with open("data/filtered_signals.csv", "rb") as doc:
            await context.bot.send_document(chat_id=CHAT_ID, document=doc, filename="filtered_signals.csv")
    except Exception as e:
        await context.bot.send_message(chat_id=CHAT_ID, text=f"❌ Ошибка с CSV: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Бот запущен. Ждёт /start...")
    app.run_polling()
