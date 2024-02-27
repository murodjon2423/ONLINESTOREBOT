
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database


db = Database(DB_NAME)

def make_product_kb():
    products = db.get_product()
    rows = []
    for cat in products:
        rows.append([
            InlineKeyboardButton(
                text=cat[1], callback_data=str(cat[1])
            )]
        )
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=rows
    )
    return inl_kb


def make_product_kb():
    rows = [
        InlineKeyboardButton(text='YES', callback_data='YES'),
        InlineKeyboardButton(text='NO', callback_data='NO')
    ]
    inl_kb = InlineKeyboardMarkup(
        inline_keyboard=[rows]
    )
    return inl_kb