from create_bot import TOKEN, App
import asyncio
import logging
import sys

if __name__ == "__main__":
    app = App(TOKEN)
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(app.run())