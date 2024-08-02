import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from unittest.mock import AsyncMock, patch
import pytest
from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from handlers.commands import start_command, wait_for_response

@pytest.fixture
def mock_message():
    message = AsyncMock(spec=types.Message)
    message.from_user = AsyncMock(spec=types.User)
    message.from_user.id = 123
    message.from_user.first_name = "John"  # Add first_name attribute
    return message

@pytest.fixture
def mock_flags():
    return {}

@pytest.fixture
def mock_dispatcher():
    dispatcher = AsyncMock(spec=Dispatcher)
    dispatcher.process_message = AsyncMock()  # Add process_message attribute
    return dispatcher

@pytest.mark.asyncio
async def test_start_command(mock_message, mock_flags, mock_dispatcher):
    mock_message.answer = AsyncMock()
    mock_message.reply_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Choice 1", callback_data="choice_1")],
        [InlineKeyboardButton(text="Choice 2", callback_data="choice_2")]
    ])

    await start_command(mock_message, mock_flags)

    mock_message.answer.assert_called_once_with(
        "Привет, John! Как ты сегодня?",
        reply_markup=mock_message.reply_markup
    )
    assert mock_flags['waiting_for_response'] is True
    assert mock_flags['task'] is not None
    assert isinstance(mock_flags['task'], asyncio.Task)
    assert mock_flags['task'].get_coro().__name__ == wait_for_response.__name__
    mock_dispatcher.process_message.assert_not_called()

@pytest.mark.asyncio
async def test_wait_for_response(mock_message, mock_flags):
    mock_message.answer = AsyncMock()
    mock_flags['waiting_for_response'] = True

    await wait_for_response(mock_message, mock_flags)

    mock_message.answer.assert_called_once_with('Вы забыли ответить')
    assert mock_flags['waiting_for_response'] is False