from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils import formatting
from aiogram.utils.chat_action import ChatActionSender

from ISICVerifier import ISICVerifier

router: Router = Router()


class VerificationConsent(CallbackData, prefix="vc"):
    ISICChipId: int
    AISId: int
    faculty: int


class VerificationDecline(CallbackData, prefix="vnc"):
    pass


@router.message(Command("verify"))
async def command_verify_handler(message: Message, ISIC: ISICVerifier) -> None:
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
                    f"Faculty: {result.faculty.name}",
                    f"Valid until: {result.validDate.strftime("%d.%m.%Y")}",
                )
            ),
            formatting.Text(
                "Do you wish to verify that you are a student ? You data will remain anonymous!"
            ),
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Yes✅",
                        callback_data=VerificationConsent(
                            ISICChipId=result.ISICChipId,
                            AISId=result.AISId,
                            faculty=result.faculty,
                        ).pack(),
                    ),
                    InlineKeyboardButton(
                        text="No❌", callback_data=VerificationDecline().pack()
                    ),
                ]
            ]
        )
        await message.answer(**payload.as_kwargs(), reply_markup=keyboard)


@router.callback_query(
    VerificationConsent.filter(),
)
async def verification_consent_handler(callback_query: CallbackQuery):
    await callback_query.answer("Accepted!")
    # await callback_query.


@router.callback_query(
    VerificationDecline.filter(),
)
async def verification_decline_handler(callback_query: CallbackQuery):
    await callback_query.answer("Declined!")
