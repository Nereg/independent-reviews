import logging

import asyncpg
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import sql
import sql.util
from sql import users

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message, db: asyncpg.Pool) -> None:
    """
    This handler receives messages with `/createGroup` command
    """
    # params = message.text.split(" ")[1:]
    # print(await CreateGroup(int(params[0]), params[1]).run())
    await message.answer("Hi\!")
    async with db.acquire() as con:
        querier = users.AsyncQuerier(sql.util.convert(con))
        id = await querier.register_telegram(
            telegramId=message.from_user.id, chatId=message.chat.id
        )
        logger.debug(f"Registered user {id}")
