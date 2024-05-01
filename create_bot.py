from aiogram import Bot, Dispatcher
import user
from aiogram import Bot, Dispatcher
import asyncio
import logging
import sys

TOKEN: str = '6726585823:AAE7FCNk_8DlM1Zktj3m07nn2JaoDz27KI4'


class App:
    def __init__(self, token):
        self.dp = Dispatcher()
        self.bot = Bot(token, parse_mode="html")

    def register_handlers(self):
        user.register(self.dp)

    async def run(self, ):
        self.register_handlers()
        try:
            await self.dp.start_polling(self.bot, skip_updates=True)
        except KeyboardInterrupt:
            await self.bot.close()
            await self.dp.storage.close()
            await self.dp.storage.wait_closed()