from aiogram import Dispatcher

from handlers import registration, start


async def load_all_commands(dp: Dispatcher):

    dp.include_router(registration.router)
    dp.include_router(start.router)
