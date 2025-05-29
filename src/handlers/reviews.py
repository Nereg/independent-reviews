import logging

import aiogram.utils.formatting as tfmt
import asyncpg
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from handlers.reviews_common import commonLayout
from sql.reviews import get_review_by_id

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message(Command("getReviewById"))
async def command_start_handler(message: Message, db: asyncpg.Pool) -> None:
    """
    This handler receives messages with `/createGroup` command
    """
    params = message.text.split(" ")[1:]
    if len(params) >= 1:
        # print(await CreateGroup(int(params[0]), params[1]).run())
        async with db.acquire() as con:
            review = await get_review_by_id(con, id_=int(params[0]))
            logger.debug(review)
            await message.answer(**commonLayout(review).as_kwargs())


@router.message(Command("subject"))
async def subject_search_handler(message: Message, db: asyncpg.Pool) -> None:
    """
    Signature: /subject name or code
    """
    params = message.text.split(" ")[1:]
    if len(params) >= 1:
        pass
    else:
        payload = tfmt.as_list(
            tfmt.Bold(
                "You can use this command to search reviews about a specific subject."
            ),
            tfmt.Text(
                "You can search for a subject's name in slovak (diacritics are optional): ",
                tfmt.BotCommand("/subject anglicky jazyk"),
            ),
            tfmt.Text(
                "You can search for a subject's AIS code: ",
                tfmt.BotCommand("/subject AJ"),
            ),
        )
        await message.answer(**payload.as_kwargs())
        return
