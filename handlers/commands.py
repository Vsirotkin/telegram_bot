import asyncio
from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Define dictionaries to store user states and tasks
user_states = {}
user_tasks = {}

async def start_command(message: types.Message):
    user_id = message.from_user.id
    # Cancel any existing task for this user
    if user_id in user_tasks:
        user_tasks[user_id].cancel()

    # Create an inline keyboard with two buttons
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Choice 1", callback_data="choice_1")],
        [InlineKeyboardButton(text="Choice 2", callback_data="choice_2")]
    ])
    await message.answer(f"Привет, {message.from_user.first_name}! Как ты сегодня?", reply_markup=keyboard)

    # Set the waiting state for the user
    user_states[user_id] = True

    # Start a task to check for the response
    user_tasks[user_id] = asyncio.create_task(wait_for_response(message))

async def wait_for_response(message: types.Message):
    await asyncio.sleep(10)
    user_id = message.from_user.id
    if user_states.get(user_id, False):
        await message.answer("Вы забыли ответить")
        user_states[user_id] = False

async def help_command(message: types.Message):
    await message.answer("You can use the following commands:\n/start - Start the bot\n/help - Get help\n/echo - Echo your message")

async def echo_command(message: types.Message):
    user_id = message.from_user.id
    
    if user_states.get(user_id):
        text_to_echo = message.text
        await message.answer(text_to_echo)
        user_states[user_id] = False
    else:
        await message.answer("Please provide a message to echo. Send /cancel to cancel.")
        user_states[user_id] = True

async def cancel_command(message: types.Message):
    user_id = message.from_user.id
    if user_states.get(user_id):
        await message.answer("Echo command cancelled.")
        user_states[user_id] = False

async def button_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    # Cancel any existing task for this user
    if user_id in user_tasks:
        user_tasks[user_id].cancel()
        user_tasks.pop(user_id)

    choice = callback_query.data
    if choice == "choice_1":
        response = "You have chosen Choice 1"
    elif choice == "choice_2":
        response = "You have chosen Choice 2"
    else:
        response = "Invalid choice"

    await callback_query.message.answer(response)
    await callback_query.answer()  # Acknowledge the callback

    # Reset the waiting state for the user
    user_states[user_id] = False

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(start_command, Command('start'))
    dp.message.register(help_command, Command('help'))
    dp.message.register(echo_command, Command('echo'))
    dp.message.register(cancel_command, Command('cancel'))
    dp.callback_query.register(button_handler)
