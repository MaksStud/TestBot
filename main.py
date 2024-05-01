import user
from create_bot import bot, dp
import asyncio
import logging
import sys


async def main():
    try:
        await dp.start_polling(bot, skip_updates=True)
    except KeyboardInterrupt:
        await bot.close()
        await dp.storage.close()
        await dp.storage.wait_closed()


if __name__ == "__main__":
    user.register(dp)
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
