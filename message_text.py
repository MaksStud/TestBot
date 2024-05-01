from aiogram.types import Message


class User_message_text:

    def hello_user_message(self) -> str:
        return 'Привіт'

    def echo_user_message(self, text) -> str:
        return text