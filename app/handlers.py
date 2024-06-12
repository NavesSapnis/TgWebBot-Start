from aiogram import Router, html, F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from app.buttons import answer

router = Router()


@router.message(Command("play"))
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",reply_markup=answer)

