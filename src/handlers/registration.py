from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router: Router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/createGroup` command
    """
    params = message.text.split(" ")[1:]
    # print(await CreateGroup(int(params[0]), params[1]).run())
    await message.answer("Hi\!")
