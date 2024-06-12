from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

web_app_info=WebAppInfo(url = "web_app_url")

answer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Play",web_app=web_app_info)],
    [InlineKeyboardButton(text="Join community",url="https://t.me/logovo_kaban")],
])