from aiogram import Dispatcher

from handlers import registration, reviews, start


async def load_all_commands(dp: Dispatcher):

    dp.include_router(registration.router)
    dp.include_router(start.router)
    dp.include_router(reviews.router)
