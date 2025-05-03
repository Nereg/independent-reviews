import asyncio
import logging

import aiohttp
import asyncpg
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import AsyncConnection

import handlers
from config import GlobalConfig
from ISICVerifier import ISICVerifier


def setupLogging(cfg: GlobalConfig) -> None:
    """
    Sets up global logging
    """
    # get root logger
    rootLogger = logging.getLogger("")
    # create a rotating file handler with 1 backup file and 1 megabyte size
    # fileHandler = RotatingFileHandler(LOGGING_PATH, "wa", 1_000_000, 1, "UTF-8")
    # create a default console handler
    consoleHandler = logging.StreamHandler()
    # create a formatting style (modified from hikari)
    formatter = logging.Formatter(
        fmt="%(levelname)-1.1s %(asctime)23.23s %(name)s @ %(lineno)d: %(message)s"
    )
    # set a different logging level for the telethon library
    # telegramLogger = logging.getLogger("telethon")
    # telegramLogger.setLevel(cfg.telegram.debug_level)
    # add the formatter to both handlers
    consoleHandler.setFormatter(formatter)
    # fileHandler.setFormatter(formatter)
    # add both handlers to the root logger
    # rootLogger.addHandler(fileHandler)
    rootLogger.addHandler(consoleHandler)
    # set logging level whatever
    rootLogger.setLevel(cfg.logging_level)
    rootLogger.info("Set up logging!")


async def runBot(
    cfg: GlobalConfig, db: asyncpg.Pool, http: aiohttp.ClientSession, ISIC: ISICVerifier
) -> tuple[Bot, Dispatcher]:
    bot = Bot(
        cfg.telegram.token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
    )
    dp = Dispatcher()
    await handlers.load_all_commands(dp)
    asyncio.create_task(
        await dp.start_polling(bot, db=db, http=http, config=cfg, ISIC=ISIC),
        name="Main Bot task",
    )
    return (bot, dp)


async def main():
    cfg = GlobalConfig.load()
    setupLogging(cfg)
    dbPool = asyncpg.create_pool(cfg.db.dsn)
    session = aiohttp.ClientSession()
    verif = await ISICVerifier.create(session)
    await runBot(cfg, dbPool, session, verif)
    # print(await verif.verify("S421000648595J"))
    # print("Hello from independent-reviews!")


if __name__ == "__main__":
    asyncio.run(main())
