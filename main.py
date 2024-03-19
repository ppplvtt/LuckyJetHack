from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import random


# Объект бота
bot = Bot(token="7171807612:AAGUmeIpzmWyZCiQims7jDllrLRIKuNnPgM")
# Диспетчер
dp = Dispatcher(bot)



@dp.message_handler(commands = 'Прогноз')
async def number(message: types.Message):
    kb = [
        [types.KeyboardButton(text="/Прогноз")],
        [types.KeyboardButton(text="/Спонсоры")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    n = random.uniform(1, 2)
    numn = "{:.2f}".format(n)

    c = random.uniform(2, 5)
    numc = "{:.2f}".format(c)


    b = random.uniform(5, 10)
    numb= "{:.2f}".format(b) 

    a = random.uniform(10, 100)
    numa= "{:.2f}".format(b) 

    values = [numn, numc, numb, numa]
    data = random.choices(values, weights=[0.655, 0.2, 0.1, 0.005])

    x = str(data)

    def remove_char(s):
        result = s[2 : -2]
        return result
    
    await message.answer(remove_char(x), reply_markup=keyboard) 

@dp.message_handler(commands = 'start')
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="/Прогноз")],
        [types.KeyboardButton(text="/Спонсоры")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет, я - бот, который поможет тебе заработать.", reply_markup=keyboard)

    while True:
        number()


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
