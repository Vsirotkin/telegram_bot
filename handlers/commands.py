# handlers/commands.py
import asyncio
from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_command(message: types.Message, flags: dict):
    user_id = message.from_user.id
    # Cancel any existing task for this user
    if 'task' in flags:
        flags['task'].cancel()

    # Create an inline keyboard with two buttons
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Choice 1", callback_data="choice_1")],
        [InlineKeyboardButton(text="Choice 2", callback_data="choice_2")]
    ])
    await message.answer(f"Привет, {message.from_user.first_name}! Как ты сегодня?", reply_markup=keyboard)

    # Set the waiting state for the user
    flags['waiting_for_response'] = True

    # Start a task to check for the response
    flags['task'] = asyncio.create_task(wait_for_response(message, flags))

async def wait_for_response(message: types.Message, flags: dict):
    await asyncio.sleep(200)
    if flags.get('waiting_for_response', False):
        await message.answer("Вы забыли ответить")
        flags['waiting_for_response'] = False

async def help_command(message: types.Message):
    await message.answer("You can use the following commands:\n/start - Start the bot\n/help - Get help\n/echo - Echo your message")

async def echo_command(message: types.Message, flags: dict):
    user_id = message.from_user.id
    
    if flags.get('waiting_for_response', False):
        text_to_echo = message.text
        await message.answer(text_to_echo)
        flags['waiting_for_response'] = False
    else:
        await message.answer("Please provide a message to echo. Send /cancel to cancel.")
        flags['waiting_for_response'] = True

async def cancel_command(message: types.Message, flags: dict):
    if flags.get('waiting_for_response', False):
        await message.answer("Echo command cancelled.")
        flags['waiting_for_response'] = False
    else:
        await message.answer("No active echo command to cancel.")

async def button_handler(callback_query: types.CallbackQuery, flags: dict):
    user_id = callback_query.from_user.id
    # Cancel any existing task for this user
    if 'task' in flags:
        flags['task'].cancel()
        flags.pop('task')  # Remove the task from flags

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
    flags['waiting_for_response'] = False

async def message_handler(message: types.Message, flags: dict):
    user_id = message.from_user.id
    # Cancel any existing task for this user
    if 'task' in flags:
        flags['task'].cancel()
        flags.pop('task')  # Remove the task from flags

    # Reset the waiting state for the user
    flags['waiting_for_response'] = False

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(start_command, Command('start'))
    dp.message.register(help_command, Command('help'))
    dp.message.register(echo_command, Command('echo'))
    dp.message.register(cancel_command, Command('cancel'))
    dp.callback_query.register(button_handler)
    dp.message.register(message_handler)  # Register the message handler
