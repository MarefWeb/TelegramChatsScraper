from telethon import TelegramClient, events
from config import DESTINATION, API_ID, API_HASH, SESSION, CHATS, KEY_WORDS


client = TelegramClient(SESSION, API_ID, API_HASH)


if __name__ == '__main__':
    print("Program is running...")

    @client.on(events.NewMessage(chats=CHATS))
    async def new_order(event):
        try:
            print('Delivery new order...')
            contain_key_word = False

            for key_word in KEY_WORDS:
                if key_word in event.message.message:
                    contain_key_word = True

            if contain_key_word:
                await client.forward_messages(DESTINATION, event.message)

        except Exception as ex:
            print(f'Exception: {ex}')


    client.start()
    client.run_until_disconnected()
