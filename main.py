from telethon import TelegramClient, events
import os

bot_token = os.getenv("TG_BOT_TOKEN")
receiver = os.getenv("TG_RECEIVER")
keywords = ['launchpool', 'lauchpool', 'launchpool!']

client = TelegramClient('session_bot', api_id=None, api_hash=None).start(bot_token=bot_token)

@client.on(events.NewMessage(chats='@binance_announcements'))
async def handler(event):
    if any(word in event.raw_text.lower() for word in keywords):
        try:
            await event.forward_to(receiver)
            print("Сообщение переслано")
        except Exception as e:
            print(f"Ошибка при пересылке: {e}")

client.run_until_disconnected()
