import os
import asyncio
from telethon import TelegramClient, events

bot_token = os.getenv("TG_BOT_TOKEN")
receiver = os.getenv("TG_RECEIVER")
keywords = ['launchpool', 'lauchpool', 'launchpool!']

client = TelegramClient('session_bot', api_id=12345, api_hash='dummy')  # нужны фиктивные значения

async def main():
    await client.start(bot_token=bot_token)

    @client.on(events.NewMessage(chats='@binance_announcements'))
    async def handler(event):
        if any(word in event.raw_text.lower() for word in keywords):
            try:
                await event.forward_to(receiver)
                print("✅ Сообщение переслано")
            except Exception as e:
                print(f"❌ Ошибка: {e}")

    print("🤖 Бот запущен. Ожидаем сообщения...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
