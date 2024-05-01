from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from message_text import User_message_text
import keyboards as kb

user_text = User_message_text()


async def command_start(message: Message) -> None:
    await message.answer(user_text.hello_user_message(), reply_markup=kb.hello_kb)


async def echo(message: Message) -> None:
    await message.answer(user_text.echo_user_message(message.text))


def register(dp: Dispatcher):
    dp.message.register(command_start, Command('start'))
    dp.message.register(echo)
