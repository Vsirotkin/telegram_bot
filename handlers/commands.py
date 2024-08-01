from aiogram import types, Dispatcher
from aiogram.filters import Command


user_states = {}

async def start_command(message: types.Message):
    await message.answer("Hello! I'm a bot. How can I help you today?")

async def help_command(message: types.Message):
    await message.answer("You can use the following commands:\n/start - Start the bot\n/help - Get help\n/echo - Echo your message")

async def echo_command(message: types.Message):
    user_id = message.from_user.id
    
    # If the user is currently waiting for a message
    if user_states.get(user_id):
        text_to_echo = message.text
        await message.answer(text_to_echo)
        user_states[user_id] = False  # Reset the state
    else:
        # Prompt the user to enter a message
        await message.answer("Please provide a message to echo. Send /cancel to cancel.")
        user_states[user_id] = True  # Set the state to indicate waiting for message

async def cancel_command(message: types.Message):
    user_id = message.from_user.id
    if user_states.get(user_id):
        await message.answer("Echo command cancelled.")
        user_states[user_id] = False

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(start_command, Command('start'))
    dp.message.register(help_command, Command('help'))
    dp.message.register(echo_command, Command('echo'))
    dp.message.register(cancel_command, Command('cancel'))
