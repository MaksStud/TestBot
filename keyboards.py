from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

hello_buttons = [[InlineKeyboardButton(text='Мої канали', callback_data='Мої канали')],
                [InlineKeyboardButton(text='Підклюити копіювання', callback_data='Підклюити копіювання')],
                [InlineKeyboardButton(text='Продовжити підписку', callback_data='Продовжити підписку')],]

hello_kb = InlineKeyboardMarkup(inline_keyboard=hello_buttons)
