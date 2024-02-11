from decouple import config
from openai import OpenAI
from pyrogram import Client

api_key = config('api_key')
gpt_client = OpenAI(api_key=api_key)

API_ID = config('api_id')
API_HASH=config('api_hash')
client = Client("bot", api_id=API_ID, api_hash=API_HASH)




