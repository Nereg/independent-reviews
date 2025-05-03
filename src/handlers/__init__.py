from aiogram import Dispatcher

from handlers import registration


async def load_all_commands(dp: Dispatcher):

    dp.include_router(registration.router)
