from telethon import TelegramClient, events
import os

api_id = int(os.getenv("TG_API_ID"))
api_hash = os.getenv("TG_API_HASH")
receiver = os.getenv("TG_RECEIVER")

keywords = ['launchpool', 'lauchpool', 'launchpool!']

client = TelegramClient('session_render', api_id, api_hash)

@client.on(events.NewMessage(chats='@binance_announcements'))
async def handler(event):
    text = event.raw_text.lower()
    if any(word in text for word in keywords):
        try:
            await event.forward_to(receiver)
            print(f"Forwarded: {event.raw_text}")
        except Exception as e:
            print(f"Error: {e}")

client.start()
print("Listening for messages...")
client.run_until_disconnected()