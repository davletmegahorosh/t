from funcs import send_photo, send_message, send_message_chanel, send_photo_chanel
from datetime import datetime
from pyrogram import types
from config import client
from db import quries
import asyncio
import logging
from db.quries import change_request, add_chat, get_chats

#
@client.on_message()
async def forward_messages_to_channel(client, message: types.Message):

    if message.chat.id == -4106461694:
        try:
            chat_id = int(message.text)
            add_chat(chat_id)
            await client.send_message(-4106461694, f"group with ID {chat_id} was inserted to exceptions")

        except:
            change_request(message.text)
            await client.send_message(-4106461694, f'request to AI was changed to "{message.text}"')

    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace('-', '.')

    if (quries.check_db(message.text if message.text else message.caption)
        and message.chat.id not in get_chats()
        and message.chat.type != 'private'):

        if message.from_user and message.from_user.username:
            if message.photo and message.caption:
                await send_photo(message.photo.file_id, message.caption, current_time_str, message.from_user.username, client)
            elif message.text:
                await send_message(message.text,current_time_str, message.from_user.username, client)
        else:
            if message.photo and message.caption:
                await send_photo_chanel(message.photo.file_id, message.caption, current_time_str, client)
            elif message.text:
                await send_message_chanel(message.text, current_time_str, client)


if __name__ == "__main__":
    quries.init_db()
    quries.create_tables()
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    client.run()