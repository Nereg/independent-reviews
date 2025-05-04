from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils import formatting
from aiogram.utils.chat_action import ChatActionSender

from ISICVerifier import ISICVerifier

router: Router = Router()


@router.message(Command("verify"))
async def command_start_handler(message: Message, ISIC: ISICVerifier) -> None:
    """
    This handler receives messages with `/createGroup` command
    """
    params = message.text.split(" ")[1:]
    if len(params) <= 0:
        payload = formatting.as_list(
            formatting.Bold(
                "You need your ISIC card number to verify that you are a student!\n"
            ),
            formatting.BlockQuote(
                formatting.Text(
                    "ISIC card number is 14 characters long, begins and ends with a letter and is located above your photo on your ISIC card.\n"
                ),
                formatting.Text("For example: "),
                formatting.BotCommand("/verify S421000555444K"),
            ),
        )
        await message.answer(**payload.as_kwargs())
        return
    if len(params[0]) < 10 or len(params[0]) > 20:
        await message.answer(f"`{params[0]}` is not a valid ISIC chip/card number\!")
        return
    else:
        await message.answer(
            "ISIC card number seems valid\! Please wait, while we verify that you are a student\!"
        )
        async with ChatActionSender(bot=message.bot, chat_id=message.chat.id):
            try:
                result = await ISIC.verify(params[0])
            except ValueError as e:
                await message.answer(
                    f"`{params[0]}` is not a valid ISIC chip/card number\!"
                )
                return
        if not result.valid:
            await message.answer(
                f"ISIC `{params[0]}` was valid until `{result.validDate.strftime("%d.%m.%Y")}`\!"
            )
            return
        payload = formatting.as_list(
            formatting.Bold("ISIC found!"),
            formatting.BlockQuote(
                formatting.as_list(
                    formatting.Bold("ISIC Data"),
                    f"Name: {result.name}",
                    f"Surname: {result.surname}",
                    f"Faculty: {result.faulty.name}",
                    f"Valid until: {result.validDate.strftime("%d.%m.%Y")}",
                )
            ),
            formatting.Text(
                "Do you wish to verify that you are a student ? You data will remain anonymous!"
            ),
        )
        await message.answer(**payload.as_kwargs())

    # print(await CreateGroup(int(params[0]), params[1]).run())
    await message.answer("Hi\!")
