from telethon import TelegramClient
import asyncio

api_id = 35871770
api_hash = '96b84d95e540efdc58bb59a5b779a7aa'

group = 'https://t.me/Referaly2'

message_text = """• Вз лс, бан - реакция
(Много спонсоров не делаю)
(Скам - @tylerd64 @Ihorco @Ludmillaf1)"""

client = TelegramClient('session', api_id, api_hash)

async def main():
    while True:
        try:
            await client.send_message(group, message_text)
            print("Отправлено")
        except Exception as e:
            print("Ошибка:", e)

        await asyncio.sleep(30)  # каждые 30 сек

with client:
    client.loop.run_until_complete(main())х