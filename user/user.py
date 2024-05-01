import logging
from aiogram import types, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from . import message_text as m
from . import keyboards as kb
from create_bot import bot


async def command_start(message: Message) -> None:
    await message.answer(m.hello_message, reply_markup=kb.hello_kb)


def register(dp: Dispatcher):
    dp.message.register(command_start, Command('start'))
