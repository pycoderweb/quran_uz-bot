import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

def quran_uzb(sura,oyat):
    url_uz = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json"
    r = requests.get(url_uz).json()
    for quran in r["quran"]:
       if quran['chapter'] == sura and quran['verse'] == oyat:
           return str(quran['text'])

API_TOKEN = '6299448173:AAH0WiNuaFuY84ZaDuyrBXS4KYWhp4wGkPY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("salom. botimizga hush kelibsiz bu bot orqali istalgan oyat matnini topishingiz mumkin \nmasalan 2 1 (2-sura 1 - oyat) shu tartibda kiriting orasini bitta probel bilan ajratgan xolda\n\n\nbot admini ||rahmonov_shaxzod||")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        sura = message.text.split(" ")[0]
        oyat = message.text.split(" ")[1]
        sura = int(sura)
        oyat = int(oyat)

        natija = f"{sura} - sura ({oyat} - oyat) :\n{quran_uzb(sura,oyat)}"
        await message.answer(natija)
    except:
        await message.answer("iltimos qaytadan to'g'ri kiriting!!!!!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)