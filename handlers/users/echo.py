from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang('uz')


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")
