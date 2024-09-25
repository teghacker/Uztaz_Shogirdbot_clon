import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import callback_query, Message
from config import *
from buttons import *
from states import *
import re
andoza1 = "(?:\+[9]{2}[8][0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2})"

router = Router()
bot = Bot(token=token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
dp.include_router(router)

@router.message(CommandStart())
async def star(message: Message):
    await message.answer(f"""Assalom alaykum {message.from_user.full_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=sahifa)
    
@router.message(Command("help"))
async def star(message: Message):
    await message.answer(f"""UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @UstozShogirdBot

Admin @UstozShogirdAdminBot""")

@router.message(F.text == "Sherik kerak")
async def star(message: Message, state:FSMContext):
    await message.answer("""Sherik topish uchun ariza berish

Hozir sizga birnecha savollar beriladi.
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer(html.bold("Ism, familiyangizni kiriting?"), parse_mode="html")
    await state.set_state(Sherik_kerak.full_name)

@router.message(F.text == "Ish joyi kerak")
async def star(message: Message, state:FSMContext):
    await message.answer("""Ish joyi topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer(html.bold("Ism, familiyangizni kiriting?"), parse_mode='html')

@router.message(F.text == "Hodim kerak")
async def star(message: Message, state:FSMContext):
    await message.answer("""Xodim topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer(html.bold("🎓 Idora nomi?"), parse_mode='html')

@router.message(F.text == "Ustaz kerak")
async def star(message: Message, state:FSMContext):
    await message.answer("""Ustoz topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer(html.bold("Ism, familiyangizni kiriting?"), parse_mode='html')


@router.message(F.text, Sherik_kerak.full_name)
async def star(message: Message, state:FSMContext):
    fullname = message.text
    if fullname.isdigit():
        await message.reply('Faqat harf yozing')
        await state.set_state(Sherik_kerak.full_name)
    else:
        await state.update_data(
            {
                'fullname':fullname
            })
        await message.answer('''📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#''')
        await state.set_state(Sherik_kerak.Texnologiya)


@router.message(F.text, Sherik_kerak.Texnologiya)
async def star(message: Message, state:FSMContext):
    tex = message.text
    if tex.isdigit():
        await message.reply('Faqat harf yozing')
        await state.set_state(Sherik_kerak.Texnologiya)
    else:
        await state.update_data(
            {
                'Texnologiya':tex
            })
        await message.answer('''📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67''')
        await state.set_state(Sherik_kerak.Aloqa)



@router.message(F.text, Sherik_kerak.Aloqa)
async def star(message: Message, state:FSMContext):
    Aloqa = message.text
    if not re.match(andoza1,Aloqa):
        await message.reply('Xota uz nomer yuboring')
        await state.set_state(Sherik_kerak.Aloqa)
    else:
        await state.update_data(
            {
                'Aloqa':Aloqa
            })
        await message.answer('''🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.''')
        await state.set_state(Sherik_kerak.Hudud)


@router.message(F.text, Sherik_kerak.Hudud)
async def star(message: Message, state:FSMContext):
    Hudud = message.text
    if Hudud.isdigit():
        await message.reply('Faqat harf yozing')
        await state.set_state(Sherik_kerak.Hudud)
    else:
        await state.update_data(
            {
                'Hudud':Hudud
            })
        await message.answer('''💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?''')
        await state.set_state(Sherik_kerak.Narxi)



@router.message(F.text, Sherik_kerak.Narxi)
async def star(message: Message, state:FSMContext):
    Narxi = message.text
    await state.update_data(
        {
            'Narxi':Narxi
        })
    await message.answer('''👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba''')
    await state.set_state(Sherik_kerak.Kasbi)



@router.message(F.text, Sherik_kerak.Kasbi)
async def star(message: Message, state:FSMContext):
    Kasbi = message.text
    await state.update_data(
        {
            'Kasbi':Kasbi
        })
    await message.answer('''🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00''')
    await state.set_state(Sherik_kerak.vaqti)


@router.message(F.text, Sherik_kerak.vaqti)
async def star(message: Message, state:FSMContext):
    vaqti = message.text
    await state.update_data(
        {
            'vaqti':vaqti
        })
    await message.answer('''🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.''')
    await state.set_state(Sherik_kerak.Maqsad)



@router.message(F.text, Sherik_kerak.Maqsad)
async def star(message: Message, state:FSMContext):
    Maqsad = message.text
    await state.update_data(
        {
            'Maqsad':Maqsad
        })
    data = await state.get_data()
    await message.answer(f'''Sherik kerak:

🏅 Sherik: {data.get('fullname')}
📚 Texnologiya: {data.get('Texnologiya')}
🇺🇿 Telegram: {html.link(message.from_user.username,f"https://t.me/{message.from_user.username}")}
📞 Aloqa: {data.get('Aloqa')} 
🌐 Hudud: {data.get('Hudud')} 
💰 Narxi: {data.get('Narxi')} 
👨🏻‍💻 Kasbi: {data.get('Kasbi')} 
🕰 Murojaat qilish vaqti: {data.get('vaqti')} 
🔎 Maqsad: {Maqsad} 

#sherik

''', parse_mode="html")
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=hy)
    await state.set_state(Sherik_kerak.finish)

@router.message(F.text, Sherik_kerak.finish)
async def star(message: Message,state:FSMContext):
    data = await state.get_data()
    if message.text == "Yo'q":
        await message.answer('Qabul qilinmadi')
        await state.clear()
    else:
        await bot.send_message(chat_id=5247497294,text=f'''Sherik kerak:

🏅 Sherik: {data.get('fullname')}
📚 Texnologiya: {data.get('Texnologiya')}
🇺🇿 Telegram: {html.link(message.from_user.username,f"https://t.me/{message.from_user.username}")}
📞 Aloqa: {data.get('Aloqa')} 
🌐 Hudud: {data.get('Hudud')} 
💰 Narxi: {data.get('Narxi')} 
👨🏻‍💻 Kasbi: {data.get('Kasbi')} 
🕰 Murojaat qilish vaqti: {data.get('vaqti')} 
🔎 Maqsad: {data.get('Maqsad')} 

#sherik

''')
        await message.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!

E'lon 24-48 soat ichida kanalda chiqariladi.""")
        await state.clear()


@router.message(F.text)
async def star(message: Message):
    await message.answer("/start so`zini bosing. E'lon berish qaytadan boshlanadi️")




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())