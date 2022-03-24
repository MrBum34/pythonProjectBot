from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from datetime import datetime

R = "Пусто"
bot = Bot("1905938665:AAHSEO2o_bcmBXPKJvHu1V_Rcr7cmnAnhsc")
dp = Dispatcher(bot)


@dp.message_handler()
async def void(msg: types.message):
    user_id = str(msg.chat.id)
    user_name = msg.from_user.full_name
    R = r"CAACAgIAAxkBAAECtQVhD9mXXlSYDtDYz_tW5CRmwurJFAACpAAD5KDOBx54SxCBG0A9IAQ"

    new = datetime.now()
    time = "{}.{}.{}  {}:{}:{}".format(new.day, new.month, new.year, new.hour, new.minute, new.second)
    with open("log.txt", "a+") as f:
        f.write("\n" + time + " " + user_name + " [" + user_id + "] " + " Текст: " + msg.text + " \n Ответ: " + R)
        f.close()

    await bot.send_sticker(user_id, R), print(
        "\n" + time + user_name + " [" + user_id + "] " + " Текст: " + msg.text + " \n Ответ: " + R)


executor.start_polling(dp)
