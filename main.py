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
dotenv.load_dotenv(encoding='utf-8')
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


client = TelegramClient('session', os.environ['API_ID'], os.environ['API_HASH'],
                        #proxy=(socks.SOCKS5, 'hostname', 443, True, "username", "password"),
                        timeout=60)
print("telegram reposter started at {}".format(str(datetime.datetime.now())))
client.start()
### INIT

dialogs = client.get_dialogs()

TARGET_CHAT_NAMES_LIST = os.environ['TARGET_CHAT_NAMES'].split(";;;")
SOURCE_CHAT_NAMES_LIST = os.environ['SOURCE_CHAT_NAMES'].split(";;;")

if len(TARGET_CHAT_NAMES_LIST) != len(SOURCE_CHAT_NAMES_LIST):
    quit()

SOURCE_TARGET_CHAT_MAP = {}

source_chats_set = set()
for i in range(0, len(TARGET_CHAT_NAMES_LIST)):
    TARGET_CHAT_NAME = TARGET_CHAT_NAMES_LIST[i]
    SOURCE_CHAT_NAMES = SOURCE_CHAT_NAMES_LIST[i].split(",,,")  # in case you need multiple chats - split them by ,,,

    # print(list(map(lambda n: n.name, dialogs)))
    target_chat = list(filter(lambda d: str(d.name) == TARGET_CHAT_NAME, dialogs))[0]
    print("TARGET CHAT: {}".format(target_chat.name))

    source_chats = list(filter(lambda d: str(d.name) in SOURCE_CHAT_NAMES, dialogs))
    source_chat_names = list(map(lambda c: c.name, source_chats))
    print("SRC CHATS: {}".format(source_chat_names))

    for source_chat in source_chats:
        source_chats_set.add(source_chat)
        if source_chat.id in SOURCE_TARGET_CHAT_MAP:
            SOURCE_TARGET_CHAT_MAP[source_chat.id].append(target_chat)
        else:
            SOURCE_TARGET_CHAT_MAP[source_chat.id] = [target_chat]

for key in SOURCE_TARGET_CHAT_MAP:
    print(key, '->', SOURCE_TARGET_CHAT_MAP[key])

@client.on(events.NewMessage(chats=list(source_chats_set)))
async def handler(event):
    print(event, '\n')
    if hasattr(event, 'message'):
        for target_chat in SOURCE_TARGET_CHAT_MAP[event.chat_id]:
            await client.forward_messages(target_chat, event.message, event.chat_id)


client.run_until_disconnected()
