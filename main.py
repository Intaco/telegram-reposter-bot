from telethon import TelegramClient, events, sync
import schedule
import socks
import logging
import time
import asyncio
import sys
import datetime
import os
import dotenv
dotenv.load_dotenv()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


client = TelegramClient('session', os.environ['API_ID'], os.environ['API_HASH'],
                        #proxy=(socks.SOCKS5, 'hostname', 443, True, "username", "password"),
                        timeout=60)
print("telegram reposter started at {}".format(str(datetime.datetime.now())))
client.start()
### INIT

dialogs = client.get_dialogs()

TARGET_CHAT_NAME = os.environ['TARGET_CHAT_NAME']
SOURCE_CHAT_NAMES = os.environ['SOURCE_CHAT_NAMES'].split(",,,") # in case you need multiple chats - split them by ,,,

#print(list(map(lambda n: n.name, dialogs)))
target_chat = list(filter(lambda d: str(d.name) == TARGET_CHAT_NAME, dialogs))[0]
print("TARGET CHAT: {}".format(target_chat.name))

source_chats = list(filter(lambda d: str(d.name) in SOURCE_CHAT_NAMES, dialogs))
source_chat_names = list(map(lambda c: c.name, source_chats))
print("SRC CHATS: {}".format(source_chat_names))

@client.on(events.NewMessage(chats=source_chats))
async def handler(event):
    if hasattr(event, 'message'):
        print(event)
        await client.forward_messages(target_chat, event.message, event.chat_id)


client.run_until_disconnected()
