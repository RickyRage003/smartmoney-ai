import asyncio
from aiogram import Bot

# Вставляем твои данные
TOKEN = "8098525447:AAEsFdcF2KmTN_aNrarPSo-BwUAjwtWMQRg"
CHAT_ID = "6974593254"

async def test_bot():
    bot = Bot(token=TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text="✅ Бот успешно работает!")
        print("✅ УСПЕШНО: сообщение отправлено.")
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
    finally:
        await bot.session.close()

asyncio.run(test_bot())
