from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

sahifa=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustaz kerak")],
        [KeyboardButton(text="Shogird kerak")],
    ],resize_keyboard=True
)

hy=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ],resize_keyboard=True,
    one_time_keyboard=True
)







# sahifa = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="Menu 🍟"), KeyboardButton(text="Cantact ☎️", request_contact=True)],
#     [KeyboardButton(text="shopping", web_app=WebAppInfo(url="https://chatgpt.com/")), KeyboardButton(text="Basket 🛒")]
#     ],resize_keyboard=True
# )