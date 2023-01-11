from aiogram import Bot, Dispatcher, executor, types
import requests
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

API_TOKEN: str = '5926602129:AAFTv3Cst_TM34lTgFc7BvR-QFOrN-nWLp8'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

API_DOGS_URL: str = 'https://dog.ceo/api/breeds/image/random'

API_CATS_URL: str = 'https://aws.random.cat/meow'

async def process_start_command(message: types.Message):
    await message.answer("Hi! \n I'm gonna show u some cuties \n text me something")


async def process_help_command(message: types.Message):
    await message.answer('I will reply with a pic of a cutie to your text')


async def send_echo(message: types.Message):
    await message.reply(message.text)


async def send_random_cat(message: types.Message):
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()['file']
        #updates = bot.get_updates()

        await message.answer_photo(photo = cat_link)
    else:
        await message.reply('it had to be a pic of a cutie but something went wrong :(')


async def send_dog_random(message: types.Message):
    dog_response = requests.get(API_DOGS_URL)
    if dog_response.status_code == 200:
        dog_link = dog_response.json()['message']
        await message.answer_photo(photo = dog_link)
    else:
        await message.reply('this should be a dog pic but sth went wrong :(')
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(send_random_cat, commands='cat')
dp.register_message_handler(send_dog_random, commands='dog' )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)