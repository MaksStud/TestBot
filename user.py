from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from message_text import User_message_text
import keyboards as kb


async def command_start(message: Message) -> None:
    user_text = User_message_text()
    await message.answer(user_text.hello_user_message(), reply_markup=kb.hello_kb)


async def echo(message: Message) -> None:
    user_text = User_message_text()
    await message.answer(user_text.eho_user_message(message.text))


def register(dp: Dispatcher):
    dp.message.register(command_start, Command('start'))
    dp.message.register(echo)
