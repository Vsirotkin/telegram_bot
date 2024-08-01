from aiogram import types, Router

router = Router()

@router.callback_query(lambda c: c.data and c.data.startswith('choice'))
async def choice_callback(callback_query: types.CallbackQuery):
    choice = callback_query.data.split('_')[1]
    await callback_query.message.edit_text(f"You have chosen Choice {choice}")
    await callback_query.answer(f"You have chosen Choice {choice}")

def register_callbacks(dp):
    dp.include_router(router)
