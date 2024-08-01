# handlers/middleware.py
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Awaitable, Dict, Any

class FlagsMiddleware(BaseMiddleware):
    def __init__(self):
        self.user_flags: Dict[int, Dict[str, Any]] = {}

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user_id = data['event_from_user'].id
        if user_id not in self.user_flags:
            self.user_flags[user_id] = {}
        data['flags'] = self.user_flags[user_id]
        result = await handler(event, data)
        self.user_flags[user_id] = data['flags']
        return result
