from .gpt_check import check_topic
from db import quries
from pyrogram import types

async def send_message(text, timee, username, client):
    if str(check_topic(text)).startswith('True'):
        send_text = (f'{text}\n'
                f'{timee}\n'
                f'<a href="https://t.me/{username}">Перейти в личку</a>\n')
        await client.send_message(-1002096315255, send_text)
        quries.drop_db()
        quries.save_text(text)

async def send_photo(photo_file_id, caption, time_str, username, client):
    if str(check_topic(caption)).startswith('True'):
        photo = types.InputMediaPhoto(media=photo_file_id, caption=(f'{caption}\n{time_str}\n<a href="https://t.me/{username}">Перейти в личку</a>\n'))
        await client.send_media_group(chat_id=-1002096315255, media=[photo])
        quries.drop_db()
        quries.save_text(caption)

async def send_message_chanel(text, timee, client):
    if str(check_topic(text)).startswith('True'):
        send_text = (f'{text}\n'
                f'{timee}\n')
        await client.send_message(-1002096315255, send_text)
        quries.drop_db()
        quries.save_text(text)

async def send_photo_chanel(photo_file_id, caption, time_str, client):
    if str(check_topic(caption)).startswith('True'):
        photo = types.InputMediaPhoto(media=photo_file_id, caption=(f'{caption}\n{time_str}'))
        await client.send_media_group(chat_id=-1002096315255, media=[photo])
        quries.drop_db()
        quries.save_text(caption)