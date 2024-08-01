import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from handlers.commands import register_handlers_commands

load_dotenv()  # Load environment variables from .env file
API_TOKEN = os.getenv('BOT_TOKEN')

async def on_startup(dispatcher: Dispatcher):
    print("Bot is starting up...")

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    
    # Register handlers
    register_handlers_commands(dp)
    
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
